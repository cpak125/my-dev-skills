from django.db import models
# import the User
from django.contrib.auth.models import User
from django.urls import reverse

SKILL_LEVELS = (
  # first item represents the value that will be stored in the database
  # second item represents the human-friendly "display" value,
  (1,'1 - Fundamental Awareness'),
  (2,'2 - Novice'),
  (3,'3 - Intermediate'),
  (4,'4 - Advanced'),
  (5,'5 - Expert'),
)

# Create your models here.

# Models represent the database's Schema
# Models are used to perform CRUD data operations on a database.
# A Django Model represents a single entity from the ERD.
# Instances of these models represents a row from the corresponding table.
# Each Model is defined as a Python class that inherits from django.db.models.Model .

# By default, User Model is provided with following attributes:
# username, password, email, first_name, last_name

class Skill(models.Model):
  # each field (attribute) is represented by a Field class, e.g., CharField 
  description = models.TextField(max_length=250, unique=True)
  level =  models.IntegerField(
    'Skill Level',
    choices=SKILL_LEVELS,
    default=SKILL_LEVELS[0][0]
  )
  # the foreign key linking to a user instance
  # by default, creates user_id FK
  # avoids orphan records
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.description} skill level is ({self.get_level_display()})'

  def get_absolute_url(self):
    return reverse('skills_detail', kwargs={'skill_id': self.id})  

class Note(models.Model):
  date = models.DateField()
  content = models.TextField(max_length=250, unique=True, default="")
  # the foreign key linking to a skill instance
  # avoid orphan records
  # by default, creates skill_id FK
  skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.date}: {self.content}"

  class Meta:
    ordering = ['-date']


