'''
-*- coding: utf-8 -*-
    @Author   : lingling
    @Time     : 2024/4/17 14:50
    @File     : serializers.py
    @references  :https://en.wikipedia.org/wiki/Letter_frequency  -for detect language
                chatgtp -for python and javaScript and html execute
    @Project  : assignment04
'''
def SuccessResponce(validated_data):
    result = {
        'code': 200,
        'data': validated_data,
        'msg': 'success'
    }
    print(result)
    return result


def SuccessListResponce(validated_data):
    result = {
        'code': 200,
        'total': len(validated_data),
        'data': validated_data,
        'msg': 'success'
    }
    print(result)
    return result


def ErrorResponce(error_msg):
    result = {
        'code': 400,
        'data': error_msg,
        'msg': 'failed'
    }
    return result
