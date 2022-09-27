
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, name, department, role, password=None):
        if not email:

            """Validating email field"""
            raise ValueError("Email field cannot be blank")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, department=department, role=role, password=password)

        """Useful for hashing user passwords"""
        user.set_password(password)

        """Useful for implementing different databases compatibilities"""
        user.save(using=self._db)

        return user 

    def create_superuser(self, email, name, department, role, password):
        user = self.create_user(email, name, department, role)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.set_password(password)

        user.save(using=self._db)

        return user 



