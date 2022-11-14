from django.forms import ModelForm
from .models import Note

# custom ModelForm
class NoteForm(ModelForm):
  # declare the Model being used and the fields we want inputs generated for
  class Meta:
    model = Note
    fields = ['date', 'content']