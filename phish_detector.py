import argparse
from abc import ABC

import validators

from phish_tank import PhishTank


class PhishDetectorBase(ABC):
    """
    Abstract phish detector class to define unified interface of child detectors
    """
    def check_url(self, url: str):
        """
        Abstract check url status method all child detectors must implement
        :param url: url address
        :return: None
        """
        raise NotImplementedError('Method not Implemented, please override')


class BlackListPhishDetector(PhishDetectorBase):
    """
    Blacklist phish detector class
    """
    def check_url(self, url: str):
        """
        Implements blacklist phish detector
        :param url: url address
        :return: None
        """
        black_list_phish_detector = PhishTank()
        url_data = black_list_phish_detector.check_url(url)
        if url_data['in_database'] == 'false':
            print(f"{url} is unknown for the phishtank database")
        elif url_data['valid'] == 'false':
            print(f"{url} is a legitimate url")
        else:
            print(f"{url} is phish!!!")


def test_phish_detector():
    """
    Runs phish detection on given addresses
    :return: None
    """
    phish_detector = BlackListPhishDetector()   # can easily switch between different detector implementation

    parser = argparse.ArgumentParser()
    parser.add_argument('--url', default=None)
    args = parser.parse_args()

    if not args.url:
        print("No URL was given, printing example URLs:")
        example_url_list = ["https://ythfdsf.aio49f4vsd.workers.dev/",
                        "https://outlook.hillebrandgroup.com/owa/",
                        "https://www.microsoft.com/he-il/windows/features?activetab=NewPopular&rtcL2"]
        for url in example_url_list:
            phish_detector.check_url(url)
    elif not validators.url(args.url):
        print("Given input was not a valid URL")
    else:
        phish_detector.check_url(args.url)


if __name__ == '__main__':
    test_phish_detector()
