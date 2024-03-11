from django.urls import path
from proposal import views

urlpatterns = [
    path('proposal/<int:doctor_id>/', views.proposal, name='proposal'),
    path('change_proposal/<int:proposal_id>/', views.change_proposal, name='change_proposal'),
    path('proposals/', views.all_proposals, name='all_proposals'),
]
