# Generated by Django 4.2.11 on 2024-08-06 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_alter_myuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='users_shared_with',
            field=models.ManyToManyField(related_name='tasks_shared_with_user', to='my_app.myuser'),
        ),
    ]
