from django.test import TestCase
from django.contrib.auth.models import User
from .models import *

# Create your tests here.

class MovieTest(TestCase):

    @classmethod
    def setUpTestData(self):
        # Crete user
        testuser1 = User.objects.create_user(
            username= 'testuser1',
            password = 'abc123'
        )
        testuser1.save()

        # Create movie
        test_movie= Movie.objects.create(
            author = testuser1,
            title = 'Movie title',
            body = 'Great Movies',
        )
        test_movie.save()
    
    def test_movie_content(self):
        movie = Movie.objects.get(id=1)
        author = f'{movie.author}'
        title = f'{movie.title}'
        body = f'{movie.body}'
        self.assertEqual(author , 'testuser1')
        self.assertEqual(title , 'Movie title')
        self.assertEqual(body , 'Great Movies')