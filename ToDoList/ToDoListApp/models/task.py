from django.db import models


class Task(models.Model):

    PRIORITY_CHOICES = (('1', 'High'), ('2', 'Medium'), ('3', 'Low'))

    task_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name="عنوان")
    description = models.CharField(max_length=1000)
    deadline = models.DateField()
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, )
    to_do_lists = models.ManyToManyField(to='ToDoListApp.ToDoList', related_name='tasks')
    users_shared_with = models.ManyToManyField(to='ToDoListApp.MyUser',
                                               related_name='tasks_shared_with_user')
    owner = models.ForeignKey(to='ToDoListApp.MyUser', on_delete=models.SET_NULL, null=True)
