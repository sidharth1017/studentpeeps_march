# Generated by Django 3.2.7 on 2021-09-21 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_alter_registers_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='unverified',
            name='verification_url',
            field=models.CharField(default='', max_length=500),
        ),
    ]