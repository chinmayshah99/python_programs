'''
    An example program to fetch images from Labelbox
    Labelbox is an online service that allows you to manually label the images

    This is a sample script to fetch these semantically labeled images which are exported
    in the JSON file from Labelbox.
    Each image is a different class labeled.

    MIT License
    Copyright (c) 2020 Chinmay Shah
'''

import json
import urllib.request as urllib

class HttpHandler():
    def retrive_file(self, url, filename):
        print('starting: ', filename)
        testfile = urllib.URLopener()
        testfile.retrieve(url, filename+'.png')
        testfile.close()


if __name__ == "__main__":
    json_file_name = 'export-2020-03-26T12_53_58.856Z.json'
    with open(json_file_name) as f:
        json_str = f.read()
        data = json.loads(json_str)
    
    for item in data:
        file_name = item['ID']
        print(file_name)
        instance_objects = item["Label"]['objects']
        counter = 0
        for obj in instance_objects:
            obj1 = HttpHandler() # each loop is creating a new object, allowing to simultaneously download the images.
            print(obj['title'])
            filename =  str(item['ID']) + '_' +str(counter)  + '_' + str(obj['title'])
            obj1.retrive_file(obj['instanceURI'], filename)
            counter = counter + 1 # keeping track of different classes