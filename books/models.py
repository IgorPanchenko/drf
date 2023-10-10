from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=150, verbose_name='название')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='цена')

