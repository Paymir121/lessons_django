from django.contrib import admin
from .models import Author, Book, Review


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('first_name', 'last_name', 'email')
    list_editable = ('is_active',)
    ordering = ('last_name', 'first_name')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'price', 'discount', 'display_final_price')
    list_filter = ('author', 'published_date')
    search_fields = ('title', 'author__first_name', 'author__last_name')
    date_hierarchy = 'published_date'
    raw_id_fields = ('author',)

    def display_final_price(self, obj):
        return obj.price - obj.discount

    display_final_price.short_description = 'Final Price'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'rating', 'created_at', 'short_comment')
    list_filter = ('rating', 'created_at')
    search_fields = ('book__title', 'comment')
    date_hierarchy = 'created_at'

    def short_comment(self, obj):
        if obj.comment:
            return obj.comment[:50] + '...' if len(obj.comment) > 50 else obj.comment
        return ''

    short_comment.short_description = 'Comment'