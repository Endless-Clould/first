from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    pub_date = models.DateField()
    publish = models.ForeignKey('Publish', on_delete=models.CASCADE, null=True)
    authors = models.ManyToManyField("Author")


class Publish(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    email = models.CharField(max_length=255)


class Author(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    au_detail = models.OneToOneField("AuthorDetail", on_delete=models.CASCADE, null=True)


class AuthorDetail(models.Model):
    tel = models.CharField(max_length=255)
    addr = models.CharField(max_length=255)
    birthday = models.DateField()

class Emp(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    dep = models.CharField(max_length=32)
    province = models.CharField(max_length=32)

class Emps(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    dep = models.ForeignKey("Dep", on_delete=models.CASCADE)
    province = models.CharField(max_length=32)


class Dep(models.Model):
    title = models.CharField(max_length=32)

class User(models.Model):
    username =models.CharField(max_length=255)
    password =models.CharField(max_length=255)
    usermsg =models.OneToOneField("Usermsg",on_delete=models.CASCADE,null=True)


class Usermsg(models.Model):
    name =models.CharField(max_length=255)
    age= models.IntegerField()
    sex =models.BooleanField()
    addr =models.CharField(max_length=255)
    tel =models.CharField(max_length=255)
    QQ =models.CharField(max_length=255)