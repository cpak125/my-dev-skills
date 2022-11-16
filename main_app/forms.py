from django.forms import ModelForm
from .models import Note, Skill

# Django ModelForm is a class that is used to directly convert a model into a Django form
# custom ModelForm
class NoteForm(ModelForm):
  # declare the Model being used and the fields we want inputs generated for
  class Meta:
    model = Note
    fields = ['date', 'content']

class SkillForm(ModelForm):
  class Meta:
    model = Skill
    fields = ['description', 'level']