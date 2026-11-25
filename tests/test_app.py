import unittest

from app import app


class HandbookTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_catalog_and_detail(self):
        catalog = self.client.get("/").get_data(as_text=True)
        self.assertIn("/recipes/syrniki", catalog)
        page = self.client.get("/recipes/syrniki").get_data(as_text=True)
        self.assertIn("Сырники", page)
        self.assertIn("Приготовление", page)

    def test_ingredient_search(self):
        body = self.client.get("/ingredients", query_string={"q": " ТВОРОГ "}).get_data(as_text=True)
        self.assertIn("Сырники", body)
        self.assertNotIn("/recipes/salad", body)

    def test_empty_result(self):
        body = self.client.get("/ingredients?q=mango").get_data(as_text=True)
        self.assertIn("Рецептов с таким ингредиентом пока нет", body)

    def test_navigation(self):
        for path in ["/", "/ingredients", "/recipes/syrniki"]:
            with self.subTest(path=path):
                body = self.client.get(path).get_data(as_text=True)
                self.assertIn('href="/"', body)
                self.assertIn('href="/ingredients"', body)

    def test_unknown_recipe(self):
        self.assertEqual(self.client.get("/recipes/missing").status_code, 404)

