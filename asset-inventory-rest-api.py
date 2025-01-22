import os
import google.auth
from google.auth.transport.requests import Request
import requests

# Constants
ASSET_API_URL = "https://cloudasset.googleapis.com/v1"
PROJECT_ID = "701858774570"  #  project ID

def get_access_token():
    """Fetch an access token using google-auth."""
    # Authenticate and get credentials
    credentials, _ = google.auth.default()
    credentials.refresh(Request())
    return credentials.token

def list_assets():
    """Call the Cloud Asset Inventory API to list assets."""
    access_token = get_access_token()

    # API endpoint to list assets
    url = f"{ASSET_API_URL}/projects/{PROJECT_ID}/assets"

    # Request headers with the access token
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    # Optional: Add query parameters (e.g., asset types, content types, etc.)
    params = {
        "contentType": "RESOURCE",  # Options: RESOURCE, IAM_POLICY, etc.
        "pageSize": 10              # Number of assets to list
    }

    # Make the API request
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        # Parse and print the response
        assets = response.json().get("assets", [])
        print("Assets:")
        for asset in assets:
            print(asset)
    else:
        # Print error details
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    list_assets()
