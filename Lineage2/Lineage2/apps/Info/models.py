from django.db import models


class Info(models.Model):
    about_us = models.TextField('Про нас')
    photo = models.ImageField('Фото сервера', upload_to='images', default='contact_default')

    class Meta:
        verbose_name ='Про нас'
        verbose_name_plural ='Про нас'