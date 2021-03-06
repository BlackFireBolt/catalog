# Generated by Django 2.2.10 on 2020-02-25 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Название')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='Алиас')),
                ('order', models.SmallIntegerField(db_index=True, default=0, verbose_name='Порядок')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
            ],
            options={
                'verbose_name': 'Подкатегория',
                'verbose_name_plural': 'Подкатегории',
                'ordering': ('super_category__order', 'super_category__name', 'order', 'name'),
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('main.category',),
        ),
        migrations.CreateModel(
            name='SuperCategory',
            fields=[
            ],
            options={
                'verbose_name': 'Надкатегория',
                'verbose_name_plural': 'Надкатегории',
                'ordering': ('order', 'name'),
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('main.category',),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Нзвание')),
                ('slug', models.SlugField(max_length=200, verbose_name='Алиас')),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d', verbose_name='Изображение')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('stock', models.PositiveIntegerField(verbose_name='Остаток')),
                ('available', models.BooleanField(default=True, verbose_name='Наличие')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='main.Category', verbose_name='Категория')),
            ],
            options={
                'ordering': ('name',),
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.AddField(
            model_name='category',
            name='super_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.SuperCategory', verbose_name='Надкатегория'),
        ),
    ]
