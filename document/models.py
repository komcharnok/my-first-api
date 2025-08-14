from django.db import models

# Create your models here.

class Categories(models.TextChoices):
    EXTENSION = 'EXTENSION', 'Extension'
    UI_FRAMEWORK = 'UI_FRAMEWORK', 'UI Framework'   
    CSS_FRAMEWORK = 'CSS_FRAMEWORK', 'CSS Framework'
    LIBRARY = 'LIBRARY', 'Library'
    TOOL = 'TOOL', 'Tool'

class Document(models.Model):       
    title = models.CharField(max_length=200)
    content = models.JSONField(default=list, blank=True)  
    categories = models.CharField(
        max_length=20,
        choices=Categories.choices,
        default=Categories.EXTENSION
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"