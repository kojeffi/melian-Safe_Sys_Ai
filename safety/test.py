from django.test import Client, TestCase

class SafetyFunctionalTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)  # Check for successful response
        self.assertContains(response.content, b'Recent Safety Alerts')

    def test_list_alerts_view(self):
        response = self.client.get('/safety/list_alerts/')
        self.assertEqual(response.status_code, 200)  # Check for successful response
        self.assertContains(response.content, b'All Safety Alerts')
