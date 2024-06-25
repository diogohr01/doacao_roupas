from django.contrib.auth.backends import ModelBackend
from accounts.models import User

class AccountBackend(ModelBackend):
    def authenticate(self, request, name=None, senha=None, **kwargs):
        try:
            user = User.objects.get(name=name)
        except User.MultipleObjectsReturned as e:
            users = User.objects.filter(name=name)
        print(f"get() returned more than one User -- it returned {e.count()}!")
        if users.exists():
            for user in users:
                if user.check_senha(senha) and self.user_can_authenticate(user):
                    return user
        return None

    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return None
        
    
