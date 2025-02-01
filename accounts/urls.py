from django.urls import path

from .views import ProfileEditView

urlpatterns = [
    path("<int:pk>/edit_profile/", ProfileEditView.as_view(), name="edit_profile"),
]
