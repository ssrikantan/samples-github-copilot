""" implement the following steps:
1) call the REST API of Azure Cognitive Services Text Analytics to perform sentiment analysis on the text passed as input parameter
2) Read the input parameter as command line argument
3) evaluate the sentiment score and sentiment label returned by the API
4) print the sentiment score and sentiment label to console

Endpoint: https://languagemtc.cognitiveservices.azure.com/
api-key: 7ffe0f68cbbd424d9b3b6b93ef14a065
"""

def analyze_sentiment():
    import sys
    import os
    import requests
    import json

    # read the input parameter
    input_text = sys.argv[1]
    print(f"Input text: {input_text}")

    # set the API key and endpoint
    api_key = "7ffe0f68cbbd424d9b3b6b93ef14a065"
    endpoint = "https://languagemtc.cognitiveservices.azure.com/"

    # set the API URL
    sentiment_api_url = f"{endpoint}/text/analytics/v2.1/sentiment"

    # set the headers
    headers = {"Ocp-Apim-Subscription-Key": api_key}

    # set the request payload
    request_payload = {"documents": [{"id": "1", "language": "en", "text": input_text}]}

    # call the REST API
    response = requests.post(sentiment_api_url, headers=headers, json=request_payload)

    # extract the sentiment score and sentiment label
    sentiment_score = response.json()["documents"][0]["score"]
    sentiment_label = "positive" if sentiment_score >= 0.5 else "negative"

    # print the sentiment score and sentiment label
    print(f"Sentiment score: {sentiment_score}")
    print(f"Sentiment label: {sentiment_label}")

if __name__ == "__main__":
    analyze_sentiment()





