from .conf import bot
from telebot import types
from django.db import models
from django.urls import reverse
from django.utils import timezone


class UserProfile(models.Model):
    telegram_id = models.BigIntegerField(null=True)
    username = models.CharField(max_length=256, null=True)

    def __str__(self):
        return f"User: {self.username}, ID: {self.telegram_id}"

    class Meta:
        db_table = "userprofile"


class Start(models.Model):
    text = models.TextField(verbose_name="Старт", null=True)

    def __str__(self):
        return f"Text: {self.text}"

    class Meta:
        db_table = "start"

class MinimalDepozitQancha(models.Model):
    text = models.TextField(verbose_name="MinimalDepozitQancha", null=True)

    def __str__(self):
        return f"Text: {self.text}"

    class Meta:
        db_table = "minimal_depozit_qancha"


class OneDeposite(models.Model):
    text = models.TextField(verbose_name="OneDeposite", null=True)

    def __str__(self):
        return f"Text: {self.text}"

    class Meta:
        db_table = "one_deposite"


class CallBack(models.Model):
    text = models.TextField(verbose_name="CallBack", null=True)

    def __str__(self):
        return f"Text: {self.text}"

    class Meta:
        db_table = "call_back"


class Pul(models.Model):
    text = models.TextField(verbose_name="Pul", null=True)

    def __str__(self):
        return f"Text: {self.text}"

    class Meta:
        db_table = "pul"


class Sharhlar(models.Model):
    text = models.TextField(verbose_name="Sharhlar", null=True)

    def __str__(self):
        return f"Text: {self.text}"

    class Meta:
        db_table = "sharhlar"


class SharhlarImage(models.Model):
    sharhlar = models.ForeignKey(Sharhlar, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img/%Y/%m/%d', blank=True)

    class Meta:
        db_table = "sharhlar_images"


class Litsenziya(models.Model):
    image = models.ImageField(upload_to='img/%Y/%m/%d', blank=True)

    class Meta:
        db_table = "litsenziya"