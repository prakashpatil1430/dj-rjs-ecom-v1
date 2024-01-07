from rest_framework import serializers
from userauths.models import User, Profile


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__al__'


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = '__al__'

    def to_representation(self, instance):
        # Call the original to_representation method to get the default representation
        response = super().to_representation(instance)
        
        # Serialize the associated User object and add it to the response
        response['user'] = UserSerializer(instance.user).data

        # Return the modified representation
        return response
