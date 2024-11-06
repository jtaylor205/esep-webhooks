import json
import os
import requests

def lambda_handler(event, context):
    # Log the received input
    print(f"Received event: {event}")

    # Parse the JSON input to extract the issue URL
    issue_url = event.get("issue", {}).get("html_url", "No URL provided")
    
    # Prepare the payload for Slack
    payload = json.dumps({"text": f"Issue Created: {issue_url}"})
    
    # Send the payload to Slack
    slack_url = os.getenv("SLACK_URL")
    headers = {'Content-Type': 'application/json'}
    response = requests.post(slack_url, data=payload, headers=headers)
    
    # Read and return the response content
    return response.text
