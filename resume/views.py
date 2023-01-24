from django.utils import timezone
from django.views.generic import TemplateView

YEAR = timezone.now().year
# Create your views here.
class HomeView(TemplateView):
    extra_context = {"year": YEAR}
    template_name = "resume/home.html"
