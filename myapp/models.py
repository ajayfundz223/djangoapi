from django.db import models
from utils.models_abstracts import Model
from django_extensions.db.models import (TitleDescriptionModel, ActivatorModel, TimeStampedModel)

# Create your models here.
class Contact(TitleDescriptionModel, ActivatorModel, TimeStampedModel):
    
    class Meta:
        app_label = 'myapp'
        verbose_name_plural = "Contacts"
        
    email = models.EmailField(verbose_name="Email")
    
    def __str__(self):
        return f'{self.title}'
    