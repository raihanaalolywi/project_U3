from django.db import models
from django.contrib.auth.models import User


# مودل أنواع الهيئات (الأدمن هو الذي يضيفها)
class AuthorityType(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


# مودل لإضافة الهيئات
class Authority(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    # ربط الهيئة بنوع الهيئة
    type = models.ForeignKey(
        AuthorityType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    name = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to="authority/")
    location = models.CharField(max_length=150)
    map_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


# مودل المتحف التابع لهيئة
class Museum(models.Model):
    authority = models.ForeignKey(Authority, on_delete=models.CASCADE)

    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to="museum/")
    location = models.CharField(max_length=150)
    description = models.TextField()

    # حقول جديدة
    open_time = models.TimeField(null=True, blank=True)
    close_time = models.TimeField(null=True, blank=True)
    map_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name
