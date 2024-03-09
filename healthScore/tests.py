from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from datetime import datetime
import json

from healthScore.models import (
    HealthRecord,
    Hospital,
    User,
    HospitalStaff,
    Appointment,
)
from healthScore.views import (
    view_health_history, 
    view_health_history_requests,
    login_view,
    registration
)

### views.py
class viewHealthHistoryTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

        # Adding data to the Hospital table
        h1 = Hospital.objects.create(
            name="Hospital A",
            address="Address A",
            email="hospital_a@example.com",
            password="123456",
            contactInfo="123456781",
            status="approved",
        )
        h2 = Hospital.objects.create(
            name="Hospital B",
            address="Address B",
            email="hospital_b@example.com",
            password="123456",
            contactInfo="123456781",
            status="pending",
        )
        h3 = Hospital.objects.create(
            name="Hospital C",
            address="Address C",
            email="hospital_c@example.com",
            password="123456",
            contactInfo="123456781",
            status="rejected",
        )
        h4 = Hospital.objects.create(
            name="Hospital D",
            address="Address D",
            email="hospital_d@example.com",
            password="123456",
            contactInfo="123456781",
            status="pending",
        )

        # Adding hospitalStaff data
        HospitalStaff.objects.create(
            hospitalID=h1,
            admin=True,
            name="Admin A",
            email="admin_a@hospitala.com",
            password="pass1234",
            specialization="",
            contactInfo="1234567890",
        )
        HospitalStaff.objects.create(
            hospitalID=h1,
            admin=False,
            name="Doctor A",
            email="doctor_a@hospitala.com",
            password="pass1234",
            specialization="Anesthesiology",
            contactInfo="1234567890",
        )
        HospitalStaff.objects.create(
            hospitalID=h2,
            admin=True,
            name="Admin B",
            email="admin_b@hospitalb.com",
            password="pass1234",
            specialization="",
            contactInfo="1234567890",
        )
        HospitalStaff.objects.create(
            hospitalID=h2,
            admin=False,
            name="Doctor B",
            email="doctor_b@hospitalb.com",
            password="pass1234",
            specialization="Cardiology",
            contactInfo="1234567890",
        )
        HospitalStaff.objects.create(
            hospitalID=h3,
            admin=True,
            name="Admin C",
            email="admin_c@hospitalc.com",
            password="pass1234",
            specialization="",
            contactInfo="1234567890",
        )
        HospitalStaff.objects.create(
            hospitalID=h3,
            admin=False,
            name="Doctor C",
            email="doctor_c@hospitalc.com",
            password="pass1234",
            specialization="Dermatology",
            contactInfo="1234567890",
        )
        HospitalStaff.objects.create(
            hospitalID=h4,
            admin=True,
            name="Admin D",
            email="admin_d@hospitald.com",
            password="pass1234",
            specialization="",
            contactInfo="1234567890",
        )
        HospitalStaff.objects.create(
            hospitalID=h4,
            admin=False,
            name="Doctor D",
            email="doctor_d@hospitald.com",
            password="pass1234",
            specialization="Forensic Pathology",
            contactInfo="1234567890",
        )

        # Adding user data
        u1 = User.objects.create(
            email="user1@example.com",
            name="User1",
            password="userpass1",
            username="user1",
            dob="1990-01-01",
            contactInfo="1234567890",
            proofOfIdentity="Proof1",
            address="Address1",
            securityQues="",
            securityAns="",
            bloodGroup="A+",
        )
        u2 = User.objects.create(
            email="user2@example.com",
            name="User2",
            password="userpass2",
            username="user2",
            dob="1990-01-01",
            contactInfo="1234567890",
            proofOfIdentity="Proof2",
            address="Address2",
            securityQues="",
            securityAns="",
            bloodGroup="B+",
        )
        u3 = User.objects.create(
            email="user3@example.com",
            name="User3",
            password="userpass3",
            username="user3",
            dob="1990-01-01",
            contactInfo="1234567890",
            proofOfIdentity="Proof3",
            address="Address3",
            securityQues="",
            securityAns="",
            bloodGroup="O+",
        )
        u4 = User.objects.create(
            email="user4@example.com",
            name="User4",
            password="userpass4",
            username="user4",
            dob="1990-01-01",
            contactInfo="1234567890",
            proofOfIdentity="Proof4",
            address="Address4",
            securityQues="",
            securityAns="",
            bloodGroup="AB+",
        )

        # Adding appointment Data
        a1 = Appointment.objects.create(
            name="Vaccine",
            properties=json.dumps(
                {"type": "vaccine A", "dose_2": False, "date": datetime.now()},
                default=str,
            ),
        )
        a2 = Appointment.objects.create(
            name="Vaccine",
            properties=json.dumps(
                {"type": "vaccine A", "dose_2": True, "date": datetime.now()},
                default=str,
            ),
        )
        a3 = Appointment.objects.create(
            name="Blood test",
            properties=json.dumps(
                {"type": "Iron check", "dose_2": False, "date": datetime.now()},
                default=str,
            ),
        )
        a4 = Appointment.objects.create(
            name="MRI",
            properties=json.dumps(
                {"type": "N/A", "dose_2": False, "date": datetime.now()}, default=str
            ),
        )

        # healthRecord data
        HealthRecord.objects.create(
            doctorID=2,
            userID=u1,
            hospitalID=1,
            status="approved",
            createdAt=datetime.now(),
            updatedAt=datetime.now(),
            appointmentId=a1,
            healthDocuments="",
        )
        HealthRecord.objects.create(
            doctorID=2,
            userID=u2,
            hospitalID=2,
            status="rejected",
            createdAt=datetime.now(),
            updatedAt=datetime.now(),
            appointmentId=a2,
            healthDocuments="",
        )
        HealthRecord.objects.create(
            doctorID=3,
            userID=u3,
            hospitalID=3,
            status="approved",
            createdAt=datetime.now(),
            updatedAt=datetime.now(),
            appointmentId=a3,
            healthDocuments="",
        )
        HealthRecord.objects.create(
            doctorID=4,
            userID=u4,
            hospitalID=4,
            status="pending",
            createdAt=datetime.now(),
            updatedAt=datetime.now(),
            appointmentId=a4,
            healthDocuments="",
        )

    def test_view_history(self):
        url = reverse("view_health_history")

        # appointment name healthcare_worker, healthcare_facility and date are passed
        request_struct = {
            "appointment_name": "Vaccine",
            "healthcare_worker": "Doctor A",
            "healthcare_facility": "Hospital A",
            "date": "2024-03-08",
        }
        request = self.factory.get(url, request_struct)
        response = view_health_history(request)

        self.assertEqual(response.status_code, 200)

    def test_view_history_requests(self):
        url = reverse("view_requests")

        # appointment name healthcare_worker, healthcare_facility date and record_status are passed
        request_struct = {
            "appointment_name": "Vaccine",
            "healthcare_worker": "Doctor A",
            "healthcare_facility": "Hospital A",
            "date": "2024-03-08",
            "record_status": "approved",
        }
        request = self.factory.get(url, request_struct)
        response = view_health_history_requests(request)

        self.assertEqual(response.status_code, 200)

