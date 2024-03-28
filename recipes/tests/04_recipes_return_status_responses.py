from django.test import TestCase
from django.urls import reverse


class RecipesReturnStatusResponses(TestCase):
    def test_recipe_home_response_status_200_ok(self):
        response = self.client.get(reverse('recipes-home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_category_response_status_200_ok(self):
        response = self.client.get(reverse('category', kwargs={'category_id': 1}))
        self.assertEqual(response.status_code, 200)

    def test_recipe_detail_response_status_200_ok(self):
        response = self.client.get(reverse('recipes-details', kwargs={'recipe_id': 1}))
        self.assertEqual(response.status_code, 200)
