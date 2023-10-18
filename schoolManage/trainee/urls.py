from django.urls import path
from trainee.views import *

urlpatterns = [
    path('list', traineeList, name='trainee_list'),
    path('add', TraineeAdd.as_view(), name='trainee_add'),
    path('update/<int:id>', TraineeUpdate.as_view(), name='trainee_update'), 
    path('delete/<int:id>', traineeDelete, name='trainee_delete'), 
]