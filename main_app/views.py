from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# protect view functions/routes dependent upon a user being logged in
from django.contrib.auth.decorators import login_required 
from .models import Skill, Note
# protect class-based views from unauthorized users
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import NoteForm, SkillForm

# Create your views here.

# Define the home view
#  all view functions need to define positional parameter to accept a request object Django passes in
def home(request):
  return render(request, 'home.html')

# Define skills index view
@login_required
def skills_index(request):
  # Perform query operations on a Model to retrieve model objects (rows) 
  # from a database table, via a Manager object.
  # By default, Django adds a Manager to every Model class i.e.,the 'objects' attribute attached to Skill 
  skills = Skill.objects.filter(user=request.user)
  # You could also retrieve the logged in user's skills like this
  # skills = request.user.skill_set.all()
  return render(request, 'skills/index.html', {'skills': skills})

# Define skill create view
@login_required
def skills_create(request):
  # create a ModelForm instance using the data in request.POST or set to None
  skill_form = SkillForm(request.POST or None)
  if(request.method == 'POST'):
    # validate the form
    if skill_form.is_valid():
    # don't save the form to the db until it has the user_id assigned
      new_skill = skill_form.save(commit=False)
      new_skill.user = request.user
      new_skill.save()
      return redirect('skills_detail', skill_id=new_skill.id)  
  return render(request, 'skills/form.html', {'skill_form': skill_form})

# Define skill detail view
@login_required
def skills_detail(request, skill_id):
  # A Manager object is the interface through which database query operations are provided to Django models
  # By default, Django adds a Manager to every Model class - this is the objects attribute
  # Django passes any captured URL parameters as a named argument to the view function i.e., skill_id
  skill = Skill.objects.get(id=skill_id)
  #  when a 1-M or M-M relationship exists, Django creates a related manager object
  # used to access the data related to a model instance.
  # 'note_set' is the related manager object
  # Skill objects have access to their related Note objects
  notes = skill.note_set.all()
  # instantiate NoteForm to be rendered in the template
  note_form = NoteForm()
  # pass a dictionary of data (called the context) to a template called detail.html.
  return render(request, 'skills/detail.html', {
    # include the cat and feeding_form in the context
    'skill': skill,
    'notes': notes,
    'note_form': note_form
})

# Define note create view
@login_required
def add_note(request, skill_id):
  # create a ModelForm instance using the data in request.POST
  form = NoteForm(request.POST)
  # validate the form
  if form.is_valid():
  # don't save the form to the db until it has the skill_id assigned
    new_note = form.save(commit=False)
    new_note.skill_id = skill_id
    new_note.save()
  return redirect('skills_detail', skill_id = skill_id)

# Define note delete view
@login_required
def delete_note(request, skill_id, note_id):
  note = Note.objects.get(id=note_id)
  note.delete()
  return redirect('skills_detail', skill_id=skill_id)

# CBVs that work with a single model instance automatically pass as part 
# of the context two attributes that are assigned the model instance. 
# The attributes are named 'object' and the lowercase name of the Model e.g.,'note', 'skill'

# Define skills update view
def skills_update(request, skill_id):
  skill = Skill.objects.get(id=skill_id)
  form = SkillForm(request.POST or None, instance=skill)

  if request.method == 'POST':
    if form.is_valid():
      form.save()
      return redirect('skills_detail', skill_id=skill_id)
  return render(request, 'skills/form.html', {
    'form': form, 
    'skill': skill
})  

# Define skill delete view
def skills_delete(request, skill_id):
  skill = Skill.objects.get(id=skill_id)
  if request.method == 'POST':
    skill.delete()
    return redirect('skills_index')
  return render(request, 'skills/delete.html', {'skill': skill})  

# Define signup functionality
def signup(request):
  error_message = ''
  if request.method == 'POST':
    # create a 'user' form object that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # Add the user to the database
      user = form.save()
      # log the user in
      login(request, user)
      return redirect('skills_index')
    else:
        error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request occured, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)



