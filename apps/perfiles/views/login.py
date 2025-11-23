from django.contrib.auth.views import LoginView as BaseLoginView
from ..forms import LoginEmailForm


# View encargada de manejar el proceso de login del usuario
class LoginView(BaseLoginView):
    authentication_form = LoginEmailForm

    # Este es para redireccionar al usuario si ya esta autenticado, por defecto se usa el REDIRECT_LOGIN_URL
    redirect_authenticated_user = True

