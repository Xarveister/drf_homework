from main.apps import MainConfig
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, PaymentListAPIView, PaymentRetrieveAPIView, PaymentsCreateAPIView, \
    SubscriptionViewSet

app_name = MainConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')
router.register(r'subscription', SubscriptionViewSet, basename='subscription')

urlpatterns = [
                  path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
                  path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
                  path('lesson/<int:pk>/detail/', LessonRetrieveAPIView.as_view(), name='lesson_detail'),
                  path('lesson/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson_update'),
                  path('lesson/<int:pk>/delete/', LessonDestroyAPIView.as_view(), name='lesson_delete'),
                  path('payments/', PaymentListAPIView.as_view(), name='payments_list'),
                  path('payments/<int:pk>/', PaymentRetrieveAPIView.as_view(), name='payments_get'),
                  path('payment/<int:pk>/', PaymentRetrieveAPIView.as_view(), name='payment_retrieve'),
                  path('payments/create/', PaymentsCreateAPIView.as_view(), name='payments_create'),
              ] + router.urls
