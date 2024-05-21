from rest_framework import serializers
from .models import User, Skill, Project, Image

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields =  "__all__"

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields =  "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Project
        fields =  "__all__"
