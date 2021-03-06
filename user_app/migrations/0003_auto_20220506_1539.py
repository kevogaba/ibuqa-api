# Generated by Django 3.2.13 on 2022-05-06 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_auto_20220506_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, verbose_name='phone_number'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=128, verbose_name='first_name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=128, verbose_name='last_name'),
        ),
    ]
