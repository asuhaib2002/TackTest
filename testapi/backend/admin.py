from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Performance)
admin.site.register(HourlyPerformance)
admin.site.register(DailyPerformance)

