from django.db import models
from django.core.validators import MinLengthValidator
from django.urls import reverse
# Create your models here.


# Author model (first name, last name, email address) (one to many to Post)
class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length = 30)
    email_address = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Tag model (caption) (Many to Many with Post)
class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption

# Post model (title, excerpt, image name, date, slug, content)
class Post(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    date = models.DateField(auto_now=True)
    excerpt = models.CharField(max_length=200)
    content = models.TextField(validators=[MinLengthValidator(10)])
    slug = models.SlugField(unique=True, db_index=True)
    image = models.CharField(max_length=256)
    tags = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return reverse("post-detail", args=[self.slug])





