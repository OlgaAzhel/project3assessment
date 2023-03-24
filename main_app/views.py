from django.shortcuts import render
from .models import Wish
from django.views.generic.edit import CreateView, DeleteView

# Create your views here.

def wishes_index(request):
    wishes = Wish.objects.all()
    return render(request, 'index.html', {'wishes': wishes})


class WishCreate(CreateView):
  model = Wish
  fields = '__all__'


class WishDelete(DeleteView):
  model = Wish
  success_url = '/'
