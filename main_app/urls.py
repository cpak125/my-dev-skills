# function used to define each route
from django.urls import path 
from . import views


urlpatterns = [
  # defines root path using empty string, maps it to a view function, 
  # kwarg used to reference this route from within templates
  path('', views.home, name='home'),
  path('skills/', views.skills_index, name='skills_index'),
  path('skills/create/', views.SkillCreate.as_view(), name='skills_create'),
  # we use angle brackets to declare a URL parameter to capture values within the segments of a URL as follows.
  path('skills/<int:skill_id>', views.skills_detail, name='skills_detail'),
  path('skills/<int:skill_id>/add_note', views.add_note, name='add_note'),
  path('skills/<int:skill_id>/notes/<int:note_id>/delete', views.delete_note, name='delete_note'),
  # By convention, CBVs that work with individual model instances will expect to find a named parameter of pk 
  path('skills/<int:pk>/update', views.SkillUpdate.as_view(), name='skills_update'),
  path('skills/<int:pk>/delete', views.SkillDelete.as_view(), name='skills_delete'),
  path('accounts/signup/', views.signup, name='signup'),
]