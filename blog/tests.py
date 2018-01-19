from django.test import TestCase
from .view import getposts

class TestBlogViews(TestCase):
    def test_get_blog_page(self):
        page = self.client.get("/blog")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "blogposts.html")
