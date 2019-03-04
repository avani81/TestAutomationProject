from unittest import TestCase

from libs.api.movies_api import MoviesAPI
from libs.api.movies_schemas import MovieSchema
from libs.utils.config_management import AutomationConfig

from jsonschema import validate


class MoviesTests(TestCase):
    """
    Test class includes API tests for Movies section

    """

    @classmethod
    def setUpClass(cls):
        cls.movies_api = MoviesAPI()
        cls.automationConfig = AutomationConfig()
        cls.api_key =  cls.automationConfig.parser.get('Keys','api_key')

    def test_get_movie_200(self):
        """
        Test 1 - Validate Get movie details with valid movie_id
        Validation - Verify Response code 200 , movie title , schema of response json
        """
        resp = self.movies_api.get_movie_details_by_id(
            api_key=self.api_key, id=19404)
        self.assertEqual(200,resp.status_code,msg='response code does not match')
        obj = resp.json()
        self.assertEqual(19404, obj['id'], msg='title does not match')
        self.assertEqual('Dilwale Dulhania Le Jayenge',obj['title'],msg='title does not match')
        validate(obj, schema=MovieSchema.movie_details_schema)

    def test_get_movie_status_codes_401(self):
        """
        Test 2 - Validate Get movie details with invalid api_key
        Validation - Verify Response code error 401 , validate response error status_code , status_message and schema
        """
        resp = self.movies_api.get_movie_details_by_id(
            api_key='INVALID KEY', id=19404)
        expected = [401, 7, 'Invalid API key: You must be granted a valid key.']
        self.validate_response(expected, response=resp)

    def test_get_movie_status_codes_404(self):
        """
        Test 3 - Validate Get movie details with invalid movie_id
        Validation - Verify Response code error 404 , validate response error status_code , status_message and schema
        """
        resp = self.movies_api.get_movie_details_by_id(
            api_key=self.api_key, id=-1)
        expected = [404, 34, 'The resource you requested could not be found.']
        self.validate_response(expected=expected, response=resp)

    def test_rate_movie_201(self):
        """
        Test 4 - Validate Post movie rating with valid input
        Validation - Verify response code 201 , validate response  status_code , status_message and schema
        Note-There is not get_movie_rate API-Ideally it should be validated with get response to complete end to end flow
        """
        resp = self.movies_api.rate_movie(api_key=self.api_key, id=19404, value=8)
        expected = [201,1,'Success.']
        self.validate_response(expected=expected,response=resp)

    def test_rate_movie_404(self):
        """
        Test 5 - Validate Post movie rating with invalid movie_id
        Validation - Verify Response code error 404 , validate response error status_code , status_message and schema
        """
        resp = self.movies_api.rate_movie(api_key=self.api_key, id=-1, value=8)
        expected = [404, 34, 'The resource you requested could not be found.']
        self.validate_response(expected=expected, response=resp)

    def test_rate_movie_error_status_codes_400(self):
        """
        Test 6 - Validate Post movie rating with invalid movie rating vale i.e. more than 10
        Validation - Verify Response code error 400 , validate response error status_code , status_message and schema
        """
        resp = self.movies_api.rate_movie(
            api_key=self.api_key, id=19404, value=50)
        obj = resp.json()
        expected = [400, 18, 'Value too high: Value must be less than, or equal to 10.0.']
        self.validate_response(expected=expected, response=resp)

    def test_rate_movie_status_codes_401_invalid_guest_session(self):
        """
        Test 7 - Validate Post movie rating with invalid Guest_session_id
        Validation - Verify Response code error 401 , validate response error status_code , status_message and schema
        """
        resp = self.movies_api.rate_movie_with_invalid_authentication(
            api_key=self.api_key, id=19404, value=10, invalid_flag="GUEST_SESSION_ID")
        expected = [401, 3, 'Authentication failed: You do not have permissions to access the service.']
        self.validate_response(expected,response=resp)

    def test_rate_movie_status_codes_401_invalid_api_key(self):
        """
        Test 8 - Validate Post movie rating API with invalid api_key
        Validation - Verify Response code error 401 , validate response error status_code , status_message and schema
        """
        resp = self.movies_api.rate_movie_with_invalid_authentication(
            api_key=self.api_key, id=19404, value=10, invalid_flag="API_KEY")
        expected = [401, 7, 'Invalid API key: You must be granted a valid key.']
        self.validate_response(expected, response=resp)

    def test_get_movie_external_ids_response_schema(self):
        """
        Test 9 - Validate Get movie external id API with valid movie_id
        Validation - Verify Response code 200 , schema of response json
        """
        resp = self.movies_api.get_external_ids(api_key=self.api_key, movie_id=19404)
        self.assertEqual(200, resp.status_code, msg='response code does not match')
        obj = resp.json()
        # Validating json schema for response
        validate(instance=obj, schema=MovieSchema.movie_external_ids_schema)

    def test_get_movie_external_ids_error_404(self):
        """
        Test 10 - Validate Get movie external id API with valid Invalid movie_id
        Validation - Verify Response code 404 ,  schema of response json
        """
        resp = self.movies_api.get_external_ids(api_key=self.api_key, movie_id=-1)
        expected = [404, 34, 'The resource you requested could not be found.']
        self.validate_response(expected=expected, response=resp)

    def validate_response(self,expected,response):
        """ This method will verify API response
            1. Validate correct API status_code  return
            2. Validate response body schema - status_code, status_message
            3. Validate response body parameter values i.e. status_code = 3
        """
        obj = response.json()
        validate(obj, schema=MovieSchema.error_code_status_schema)
        self.assertEqual(expected[0], response.status_code, msg='response code does not match')
        self.assertEqual(expected[1], obj['status_code'], msg='Error Status_code does not match')
        self.assertEqual(expected[2],
                         obj['status_message'], msg='Error status_message does not match')

    @classmethod
    def tearDownClass(cls):
        pass
