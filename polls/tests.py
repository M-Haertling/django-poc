import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Person, Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)


    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

class CRUDApiTest(TestCase):
    def test_main(self):
        from rest_framework.test import APIClient

        client = APIClient()
        #print(client.login(username='admin', password='admin'))
        print(client.post('/api/persons/', {"name": "Wendy","email": "wendy@gmail.com"}, format='json'))
        assert(Person.objects.all().count(), 1)
        
        print(client.delete('/api/persons/1'))
        assert(Person.objects.all().count(), 0)
