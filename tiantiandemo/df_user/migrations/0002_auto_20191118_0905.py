# Generated by Django 2.2.7 on 2019-11-18 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='uaddress',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uphone',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='ushou',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uyoubian',
            field=models.CharField(default='', max_length=6),
        ),
    ]
