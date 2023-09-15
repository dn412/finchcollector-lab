from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# in order to use the model, we have to import
from .models import Finch
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Finch, Toy
# Import the FeedingForm
from .forms import FeedingForm




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
    # instantiate FeedingForm to be rendered in the template
    feeding_form = FeedingForm()
    id_list = finch.toys.all().values_list('id')
    toys_finch_doesnt_have = Toy.objects.exclude(id__in=id_list)
    return render(request, 'finches/detail.html', { 'finch': finch, 'feeding_form': feeding_form, 'toys': toys_finch_doesnt_have })

def add_feeding(request, finch_id):
  # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the finch_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.finch_id = finch_id
    new_feeding.save()
  return redirect('detail', finch_id=finch_id)

class FinchCreate(CreateView):
  model = Finch
  fields = ['name', 'species', 'description', 'lifespan']

class FinchUpdate(UpdateView):
  model = Finch
  # Let's disallow the renaming of a finch by excluding the name field!
  fields = ['species', 'description', 'lifespan']

class FinchDelete(DeleteView):
  model = Finch
  success_url = '/finches'


# Views for Toys

# ToyList
class ToyList(ListView):
    model = Toy
    template_name = 'toys/index.html'

# ToyDetail
class ToyDetail(DetailView):
    model = Toy
    template_name = 'toys/detail.html'

# ToyCreate
class ToyCreate(CreateView):
    model = Toy
    fields = ['name', 'color']

    def form_valid(self, form):
        return super().form_valid(form)
    
# ToyUpdate
class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

# ToyDelete
class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'

# adds toy to finch
def assoc_toy(request, finch_id, toy_id):
   
    Finch.objects.get(id=finch_id).toys.add(toy_id)
    return redirect('detail', finch_id=finch_id)

# removes toy from finch
def unassoc_toy(request, finch_id, toy_id):
    # to make the association, we target the finch and pass the toy id
    Finch.objects.get(id=finch_id).toys.remove(toy_id)
    return redirect('detail', finch_id=finch_id)