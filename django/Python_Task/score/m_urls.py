from django.urls import path, include

from score.views import CreateMenuView, MenuListView, VoteMenuView

app_name = 'menu'

urlpatterns = [
    path('list/', MenuListView.as_view(), name='list'),
    path('create/', CreateMenuView.as_view(), name='create'),
    path('vote/<int:pk>/', VoteMenuView.as_view(), name='vote'),
    ]
