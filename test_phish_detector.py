import argparse

import validators

from phish_detector import BlackListPhishDetector, PhishDetectorBase


def test_phish_detector(url_to_check: str = None, phish_detector_class: PhishDetectorBase = BlackListPhishDetector):
    """
    Runs several example URLs on given phish detector
    :param url_to_check: URL to check if phish
    :param phish_detector_class: phish detector type
    :return: None
    """
    phish_detector = phish_detector_class()

    if url_to_check is None:
        example_url_list = ["https://ythfdsf.aio49f4vsd.workers.dev/",
                            "https://outlook.hillebrandgroup.com/owa/",
                            "https://www.microsoft.com/he-il/windows/features?activetab=NewPopular&rtcL2"]
        for url in example_url_list:
            phish_detector.check_url(url)
    else:
        phish_detector.check_url(url=url_to_check)


def main():
    """
    Runs phish detection on given addresses
    :return: None
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', default=None)
    args = parser.parse_args()

    if not args.url:
        print("No URL was given, printing example URLs:")
        test_phish_detector()
    elif not validators.url(args.url):
        print("Given input was not a valid URL")
    else:
        test_phish_detector(url_to_check=args.url)


if __name__ == '__main__':
    main()