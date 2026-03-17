import requests
import json

url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze : str):
    input = {"raw_document": { "text": text_to_analyze}}
    response = requests.post(url, json = input, headers=header)

    formatted_response = json.loads(response.text)
    
    emotion = formatted_response["emotionPredictions"][0]["emotion"]

    dominant_emotion = ''
    dominant_emotion_score = 0

    for key in emotion.keys():
        print(f"{key} {emotion[key]}")
        if emotion[key] > dominant_emotion_score:
            dominant_emotion = key
            dominant_emotion_score = emotion[key]

    emotion["dominant_emotion"] = dominant_emotion
    return emotion

if __name__ == '__main__':
    print(emotion_detector("I am so happy I am doing this."))