import requests
import json

def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(URL, json=myobj, headers=header)

    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        return formatted_response
    else:
        return {"error": f"Request failed with status {response.status_code}"}