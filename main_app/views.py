from django.shortcuts import render
from django.views.generic.edit import CreateView
# in order to use the model, we have to import
from .models import Finch

# finches = [ 
#     {'name': 'Canary', 'species': 'Serinus canaria', 'description': 'streak-backed greenish brown', 'lifespan': 15},

# ]

# Create your views here.

# define the home view
def home(request):
    # unlike EJS templating, we need the html file extension
    return render(request, 'home.html')

# define the about view
def about(request):
    # unlike EJS templating, we need the html file extension
    return render(request, 'about.html')

# define the All Finches view
def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', { 'finches': finches })

# Detail view for a single finch
def finches_detail(request, finch_id):
    # find the finch
    finch = Finch.objects.get(id=finch_id)
    # to check this view function before we have html, use a print!
    # print('this is the finch django found')
    # print(finch)
    return render(request, 'finches/detail.html', { 'finch': finch })

class FinchCreate(CreateView):
  model = Finch
  fields = '__all__'
  success_url = '/finches/{finch_id}'