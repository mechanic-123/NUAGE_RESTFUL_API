import json
import unittest

from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from .views import create_iou, create_user, get_users

# Create your tests here.


class UserTestCase(TestCase):
    # Testcases for different scenerio for create user.
    def test_create_user(self):
        url = reverse("create_user")
        response = self.client.post(
            url, data={"user": "prateek"}, content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user_for_invalid_data(self):
        url = reverse("create_user")
        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def test_create_user_for_invalid_method(self):
        url = reverse("create_user")
        response = self.client.get(
            url, data={"user": "prateek"}, content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Testcases for different scenerio for create iou.
    def test_create_iou(self):
        url = reverse("create_iou")

        response = self.client.post(
            url,
            data={
                "lender": "prateek",
                "borrower": "saurabh",
                "amount": 5,
            },
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def test_create_iou_for_inavalid_method(self):
        url = reverse("create_iou")

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Testcases for different scenerio for getting user.
    def test_get_users(self):
        url = reverse("get_users")
        response = self.client.get(
            url,
            data={
                "users": ["prateek"],
            },
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def test_get_users_for_invalid_mathod(self):
        url = reverse("get_users")
        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
