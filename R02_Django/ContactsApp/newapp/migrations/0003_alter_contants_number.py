# Generated by Django 4.2.17 on 2024-12-25 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_contants_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contants',
            name='number',
            field=models.IntegerField(),
        ),
    ]