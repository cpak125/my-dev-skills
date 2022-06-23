from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Skill

# Create your views here.

# Define the home view
def home(request):
  return render(request, 'home.html')

# Class-Based View to list all skills of logged-in user
class SkillList(ListView):
  model = Skill

  def get_queryset(self):
    return self.request.user.skill_set.all()

# Class-Based View to create/add new skill for logged-in user
class SkillCreate(CreateView):
  model = Skill
  fields = ['description', 'level']
  success_url = '/skills/'

  # This inherited method is called when a valid skill form is being submitted
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    # form.instance is the skill
    form.instance.user = self.request.user
    # Let CreateView do its job as usual
    return super().form_valid(form)

# Class-Based View to get details of a skill
class SkillDetail(DetailView):
  model = Skill

# Define signup functionality
def signup(request):
  error_message = ''
  if request.method == 'POST':
    # create a 'user' form object 
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid:
      # Add the user to the database
      user = form.save()
      # log the user in
      login(request, user)
      return redirect('skills_index')
    else:
        error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request occured, so render
  # signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)



