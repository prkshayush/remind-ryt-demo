# Generated by Django 5.0.3 on 2024-05-29 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_message_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='prg_msg',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='task',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
