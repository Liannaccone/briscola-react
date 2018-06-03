from django.contrib import admin
from hunters_log.models import User
from hunters_log.models import Location
from hunters_log.models import Game
from hunters_log.models import Log

# Register your models here.
admin.site.register(User)
admin.site.register(Location)
admin.site.register(Game)
admin.site.register(Log)
