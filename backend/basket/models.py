# from django.db import models

# from authentication.models import User
# from dish.models import Dish


# class Basket(models.Model):
#     user_id = models.ManyToManyField(
#         verbose_name='Пользователь', to=User, related_name='id')
#     dish_id = models.ManyToManyField(
#         verbose_name='Блюдо', to=Dish, related_name='id')

#     def __str__(self):
#         return self.dish_id

#     class Meta:
#         verbose_name = 'В корзине'
#         verbose_name_plural = 'В корзине'
