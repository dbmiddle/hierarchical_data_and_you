from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from mpttfun.models import Filesystem
# Register your models here.

admin.site.register(Filesystem, DraggableMPTTAdmin)
