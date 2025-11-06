from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

User = get_user_model()

class Page(models.Model):
    # Mínimos: 2 CharField, 1 RichText, 1 Image, 1 Date
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    content = RichTextField()  # texto enriquecido (j)
    image = models.ImageField(upload_to='pages/', blank=True, null=True)  # (e)
    created_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title