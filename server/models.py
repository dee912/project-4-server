from django.db import models

# Create your models here.

class Categories(models.Model):

    name = models.CharField(max_length=50)
    store = models.ForeignKey(
        'self',blank=True,
        null=True,
        related_name='stores',
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return f'{self.name}'

class Store(models.Model):

    name = models.CharField(max_length=50)
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING
    )
    image_shop = models.CharField(max_length=250)
    image_product = models.CharField(max_length=250)
    address  = models.TextField(max_length=250)
    description = models.TextField(max_length=350)
    favourites = models.ManyToManyField(
        'jwt_auth.user',
        related_name='favorites',
        blank=True
    )

    def __str__(self):
        return f'{self.name} - {self.type}'

class Comment(models.Model):

    content = models.TextField(max_length=250)
    store = models.ForeignKey(
        Store,
        related_name='comments',
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
            'jwt_auth.User',
            related_name='comments',
            on_delete=models.CASCADE
        )

    def __str__(self):
        return f'Comment {self.id} on {self.store}'
