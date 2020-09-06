from django.urls import path
from firstapp import views

app_name = "firstapp"

urlpatterns = [
    path('people/', views.PeopleView.as_view(), name="people"),
    path('message/<int:person_id>/', views.MessageView.as_view(), name="message"),
]
