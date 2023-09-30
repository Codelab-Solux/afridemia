from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    #
    path('blog/', blog, name='blog'),
    path('blog/create', create_blogpost, name='create_blogpost'),
    path('blog/<str:pk>/', blogpost, name='blogpost'),
    path('blog/<str:pk>/edit', edit_blogpost, name='edit_blogpost'),
    #
    path('adverts/', adverts, name='adverts'),
    path('adverts/create', create_advert, name='create_advert'),
    path('adverts/<str:pk>/', advert, name='advert'),
    path('adverts/<str:pk>/edit', edit_advert, name='edit_advert'),
    #     path('adverts/<str:pk>/delete', delete_advert, name='delete_advert'),
    #
    path('tutors/', tutors, name='tutors'),
    path('tutors/create', create_tutor, name='create_tutor'),
    path('tutors/<str:pk>/', tutor, name='tutor'),
    path('tutors/<str:pk>/edit', edit_tutor, name='edit_tutor'),
    path('tutors/<str:pk>/follow', follow_tutor, name='follow_tutor'),
    path('tutors/<str:pk>/verify', verify_tutor, name='verify_tutor'),
    path('tutors/<str:pk>/feature', feature_tutor, name='feature_tutor'),

    #     path('tutors/<str:pk>/delete', delete_tutor, name='delete_tutor'),
    #
    path('forum/', forum, name='forum'),
    path('forum/article/create', create_forum_article,
         name='create_forum_article'),
    path('forum/<str:pk>/', forum_article, name='forum_article'),
    path('forum/article/<str:pk>/edit',
         edit_forum_article, name='edit_forum_article'),
    #     path('forum/article/<str:pk>/delete',
    #          delete_forum_article, name='delete_forum_article'),
    path('pricing/', pricing, name='pricing'),

    # -----------------------------------------------------------

    path('about/', about, name='about'),
    path('accessibility/', accessibility, name='accessibility'),
    path('contact/', contact, name='contact'),
    path('faq/', faq, name='faq'),
    path('customer_service/', customer_service, name='customer_service'),
    path('help/', help, name='help'),
    path('how_it_works/', how_it_works, name='how_it_works'),
    path('info/', info, name='info'),
    path('payments/', payments, name='payments'),
    path('parameters_cookies/', parameters_cookies, name='parameters_cookies'),
    path('policy_commercial/', policy_commercial, name='policy_commercial'),
    path('policy_confidential/', policy_confidential,
         name='policy_confidential'),
    path('policy_security/', policy_security, name='policy_security'),
    path('terms_conditions/', terms_conditions, name='terms_conditions'),
    path('sales_conditions/', sales_conditions, name='sales_conditions'),
    path('not_found/', not_found, name='not_found'),


]
