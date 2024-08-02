from unittest import TestCase, main

from project.social_media import SocialMedia


class TestSocialMedia(TestCase):

    def setUp(self):
        self.social_media = SocialMedia("test_user", "Twitter", 1000, "Twitter")
        self.social_media2 = SocialMedia("test_user2", "YouTube", 1000, "YouTube")
        self.social_media2._posts = [
            {"content": "test_post", "likes": 0, "comments": []}
        ]

    def test___init__(self):
        self.assertEqual("test_user", self.social_media._username)
        self.assertEqual("Twitter", self.social_media.platform)
        self.assertEqual(1000, self.social_media.followers)
        self.assertEqual("Twitter content type", self.social_media._content_type)
        self.assertEqual([], self.social_media._posts)

    def test_platform_with_incorrect_input_raises_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.social_media.platform = "Facebook"
        self.assertEqual(
            "Platform should be one of ['Instagram', 'YouTube', 'Twitter']",
            str(ex.exception),
        )

    def test_followers_with_negative_value_raises_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.social_media.followers = -100
        self.assertEqual("Followers cannot be negative.", str(ex.exception))

    def test_create_post_correctly_appends_post_and_returns_string(self):
        expected_string = f"New Twitter post created by test_user on Twitter."
        actual_string = self.social_media.create_post("test_post")

        expected_result = {"content": "test_post", "likes": 0, "comments": []}
        actual_result = self.social_media._posts[0]

        self.assertEqual(expected_string, actual_string)
        self.assertEqual(expected_result, actual_result)

    def test_like_post_with_correct_index_returns_correct_string(self):
        expected_string = f"Post liked by test_user2."
        actual_string = self.social_media2.like_post(0)

        expected_result = {"content": "test_post", "likes": 1, "comments": []}
        actual_result = self.social_media2._posts[0]

        self.assertEqual(expected_string, actual_string)
        self.assertEqual(expected_result, actual_result)

    def test_like_post_when_post_has_reached_maximum_likes_returns_correct_string(self):
        self.social_media2._posts = [
            {"content": "test_post", "likes": 10, "comments": []}
        ]

        expected_string = f"Post has reached the maximum number of likes."
        actual_string = self.social_media2.like_post(0)

        self.assertEqual(expected_string, actual_string)

    def test_like_post_with_incorrect_index(self):
        expected_string = f"Invalid post index."
        actual_string = self.social_media2.like_post(1)

        self.assertEqual(expected_string, actual_string)

    def test_comment_on_post_correctly_appends_comment_and_returns_string(self):
        expected_string = f"Comment added by test_user2 on the post."
        actual_string = self.social_media2.comment_on_post(0, "test_comment")

        expected_result = {"user": "test_user2", "comment": "test_comment"}
        actual_result = self.social_media2._posts[0]["comments"][0]

        self.assertEqual(expected_string, actual_string)
        self.assertEqual(expected_result, actual_result)

    def test_comment_on_post_with_too_short_comment_returns_correct_string(self):
        expected_string = f"Comment should be more than 10 characters."
        actual_string = self.social_media2.comment_on_post(0, "test")

        self.assertEqual(expected_string, actual_string)


if __name__ == "__main__":
    main()
