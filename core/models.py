from django.db import models



class Tag(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name



class Task(models.Model):
    content = models.TextField(blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(blank=True, null=True)
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)


    class Meta:
        ordering =['-done','-created_time']

    def __str__(self):
        return f"{self.content[:20]}{'...' if len(self.content) > 20 else ''}"
