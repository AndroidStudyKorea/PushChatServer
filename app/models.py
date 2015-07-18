from django.db import models


class Talk(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=30)
    content = models.CharField(max_length=1000, null=False, blank=False)

    class Meta:
        ordering = ('created',)
