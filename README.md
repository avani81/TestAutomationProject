# TestAutomation
TestAutomation project includes library and tests for UI and Web APIs

## Project Requirements
Develop API Testing framework for https://developers.themoviedb.org v3 APIs (automate any API)
Automate UI flow for https://www.saucedemo.com/

## Project Description
This test automation project is developed in Python 3.7.
API testing framework is developed using python request module to send GET , POST request , jsonschema to validate json response from api Following APIs are tested
Web UI testing is developed using selenium web driver and page object model to separate page action and locators from test flows .

## Test Coverage

### Following APIs are covered from Movies and Authentication sections.

- GET /3/movie/{movie_id}
- POST /3/movie/{movie_id}/rating
- GET /3/movie/{movie_id}/external_ids
- GET /3/authentication/guest_session/new
Validation of request and response status codes , response body json schema validation ,error code and messages validation for each APIs ( based on definition given on developers.themoviedb.org websites)
Fully Automated test cases = 10

### For UI tests following scenarios are covered
- Verify elements of site and Login with standard_user
- Add to cart work flows a) from product list b) from product details
Fully Automated test cases = 4 ( Please note other test methods definition is included for future implementations)

## Project structure
TestAutomation
libs ( apis, ui, utils)
tests (apis, ui)

## Instructions
1. Setup Python environment for project ( Python 3.7 ) . Editor used is PyCharm Community
2. Download project repository and run pip install requirements.txt ( This will install project dependancies like selenium , nosetests and other required modules )
3. From project directory copy geckodriver(for Firefox) and chromedriver in path /usr/local/bin to run locally
### To run API tests
1. Add your api_key in file tests/api/movies_latests_tests.py line #14 for self.api_key = ‘Your_api_key’
2. From command line run - nosetests -v tests/api/movies_latests_tests.py
### To run UI tests
1. Specify local browser - Firefox or Chrome in tests/ui/base_ui_test.py( default Firefox)
2. From command line run - nosetests -v tests/ui/test_product_cart_flows.py

### Limitation and more improvements
- Remove hardcoding of api_key from setup to pass as parameterize . Better approach would be generate token or session in test setup and discard in tearDown method after running tests.
- base_ui_test.py can be improvise to removing hardcoding of browser or running test on headless browser example phantomjs.
- more logging can be added with printStep(), printDebug(), printError().
- more exception handling can be added.
- more test coverage can be added. Included some in test defination in files for future implemenations
