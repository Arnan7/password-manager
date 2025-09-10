from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        # SimpleJWT (and other callers) may pass the email under different keys
        # (e.g. username or email). Normalize to `email_value` so we can lookup.
        email_value = None
        if username:
            email_value = username
        elif 'email' in kwargs:
            email_value = kwargs.get('email')
        elif 'username' in kwargs:
            email_value = kwargs.get('username')

        if not email_value:
            # Nothing to authenticate against
            return None

        try:
            user = UserModel.objects.get(email__iexact=email_value)
            if password and user.check_password(password):
                if self.user_can_authenticate(user):
                    return user
        except UserModel.DoesNotExist:
            return None

        return None