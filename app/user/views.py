"""
Views for the User API.
"""
from rest_framework import generics, permissions
from rest_framework_simplejwt import authentication as jwt_authentication

from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user. (No POST allowed)"""
    serializer_class = UserSerializer
    authentication_classes = [jwt_authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user
