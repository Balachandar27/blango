from rest_framework import permissions

class AuthorModifyOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
      if request.method in permissions.SAFE_METHODS: # - GET, HEAD and OPTIONS
          return True
      return request.user == obj.author
    
    # def has_permission(self, request, view):
    #   email = getattr(request.user, "email", "")
    #   return email.split("@")[-1] == "example.com"

class IsAdminUserForObject(permissions.IsAdminUser):
    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_staff)