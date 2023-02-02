from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('create_book/',views.BookCreateView.as_view(),name='create_view'),
    path('book/<int:pk>/',views.BookDetailView.as_view(),name='book_detail'),
    path('my_view/',views.my_views, name='my_view'),
    path('signup/',views.SignUpView.as_view(),name='signup')
]
