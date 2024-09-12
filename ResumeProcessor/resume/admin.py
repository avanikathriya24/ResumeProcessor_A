from django.contrib import admin # type: ignore
from .models import Candidate

# Register the Candidate model so it's visible in the Django admin panel
admin.site.register(Candidate)

