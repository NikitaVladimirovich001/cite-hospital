from django.urls import path
from glav import views


urlpatterns = [
    path('', views.index, name='glav'),
    path('post/', views.post, name='post'),
    path('about/', views.about, name='about'),
    path('timeslot/', views.timeslot, name='timeslot'),
    path('kabinet/', views.kabinet, name='kabinet'),
    path('comment/<int:post_id>/', views.comment, name='comment'),
]
