# Generated by Django 3.2.7 on 2022-03-03 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_college'),
    ]

    operations = [
        migrations.AddField(
            model_name='yourdetail',
            name='email',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='yourdetail',
            name='password',
            field=models.CharField(default='', max_length=100),
        ),
    ]