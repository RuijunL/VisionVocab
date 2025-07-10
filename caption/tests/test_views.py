import tempfile
from PIL import Image as PILImage
from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

class CaptionViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def create_test_image(self):
        temp_img = tempfile.NamedTemporaryFile(suffix=".jpg")
        image = PILImage.new("RGB", (100, 100), color="blue")
        image.save(temp_img, format="JPEG")
        temp_img.seek(0)
        return SimpleUploadedFile("test.jpg", temp_img.read(), content_type="image/jpeg")

    def test_generate_caption_success(self):
        image_file = self.create_test_image()
        response = self.client.post("/caption/", {"image": image_file})

        self.assertEqual(response.status_code, 200)
        self.assertIn("caption", response.json())

    def test_generate_caption_missing_file(self):
        response = self.client.post("/caption/")
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
