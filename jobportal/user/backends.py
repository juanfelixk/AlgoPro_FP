from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q #Q is used to check multiple fields

UserModel = get_user_model() #return User

class EmailBackend(ModelBackend):
    def authenticate(self, request, username = None, password = None, **kwargs): #authenticate user
        try:
            user = UserModel.objects.get(Q(username__iexact = username) | Q(email__iexact = username)) #check whether the username or email matches the username parameter
        except UserModel.DoesNotExist: #username does not exist 
            UserModel().set_password(password)
            return #nothing
        except UserModel.MultipleObjectsReturned: #pick the first username if multiple matches
            user = UserModel.objects.filter(Q(useraname__iexact = username) | Q(email__iexact = username)).order_by('id').first()
        if user.check_password(password) and self.user_can_authenticate(user): #check whether password matches
            return user