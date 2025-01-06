import httpx
import time
from pprint import pprint
from leetcode_helpers import CSRFTOKEN, LEETCODE_SESSION
# TODO: Turn this into a method so data can be substituted
problem_slug = "two-sum"

url = f"https://leetcode.com/problems/{problem_slug}/interpret_solution/"

headers = {
    "User-Agent": "curl/8.0.1", 
    "Accept": "*/*",
    "Content-Type": "application/json",
    "Origin": "https://leetcode.com",
    "Referer": f"https://leetcode.com/problems/{problem_slug}/",
    "x-csrftoken": CSRFTOKEN,
    "Cookie": f"LEETCODE_SESSION={LEETCODE_SESSION}; csrftoken={CSRFTOKEN}"
}

data = {
    "lang": "python3",
    "question_id": 1,
    "typed_code": """class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            if (target - num) in seen:
                return [seen[target-num], i]
            if not num in seen:
                seen[num] = i
""",
    "data_input": "[2,7,11,15]\n9\n[3,2,4]\n6\n[3,3]\n6"
}

# Use httpx to make the POST request
with httpx.Client() as client:
    response = client.post(url.format(problem_slug=problem_slug), headers=headers, json=data)
    interpret_id = response.json()['interpret_id']

time.sleep(3)

# The URL to the API endpoint
url = f"https://leetcode.com/submissions/detail/{interpret_id}/check/"

# Set up the headers, including the CSRF token and session cookie
headers = {
    "Content-Type": "application/json",
    "Referer": f"https://leetcode.com/problems/{problem_slug}/submissions",
    "x-csrftoken": CSRFTOKEN,
    "Cookie": f"LEETCODE_SESSION={LEETCODE_SESSION}; csrftoken={CSRFTOKEN}"
}

# Use httpx to make the POST request
with httpx.Client() as client:
    response = client.get(url, headers=headers)

pprint(response.json())