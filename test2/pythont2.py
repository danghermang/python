import zipfile
import json
import urllib.request


def problema1(n):
    result = []
    for element in range(n):
        result.append(element+51)
    return result


def problema2(big_string, small_string):
    if big_string.endswith(small_string):
        return True
    return False


def problema3(x):
    return x**3+2*x**2-4*x+5


def problema4(apath):
    result = []
    archive = zipfile.ZipFile(apath)
    for element in archive.namelist():
        if len(element) == 9:
            result.append(element)
    return result


def problema5(astr):
    result = []
    dictionar = json.loads(astr)
    for element in dictionar.keys():
        result.append(element)
    return result


def problema6(alink):
    url = urllib.request.urlopen(alink)
    text = url.read().decode('utf-8')
    return text.count('TESTPYTHON')

#
# print(problema1(3))
# print(problema2(big_string="13412",small_string="13"))
# print(problema3(x=2))
# print(problema4('test2.zip'))
# print(problema5(astr='{"1": 2, "3": 4, "5": 6, "7": 8}'))
# print(problema6(alink="http://md5.jsontest.com/?text=example_text"))