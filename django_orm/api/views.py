from django.db.models import Q, F, Count, Avg, ExpressionWrapper
from django.forms import DecimalField
from rest_framework import viewsets

from book.models import Author, Book, Review
from book.add_init_data import load_data_from_json
from api.serializers import AuthorSerializer, BookSerializer, ReviewSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    queryset = Author.objects.filter(is_active=True)
    queryset = Author.objects.filter(first_name='John')
    queryset = Author.objects.exclude(last_name='Doe')
    queryset = Author.objects.filter(id__in=[1, 3, 5])#Найди авторов с идентификаторами 1, 3 и 5.
    queryset = Author.objects.filter(books__published_date__range=['2023-01-01', '2023-12-31'])# Найди книги, опубликованные с 1 января по 31 декабря 2023 года.
    queryset = Author.objects.filter(last_name__iregex=r'^Mc') # Найди авторов, у которых фамилия начинается на «Mc»
    queryset = Author.objects.filter(Q(first_name='Alice') | ~Q(last_name='Brown')) # Найди книги, у которых цена равна скидке.Найди авторов с именем «Alice» или с фамилией, не равной «Brown».
    queryset = Author.objects.annotate(total_books=Count('books')) # Подсчитай количество книг каждого автора.
    queryset = Author.objects.prefetch_related('books').all() # Получи список авторов и всех их книг так, чтобы было выполнено ровно два SQL-запроса.

    def list(self, request, *args, **kwargs):
        # Запускаем загрузку данных перед выполнением стандартного list
        load_data_from_json()

        return super().list(request, *args, **kwargs)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    queryset = Book.objects.filter(price__lt=500) # Найди все книги, цена которых меньше 500.
    queryset = Book.objects.filter(price__lte=300) # Найди все книги с ценой не более 300.
    queryset = Book.objects.filter(price__gt=1000) # Найди все книги дороже 1000.
    queryset = Book.objects.filter(price__gte=500) # Найди все книги с ценой от 750 и выше.
    queryset = Book.objects.filter(title__contains='django')# Найди все книги, содержащие слово «django» в названии.
    queryset = Book.objects.filter(title__icontains='python')#Найди книги, в названии которых есть «python» (без учёта регистра).
    queryset =  Book.objects.filter(title__startswith='Advanced')# Найди книги, название которых начинается со слова «Advanced».
    queryset =  Book.objects.filter(title__istartswith='pro')# Найди книги, название которых начинается с «pro» (игнорируя регистр).
    queryset = Book.objects.filter(title__endswith='Guide') #Найди книги, название которых заканчивается на слово «Guide».
    queryset = Book.objects.filter(title__iendswith='book') #Найди книги, название которых заканчивается на слово «book» (игнорируя регистр).
    queryset = Book.objects.filter(title__iregex=r'^Python\b') # Ругулярочки.Найди книги, название которых начинается со слова «Python».
    queryset = Book.objects.filter(published_date__year=2024) # Найди книги, опубликованные в 2024 году.
    queryset = Book.objects.filter(published_date__month=6)# Найди книги, опубликованные в июне.
    queryset = Book.objects.filter(published_date__day=11) # Найди отзывы, оставленные 11-го числа любого месяца.
    queryset = Book.objects.filter(published_date__week=1) # Найди книги, опубликованные на 23-й неделе года.
    queryset = Book.objects.filter(published_date__quarter=2)# Найди книги, опубликованные во втором квартале года.
    queryset = Book.objects.filter(published_date__date='2025-06-30') # Найди отзывы, сделанные в определённую дату.
    queryset = Book.objects.filter(price=F('discount')) # Найди книги, у которых цена равна скидке.
    queryset = Book.objects.filter(price__gt=F('discount')) # Найди книги, у которых цена больше скидки.
    queryset = Book.objects.annotate(avg_rating=Avg('reviews__rating')) # Подсчитай средний рейтинг каждой книги.
    queryset = Book.objects.annotate(final_price=ExpressionWrapper(F('price') - F('discount'), output_field=DecimalField())) # Посчитай окончательную цену книги (цена минус скидка).
    queryset = Book.objects.select_related('author').all() # Получи список книг и авторов так, чтобы выполнить всего один SQL-запрос.


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    queryset = Review.objects.filter(comment__isnull=True) # Найди все отзывы без комментариев
    queryset = Review.objects.filter(comment__isnull=False) # Найди все отзывы с комментариями
    queryset = Review.objects.filter(created_at__week_day=2)# Найди отзывы, оставленные во вторник.
    queryset = Review.objects.filter(created_at__hour=15, created_at__minute=30)# Найди отзывы, сделанные ровно в 15:30.
    queryset = Review.objects.filter(created_at__hour__gte=15)# Найди отзывы, сделанные в 15 часов.
    queryset = Review.objects.filter(created_at__minute=30) #Найди отзывы, сделанные в 30 минут любого часа.
    queryset = Review.objects.filter(created_at__second=0)# Найди отзывы, созданные в момент, когда секунды были равны 0.
