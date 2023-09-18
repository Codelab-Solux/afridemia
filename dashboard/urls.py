from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('schools/', dash_schools, name='dash_schools'),
    path('tutors/', dash_tutors, name='dash_tutors'),
    path('dash_forum/', dash_forum, name='dash_forum'),
    # path('<str:pk>/', school, name='school'),
    # path('<str:pk>/edit', edit_school, name='edit_school'),
    # path('sch_list/', sch_list, name='sch_list'),
]
