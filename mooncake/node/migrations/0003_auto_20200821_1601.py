# Generated by Django 3.1 on 2020-08-21 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0002_auto_20200821_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nodetype',
            name='parent',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='node.nodetype'),
        ),
    ]
