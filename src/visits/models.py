from django.db import models

# Create your models here.

class PageVisits(models.Model):
    path= models.TextField(blank= True, null= True)
    timestamp= models.DateTimeField(auto_now_add= True)

    # class Meta:
    #     verbose_name_plural= "PageVisits"

    def __str__(self): 
        return f"{self.path} visited"  