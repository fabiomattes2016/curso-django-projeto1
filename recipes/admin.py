from django.contrib import admin
from .models import Recipe, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'is_published', 'created_at']
    list_display_links = ['title', 'created_at']
    search_fields = 'id', 'title', 'description', 'slug',
    list_filter = 'category', 'author', 'is_published',
    list_per_page = 10
    list_editable = 'is_published',
    ordering = '-id',
    prepopulated_fields = {"slug": ('title',)}

# admin.site.register(Recipe)
# admin.site.register(Category, CategoryAdmin)
