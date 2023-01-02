from rest_framework import serializers
from apps.accounts.models import User, Student, Teacher, UserTypes


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'user_type', 'first_name', 'last_name', 'email', 'password', 'password2')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords don't match")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            user_type=validated_data['user_type'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password'],
        )

        if user.user_type == UserTypes.STUDENT:
            Student.objects.create(user=user)
        elif user.user_type == UserTypes.TEACHER:
            Teacher.objects.create(user=user)

        return user