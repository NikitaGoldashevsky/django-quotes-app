from django.db import models
from django.core.exceptions import ValidationError

class Quote(models.Model):
    text = models.TextField(unique=True)
    source = models.CharField(max_length=200)
    weight = models.PositiveIntegerField(default=1)
    views = models.PositiveIntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text[:50]}..."

    def save(self, *args, **kwargs):
        # не более 3 цитат для одного источника
        if not self.pk:
            count = Quote.objects.filter(source=self.source).count()
            if count >= 3:
                raise ValidationError(f"У источника '{self.source}' уже есть 3 цитаты")
        super().save(*args, **kwargs)
