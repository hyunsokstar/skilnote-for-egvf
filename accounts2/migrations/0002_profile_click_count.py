# Generated by Django 3.2.7 on 2021-10-06 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='click_count',
            field=models.IntegerField(default=0),
        ),
    ]
