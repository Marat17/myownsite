import datetime
from django.test import TestCase
from django.utils import timezone
from .models import BlogPost
from django.urls import reverse


def create_post(post_text, days):
    """
    Create a post with the given `post_text` and published the
    given number of `days` offset to now (negative for posts published
    in the past, positive for posts that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return BlogPost.objects.create(post_text=post_text, post_date=time)

class BlockPostIndexViewTest(TestCase):
    def test_no_posts(self):
        '''if there are no posts, the appropriate message is displayed'''
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No posts are available.")
        self.assertQuerysetEqual(response.context['alltheposts'], [])

    def test_past_question(self):
        """
        Posts with a post_date in the past are displayed on the
        index page.
        """
        create_post(post_text="Past post.", days=-30)
        response = self.client.get(reverse('index'))
        self.assertQuerysetEqual(
            response.context['alltheposts'],
            ['<BlogPost: Past post.>']
        )

    def test_future_post(self):
    	'''Posts from the future are not displayed on the main page'''
    	create_post(post_text='Future post', days = 30)
    	response = self.client.get(reverse('index'))
    	self.assertContains(response, "No posts are available.")
    	self.assertQuerysetEqual(response.context['alltheposts'], [])


    def test_both_f_and_p(self):
    	#If both past and future posts created, only past posts are displayed

    	create_post(post_text='Past post', days = -30)
    	create_post(post_text='Future post', days = 30)
    	response = self.client.get(reverse('index'))
    	self.assertQuerysetEqual(response.context['alltheposts'],
    		['<BlogPost: Past post>'])


# Create your tests here.
