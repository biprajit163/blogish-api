# Generated by Django 3.1.7 on 2021-03-01 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogish', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='user',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
