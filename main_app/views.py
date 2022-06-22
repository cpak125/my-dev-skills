from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Skill

# Create your views here.

# Class-Based View to list all skills associated with logged-in user
class SkillList(ListView):
  model = Skill

  def get_queryset(self):
    return self.request.user.skill_set.all()

# Define the home view
def home(request):
  return render(request, 'home.html')

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



