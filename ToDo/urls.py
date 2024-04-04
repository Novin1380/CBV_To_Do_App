from django.urls import path
from .views import TaskComplete,TaskCreate,TaskListView,TaskUpdate,DeleteView,TaskUndo

app_name = 'ToDo'


urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("create/", TaskCreate.as_view(), name="create_task"),
    path("update/<int:pk>/", TaskUpdate.as_view(), name="update_task"),
    path("complete/<int:pk>/", TaskComplete.as_view(), name="complete_task"),
    path("undo/<int:pk>/", TaskUndo.as_view(), name="undo_task"),
    path("delete/<int:pk>/", DeleteView.as_view(), name="delete_task"),
]