from django.urls import path
from .views import *

urlpatterns = [
    path('', schools, name='schools'),
    path('create/', create_school, name='create_school'),
    path('my_school/', mySchool, name='my_school'),
    path('<str:pk>/', school, name='school'),
    path('<str:pk>/edit', edit_school, name='edit_school'),
    path('<str:pk>/verify', verify_school, name='verify_school'),
    path('<str:pk>/feature', feature_school, name='feature_school'),
    #
    path('classroom/create', create_classroom, name='create_classroom'),
    path('classroom/<str:pk>/', classroom, name='classroom'),
    path('classroom/<str:pk>/edit', edit_classroom, name='edit_classroom'),
    path('classroom/<str:pk>/delete', delete_classroom, name='delete_classroom'),
    #
    path('teacher/create', create_teacher, name='create_teacher'),
    path('teacher/<str:pk>/', teacher, name='teacher'),
    path('teacher/<str:pk>/edit', edit_teacher, name='edit_teacher'),
    path('teacher/<str:pk>/delete', delete_teacher, name='delete_teacher'),
    #
    path('structure/create', create_structure, name='create_structure'),
    path('structure/<str:pk>/', structure, name='structure'),
    path('structure/<str:pk>/edit', edit_structure, name='edit_structure'),
    path('structure/<str:pk>/delete', delete_structure, name='delete_structure'),
    #
    path('article/create', create_article, name='create_article'),
    path('article/<str:pk>/', article, name='article'),
    path('article/<str:pk>/edit', edit_article, name='edit_article'),
    path('article/<str:pk>/delete', delete_article, name='delete_article'),
    #
    path('gallery/create', create_gallery, name='create_gallery'),
    path('gallery/<str:pk>/', gallery, name='gallery'),
    path('gallery/<str:pk>/edit', edit_gallery, name='edit_gallery'),
    path('gallery/<str:pk>/delete', delete_gallery, name='delete_gallery'),
    #
    path('performance/create', create_performance, name='create_performance'),
    path('performance/<str:pk>/', performance, name='performance'),
    path('performance/<str:pk>/edit', edit_performance, name='edit_performance'),
    path('performance/<str:pk>/delete',
         delete_performance, name='delete_performance'),
]
