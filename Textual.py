'''
-*- coding: utf-8 -*-
    @Author   : lingling
    @Time     : 2024/4/14 22:20
    @File     : Textual.py
    @references  :https://en.wikipedia.org/wiki/Letter_frequency  -for detect language

    @Project  : assignment04
'''

import base64
import os
import re
import urllib.parse
from collections import OrderedDict

from langdetect import detect

FILE_PATH = 'files'


def deCodeText(text: str):
    decodedData = urllib.parse.unquote(text)
    decodedBase64Data = base64.b64decode(decodedData).decode('utf-8')
    return decodedBase64Data



def getfile(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def gettextfiles(dirname: str):
    files_and_dir = os.listdir(dirname)
    return [os.path.join(dirname, f) for f in files_and_dir if os.path.isfile(os.path.join(dirname, f))]


'''
remove picture and non-text from text
@param  :
    value(str)
@return textValue(value)
'''


def cleanTextual(value: str):
    textValue = re.sub(r'\bhttps?:\/\/\S+\b', ' ', value)
    textValue = re.sub(r'[^\w\s\.,!?\'\"]', ' ', textValue)
    textValue = re.sub(r'\s+', ' ', textValue)
    lowerText = textValue.lower()
    return lowerText


'''
separate text to sentence
@param  :
    text(str)
@return sentences(list)
'''


def separateSentence(text: str):
    sentences = re.split(r'[.!?]', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    return sentences


def separateWords(sentence: str):
    clean_sentence = re.sub(r'[^\w\s]', ' ', sentence)
    clean_sentence = re.sub(r'\s+', ' ', clean_sentence)
    words = clean_sentence.split()
    return words


'''
find individual words in sentence
@param  :
    text(str)
@return sentences(list)
'''

def findIndexInSentence(word: str, sentence: str):
    resultlist = []
    allwords = sentence.split()
    word = word.lower()
    for i in range(len(allwords)):
        if word == allwords[i]:
            # if word in allwords[i]:
            resultlist.append(i)
    return resultlist


def findWordInSentence(word: str, sentencesl: list):
    sentence_list = []
    for i in range(len(sentencesl)):
        nums = findIndexInSentence(word, sentencesl[i])
        if nums:
            sentence_list.append({'sentenceId': i, 'sentence': sentencesl[i], "wordNum": nums})
    return sentence_list


'''
count  words and frequency in sentence
@param  :
    word(str)
    sentence(str)
@return sentences(list)
'''
def countwordsInSentence(word: str, sentence: str):
    sentence = cleanTextual(sentence)
    total = countWordsInSentence(sentence)
    allwords = separateWords(sentence)
    word = word.lower()
    word = word.strip()
    count = 0
    for i in range(len(allwords)):
        if word == allwords[i]:
            count += 1
    percentage = str(count) + '/' + str(total)
    return {'findword': word, 'percent': percentage}

'''
count  all words and frequency in sentence
@param  :
    sentence(str)
@return countlist(list)
'''
def countAllwordsInSentence(sentence: str):
    sentence = cleanTextual(sentence)
    allwords = separateWords(sentence)
    total = countWordsInSentence(sentence)
    allwords_list = {}
    for word in allwords:
        allwords_list[word] = allwords_list.get(word, 0) + 1
    result_list = []
    for word, count in allwords_list.items():
        percentage = str(count) + '/' + str(total)
        result_list.append({'findword': word, 'percent': percentage})
    result_list = sorted(result_list, key=lambda x: x['percent'], reverse=True)

    return result_list


def findWordInText(word: str, text: str):
    sentencesl = separateSentence(text)
    return findWordInSentence(word, sentencesl)


def findWordsInfile(word: str, filename: str):
    file_data = getfile(filename)
    text = cleanTextual(file_data)
    sentanse_words = findWordInText(word, text)
    return sentanse_words


def findwordsInfiles(word: str, file_path=FILE_PATH):
    files = gettextfiles(FILE_PATH)
    file_words = []
    for file in files:
        sentanse_words = findWordsInfile(word, file)
        if sentanse_words:
            file_words.append({'fileName': file, 'words': sentanse_words})
    return file_words


def countWordsInSentence(sentence: str):
    return len(sentence.split())


# def countLengthOfWordsInSentence(sentence: str):
#     word_length = []
#     for word in sentence:
#         word_length.append(len(word))
#     return word_length

'''
count  char  in text
@param  :
    character 
    text(str)
@return count(int)
'''
def countCharIntext(character, text: str):
    count = 0
    character = character.lower()
    for char in text:
        if char == character:
            count += 1

    return count

'''
count  all chars  frequency in text
@param  :
    text(str)
@return letter_freq(list)
'''
def countfrequencyIntext(text: str):
    char_list = {}
    total_char = 0
    for char in text:
        if char.isalpha():
            char_list[char] = char_list.get(char, 0) + 1
            total_char += 1
    letter_freq = {}
    total_letter = 0
    for char, count in char_list.items():
        letter_freq[char] = count / total_char * 100
        if 'a' <= char <= 'z':
            total_letter += count

    english_char_freg = total_letter / total_char * 100  # english char freq
    return english_char_freg, letter_freq

'''
count  all chars  frequency in text
@param  :
    text(str)
@return letter_freq(list)
'''
def countcharsIntext(text: str):

    char_list = {}
    total_char = 0
    for char in text:
        if char.isalpha():
            char_list[char] = char_list.get(char, 0) + 1
            total_char += 1
    letter_freq = []

    for char, count in char_list.items():
        percentage_str = str(count) + '/' + str(total_char)
        percentage =round(count/total_char*100,2)
        letter_freq.append({'char': char, 'count': percentage_str,'percent(%)':percentage})
    letter_freq=sorted(letter_freq, key=lambda x: x['char'], reverse=False)
    return letter_freq

'''
detect text is English or not
using english char frequency
@param  :
    text(str)
    
    compare the letter_freq with  english_freq and french_freq and spanish_freq to get the most like language
@return True /False
'''
def isEnglish(text):
    english_freq = {'e': 12.7, 't': 9.1, 'a': 8.2, 'o': 7.5, 'i': 7.0}
    french_freq = {'e': 14.7, 'a': 7.6, 's': 7.9, 'i': 7.4, 't': 7.2}
    spanish_freq = {'e': 13.7, 'a': 11.7, 'o': 8.7, 's': 7.0, 'r': 6.8}
    German_freq = {'e': 16.4, 'n': 9.8, 's': 7.3, 'r': 7, 'i': 6.5}
    sum_freq, letter_freq = countfrequencyIntext(text)
    if sum_freq < 50:
        return False
    keys = letter_freq.keys()

    english_similarity = sum(abs(english_freq[char] - letter_freq.get(char, 0)) for char in english_freq)
    french_similarity = sum(abs(french_freq[char] - letter_freq.get(char, 0)) for char in french_freq)
    spanish_similarity = sum(abs(spanish_freq[char] - letter_freq.get(char, 0)) for char in spanish_freq)
    German_similarity = sum(abs(German_freq[char] - letter_freq.get(char, 0)) for char in German_freq)

    min_similarity = min(english_similarity, french_similarity, spanish_similarity, German_similarity)
    if min_similarity == english_similarity:
        return True
    return False


def detectFromText(text):
    text = cleanTextual(text)
    if detect(text) == 'en':
        return 'English'
    else:
        return 'Not English'


def detectFromText1(text):
    text = cleanTextual(text)
    if isEnglish(text):
        return 'English'
    else:
        return 'Not English'


if __name__ == '__main__':
    # filedata = getfile('files/french.txt')
    filedata = 'Most (on-line) information is textual, there are many simple'
    # language = detectFromText(filedata)
    # print(language)
    # language = detectFromText1(filedata)
    # print(language)
    # print(countfrequencyIntext(filedata))
    print(countwordsInSentence('是', filedata))
    # sentences = separateSentence(text)
    # print(sentences)
    # re = findIndexInSentence('dir', sentences[3])
    # print(re)
    # re=findWordInfile('clear', 'files/clanguage.txt')
    # print(re)
    file_result = findwordsInfiles("it's")
    print(file_result)
