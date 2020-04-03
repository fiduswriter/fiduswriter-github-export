from django.db import models

from book.models import Book


class BookRepository(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.deletion.CASCADE
    )
    github_repo_id = models.IntegerField()
    github_repo_full_name = models.CharField(
        max_length=256,
    )