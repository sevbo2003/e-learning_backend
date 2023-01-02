from rest_framework import serializers
from apps.accounts.models import User, Student, Teacher, UserTypes


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'user_type', 'first_name', 'last_name', 'email')


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