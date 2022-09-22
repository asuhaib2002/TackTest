from django.db import models
# Create your models here.
class PerformanceManager(models.Manager):
    def filter_by_min_roi(self, min_roi):
        QuerySet = Performance.objects.filter(roi__gte = min_roi)
        return QuerySet
    
class DailyPerformanceManager(models.Manager):
    def filter_by_min_roi(self, min_roi):
        QuerySet = DailyPerformance.objects.filter(roi__gte = min_roi)
        return QuerySet
    
class HourlyPerformanceManager(models.Manager):
    def filter_by_min_roi(self, min_roi):
        QuerySet = HourlyPerformance.objects.filter(roi__gte = min_roi)
        return QuerySet
        
        
class Performance(models.Model):
    cost = models.FloatField()
    revenue = models.FloatField()
    creation_date = models.DateField(auto_now_add=True)
    profit = models.FloatField(blank = True)
    roi = models.FloatField(blank = True)
    
    objects = PerformanceManager()
    
    def save(self, *args, **kwargs):
        self.profit = self.revenue - self.cost
        self.roi = self.profit / self.cost
        
        super(Performance, self).save(*args, **kwargs)
        
    
    
    
class HourlyPerformance(Performance):
    datetime = models.DateTimeField(auto_now_add=True)
    objects = HourlyPerformanceManager()
    
    
class DailyPerformance(Performance):
    date = models.DateField(auto_now_add=True)
    objects = DailyPerformanceManager()