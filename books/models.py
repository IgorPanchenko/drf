from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=150, verbose_name='название')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='цена')
    author = models.CharField(max_length=255, verbose_name='автор', default='автор')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
