from unittest import TestCase

from libs.api.movies_api import MoviesAPI
from libs.api.movies_schemas import MovieSchema

from jsonschema import validate


class MoviesTests(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.movies_api = MoviesAPI()
        cls.api_key = 'a0064fa96aef465850fb9ec67c6e0136'

    def test_get_movie_200(self):
        """
        Test 1 - Validate Get movie details with valid movie_id
        Validation - Verify Response code 200 , movie title , schema of response json
        """
        resp = self.movies_api.get_movie_details_by_id(
            api_key=self.api_key, id=19404)
        self.assertEqual(
            200,
            resp.status_code,
            msg='response code does not match')
        obj = resp.json()
        self.assertEqual(
            'Dilwale Dulhania Le Jayenge',
            obj['title'],
            msg='title does not match')
        validate(obj, schema=MovieSchema.movie_details_schema)

    def test_get_movie_status_codes_401(self):
        """
        Test 2 - Validate Get movie details with invalid api_key
        Validation - Verify Response code error 401 , validate response error status_code , status_message and schema
        """
        resp = self.movies_api.get_movie_details_by_id(
            api_key='INVALID KEY', id=19404)
        obj = resp.json()
        self.assertEqual(
            401,
            resp.status_code,
            msg='response code does not match')
        self.assertEqual(
            7,
            obj['status_code'],
            msg='Error Status_code does not match')
        self.assertEqual(
            'Invalid API key: You must be granted a valid key.',
            obj['status_message'],
            msg='Error status_message does not match')
        validate(obj, schema=MovieSchema.error_code_status_schema)

    def test_get_movie_status_codes_404(self):
        """
        Test 3 - Validate Get movie details with invalid movie_id
        Validation - Verify Response code error 404 , validate response error status_code , status_message and schema
        """
        resp = self.movies_api.get_movie_details_by_id(
            api_key=self.api_key, id=-1)
        obj = resp.json()
        self.assertEqual(
            404,
            resp.status_code,
            msg='response code does not match')
        self.assertEqual(
            34,
            obj['status_code'],
            msg='Error Status_code does not match')
        self.assertEqual(
            'The resource you requested could not be found.',
            obj['status_message'],
            msg='Error status_message does not match')
        validate(obj, schema=MovieSchema.error_code_status_schema)

    def test_rate_movie_201(self):
        """
        Test 4 - Validate Post movie rating with valid input
        Validation - Verify response code 201 , validate response  status_code , status_message and schema
        """
        resp = self.movies_api.rate_movie(
            api_key=self.api_key, id=19404, value=8)
        obj = resp.json()
        self.assertEqual(
            201,
            resp.status_code,
            msg='response code does not match')
        self.assertEqual(
            1,
            obj['status_code'],
            msg='Error Status_code does not match')
        self.assertEqual('Success.', obj['status_message'],
                         msg='Error status_message does not match')
        validate(obj, schema=MovieSchema.error_code_status_schema)

    def test_rate_movie_404(self):
        """
        Test 5 - Validate Post movie rating with invalid movie_id
        Validation - Verify Response code error 404 , validate response error status_code , status_message and schema
        """
        resp = self.movies_api.rate_movie(api_key=self.api_key, id=-1, value=8)
        obj = resp.json()
        self.assertEqual(
            404,
            resp.status_code,
            msg='response code does not match')
        self.assertEqual(
            34,
            obj['status_code'],
            msg='Error Status_code does not match')
        self.assertEqual(
            'The resource you requested could not be found.',
            obj['status_message'],
            msg='Error status_message does not match')
        validate(obj, schema=MovieSchema.error_code_status_schema)

    def test_rate_movie_error_status_codes_400(self):
        """
        Test 6 - Validate Post movie rating with invalid movie rating vale i.e. more than 10
        Validation - Verify Response code error 400 , validate response error status_code , status_message and schema
        """
        resp = self.movies_api.rate_movie(
            api_key=self.api_key, id=19404, value=50)
        obj = resp.json()
        self.assertEqual(
            400,
            resp.status_code,
            msg='response code does not match')
        self.assertEqual(
            18,
            obj['status_code'],
            msg='Error Status_code does not match')
        self.assertEqual(
            'Value too high: Value must be less than, or equal to 10.0.',
            obj['status_message'],
            msg='Error status_message does not match')
        validate(obj, schema=MovieSchema.error_code_status_schema)

    def test_rate_movie_status_codes_401_invalid_guest_session(self):
        """
        Test 7 - Validate Post movie rating with invalid Guest_session_id
        Validation - Verify Response code error 401 , validate response error status_code , status_message and schema
        """
        resp = self.movies_api.rate_movie_with_invalid_authentication(
            api_key=self.api_key, id=19404, value=10, invalid_flag="GUEST_SESSION_ID")
        obj = resp.json()
        self.assertEqual(
            401,
            resp.status_code,
            msg='response code does not match')
        self.assertEqual(
            3,
            obj['status_code'],
            msg='Error Status_code does not match')
        self.assertEqual(
            'Authentication failed: You do not have permissions to access the service.',
            obj['status_message'],
            msg='Error status_message does not match')
        validate(obj, schema=MovieSchema.error_code_status_schema)

    def test_rate_movie_status_codes_401_invalid_api_key(self):
        """
        Test 8 - Validate Post movie rating API with invalid api_key
        Validation - Verify Response code error 401 , validate response error status_code , status_message and schema
        """
        resp = self.movies_api.rate_movie_with_invalid_authentication(
            api_key=self.api_key, id=19404, value=10, invalid_flag="API_KEY")
        obj = resp.json()
        self.assertEqual(
            401,
            resp.status_code,
            msg='response code does not match')
        self.assertEqual(
            7,
            obj['status_code'],
            msg='Error Status_code does not match')
        self.assertEqual(
            'Invalid API key: You must be granted a valid key.',
            obj['status_message'],
            msg='Error status_message does not match')
        validate(obj, schema=MovieSchema.error_code_status_schema)

    def test_get_movie_external_ids_response_schema(self):
        """
        Test 9 - Validate Get movie external id API with valid movie_id
        Validation - Verify Response code 200 , schema of response json
        """

        resp = self.movies_api.get_external_ids(
            api_key=self.api_key, movie_id=19404)
        self.assertEqual(
            200,
            resp.status_code,
            msg='response code does not match')
        obj = resp.json()
        # Validating json schema for response
        validate(instance=obj, schema=MovieSchema.movie_external_ids_schema)

    def test_get_movie_external_ids_error_404(self):
        """
        Test 10 - Validate Get movie external id API with valid Invalid movie_id
        Validation - Verify Response code 404 ,  schema of response json
        """
        resp = self.movies_api.get_external_ids(
            api_key=self.api_key, movie_id=-1)
        obj = resp.json()
        self.assertEqual(
            404,
            resp.status_code,
            msg='response code does not match')
        self.assertEqual(
            34,
            obj['status_code'],
            msg='Error Status_code does not match')
        self.assertEqual(
            'The resource you requested could not be found.',
            obj['status_message'],
            msg='Error status_message does not match')
        validate(obj, schema=MovieSchema.error_code_status_schema)

    @classmethod
    def tearDownClass(cls):
        pass
