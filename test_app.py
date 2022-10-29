from app import app
from unittest import TestCase
from models import db
# RUN TEST: python3 -m unittest tests_app.py


class RoutingTestCase(TestCase):
    """Testing if routes working properly"""

    def setUp(self):
        """Clean up existing client"""
        app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql:///axon_test'
        db.create_all()

    def tearDown(self):
        """Clean up any fouled transaction"""
        db.session.rollback()
        db.drop_all()

    def test_client_listing(self):
        with app.test_client() as client:
            res = client.get("/")

            self.assertEqual(res.status_code, 200)

    # Test happy data 🙂
    def test_add_client_form(self):
        with app.test_client() as client:
            res = client.post(
                "/",
                data={
                    "firstname": "Daniel",
                    "lastname": "Burns",
                    "phone": "5555555555",
                    "email": "danielburns@pretendmail.com",
                    "goals": "weight loss",
                    "date": "10/31/2022",
                },
            )

            self.assertEqual(res.status_code, 302)

    # Test sad data 🙁
    def test_incomplete_client_form(self):
        with app.test_client() as client:
            res = client.post(
                "/",
                data={
                    "phone": "5555555555",
                    "email": "danielburns@pretendmail.com",
                    "goals": "weight loss",
                    "date": "10/31/2022",
                },
            )

            self.assertEqual(res.status_code, 500)