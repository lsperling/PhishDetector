from abc import ABC

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
