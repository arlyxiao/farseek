from django.urls import path


from .views import index


app_name = 'ask'

urlpatterns = [
    path('', index, name='index'),
]
