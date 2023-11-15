from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),

    path('', views.index, name='task-home'),
    path('all', views.all_tasks, name='all-tasks'),

    path('add-task', views.create_task, name='add-task'),
    path('update-task/<task_id>', views.update_task, name='update-task'),
    path('delete-task/<pk>', views.delete_task, name='delete-task'),

]