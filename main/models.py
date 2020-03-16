from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='Алиас')
    order = models.SmallIntegerField(default=0, db_index=True, verbose_name='Порядок')
    super_category = models.ForeignKey('SuperCategory', on_delete=models.PROTECT, null=True,
                                       blank=True, verbose_name='Надкатегория')


class SuperCategoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(super_category__isnull=True)


class SuperCategory(Category):
    objects = SuperCategoryManager()

    def __str__(self):
        return self.name

    class Meta:
        proxy = True
        ordering = ('order', 'name', )
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class SubCategoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(super_category__isnull=False)


class SubCategory(Category):
    objects = SubCategoryManager()

    def __str__(self):
        return '%s - %s' % (self.super_category.name, self.name)

    class Meta:
        proxy = True
        ordering = ('super_category__order', 'super_category__name',
                    'order', 'name', )
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def get_absolute_url(self):
        return reverse('main:product_list_by_category',
                       args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(SubCategory, related_name='products', on_delete=models.PROTECT,
                                 verbose_name='Категория')
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='Алиас')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    stock = models.PositiveIntegerField(verbose_name='Остаток')
    available = models.BooleanField(default=True, verbose_name='Наличие')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    OPTIONS = (
        ('n', 'Не установлено'),
        ('b', 'Лидер продаж'),
        ('s', 'Скидка'),
    )
    status = models.CharField(max_length=1, choices=OPTIONS, blank=True, default='n',
                              verbose_name='Статус')
    discount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Скидка', blank=True, default=0)

    class Meta:
        ordering = ('-created', 'available', )
        index_together = (('id', 'slug'), )
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:product_detail',
                       args=[self.id, self.slug])
