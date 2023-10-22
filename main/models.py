from django.db import models

from config import settings
from users.models import NULLABLE


class Course(models.Model):
    """Модель курсов"""
    course_name = models.CharField(max_length=250, verbose_name='Наименование')
    course_preview = models.ImageField(upload_to='main/course/', verbose_name='Превью', **NULLABLE)
    course_description = models.TextField(verbose_name='Описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='владелец курса',
                              **NULLABLE)
    price = models.PositiveIntegerField(default=0, verbose_name='Цена')

    def __str__(self):
        return f'{self.course_name}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    """Модель уроков"""
    lesson_name = models.CharField(max_length=250, verbose_name='Наименование', **NULLABLE)
    lesson_description = models.TextField(verbose_name='Описание')
    lesson_preview = models.ImageField(upload_to='main/lesson/', verbose_name='Превью', **NULLABLE)
    video_url = models.URLField(verbose_name='Ссылка на видео', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='владелец урока',
                              **NULLABLE)

    def __str__(self):
        return f'{self.lesson_name}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Payment(models.Model):
    METHOD_CHOICES = (
        ('CASH', 'Наличные'),
        ('TRANSFER', 'Перевод на счет'),
    )
    CURRENCY = [
        ('usd', 'USD'),
        ('eur', 'EURO')
    ]

    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата оплаты')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Оплаченный курс')
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Оплаченный урок')
    amount = models.PositiveIntegerField(verbose_name='Сумма оплаты')
    method = models.CharField(max_length=20, verbose_name='Метод оплаты', default='transfer', choices=METHOD_CHOICES)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='владелец платежа',
                              **NULLABLE)
    currency = models.CharField(choices=CURRENCY, verbose_name='валюта', default='usd')
    stripe_id = models.CharField(max_length=100, verbose_name='Stripe ID', **NULLABLE)
    stripe_status = models.CharField(max_length=50, verbose_name='Stripe статус', **NULLABLE)

    def __str__(self):
        return f'Платеж от {self.user} на сумму {self.amount}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'


class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             verbose_name="пользователь подписки", )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', **NULLABLE)
    is_subscribed = models.BooleanField(default=False, verbose_name='статус подписки')

    def __str__(self):
        return f"{self.user} - {self.course}"

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
