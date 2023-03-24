from django.db import models
from uuid import uuid4

# Create your models here.

class Job(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    script = models.TextField(null=False, blank=False)
    
    class State(models.TextChoices):
        WAITING = 'waiting'
        IN_PROGRESS = 'in-progress'
        DONE = 'done'

    state = models.CharField(choices=State.choices, default=State.WAITING, max_length=20)