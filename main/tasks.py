from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from datetime import datetime, timedelta

from main.models import Subscription, Course
from users.models import User


@shared_task
def send_updated_email(course_id):

    course = Course.objects.get(pk=course_id)
    subscriptions = Subscription.objects.filter(course=course_id)
    if subscriptions:
        for subscription in subscriptions:
            send_mail(
                subject="Обновление курса!",
                message=f"У курса {course.title} появился новый урок!",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[subscription.subscriber]
            )


@shared_task
def check_user():

    now = datetime.now()
    month_ago = now - timedelta(days=30)
    inactive_users = User.objects.filter(last_login__gt=month_ago)
    inactive_users.update(is_active=False)

    for user in inactive_users:
        user.is_active = False
        user.save()
        print(f'Пользователь {user.username} заблокирован')