# Generated by Django 5.1.2 on 2024-12-11 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppV', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='entradas/'),
        ),
    ]
