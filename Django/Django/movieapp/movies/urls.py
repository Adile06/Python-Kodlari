# http://127.0.0.1:8000/
# http://127.0.0.1:8000/home
# http://127.0.0.1:8000/movies
# http://127.0.0.1:8000/movies/3
# http://127.0.0.1:8000/movies/walking-dead

from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home),
    path("movies", views.movies,name="movies")
]
