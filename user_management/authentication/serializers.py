from rest_framework import serializers
from django.contrib.auth.models import User, Group
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.shortcuts import  get_object_or_404


class GroupSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Group
        fields = ('name',)
        
class AddUserToGroupSerializer(serializers.Serializer):    
    # import pdb;pdb.set_trace()
    class Meta:
        model = Group
        fields = ('username','group_name',)
    # username = serializers.CharField()
    # group_name = serializers.CharField()
    # print(username)

    def create(self, attrs):
        import pdb;pdb.set_trace()
        user = get_object_or_404(User, username=attrs.get('username'))
        print(user)
        group = get_object_or_404(Group, name=attrs.get('group_name'))
        group.user_set.add(user)

        if user.groups.filter(name = attrs.get('group_name')):
            return "user added to group"
        else:
            return "User not Added"

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name','groups')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        del validated_data['password2']
        groups_data = validated_data.pop('groups')
        user = User.objects.create(**validated_data)

        user.set_password(validated_data['password'])
        user.save()
        for group_data in groups_data:
            user.groups.add(group_data)

        return user
   

# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     url = serializers.HyperlinkedIdentityField(view_name="authentication:group-detail")
#     class Meta:
#         model = Group
#         lookup_field = 'name'
#         fields = ['name', 'url']

        
    # def create(self, validated_data):
    #     new_group, created = Group.objects.get_or_create(name=validated_data['name'])
    #     new_group.save()
    #     return new_group