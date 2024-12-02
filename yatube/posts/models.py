from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    # Поле title: название группы
    title = models.CharField(max_length=200, verbose_name="Название группы")
    
    # Поле slug: уникальный адрес группы
    slug = models.SlugField(unique=True, verbose_name="Адрес группы")
    
    # Поле description: описание группы
    description = models.TextField(verbose_name="Описание группы")
    
    # Метод __str__: возвращает поле title при выводе объекта
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,  # Меняем на SET_NULL для nullable ForeignKey
        blank=True,
        null=True,
        related_name='posts'
    )

    class Meta:
        ordering = ['-pub_date']
