from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Добавление тестовых данных'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category1 = Category.objects.create(name="Электроника", description="Все электронные устройства")
        category2 = Category.objects.create(name="Одежда", description="Мужская и женская одежда")

        Product.objects.create(name="Смартфон", description="Новый смартфон", price=19999.99, category=category1)
        Product.objects.create(name="Футболка", description="Хлопковая футболка", price=999.99, category=category2)

        self.stdout.write(self.style.SUCCESS("Тестовые данные успешно добавлены!"))
