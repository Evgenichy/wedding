from django.db import models


class Vote(models.Model):
    name = models.CharField(max_length=150, blank=True, verbose_name='Имя и фамилия')
    presence = models.ManyToManyField('PresenceVote', blank=True, verbose_name='Присутствие')
    drink = models.ManyToManyField('Drinks', blank=True, verbose_name='Напитки')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Анкета'
        verbose_name_plural = 'Анкеты'


class Drinks(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Напиток'
        verbose_name_plural = 'Напитки'


class PresenceVote(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Присутствие'
        verbose_name_plural = 'Присутствие'

