
from  django.contrib  import admin
from django.urls import path
from skapp import views
urlpatterns = [
    path('index/', views.home, name='index'),

    path('about/', views.about, name='about'),


    path('contact/', views.contact, name='contact'),

    path('starter/', views.starter, name='starter'),

    path('properties/', views.properties, name='properties'),

    path('services/', views.services, name='services'),

    path('booking/', views.booking, name='booking'),

    path('show/', views.show, name='show'),

    path('agents/', views.agents, name='agents'),

    path('testimonials/', views.testimonials, name='testimonials'),

    path('service-details/', views.details, name='service-details'),

    path('property-single/', views.single, name='property-single'),

    path('detail/', views.detail, name='detail'),

    path('delete/<int:id>', views.delete),

    path('edit/<int:id>', views.edit),

    path('update/<int:id>', views.update, name='update'),

    path('change/<int:id>', views.change ),

    path('eliminate/<int:id>', views.eliminate),

    path('modify/<int:id>', views.modify, name='modify'),

    path('login/', views.login, name='login'),

    path('', views.register, name='register'),

    path('uploadimage/', views.upload_image, name='upload'),

    path('showimage/', views.show_image, name='image'),


#Mpesa API urls
    path('pay/', views.pay, name='pay'),

    path('stk/', views.stk, name='stk'),

    path('token/', views.token, name='token')
]

