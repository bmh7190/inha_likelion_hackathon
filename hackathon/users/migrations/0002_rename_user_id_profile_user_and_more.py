# Generated by Django 5.0.6 on 2024-06-30 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='user_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_id',
        ),
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
