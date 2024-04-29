'''
-*- coding: utf-8 -*-
    @Author   : lingling
    @Time     : 2024/4/17 16:00
    @File     : router.py
    @references  :https://en.wikipedia.org/wiki/Letter_frequency  -for detect language
                chatgtp -for python and javaScript and html execute
    @Project  : assignment04
'''
import json

from flask import Flask, render_template, request, jsonify

from Textual import cleanTextual, deCodeText, findWordInText, countCharIntext, separateSentence, \
    countAllwordsInSentence, countwordsInSentence, countfrequencyIntext, countcharsIntext, detectFromText1, \
    detectFromText
from serializers import SuccessResponce, ErrorResponce, SuccessListResponce

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/functions.js')
def functions():
    return render_template('functions.js')


@app.route('/api/cleanText', methods=['POST'])
def cleanText():
    try:
        data = request.get_json()
        text = data.get('text', '')
    except json.JSONDecodeError:
        return ErrorResponce("Request must be JSON")
    if text:
        text = deCodeText(text)
        cleaned_text = cleanTextual(text)

        return SuccessResponce(cleaned_text)
    else:
        return ErrorResponce("No text provided")


@app.route('/api/separateToSentence', methods=['POST'])
def separateToSentence():
    try:
        data = request.get_json()
        text = data.get('text', '')
    except json.JSONDecodeError:
        return ErrorResponce("Request must be JSON")
    if text:
        text = deCodeText(text)
        text = cleanTextual(text)
        sentence_list = separateSentence(text)
        result_list = []

        for i in range(len(sentence_list)):
            result_list.append({'num': i + 1, "sentence": sentence_list[i]})
        return SuccessListResponce(result_list)
    else:
        return ErrorResponce("No text provided")


@app.route('/api/findWord', methods=['POST'])
def findWord():
    try:
        data = request.get_json()
        word = data.get('word', '')
        text = data.get('text', '')
    except json.JSONDecodeError:
        return ErrorResponce("Request must be JSON")
    if text:
        text = deCodeText(text)

        sentence_list = countwordsInSentence(word, text)
        return SuccessListResponce(sentence_list)
    else:
        return ErrorResponce("No text provided")


@app.route('/api/countWord', methods=['POST'])
def countWord():
    try:
        data = request.get_json()
        text = data.get('text', '')
    except json.JSONDecodeError:
        return ErrorResponce("Request must be JSON")
    if text:
        text = deCodeText(text)

        sentence_list = countAllwordsInSentence(text)
        return SuccessListResponce(sentence_list)
    else:
        return ErrorResponce("No text provided")


@app.route('/api/countCharacters', methods=['POST'])
def countCharacters():
    try:
        data = request.get_json()
        text = data.get('text', '')
    except json.JSONDecodeError:
        return ErrorResponce("Request must be JSON")
    if text:
        text = deCodeText(text)
        text = cleanTextual(text)
        count_list = countcharsIntext(text)

        return SuccessListResponce(count_list)
    else:
        return ErrorResponce("No text provided")

@app.route('/api/dectectEnglish', methods=['POST'])
def dectectEnglish():
    try:
        data = request.get_json()
        text = data.get('text', '')
    except json.JSONDecodeError:
        return ErrorResponce("Request must be JSON")
    if text:
        text = deCodeText(text)
        detect_result = detectFromText1(text)


        return SuccessResponce(detect_result)
    else:
        return ErrorResponce("No text provided")

@app.route('/api/dectectEnglish2', methods=['POST'])
def dectectEnglish2():
    try:
        data = request.get_json()
        text = data.get('text', '')
    except json.JSONDecodeError:
        return ErrorResponce("Request must be JSON")
    if text:
        text = deCodeText(text)
        detect_result = detectFromText(text)
        return SuccessResponce(detect_result)
    else:
        return ErrorResponce("No text provided")
if __name__ == '__main__':
    app.run(debug=False)
