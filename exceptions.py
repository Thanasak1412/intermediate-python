"""When handling exception in the context of calling an API, there are several best practices to follow,
    These practices ensure that your application can handle errors gracefully and provide meaningful feedback to the user
    or other parts of the system.
"""

# Best Practices for Handling Exception in API calls

"""Use Specific Exception Handling:
    - Catch specific exceptions rather than a general `Exception` to better understand
    and handler different error scenarios.
"""

import requests # type: ignore
import logging
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry # type: ignore

URL = "https://reqres.in/api/users?page=2"

def fetch_data_with_except_specific():
    try:
        response = requests.get(URL)

        response.raise_for_status() # Raises an HTTPError for bad responses (4xx and 5xx)
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")
    else:
        print("Success!")
    finally:
        print("API call execution complete.")

"""Log the Errors:
    - Use logging to record details of exceptions for future debugging and analysis.
"""

def fetch_data_with_log_errors():
    logging.basicConfig(level=logging.ERROR, filename="app.log", filemode="a", format="%(name)s - %(levelname)s - %(message)s")

    try:
        response = requests.get(URL)
        
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")
    
"""Retry mechanism:
    - Implement a retry mechanism for transient errors like timeouts or temporary network issues.
"""

def fetch_data_with_retry():
    session = requests.Session()
    retry = Retry(total=3, backoff_factor=1, status_forcelist=[502, 503, 504], raise_on_status=False)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    try:
        response = session.get(URL)
        response.raise_for_status()

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")
    finally:
        print("API call execution complete.")
        
fetch_data_with_retry()

"""Provide User Feedback:
    - inform the user of the error in a user-friendly manner.
"""
def fetch_data_with_user_friendly():
    try:
        response = requests.get(URL)
        response.raise_for_status()

    except requests.exceptions.RequestException:
        print("Sorry, there was a problem with your request. Please try again later.")
        
"""Use Timeouts:
    Set appropriate timeout values to prevent hanging indefinitely.
"""
def fetch_data_with_timeout():
    try:
        response = requests.get(URL, timeout=5)
        response.raise_for_status()
    
    except requests.exceptions.Timeout:
        print("The request timed out. Please try again later.")

"""Handle JSON Decode Errors:
    - If expecting JSON responses, handle potential JSON decoding errors.
"""
def fetch_data_with_json_errors():
    try:
        response = requests.get(URL)
        response.raise_for_status()
        data = response.json()

        return data

    except requests.exceptions.RequestException as req_err:
        print(f"Request error: {req_err}")
    except ValueError as json_err:
        print(f"JSON decode error: {json_err}")
        
fetch_data_with_json_errors()

# Here is a complete example demonstrating these best practices:
logging.basicConfig(level=logging.ERROR, filename='app.log', filemode='a',
                    format='%(name)s - %(levelname)s - %(message)s')

def fetch_data_from_api(url):
    session = requests.Session()
    retry = Retry(total=3, backoff_factor=1, status_forcelist=[502, 503, 504])
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    try:
        response = session.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        return data
    
    except requests.exceptions.HTTPError as http_err:
        logging.error(f'HTTP error occurred: {http_err}')
        print('A server error occurred. Please try again later.')
    except requests.exceptions.ConnectionError as conn_err:
        logging.error(f'Connection error occurred: {conn_err}')
        print('Failed to connect to the server. Please check your network connection.')
    except requests.exceptions.Timeout as timeout_err:
        logging.error(f'Timeout error occurred: {timeout_err}')
        print('The request timed out. Please try again later.')
    except requests.exceptions.RequestException as req_err:
        logging.error(f'An error occurred: {req_err}')
        print('An error occurred. Please try again later.')
    except ValueError as json_err:
        logging.error(f'JSON decode error: {json_err}')
        print("Failed to parse the response. Please try again later.")
    finally:
        print("API call execution complete.")
        
data = fetch_data_from_api(URL)

if data:
    print(data)