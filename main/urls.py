from django.contrib.auth.views import LogoutView
from django.urls import path
from . views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, RegisterUser, LoginUser
urlpatterns = [
    path('', TaskList.as_view(), name='home'),
    path('task/<slug:pk>/detail', TaskDetail.as_view(), name='detail'),
    path('task/create', TaskCreate.as_view(), name='create'),
    path('task/<slug:pk>/edit', TaskUpdate.as_view(), name='update'),
    path('task/<slug:pk>/delete', TaskDelete.as_view(), name='delete'),

    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout')

]