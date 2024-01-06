from django.contrib import admin
from .models import Book, Author, Address, Country

# Register your models here.
class CountryAdmin(admin.ModelAdmin):
    list_display = ("code", "name")

class AuthorAdmin(admin.ModelAdmin):
    list_diplay = ["first_name","last_name"]
    list_filter = ("first_name", "last_name")


class BookAdmin(admin.ModelAdmin):
    #readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author","rating")
    list_display = ("title","author")


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address)
admin.site.register(Country, CountryAdmin)
