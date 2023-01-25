from django.db import models


class Subscriber(models.Model):
    """Подписчик на рассылку электронных писем"""

    name = models.CharField(max_length=64, verbose_name='Имя')
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'
