from django.db import models

# Create your models here.

class Movie(models.Model) :
    title = models.CharField(max_length=255,null=False,blank=False)
    desc = models.TextField(blank=True)
    rating = models.FloatField()
    duration = models.CharField(max_length=30)
    year = models.CharField(max_length=4,default="2000")
    img = models.ImageField(max_length=None,upload_to='pictures/',default="pictures/none.jpg")
    category = models.CharField(max_length=255,default="")

    def __str__(self) :
        return '{}. {}'.format(self.id,self.title)