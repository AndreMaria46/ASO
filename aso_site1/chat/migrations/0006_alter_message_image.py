# Generated by Django 4.1.2 on 2022-12-06 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_alter_message_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='image',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
