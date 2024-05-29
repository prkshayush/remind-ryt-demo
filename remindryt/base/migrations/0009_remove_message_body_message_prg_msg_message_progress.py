# Generated by Django 5.0.3 on 2024-05-28 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_delete_audiorecord'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='body',
        ),
        migrations.AddField(
            model_name='message',
            name='prg_msg',
            field=models.CharField(default='none', max_length=20),
        ),
        migrations.AddField(
            model_name='message',
            name='progress',
            field=models.IntegerField(default=0),
        ),
    ]
