# Generated by Django 2.2.7 on 2019-11-20 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0002_auto_20191118_0914'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GoodInfo',
            new_name='GoodsInfo',
        ),
    ]