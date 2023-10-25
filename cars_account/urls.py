from django.urls import path

from .views import PositionView, UserProfileView, UserProfileEdit, PositionEdit, UserProfileClient

urlpatterns = [
    path('position', PositionView.as_view(), name="user_position"),
    path('position/<int:pk>', PositionEdit.as_view(), name="user_position_edit"),
    path('userprofile', UserProfileView.as_view(), name="user_profile"),
    path('userprofile/<int:pk>', UserProfileEdit.as_view(), name="user_profile_edit"),
    path('userprofileclient/<int:pk>', UserProfileClient.as_view(), name="user_profile_client"),

]
