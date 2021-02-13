from django.urls import path
#from . import views
from .views import HomeView, PostView

urlpatterns = [
    #path('', views.all_blogs, name='all_blogs'),
    path('', HomeView.as_view(), name = "home"),
    path('PostDetail/<int:pk>', PostView.as_view(), name= 'PostDetail'),
]
