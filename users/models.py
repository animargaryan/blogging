from django.db import models


class Role(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, default='')


class Blogger(models.Model):
    id = models.IntegerField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100, blank=True, default='')
    last_name = models.CharField(max_length=100, blank=True, default='')
    role = models.ForeignKey(Role)

    class Meta:
        ordering = ('created',)
