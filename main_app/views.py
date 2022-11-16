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
from .forms import NoteForm

# Create your views here.

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
# Define the home view
#  all view functions need to define positional parameter to accept a request object Django passes in
def home(request):
  return render(request, 'home.html')

# • Class-based Views are classes defined in the Django framework 
#   that we can extend and use instead of view functions.
# • All CBVs by default will render templates from a folder inside of the templates folder 
#   with a name the same as the app

# CreateView CBV will automatically:
# • Create a Django ModelForm used to automatically create the form's inputs based on the Model.
# • If the request is a GET, render a template that includes a <form>
# • In the case of a POST, use the posted form's contents 
#   to automatically create data and perform a redirect.
# CreateView renders a default template named as follows: <name of model>_form.html

# Class-Based View to create/add new skill for logged-in user
class SkillCreate(LoginRequiredMixin, CreateView):
  model = Skill
  # fields attribute is required for CreateView, specify what fields from the Model are displayed in the ModelForm
  fields = ['description', 'level']

  # Skill model's get_absolute_url method will rediret to newly added skill's detail page
  # success_url = '/skills/'

  # This inherited method is called when a valid skill form is being submitted
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    # the built-in auth automatically assigns the user to the request object
    form.instance.user = self.request.user  # form.instance is the skill
    # Let CreateView do its job as usual
    return super().form_valid(form)

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

@login_required
def delete_note(request, skill_id, note_id):
  note = Note.objects.get(id=note_id)
  note.delete()
  return redirect('skills_detail', skill_id=skill_id)

# CBVs that work with a single model instance automatically pass as part 
# of the context two attributes that are assigned the model instance. 
# The attributes are named 'object' and the lowercase name of the Model e.g.,'note', 'skill'

# Class-Based View to update a skill
class SkillUpdate(LoginRequiredMixin, UpdateView):
  model = Skill
  fields = ['description', 'level']

# DeleteView automatically renders a confirmation template i.e., <lowercase model>_confirm_delete_html
# Class-Based View to delete a skill
class SkillDelete(LoginRequiredMixin, DeleteView):
  model = Skill
  success_url = '/skills/'


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



