from django.db import models

# Create your models here.
class Shout(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField(max_length=20)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return '{} : {}'.format(self.title, self.content)