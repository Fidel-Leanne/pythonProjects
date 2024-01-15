# import cowsay

# import sys

# if (len(sys.argv)==2):
#     cowsay.trex('hello. '+ sys.argv[1])

from requests import get
import sys

if len(sys.argv) != 2:
    sys.exit()

# Get the search term from command line argument
search_term = sys.argv[1]

# Construct the complete URL with the search term
url = f'http://itunes.apple.com/search/?entity=song&limit=1&term={search_term}'

# Make the request and store the response
response = get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the JSON content of the response
    print(response.json(),)
else:
    print(f"Error: {response.status_code}")