class HomepageViewTest(TestCase):
    def test_homepage_view(self):
        response = self.client.get(reverse('homepage')) # test the view
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'homepage.html')

class LoginViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='test@example.com',
            password='testpassword'
        )

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_post_request_valid_credentials(self):
        response = self.client.post(reverse('login'), {
            'email': 'test@example.com', 
            'password': 'testpassword'})
        self.assertRedirects(response, reverse('homepage'))

    def test_post_request_invalid_credentials(self):
        response = self.client.post(reverse('login'), {
            'email': 'test@example.com', 
            'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Invalid email or password. Please try again.', response.content.decode())

class RegistrationViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='test@example.com',
            password='testpassword',
            username='testuser',
            name='Test User'
        )
    
    def test_registration_view(self):
        response = self.client.get(reverse('registration'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration.html')

    def test_post_request_email_exist(self):
        response = self.client.post(reverse('registration'), {
            'email': 'test@example.com', 
            'password': 'testpassword'})
        user = User.objects.get(email='test@example.com')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(response.status_code, 200)
        self.assertIn("An account already exists for this email address. Please log in.",response.content.decode())

    def test_post_request_username_exist(self):
        response = self.client.post(reverse('registration'), {
            'username': 'testuser', 
            'password': 'testpassword'})
        user = User.objects.get(username='testuser')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Username already exists. Please choose a different one.", response.content.decode())
    
    def test_post_request_new_user_registered(self):
        response = self.client.post(reverse('registration'), {
            'email': 'newuser@example.com', 
            'password': 'newpassword', 
            'username': 'newuser',
            'fullname': 'New User',
            'gender': 'female',
            'phone_number': '0000000000',
            'street_address:': '1 High St',
            'city': 'Jersey City',
            'state': 'NJ'
            })
        user = User.objects.get(email='newuser@example.com')
        self.assertEqual(user.email, 'newuser@example.com')
        self.assertRedirects(response, reverse('homepage'))

### models.py
class CustomUserManagerTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        email = "test@example.com"
        password = "testpassword"
        user = User.objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.check_password(password))

    def test_create_superuser(self):
        User = get_user_model()
        email = "admin@example.com"
        password = "adminexample"
        user = User.objects.create_superuser(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.check_password(password))

    def test_create_user_missing_email(self):
        User = get_user_model()
        with self.assertRaises(ValueError):
            User.objects.create_user(email=None, password="testpassword")


class UserTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='test@exmaple.com',
            username='testuser',
            password='password',
            name='Test User'
        )

    def test_get_full_name(self):
        full_name = self.user.get_full_name()
        self.assertEqual(full_name, 'Test User')
    
    def test_get_short_name(self):
        short_name = self.user.get_short_name()
        self.assertEqual(short_name, 'testuser')