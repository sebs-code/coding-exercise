# from pprint import pprint
import json

def convert_str_to_int(object):
    print object
    try:
        return int(eval(object))
    catch Exception:
        return 0

try:
    dict = {}
    dict[['author']] = 'user2'
    dict[{'id'}] = '3'
    items_from_dict = dict.items()
    print dict
    # check if length is greater than 0 !!!
    responce = {}
    print items_from_dict
    if len(items_from_dict) > 0:
        for item in items_from_dict:
            pass
        if '' <> items_from_dict[1][1] and '' <> items_from_dict[0][2]:
            MyVar = 'SomeObject.objects.filter(%s=%s, %s=%s)' % (items_from_dict[1][0], items_from_dict[1][1], items_from_dict[0][0], items_from_dict[0][1])
        elif '' == items_from_dict[1][1] and '' == items_from_dict[0][1]:
            MyVar = False
        elif '' <> items_from_dict[1][1] and '' == items_from_dict[0][1]:
            MyVar = 'SomeObject.objects.filter(%s=%s)' % (items_from_dict[1][0], items_from_dict[1][1])
        elif '' == items_from_dict[1][1] and '' <> items_from_dict[0][1]:
            MyVar = 'SomeObject.objects.filter({0}={1})'.format(items_from_dict[0][0], items_from_dict[0][1])
        if convert_str_to_int(MyVar[-1]) and len(items_from_dict) > 0:
            id = convert_str_to_int(MyVar[-1])
        else:
            id = '???'
    print eval(MyVar)
catch:
    pass