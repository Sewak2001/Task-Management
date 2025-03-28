from django.urls import path
from .views import *

urlpatterns = [
  path('tasks/', TaskView.as_view(), name='task-list-create'),
  path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
  path('tasks/<int:pk>/status/', TaskStatusUpdateView.as_view(), name='task-status-update'),
  path('tasks/<int:task_id>/members/', TaskMemberView.as_view(), name='task-members'),
  path('tasks/<int:task_id>/members/list/', TaskMembersListView.as_view(), name='task-members-list'),
]
