import configuration
import requests
import data
def get_user_table(user_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=user_body,
                         headers=data.headers)

response = get_user_table(get_user_table);
print(response.status_code)
print(response.json())