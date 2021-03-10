from rest_framework.test import APIRequestFactory, APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Task


class TasksTests(APITestCase):
    # Create user and save token
    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.user = User.objects.create_user('testuser', email='', password='testing')
        self.user.save()
        token = Token.objects.create(user=self.user)
        token.save()

    # Login user
    def _require_login(self):
        self.client.login(username='testuser', password='testing')

    # Test get tasks by user
    def test_get_tasks(self):
        self._require_login()
        url = reverse('get_tasks')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test add task
    def test_add_task(self):
        self._require_login()
        url = reverse('add_task')
        data = {'title': 'Task a', 'description': 'Description Task a'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.get().title, 'Task a')
        return Task.objects.get(title='Task a').id

    # Test update task
    def test_update_task(self):
        test_task = self.test_add_task()
        self._require_login()
        url = reverse('update_task', kwargs={'task_id': test_task})
        data = {'title': 'Task a Updated'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.get().title, 'Task a Updated')

    # Test delete task
    def test_delete_task(self):
        test_task = self.test_add_task()
        self._require_login()
        url = reverse('delete_task', kwargs={'task_id': test_task})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # Test search task by description
    def test_search_task(self):
        self.test_add_task()
        self._require_login()
        url = reverse('search_task')
        data = {'description': 'Task'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test change status task
    def test_change_status(self):
        test_task = self.test_add_task()
        self._require_login()
        url = reverse('change_state', kwargs={'task_id': test_task})
        data = {'status': True}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.get(id=test_task).status, True)
