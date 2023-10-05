from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from main.models import Course, Lesson, Payment
from users.models import User


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для модели курсов"""

    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор для модели уроков"""

    class Meta:
        model = Lesson
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    """ Сериализотор для модели платежей """

    course = SlugRelatedField(slug_field='name', queryset=Course.objects.all())
    lesson = SlugRelatedField(slug_field='name', queryset=Lesson.objects.all())
    owner = SlugRelatedField(slug_field='first_name', queryset=User.objects.all())

    class Meta:
        model = Payment
        fields = '__all__'


class PaymentForOwnerSerializer(serializers.ModelSerializer):
    """ Сериализотор для модели платежей для использования его в выводе у пользователей """

    class Meta:
        model = Payment
        fields = ['id', 'amount', 'payment_date', 'payment_method']
