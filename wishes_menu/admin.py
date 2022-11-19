from django.contrib import admin
from .models import Birthday, EmailBroadcast


admin.site.register(Birthday)
admin.site.register(EmailBroadcast)