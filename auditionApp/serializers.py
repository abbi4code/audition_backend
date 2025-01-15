from rest_framework import serializers
from .models import AuditionPortal,DesignWorkshop,ValorantGaming,BgmiGaming


class AuditionPortalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditionPortal
        fields =  "__all__"

class DesignWorkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesignWorkshop
        fields =  "__all__"

class ValorantGamingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValorantGaming
        fields =  "__all__"

class BgmiGamingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BgmiGaming
        fields =  "__all__"