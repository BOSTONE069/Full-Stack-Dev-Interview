from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post
from .serializers import PostSerializer

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        """
        The `perform_create` function saves the author of the data as the current user making the
        request.
        
        :param serializer: The serializer parameter in the code snippet refers to an instance of a
        serializer class that is used to validate and process data in Django REST framework. It is
        responsible for converting complex data types like querysets and model instances into native
        Python datatypes that can be easily rendered into JSON, XML, or other content
        """
        serializer.save(author=self.request.user)
        
    def permissions(self):
        """
        The function `permissions` checks the action being performed and returns the appropriate
        permissions based on the action.
        :return: The `permissions` method is returning a list of permission classes based on the value
        of `self.action`. If the action is 'update', 'partial_update', or 'destroy', it returns a list
        containing `IsAuthenticated` and `Author` permissions. Otherwise, it returns a list containing
        only `IsAuthenticated` permission.
        """
        if self.action in ['update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), Author()]
        return [permissions.IsAuthenticated()]
        

# The `Author` class defines a custom permission in Django REST framework to check if the requesting
# user is the author of the object.
class Author(permissions.BasePermission):
    def author_has_object_permission(self, request, view, obj):
        return obj.author == request.user

