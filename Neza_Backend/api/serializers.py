from rest_framework import serializers
from user_registration.models import UserProfile
from dashboard.models import Dashboard
from stagetracking.models import OrganizationStageTracking
from stagetracking.models import OrganizationStage

class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password','org_type', 'website', 'phone_number']

class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model= Dashboard
        fields="__all__"

class ExtractedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtractedData
        fields = '__all__'

class StageTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrganizationStageTracking
        fields="__all__"

class OrgStageSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrganizationStage
        fields="__all__"
