from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile
import factory


class UserFactory(factory.django.DjangoModelFactory):
    """User factory model"""
    class Meta:
        model = User


class NewUserTestCase(TestCase):
    """Testing new users added to the db"""
    def setUp(self):
        self.link = UserFactory.create(
            username='link',
            email='link@legendofzelda.com'
        )
        self.link.set_password('hyrule')
        self.zelda = UserFactory.create(
            username='zelda',
            email='zelda@legendofzelda.com'
        )
        self.zelda.set_password('hyrule')
        self.ganon = UserFactory.create(
            username='ganon',
            email='ganon@legendofzelda.com'
        )
        self.ganon.set_password('hyrule')

    def test_users_exist(self):
        self.assertTrue(self.link)
        self.assertTrue(self.zelda)
        self.assertTrue(self.ganon)

    def test_users_have_profile(self):
        self.assertTrue(self.link.profile)
        self.assertTrue(self.zelda.profile)
        self.assertTrue(self.ganon.profile)

    def test_profile_has_bio(self):
        self.assertEquals(self.link.profile.bio, '')
        self.assertEquals(self.zelda.profile.bio, '')
        self.assertEquals(self.ganon.profile.bio, '')

    def test_num_users(self):
        self.assertEquals(len(User.objects.all()), 3)

    def test_num_profiles(self):
        self.assertEquals(len(Profile.objects.all()), 3)

    def test_usernames(self):
        self.assertEquals(self.link.username, 'link')
        self.assertEquals(self.zelda.username, 'zelda')
        self.assertEquals(self.ganon.username, 'ganon')

    def test_emails(self):
        self.assertEquals(self.link.email, 'link@legendofzelda.com')
        self.assertEquals(self.zelda.email, 'zelda@legendofzelda.com')
        self.assertEquals(self.ganon.email, 'ganon@legendofzelda.com')

    def test_user_pk_matches_profile_pk(self):
        self.assertEquals(self.link.pk, self.link.profile.pk,)
        self.assertEquals(self.zelda.pk, self.zelda.profile.pk,)
        self.assertEquals(self.ganon.pk, self.ganon.profile.pk,)


class NewUserUnsavedCase(TestCase):
    def setUp(self):
        self.mario = UserFactory.build(
            username='mario',
            email='mario@super.com'
        )
        self.mario.set_password('mushroom')
        self.luigi = UserFactory.build(
            username='luigi',
            email='luigi@super.com'
        )
        self.luigi.set_password('mushroom')

    def test_unsaved_user_exists(self):
        self.assertTrue(self.mario)
        self.assertTrue(self.luigi)

    def test_unsaved_no_id(self):
        self.assertIsNone(self.mario.id)
        self.assertIsNone(self.luigi.id)
