from django.db import models

# Create your models here.
class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_title =models.CharField(max_length=25)
    holder_id = models.CharField(max_length=10)
    e_date = models.DateField()
    duration = models.IntegerField()
    e_time = models.TimeField()
    e_detail = models.TextField()
    e_complete = models.BooleanField(default=False)
    capacity = models.IntegerField(default=50)
    place = models.CharField(max_length=10)
    cat_indoor = models.BooleanField()
    cat_category = models.CharField(
        max_length=10,
        choices=[('Career', 'Career'), ('Social', 'Social'), ('Sport', 'Sport'), ('Panel', 'Panel')],
        default='Career',
        validators=[],
    )

    def __str__(self):
        return f"Event {self.event_id}: {self.e_detail}"
