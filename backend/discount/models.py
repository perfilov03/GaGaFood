from django.db import models


class Discount(models.Model):
    title = models.CharField(
        verbose_name='Название акции или скидки', max_length=255)
    description = models.TextField(verbose_name='Описание акции')
    percent = models.IntegerField(verbose_name='Процент скидки')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Скидка / акция'
        verbose_name_plural = 'Скидки и акции'
