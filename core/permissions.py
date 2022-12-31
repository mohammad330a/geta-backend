from rest_framework.permissions import BasePermission , SAFE_METHODS

class IsStudent(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or 
            request.user and 
            request.user == obj.student.user

        )

class IsInstructor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or 
            request.user and 
            request.user == obj.instructor.user

        )