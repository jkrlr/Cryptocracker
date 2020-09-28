from django.contrib import admin
from .models import Contests, Questions, Leaderboard, Registrations, Team
# Register your models here.

admin.site.register(Contests)
admin.site.register(Questions)
admin.site.register(Leaderboard)
admin.site.register(Registrations)
admin.site.register(Team)