from django.db import models

class Trainer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

class Availability(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=9)  # e.g., 'Monday', 'Tuesday'
    start_time = models.TimeField()
    end_time = models.TimeField()

class Client(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    preferred_days = models.JSONField()  # e.g., {"Monday": ["09:00-10:00", "14:00-15:00"]}


    def __str__(self):
            return f"{self.first_name} {self.last_name}"