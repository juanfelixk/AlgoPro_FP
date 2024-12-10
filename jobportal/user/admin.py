from django.contrib import admin
from .models import User

admin.site.register(User)

#register Industry class on http://127.0.0.1:8000/admin to allow modifications of inner class by the superuser