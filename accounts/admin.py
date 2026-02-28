from django.contrib import admin
from .models import Profile

admin.site.register(Profile)

from .models import StrayReport

admin.site.register(StrayReport)
