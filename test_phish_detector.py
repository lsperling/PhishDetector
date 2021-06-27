from phish_detector import BlackListPhishDetector


def test_phish_detector():
    phish_detector = BlackListPhishDetector()

    url_to_check = input("Enter URL to check: ")
    phish_detector.check_url(url_to_check)


if __name__ == '__main__':
    test_phish_detector()