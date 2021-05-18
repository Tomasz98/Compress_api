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
    lokacja = "Gdańsk"
    cena = 1.4
    tytuł = "Sprzedam czereśnie"
    foto = "ashdjkhasd"
    return lokacja, cena,tytuł,foto
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
    lokacja, cena, tytul, b64foto = get_data_from_json(json_data)

    try:
        if len(b64foto) > 0:
            photo_name = b64_to_png(b64foto)
            foto_bool = True
            compressMe(photo_name)

        else:
            photo_name = ""
            foto_bool = False
    except Exception as error:
        photo_name = ""
        foto_bool = False
        print(error)


    to_db.main(lokacja,cena,tytul,photo_name,foto_bool)

    print("Done")



b64_to_png(b"dsadwdas")