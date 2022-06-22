from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('skills/', views.SkillList.as_view(), name='skills_index'),
  path('accounts/signup/', views.signup, name='signup'),

]