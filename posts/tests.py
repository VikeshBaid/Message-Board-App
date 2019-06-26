from django.test import TestCase
from django.urls import reverse

from .models import Post

# Create your tests here.
class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(test='Just a test')

    def test_text_content(self):
        post = Post.objects.get(id=1)

        expected_object_name = f'{post.test}'

        self.assertEqual(expected_object_name, 'Just a test')

class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(test='this is another test')

    # View location test
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')

        self.assertEqual(resp.status_code, 200)

    # Url test
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))

        self.assertEqual(resp.status_code, 200)

    # template test
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))

        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'home.html')
