from django.urls import path
from . import views
from .views import  TicketListView, TicketDetailView

urlpatterns = [
path('', TicketListView.as_view(), name='ticketing-home'),
path('<int:pk>/', TicketDetailView.as_view(), name='ticket-detail'),

]

