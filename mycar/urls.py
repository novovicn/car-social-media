from django.urls import path
from . import views

app_name = 'mycar'

urlpatterns = [
    path('create/',views.MyCarCreateView.as_view(),name='create'),
    #path('car_list/',views.MyCarListView.as_view(),name='car_list'),
    path('car_list/',views.car_list,name='car_list'),
    path('<int:pk>/',views.MyCarDetailView.as_view(),name='car_detail'),
    path('<int:pk>/update',views.MyCarUpdateView.as_view(),name='update'),
    path('<int:pk>/delete',views.MyCarDeleteView.as_view(),name='delete'),
    path('<int:pk>/comment',views.add_comment,name='add_comment'),
    path('<int:pk>/comment_delete',views.comment_remove,name='comment_remove'),

    
]