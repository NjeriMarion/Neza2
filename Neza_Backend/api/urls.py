from django.urls import path
from .views import UserView,UserDetailView
from .views import login, logout
from .views import DashboardListView
from .views import Org
from .views import OrganizationsInStageView, StageTrackingListView, StageTrackingDetailView
from .views import ExtractedDataDetailView,upload_file,ExtractedDataListView,ExtractedDataDeleteView


urlpatterns = [
    path('users/', UserView.as_view(), name = 'user_list_view'),
    path('user/details/', UserDetailView.as_view(), name='user_detail_view'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path("dashboard_location_details/", DashboardListView.as_view(),name="dashboard_list_view"),
    path("stagetracking",StageTrackingListView.as_view(),name="stage-tracking-list"),
    path("stagetrackingdetails/<int:id>/",StageTrackingDetailView.as_view(),name="stage-tracking-detail"),
    path("organizations-in-stage/<str:stage_name>/", OrganizationsInStageView.as_view(), name="organizations-in-stage"),
    path('upload/', upload_file, name='upload_file'),
    path("extracted_data/", ExtractedDataListView.as_view(),name="extracted_data_list_view"),
    path('extracted_data/<int:pk>/', ExtractedDataDetailView.as_view(), name='extracted_data_detail'),
    path('extracted_data/delete/<int:pk>/', ExtractedDataDeleteView.as_view(), name='extracted_data_delete'),
]