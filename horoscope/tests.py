from django.test import TestCase

from horoscope.views import zodiac_dict


class TestHoroscope(TestCase):

    def test_index(self):
        response = self.client.get('/horoscope/')
        self.assertEqual(response.status_code, 200)

    def test_libra(self):
        response = self.client.get('/horoscope/libra')
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
            response.content.decode()
        )

    def test_libra_redirect(self):
        response = self.client.get('/horoscope/7')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/horoscope/libra')

    def test_zodiacs(self):
        zodiacs = zodiac_dict
        for el in zodiacs:
            response = self.client.get(f'/horoscope/{el}')
            self.assertEqual(response.status_code, 200)
            self.assertIn(
                zodiac_dict[el],
                response.content.decode()
            )

    def test_zodiacs_redirect(self):
        list_of_zodiacs = list(zodiac_dict)
        for i, v in enumerate(list_of_zodiacs, start=1):
            response = self.client.get(f'/horoscope/{i}')
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.url, f'/horoscope/{v}')
