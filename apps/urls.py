from django.urls import path
from apps.views import CourseListAPIView, CourseRetrieveAPIView, UserProfileUpdateAPIView, \
    CategoryRetrieveUpdateAPIView, UserGetMeRetrieveAPIView

urlpatterns = [
    path('user', UserProfileUpdateAPIView.as_view()),
    path('user/get-me', UserGetMeRetrieveAPIView.as_view()),
    path('category/<int:pk>', CategoryRetrieveUpdateAPIView.as_view()),
    path('course', CourseListAPIView.as_view()),
    path('course/<int:pk>', CourseRetrieveAPIView.as_view())
]
