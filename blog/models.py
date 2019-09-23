from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pubdate = models.DateTimeField()
    body = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pubdate_custoize(self):
        return self.pubdate.strftime('%b %e %y')




