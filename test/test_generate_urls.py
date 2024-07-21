import unittest
from utils import generate_urls_of_all_qualities


class TestGenerateUrlsOfAllQualities(unittest.TestCase):

    def test_default_quality(self):
        url = "https://wx4.sinaimg.cn/x/41d692acgy1hrnmhkowr6j20be0be3yq.jpg"
        expected_urls = [
            "https://wx4.sinaimg.cn/large/41d692acgy1hrnmhkowr6j20be0be3yq.jpg"
        ]
        self.assertEqual(
            sorted(generate_urls_of_all_qualities(url)), sorted(expected_urls)
        )

    def test_multiple_qualities(self):
        url = "https://wx4.sinaimg.cn/large/41d692acgy1hrnmhkowr6j20be0be3yq.jpg"
        expected_urls = [
            "https://wx4.sinaimg.cn/large/41d692acgy1hrnmhkowr6j20be0be3yq.jpg",
            "https://wx4.sinaimg.cn/mw690/41d692acgy1hrnmhkowr6j20be0be3yq.jpg",
        ]
        self.assertEqual(
            sorted(generate_urls_of_all_qualities(url, ["l", "m"])),
            sorted(expected_urls),
        )

    def test_custom_and_mapped_qualities(self):
        url = "https://wx4.sinaimg.cn/abc/41d692acgy1hrnmhkowr6j20be0be3yq.jpg"
        expected_urls = [
            "https://wx4.sinaimg.cn/x/41d692acgy1hrnmhkowr6j20be0be3yq.jpg",
            "https://wx4.sinaimg.cn/large/41d692acgy1hrnmhkowr6j20be0be3yq.jpg",
            "https://wx4.sinaimg.cn/asd/41d692acgy1hrnmhkowr6j20be0be3yq.jpg",
            "https://wx4.sinaimg.cn/mw690/41d692acgy1hrnmhkowr6j20be0be3yq.jpg",
        ]
        self.assertEqual(
            sorted(generate_urls_of_all_qualities(url, ["l", "x", "asd", "m"])),
            sorted(expected_urls),
        )


if __name__ == "__main__":
    unittest.main()
