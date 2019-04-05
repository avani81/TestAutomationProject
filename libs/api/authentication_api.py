import requests


class AuthenticationAPI:

    def __init__(self):
        self.base_url = 'https://api.themoviedb.org/'

    def get_guest_session_id(self, api_key):
        url = self.base_url + '/3/authentication/guest_session/new'
        payload = {'api_key': api_key}
        response = requests.request("GET", url, params=payload)
        r = response.json()
        return r['guest_session_id']

    def get_session_id(self):
        # TODO - If more time permits
        pass

