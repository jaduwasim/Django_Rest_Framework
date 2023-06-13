import requests

BASE_URL = 'http://localhost:8000/'
END_POINT = 'jsoncbv'

get_response = requests.post(BASE_URL + END_POINT)
get_data = get_response.json()

print(get_data)

# post_response = requests.post(BASE_URL + END_POINT)
# post_data = post_response.json()

# print(post_data)

# put_response = requests.put(BASE_URL + END_POINT)
# put_data = put_response.json()

# print(put_data)

# patch_response = requests.patch(BASE_URL + END_POINT)
# patch_data = patch_response.json()

# print(patch_data)

# delete_response = requests.delete(BASE_URL + END_POINT)
# delete_data = delete_response.json()

# print(delete_data)