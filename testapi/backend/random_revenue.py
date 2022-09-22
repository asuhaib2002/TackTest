import random
from backend.models import Performance, DailyPerformance, HourlyPerformance


def database():
    for i in range(10000):
        rCost = random.randint(1,500)
        rRevenue = random.randint(1000,5000)
        rCost1 = random.randint(1,500)
        rRevenue1 = random.randint(1000,5000)
        rCost2 = random.randint(1,500)
        rRevenue2 = random.randint(1000,5000)
        rCost3 = random.randint(1,500)
        rRevenue3 = random.randint(1000,5000)
        obj1 = DailyPerformance.objects.create(cost=rCost,revenue=rRevenue)
        obj1.save()
        obj2 = DailyPerformance.objects.create(cost=rCost1,revenue=rRevenue1)
        obj2.save()
        obj3 = DailyPerformance.objects.create(cost=rCost2,revenue=rRevenue2)
        obj3.save()
        obj4 = DailyPerformance.objects.create(cost=rCost3,revenue=rRevenue3)
        obj4.save()
    return i
        
# database()
    
dailyPerformanceReport = DailyPerformance.objects.filter_by_min_roi(0.5)
print(len(dailyPerformanceReport))
print("Lenght of QuerySet for daily Performances greater than 50 percent roi is",len(dailyPerformanceReport))
print("Lenght of QuerySet for daily Performances greater than 50 percent roi multiplied by 2 is",(len(dailyPerformanceReport)*2))
a=1
for i in dailyPerformanceReport:
    
    rfactor = random.uniform(0.5, 2.0)
    print('Index',a,'/',len(dailyPerformanceReport))
    i.revenue = i.revenue * rfactor
    i.save()
    a=a+1
    
    
    
    