from rest_framework import serializers

from .models import Student
# from .models import Teacher


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','roll','city']

        # field = '__all__'


# class TeacherSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Teacher
#         # fields = ['name','subject','salary','city']
#         field = '__all__'  