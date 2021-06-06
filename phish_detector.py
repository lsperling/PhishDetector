from abc import ABC

from phish_tank import PhishTank


class PhishDetectorBase(ABC):
    def check_url(self, url):
        raise NotImplementedError('Method not Implemented, please override')


class BlackListPhishDetector:
    def check_url(self, url: str):
        black_list_phish_detector = PhishTank()
        url_data = black_list_phish_detector.check_url(url)
        if url_data['in_database'] == 'false':
            print(f"{url} is unknown for the phishtank database")
        elif url_data['valid'] == 'false':
            print(f"{url} is a legitimate url")
        else:
            print(f"{url} is a phish!!!")


def test_phish_detector():
    phish_detector = BlackListPhishDetector()   # can easily switch between different detector implementation

    example_url_list = ["https://ythfdsf.aio49f4vsd.workers.dev/",
                        "https://outlook.hillebrandgroup.com/owa/",
                        "https://www.microsoft.com/he-il/windows/features?activetab=NewPopular&rtcL2"]
    for url in example_url_list:
        phish_detector.check_url(url)


if __name__ == '__main__':
    test_phish_detector()