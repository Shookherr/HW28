from django.db import models


class Location(models.Model):
    name = models.CharField('Название', max_length=256, unique=True)
    lat = models.DecimalField('Широта', max_digits=8, decimal_places=6, null=True, blank=True)
    lng = models.DecimalField('Долгота', max_digits=8, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class UserRoles(models.TextChoices):
    MEMBER = 'member', 'Пользователь'
    MODERATOR = 'moderator', 'Модератор'
    ADMIN = 'admin', 'Администратор'


class User(models.Model):
    first_name = models.CharField('Имя', max_length=128)
    last_name = models.CharField(verbose_name='Фамилия', max_length=128)
    username = models.CharField('Никнейм', max_length=128, unique=True)
    password = models.CharField('Пароль', max_length=128)
    role = models.CharField(choices=UserRoles.choices, max_length=9)
    age = models.PositiveSmallIntegerField()
    location = models.ManyToManyField(Location)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Ad(models.Model):
    name = models.CharField(max_length=256)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.TextField()
    is_published = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True, upload_to='ad_images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
