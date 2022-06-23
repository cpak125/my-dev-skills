from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('skills/', views.SkillList.as_view(), name='skills_index'),
  path('skills/create/', views.SkillCreate.as_view(), name='skills_create'),
  path('skills/<int:pk>', views.SkillDetail.as_view(), name='skills_detail'),
  path('skills/<int:pk>/update', views.SkillUpdate.as_view(), name='skills_update'),
  path('skills/<int:pk>/delete', views.SkillDelete.as_view(), name='skills_delete'),
  path('accounts/signup/', views.signup, name='signup'),
]