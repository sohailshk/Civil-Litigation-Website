# In Django, models.py is a file where you define the structure and organization of your database tables
# Each model maps to a single database table, and each attribute of the model represents a column in that table.
from django.db import models


class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    email = models.EmailField()
    feedback = models.TextField()

    def __str__(self):
        return self.name

    
class info(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
