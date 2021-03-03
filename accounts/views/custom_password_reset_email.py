from djoser.email import PasswordResetEmail
from django.contrib.auth.tokens import default_token_generator

from djoser import utils
from djoser.conf import settings


class CustomPasswordResetEmail(PasswordResetEmail):
    template_name = "email/password_reset.html"

    def get_context_data(self):
        context = super().get_context_data()

        user = context.get("user")
        uid = utils.encode_uid(user.pk)
        token_with_timestamp = default_token_generator.make_token(user)

        context["token"] = uid + "." + token_with_timestamp
        context["url"] = settings.PASSWORD_RESET_CONFIRM_URL.format(**context)
        return context
