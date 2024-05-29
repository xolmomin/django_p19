from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.filters import CourseFilterSet
from apps.models import Course, User, Category, TeacherUserProxy
from apps.serializers import CourseModelSerializer, UserUpdateModelSerializer, CategoryModelSerializer, \
    UserModelSerializer


class CategoryRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class CourseListAPIView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseModelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CourseFilterSet


class CourseRetrieveAPIView(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseModelSerializer
    permission_classes = IsAuthenticated,


class UserProfileUpdateAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateModelSerializer
    permission_classes = IsAuthenticated,

    def put(self, request, *args, **kwargs):
        """
        hozirgi userni malumotlarini ozgartirish \n
       `ism familya yuborish`
        """
        return super().put(request, *args, **kwargs)


    def get_object(self):
        return self.request.user
#
# class UserGetMeRetrieveAPIView(RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserModelSerializer
#     permission_classes = IsAuthenticated,
#
#     def get_object(self):
#         return self.request.user


class UserGetMeRetrieveAPIView(APIView):
    permission_classes = IsAuthenticated,

    def get(self, request, *args, **kwargs):
        """
        Hozirgi userni olish\n
        `python code`

        """
        return Response(UserModelSerializer(request.user).data)
