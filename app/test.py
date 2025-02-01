import httpx
import json

# GraphQL endpoint
url = "https://www.leetcode.com/graphql/"


# Get the next two values from your browser cookies
leetcode_session = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMTI0NTgzMzIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJhbGxhdXRoLmFjY291bnQuYXV0aF9iYWNrZW5kcy5BdXRoZW50aWNhdGlvbkJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4NTI2MzhkZGExMGZhNjlmZTE3ZWRiMTU3MDc3ZmM2YjVmZDNiZDcwNzQ2MDAwZDE5NTIwYTgwODM2ZmRmZmNlIiwic2Vzc2lvbl91dWlkIjoiZmY0N2FiYWMiLCJpZCI6MTI0NTgzMzIsImVtYWlsIjoiZXRoYW5kZWlzdGVyQGdtYWlsLmNvbSIsInVzZXJuYW1lIjoiZXRoYW5EZWlzdGVyIiwidXNlcl9zbHVnIjoiZXRoYW5EZWlzdGVyIiwiYXZhdGFyIjoiaHR0cHM6Ly9hc3NldHMubGVldGNvZGUuY29tL3VzZXJzL2RlZmF1bHRfYXZhdGFyLmpwZyIsInJlZnJlc2hlZF9hdCI6MTczODMyNDA3NCwiaXAiOiIyNjAxOjYwMTpkMjg2OjQwNjA6YWRkMTpjNmE0OmZlMzk6MTQ4NyIsImlkZW50aXR5IjoiZjUxYmI0ODJjNjYwZDBlZWFkZDFmMDU4MDU4YTJiMzUiLCJkZXZpY2Vfd2l0aF9pcCI6WyI3MmZkOTQ1YWQ0OThiYTRhZWVhNzM1YTBlN2E0ZTZkZCIsIjI2MDE6NjAxOmQyODY6NDA2MDoxMGRmOmI5NTM6NmYwNzo1ZWZlIl0sIl9zZXNzaW9uX2V4cGlyeSI6MTIwOTYwMH0.PvzB8Rmw9IfyNhhQzYSH_UmRfPLnFDqUTjLwwazU5yA"
csrf_token = "PnE9r04bzXlsKipRyG0ZKUj3rvq4fYkpDqQG5j12b8T4rfNSbvAia5ASZpnyF2WU"

# Define the GraphQL query
query = """
query {
  problemsetQuestionList: questionList(
    categorySlug: ""
    limit: 100
    skip: 0
    filters: {}
  ) {
    total: totalNum
    questions: data {
      acRate
      difficulty
      frontendQuestionId: questionFrontendId
      paidOnly: isPaidOnly
      status
      title
      titleSlug
      topicTags {
        name
        id
        slug
      }
    }
  }
}
"""

# Define the variables for the query
variables = {
    "categorySlug": "",
    "limit": 10,
    "skip": 0,
    "filters": {}
}

# Prepare the payload
payload = {
    "query": query,
}

headers = {
    "Host": "leetcode.com",
    "User-Agent": "curl/8.0.1",
    "Accept": "*/*",
    "content-type": "application/json",
    "Origin": "https://leetcode.com/",
    "Content-Type": "application/json",
    "Cookie": "LEETCODE_SESSION="+leetcode_session+"; csrftoken="+csrf_token,  # Replace with actual tokens
    "X-CSRFToken": csrf_token  # You can add this if the API specifically requires it
}

# Send the HTTP POST request
async def fetch_data():
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            print("Data received:")
            print(json.dumps(response.json(), indent=2))
        else:
            print(f"Request failed with status code {response.status_code}")

# Run the async function
import asyncio
asyncio.run(fetch_data())