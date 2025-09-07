from django.db import models

class Quote(models.Model):
    text = models.TextField(unique=True)  					# уникальный текст цитаты
    source = models.CharField(max_length=200)  				# источник
    weight = models.PositiveIntegerField(default=1)  		# вес для выбора
    views = models.PositiveIntegerField(default=0)  		# счетчик просмотров
    likes = models.IntegerField(default=0)  				# лайки
    dislikes = models.IntegerField(default=0)  				# дизлайки
    created_at = models.DateTimeField(auto_now_add=True)  	# дата добавления

    def __str__(self):
        return f"{self.text[:50]}..."  # короткое отображение цитаты
