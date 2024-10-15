import requests

# Step 1: Get a math question
question_response = requests.get('http://127.0.0.1:5000/math-question')
question_data = question_response.json()
print("Question:", question_data['question'])

# Step 2: Submit an answer
answer = 18  # Replace this with the actual answer if known
submit_url = 'http://127.0.0.1:5000/submit-answer'
response = requests.post(submit_url, json={"answer": answer})
print(response.json())
