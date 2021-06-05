import base64

import requests


class PhishTank:
    def __init__(self, phish_tank_key:str = None):
        """

        :param phish_tank_key:
        """
        self._phishtank_url = "http://checkurl.phishtank.com/checkurl/"
        self.post_headers = {'format': 'json',
                             'app_key': phish_tank_key, }

    def _compose_phishtank_url_request(self, url_to_check: str) -> str:
        """
        Returns url with added URI for request
        :param url_to_check:
        :return:
        """
        new_check_bytes = url_to_check.encode()
        base64_bytes = base64.b64encode(new_check_bytes)
        base64_new_check = base64_bytes.decode('ascii')
        phishtank_url_request = self._phishtank_url + base64_new_check
        return phishtank_url_request

    def _send_the_request_to_phishtank(self, phishtank_url_request:str) -> requests.Response:
        """
        This function sends a request
        :param phishtank_url_request:
        :return:
        """
        response = requests.request("POST", url=phishtank_url_request, headers=self.post_headers)
        return response

    @staticmethod
    def _get_url_status_from_response(response:requests.Response):
        import xml.etree.ElementTree as ElementTree
        tree = ElementTree.fromstring(response.content)
        phish_data_tree = list(list(list(tree)[1])[0])
        phish_data = { data.tag: data.text for data in phish_data_tree}
        return phish_data

    def check_url(self, url: str) -> bool:
        """

        :param url:
        :return:
        """
        phishtank_url_request = self._compose_phishtank_url_request(url_to_check=url)
        response = self._send_the_request_to_phishtank(phishtank_url_request=phishtank_url_request)

        url_status = self._get_url_status_from_response(response=response)
        return url_status
