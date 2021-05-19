import os
import sys
import base64
from PIL import Image
import uuid
import json
import to_db



def get_data_from_json(json_request):
    json_req = json.loads(json_request)
    #TODO dokńczyć odczyt JSONa
    location = "Gdańsk"
    price = 1.4
    title = "Sprzedam czereśnie"
    photo = "ashdjkhasd"
    return location, price,title,photo
    #print(json_req['data'])

def b64_to_png(b64_string):
    png_recovered = base64.decodebytes(b64_string)
    new_name = str(uuid.uuid4()) + ".jpeg"
    print(new_name)
    f = open("/before/"+new_name,'wb')
    f.write(png_recovered)
    f.close()
    return new_name



def compressMe(file):

    filepath = "before/"+file
    picture = Image.open(filepath)
    picture.save("/after/" + file,"JPEG",optimize=True,quality=10)




def main(json_data):
    location, price, title, b64photo = get_data_from_json(json_data)

    try:
        if len(b64photo) > 0:
            photo_name = b64_to_png(b64photo)
            foto_bool = True
            compressMe(photo_name)

        else:
            photo_name = ""
            foto_bool = False
    except Exception as error:
        photo_name = ""
        foto_bool = False
        print(error)


    to_db.main(location,price,title,photo_name,foto_bool)

    print("Done")


