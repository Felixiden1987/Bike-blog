from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post, Comment

class TestProfileView(TestCase):
    
    def setUp(self):
        """ Create a user """
        self.user = User.objects.create_user(username='testuser', password='password123')
        
        """ Create comments for this user """
        self.post1 = Post.objects.create(title='Post 1', slug='post-1', content='Content of post 1', author=self.user)
        self.post2 = Post.objects.create(title='Post 2', slug='post-2', content='Content of post 2', author=self.user)
        
        self.comment1 = Comment.objects.create(body='Comment 1', author=self.user, post=self.post1)
        self.comment2 = Comment.objects.create(body='Comment 2', author=self.user, post=self.post2)
        
        """ Log in the user """
        self.client.login(username='testuser', password='password123')

    def test_profile_view(self):
        response = self.client.get(reverse('profiles'))  

        """ Check that the response is 200 OK """
        self.assertEqual(response.status_code, 200)
        
        """ Check that the correct template is used """
        self.assertTemplateUsed(response, 'profiles/profiles.html')

        """ Check that the comments passed to the template include the comments we created """       
        self.assertIn('comments', response.context)
        """ Since we created 2 comments """
        self.assertEqual(len(response.context['comments']), 2)


    def test_profile_view_not_logged_in(self):
        """ Log out the user """
        self.client.logout()
        
        """ Try to access the profile view """
        response = self.client.get(reverse('profiles'))
        
        """ Check that the response is a redirect (to the login page) """
        self.assertEqual(response.status_code, 302)  
        self.assertRedirects(response, '/accounts/login/?next=/profiles/profiles/')
        