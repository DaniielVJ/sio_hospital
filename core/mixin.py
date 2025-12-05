from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class MatronaRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    pass
