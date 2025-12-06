from django.db import models


class Deals(models.Model):
    time = models.CharField('Время', max_length=5)
    deal = models.CharField('Дело', max_length=250)

    def __str__(self):
        return self.time

    class Meta:
        verbose_name = 'Deal'
        verbose_name_plural = 'Deals'
