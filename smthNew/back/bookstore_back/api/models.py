from django.db import models


# Create your models here.
class BookManager(models.Manager):
    pass


class Category(models.Model):
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=300)

    def to_json(self):
        return \
            {
                'id': self.id,
                'name': self.name
            }


class Writer(models.Model):
    class Meta:
        verbose_name = 'writer'
        verbose_name_plural = 'writers'

    name = models.CharField(max_length=300)

    def to_json(self):
        return \
            {
                'id': self.id,
                'name': self.name
            }


class Book(models.Model):
    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'

    name = models.CharField(max_length=300)
    description = models.TextField(default='')
    author = models.ForeignKey(Writer, on_delete=models.CASCADE, verbose_name='writer')
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='category')
    rating = models.FloatField()

    objects = BookManager()

    def to_json(self):
        return \
            {
                'id': self.id,
                'name': self.name,
                'description': self.description,
                'price': self.price,
                'category_id': self.category.id,
                'author_name': self.author.name,
                'rating': self.rating,
            }


class BookImage(models.Model):
    class Meta:
        verbose_name = 'book image'

    src = models.ImageField(upload_to='images/')

    book = models.ForeignKey(Book, on_delete=models.CASCADE, default=1, verbose_name='book', related_name='image')