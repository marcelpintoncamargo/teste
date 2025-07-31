from django.db import models

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    userId = models.IntegerField(null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
    


