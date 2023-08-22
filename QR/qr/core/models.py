from django.db import models
from django.db.models import Sum , F , Max
# Create your models here.


class qr(models.Model):
    name = models.CharField(max_length=120 , unique=True)
    link = models.CharField(max_length=120)
    image = models.ImageField(upload_to='QRs/')
    counter = models.IntegerField()
    def __str__(self) :
        return self.name
    
    def get_data(self):
        return scan.objects.filter(qr = self).all()
    
    def get_day(self):
        day = scan.objects.filter(qr = self).all().values("date").annotate(total_scan = Max('id'))
        return day
    
class scan(models.Model):
    qr = models.ForeignKey(qr, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    ip = models.CharField(max_length=20)
    count = models.IntegerField()
    def __str__(self):
        return self.qr.name