from unittest.mock import patch

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


# def sample_user(email='test@gmail.com', password='testpass'):
#     """create sameple user"""
#     return get_user_model().objects.create_user(email, password)
#

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@gmail.com'
        password = '123456'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ test the email for a new user is normalized"""
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(email, '123456')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '123465')

    def test_create_new_superuser(self):
        """test create a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            '123455'
        )

        self.assertTrue(user.is_superuser)  # included in permissionsmixin
        self.assertTrue(user.is_staff)
    #
    # def test_tag_str(self):
    #     """test the tag string representation"""
    #     tag = models.Tag.objects.create(
    #         user=sample_user(),
    #         name='Vegan'
    #     )
    #
    #     self.assertEqual(str(tag), tag.name)
    #
    # def test_ingredient_str(self):
    #     """test ingredient string representation"""
    #     ingredient = models.Ingredient.objects.create(
    #         user=sample_user(),
    #         name='Cucumber'
    #     )
    #
    #     self.assertEqual(str(ingredient), ingredient.name)
    #
    # def test_recipe_str(self):
    #     """test the recipe string represetnation"""
    #     recipe = models.Recipe.objects.create(
    #         user=sample_user(),
    #         title='Steak and mushroom sauce',
    #         time_minutes=5,
    #         price=5.00,
    #     )
    #
    #     self.assertEqual(str(recipe), recipe.title)
    #
    # @patch('uuid.uuid4')
    # def test_recipe_file_name_uuid(self, mock_uuid):
    #     """test that image is savid in the correct location"""
    #     uuid = 'test-uuid'
    #     mock_uuid.return_value = uuid
    #     file_path = models.recipe_image_file_path(None, 'myimage.jpg')
    #
    #     exp_path = f'uploads/recipe/{uuid}.jpg'
    #
    #     self.assertEqual(file_path, exp_path)