from datetime import timedelta

from django import forms
from django.forms import ValidationError
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.db.models import Q
from django.utils.translation import gettext_lazy as _


class UserCacheMixin:
    user_cache = None


class SignIn(UserCacheMixin, forms.Form):
    password = forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if settings.USE_REMEMBER_ME:
            self.fields['remember_me'] = forms.BooleanField(label=_('Remember me'), required=False)

    def clean_password(self):
        password = self.cleaned_data['password']

        if not self.user_cache:
            return password

        if not self.user_cache.check_password(password):
            raise ValidationError(_('无效邮箱或者密码'))

        return password


class SignInViaEmailOrUsernameForm(SignIn):
    email_or_username = forms.CharField(label=_('Email or Username'))

    @property
    def field_order(self):
        if settings.USE_REMEMBER_ME:
            return ['email_or_username', 'password', 'remember_me']
        return ['email_or_username', 'password']

    def clean_email_or_username(self):
        email_or_username = self.cleaned_data['email_or_username']

        user = User.objects.filter(Q(username=email_or_username) | Q(email__iexact=email_or_username)).first()
        if not user:
            raise ValidationError(_('无效邮箱或者密码'))

        if not user.is_active:
            raise ValidationError(_('无效邮箱或者密码'))

        self.user_cache = user

        return email_or_username


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # help_texts = {
        #     'username': None,
        #     'email': None,
        #     'password1': None,
        #     'password2': None,
        # }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['minlength'] = 4
        self.fields['username'].widget.attrs['maxlength'] = 12
        self.fields['username'].widget.attrs.pop("autofocus", None)
        self.fields['password1'].widget.attrs['minlength'] = 6
        self.fields['password1'].widget.attrs['maxlength'] = 20
        self.fields['password2'].widget.attrs['minlength'] = 6
        self.fields['password2'].widget.attrs['maxlength'] = 20

        # self.error_messages['duplicate_username'] = '该用户名已经被占用'


    # username = forms.CharField(error_messages={'invalid': "无效用户名"})

    def clean_email(self):
        email = self.cleaned_data['email']

        user = User.objects.filter(email__iexact=email).exists()
        if user:
            raise ValidationError(_('请使用其它的邮箱'))

        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 != password2:
            raise ValidationError(_('密码不匹配'))
 
        return password2 




class RestorePasswordViaEmailOrUsernameForm(UserCacheMixin, forms.Form):
    email_or_username = forms.CharField(label=_('Email or Username'))

    def clean_email_or_username(self):
        email_or_username = self.cleaned_data['email_or_username']

        user = User.objects.filter(Q(username=email_or_username) | Q(email__iexact=email_or_username)).first()
        if not user:
            raise ValidationError(_('用户名或者邮箱无效'))

        if not user.is_active:
            raise ValidationError(_('该用户还没被激活'))

        self.user_cache = user

        return email_or_username
