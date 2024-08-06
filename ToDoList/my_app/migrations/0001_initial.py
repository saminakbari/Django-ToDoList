# Generated by Django 4.2.11 on 2024-08-06 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('list_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('deadline', models.DateField()),
                ('priority', models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], default='Medium', max_length=6)),
                ('to_do_lists', models.ManyToManyField(related_name='tasks', to='my_app.todolist')),
            ],
        ),
    ]
