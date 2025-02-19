import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=payload, headers=headers)
    
    # Check the response status code (200 means success)
    if response.status_code == 200:
        return response.json()
    else:
        return None
