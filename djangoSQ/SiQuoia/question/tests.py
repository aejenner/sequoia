"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from question.models import Question

class answeredTester(TestCase):
  def test_num_answered(self):
    nr = 12323;
    nw = 94246;
    q = Question(num_marked_right=nr, num_marked_wrong=nw);
    na = q.num_answered();
    self.assertEqual(na, nr + nw);

class easeTester(TestCase):
  def test_easiness(self):
    q = Question(text="test",num_marked_right=5,num_marked_wrong=3);
    e = q.easiness();
    q.num_marked_wrong += 5;
    e2 = q.easiness();
    self.assertGreater(e, e2);

class easeTester2(TestCase):
  def test_easiness2(self):
    q = Question(text="text", num_marked_right=523, num_marked_wrong=525)
    e = q.easiness();
    q.num_marked_right += 30;
    e2 = q.easiness();
    self.assertGreater(e2, e);

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
