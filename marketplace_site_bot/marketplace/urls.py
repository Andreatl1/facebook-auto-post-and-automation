from django.urls import path

from . import views

app_name = "marketplace"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:post_id>/", views.detail, name="detail"),
]

#<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>