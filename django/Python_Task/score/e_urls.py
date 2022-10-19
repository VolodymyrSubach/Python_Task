from django.urls import path

from score.views import CreateEmployeeView, EmployeeListView

app_name = 'employee'

urlpatterns = [
    path('list/', EmployeeListView.as_view(), name='list'),
    path('create/', CreateEmployeeView.as_view(), name='create')
    ]
