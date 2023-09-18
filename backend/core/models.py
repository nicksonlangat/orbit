import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-updated_at",]

class Organization(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    url = models.URLField()
    
    def __str__(self) -> str:
        return str(self.url)

class Tag(BaseModel):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self) -> str:
        return self.name


class TagSelection(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    
    def __str__(self) -> str:
        return f"{self.user.username}'s tags"
