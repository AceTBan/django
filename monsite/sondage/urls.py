from django.urls import URLPattern, path

from . import views
app_name = "sondage"
urlpatterns = [
    path('', views.index, name="index"),
    
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]