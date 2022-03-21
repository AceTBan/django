from django.contrib import admin

from vote.models import Choice, Coordonnees, Elections, Personnes, Voter


admin.site.register(Elections)
admin.site.register(Choice)
admin.site.register(Personnes)
admin.site.register(Coordonnees)
admin.site.register(Voter)