# import requests

# def download_file_from_google_drive(file_id, destination):
#     URL = "https://drive.google.com/uc?export=download&confirm=1"

#     session = requests.Session()
#     response = session.get(URL, params={'id': file_id}, stream=True)
#     token = get_confirm_token(response)

#     if token:
#         params = {'id': file_id, 'confirm': token}
#         response = session.get(URL, params=params, stream=True)

#     save_response_content(response, destination)

# def get_confirm_token(response):
#     for key, value in response.cookies.items():
#         if key.startswith('download_warning'):
#             return value
#     return None

# def save_response_content(response, destination):
#     CHUNK_SIZE = 32768

#     with open(destination, "wb") as f:
#         for chunk in response.iter_content(CHUNK_SIZE):
#             if chunk:  # filter out keep-alive new chunks
#                 f.write(chunk)

# # Example usage:
# # Replace 'your_file_id' with your actual file ID and 'destination_path' with the desired download path.
# file_id = '1gjnI1YwQyCf-jUUaFVu6DPcLpyigu-gO'
# destination = 'leave.zip'
# download_file_from_google_drive(file_id, destination)

import gdown

def download():
    url = 'https://drive.google.com/uc?id=1gjnI1YwQyCf-jUUaFVu6DPcLpyigu-gO'
    output = './models/leave.zip'
    gdown.download(url, output, quiet=False)