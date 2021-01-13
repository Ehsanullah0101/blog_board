from django.test import TestCase

from django.urls import reverse, resolve
from ..views import home, board_topics, new_topic
from ..models import Board
# Create your tests here.


class HomeTest(TestCase):

    def setUp(self):
        self.Board = Board.objects.create(
            name='Django', description='This is home test')

    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEqual(view.func, home)

    # def test_home_view_contains_link_to_topic_page(self):
    #    board_topic_url = reverse(
    #        'board_topics', kwargs={'board_id': self.Board.pk})
    #
    #    self.assertContains(
    #        self.response, 'href="{0}"'.format(board_topic_url))


class BoardTopicTests(TestCase):

    def setUp(self):
        Board.objects.create(name='Django', description='Django board.')

    def test_board_topics_view_success_status_code(self):
        url = reverse('board_topics', kwargs={'board_id': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs={'board_id': 999})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func, board_topics)


class NewTopicTest(TestCase):
    def setUp(self):
        Board.objects.create(name="Django", decription="new Topic test")

    def new_topic_view_sucess_statuc_code(self):
        url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)
