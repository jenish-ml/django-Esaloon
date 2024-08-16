from django.db import models

CAT = [
    ('sf', 'Salon / Freelance'),
    ('cs', 'Cosmetic Seller')
]

class Category(models.Model):
    name = models.CharField(max_length=50, default='', verbose_name='Category Name')
    choose = models.CharField(max_length=50, default='', choices=CAT, verbose_name='Category Type')
    
    def __str__(self) -> str:
        return self.name
