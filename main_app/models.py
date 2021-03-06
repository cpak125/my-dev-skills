from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

SKILL_LEVELS = (
  (1,'1 - Fundamental Awareness'),
  (2,'2 - Novice'),
  (3,'3 - Intermediate'),
  (4,'4 - Advanced'),
  (5,'5 - Expert'),
)
# Create your models here.
class Skill(models.Model):
  description = models.TextField(max_length=250)
  level =  models.IntegerField(
    'Skill Level',
    choices=SKILL_LEVELS,
    default=SKILL_LEVELS[0][0]
  )
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.name} ({self.id})'

  def get_absolute_url(self):
    return reverse('skills_detail', kwargs={'pk': self.id})  

