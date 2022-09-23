from backend.models import Performance, DailyPerformance, HourlyPerformance
import time


for x in DailyPerformance.objects.all()[:50]:
    print(x)
    time.sleep(60)
