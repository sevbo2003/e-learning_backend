from rest_framework import serializers
from apps.accounts.models import User, Student, Teacher, UserTypes


class UserSerializer(serializers.ModelSerializer):
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


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = ('user', 'is_subsctiption_active', 'subscription_start_date', 'subscription_end_date', 'num_of_unread_activity_notifications')


class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Teacher
        fields = ('user', 'is_verified', 'num_of_unread_activity_notifications')