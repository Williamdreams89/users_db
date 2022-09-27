
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, name, department, role, password=None):
        if not email:
            raise ValueError("Email field cannot be blank")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, department=department, role=role, password=password)

        user.set_password(password)

        user.save(using=self._db)

        return user 

