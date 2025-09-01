from django.db import models
from django.utils.translation import gettext_lazy as _ 

class Categories(models.TextChoices):
    LEARN = 'LEARN', 'Learning'
    UN_KNOW = 'UN_KNOW', 'Un_know'   


class NewTodo(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(_("description"), max_length=50)
    date_time = models.DateTimeField(auto_now_add=True)     
    is_status = models.BooleanField(default=False)
    todo_type = models.CharField(
        max_length=20,
        choices=Categories.choices,
        default=Categories.UN_KNOW
    )
