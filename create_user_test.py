import sender_stand_request
import data

def test_create_user_2_letter_in_first_name_get_success_response():

    user_body = get_user_body("Aa")

    user_response = sender_stand_request.post_new_user(user_body)


    assert user_response.status_code == 201

    assert user_response.json()["authToken"] != ""

    user_table_response = sender_stand_request.get_users_table()
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]

    def test_create_user_15_letter_in_first_name_get_success_response():
        positive_assert("Aaaaaaaaaaaaaaa")