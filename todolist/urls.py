from django.urls import path
from todolist.views import register, login_user, logout_user, show_todolist, create_task, get_todolist_json, add_task_async

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'), 
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create-task'),
    path('get_todolist_json/', get_todolist_json, name='get_todolist_json'),
    path('add/', add_task_async, name='add_task_async'),
]