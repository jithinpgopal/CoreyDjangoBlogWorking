from django.shortcuts import render
from .models  import Casefile
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)



# Create your views here.


# def home(request):
#     return render(request, 'ticketing/home.html')

class TicketListView(ListView):
    model = Casefile
    template_name = 'ticketing/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'Casefile'
    # ordering = ['-date_posted']
    # paginate_by = 5

class TicketDetailView(DetailView):
    model = Casefile
    template_name = 'ticketing/ticket.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'Casefile'
