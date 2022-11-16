# function used to define each route
from django.urls import path 
from . import views


urlpatterns = [
  # defines root path using empty string, maps it to a view function, 
  # kwarg used to reference this route from within templates
  path('', views.home, name='home'),
  path('skills/', views.skills_index, name='skills_index'),
  path('skills/create/', views.skills_create, name='skills_create'),
  # we use angle brackets to declare a URL parameter to capture values within the segments of a URL as follows.
  path('skills/<int:skill_id>', views.skills_detail, name='skills_detail'),
  path('skills/<int:skill_id>/add_note', views.add_note, name='add_note'),
  path('skills/<int:skill_id>/notes/<int:note_id>/delete', views.delete_note, name='delete_note'),
  path('skills/<int:skill_id>/update', views.skills_update, name='skills_update'),
  path('skills/<int:skill_id>/delete', views.skills_delete, name='skills_delete'),
  path('accounts/signup/', views.signup, name='signup'),
]