from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view_get(self):
        """Test IndexView GET request"""
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "page/index.html")

    @patch("web_2.views.YouTubeCommentService")
    def test_commentfetch_view_post_valid_url(self, MockYTService):
        """Test CommentFetchView POST request with valid YouTube URL"""
        mock_service = MockYTService.return_value
        mock_service.extract_video_id.return_value = "abc123"
        mock_service.fetch_comments.return_value = [
            {"author": "User1", "text": "Nice video!"}
        ]

        response = self.client.post(reverse("get_video_comments"), {
            "video_url": "https://www.youtube.com/watch?v=abc123"
        })

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "page/comments.html")
        self.assertContains(response, "Nice video!")

    @patch("web_2.views.YouTubeCommentService")
    def test_commentfetch_view_post_invalid_url(self, MockYTService):
        """Test CommentFetchView POST request with invalid YouTube URL"""
        mock_service = MockYTService.return_value
        mock_service.extract_video_id.return_value = None

        response = self.client.post(reverse("get_video_comments"), {
            "video_url": "invalid-url"
        })

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "page/index.html")
        self.assertContains(response, "Invalid YouTube URL.")

    @patch("web_2.views.YouTubeCommentService")
    def test_commentfetch_view_get(self, MockYTService):
        """Test CommentFetchView GET request"""
        response = self.client.get(reverse("get_video_comments"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "page/index.html")
