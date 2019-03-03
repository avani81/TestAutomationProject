import requests
from libs.api.authentication_api import AuthenticationAPI


class MoviesAPI:

    def __init__(self):
        self.base_url = 'https://api.themoviedb.org/'
        self.authenticate_api = AuthenticationAPI()

    def get_latest_movies(self, api_key):
        url = self.base_url + '/3/movie/latest'
        payload = {'api_key': api_key}
        resp = requests.request(method='GET', url=url, params=payload)
        return resp

    def get_movie_details_by_id(self, api_key, id):
        """ GET /3/movie/{movie_id}"""
        url = self.base_url + '/3/movie/{}'.format(id)
        payload = {'api_key': api_key, 'language': 'en-US'}
        resp = requests.request(method='GET', url=url, params=payload)
        return resp

    def rate_movie(self, api_key, id, value):
        """ POST /movie/{movie_id}/rating """
        guest_session_id = self.authenticate_api.get_guest_session_id(
            api_key=api_key)

        url = self.base_url + \
            '/3/movie/{}/rating?api_key={}&guest_session_id={}'.format(id, api_key, guest_session_id)
        data = {"value": value}
        headers = {'content-type': 'application/json;charset=utf-8'}
        resp = requests.request(
            method='POST',
            url=url,
            json=data,
            headers=headers)
        return resp

    def rate_movie_with_invalid_authentication(
            self, api_key, id, value, invalid_flag):
        """ POST /movie/{movie_id}/rating """
        if invalid_flag == 'GUEST_SESSION_ID':
            guest_session_id = "INVALID"
            url = self.base_url + \
                '/3/movie/{}/rating?api_key={}&guest_session_id={}'.format(id, api_key, guest_session_id)
            data = {"value": value}
            headers = {'content-type': 'application/json;charset=utf-8'}
            resp = requests.request(
                method='POST', url=url, json=data, headers=headers)

        elif invalid_flag == 'API_KEY':
            guest_session_id = self.authenticate_api.get_guest_session_id(
                api_key=api_key)
            url = self.base_url + '/3/movie/{}/rating?api_key={}&guest_session_id={}'.format(
                id, "INVALID_api_key", guest_session_id)
            data = {"value": value}
            headers = {'content-type': 'application/json;charset=utf-8'}
            resp = requests.request(
                method='POST', url=url, json=data, headers=headers)

        return resp

    def get_external_ids(self, movie_id, api_key):
        # GET /3/movie/{movie_id}/external_ids
        url = self.base_url + '/3/movie/{}/external_ids'.format(movie_id)
        payload = {'api_key': api_key, 'language': 'en-US'}
        resp = requests.request(method='GET', url=url, params=payload)
        return resp
