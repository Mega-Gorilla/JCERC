import requests
import json
import os,time

class config:
    prompt_name = "JERC_Test"

# Construct the file path
file_path = os.path.join(os.path.dirname(__file__), '..', 'kokugo.json')

# Read and parse the JSON file
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# data now contains the content of the kokugo.json file
# You can access the data like this:
for item in data:
    choices = ""
    for choice in item['question']['choices']:
        choices += f"{choice['label']}: {choice['text']}\n"
    variables = {"Subject":"Japanese language section",
                 "stem":item['question']['stem'],
                 "context":item['question']['context'],
                 "choices":choices}
    requests.post(f"http://127.0.0.1:8000/LLM/request/?prompt_name={config.prompt_name}&request_id={item['id']}&stream_mode={False}",json={"variables" : variables})
    while True:
        result = requests.get(f"http://127.0.0.1:8000/LLM/get/?reset=false&del_request_id={item['id']}").json()
        if result != []:
            break
        time.sleep(3)
    print(f"Result : {result[0]['content']}\nAnser Key: {item['answerKey']}\nScore: {item['score']}")