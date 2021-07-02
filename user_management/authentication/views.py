  
from django.contrib.auth.models import User, Group
from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer , GroupSerializer,AddUserToGroupSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    
    
class GroupView(generics.CreateAPIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
class AddUserToGroupView(object):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    import pdb;pdb.set_trace()
    queryset = Group.objects.all()
    
    serializer_class = AddUserToGroupSerializer
    # permission_classes = [permissions.IsAuthenticated]