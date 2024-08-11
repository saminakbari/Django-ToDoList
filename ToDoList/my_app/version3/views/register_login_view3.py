from django.views.generic import TemplateView, RedirectView


class RegisterLogin3(TemplateView):
    template_name = "v3_register_login_template.html"
    pattern_name = "register"

    # def get_redirect_url(self, *args, **kwargs):

