from django.shortcuts import render

finches = [ 
    {'name': 'Canary', 'species': 'Serinus canaria', 'description': 'streak-backed greenish brown', 'lifespan': 15},

]

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
    return render(request, 'finches/index.html', { 'finches': finches })