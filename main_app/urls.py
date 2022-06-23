from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('skills/', views.SkillList.as_view(), name='skills_index'),
  path('skills/create/', views.SkillCreate.as_view(), name='skills_create'),
  path('skills/<int:pk>', views.SkillDetail.as_view(), name='skills_detail'),
  path('accounts/signup/', views.signup, name='signup'),

]