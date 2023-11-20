from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    image = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categorys'

    # 2 - tis function is trigerd, and it call "product_by_category" url path name and pass catogory url as argument (go to urls.py)
    def get_url(self):
        return reverse('ecommerce_app:product_by_category',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)
    
class Product(models.Model):
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    description = models.TextField(blank=True)
    old_price = models.DecimalField(max_digits=10,decimal_places=2,blank=True)
    new_price = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    # "blank=True" is for optional
    image_1 = models.ImageField(upload_to='product')
    image_2 = models.ImageField(upload_to='product')
    video_file = models.FileField(upload_to='videos')
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    new = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateField(auto_now=True)

    def get_url(self):
        return reverse('ecommerce_app:proDetail',args=[self.category.slug,self.slug])

    def get_discounted_price(self):
        if self.old_price and self.new_price:
            discount_percentage = ((self.old_price - self.new_price) / self.old_price) * 100
            return int(round(discount_percentage))
        return None

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return '{}'.format(self.name)