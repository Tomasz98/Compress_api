from datetime import datetime
from sqlalchemy import *

db = create_engine('postgresql://husfarm:KLJkf5$59G5-*5KDKSD@ns3085177.ip-145-239-4.eu:5432/husfarm')
db.echo = True
metadata = MetaData(db)

offers = Table('offers',metadata,
                   Column('id',BigInteger, primary_key=True),
                   Column('uuid',VARCHAR),
                   Column('lokacja',VARCHAR),
                   Column('cena',FLOAT),
                   Column('tytuł',VARCHAR),
                   Column('foto',BOOLEAN),
                   )
metadata.create_all(db)


def main(lokacja,cena,tytul,photo_name,photo_bool):
    start = datetime.now()
    row = []
    row.append(photo_name)
    row.append(lokacja)
    row.append(cena)
    row.append(tytul)
    row.append(photo_bool)

    walidator(row)
    end = datetime.now()
    total = end - start
    print("Czas {}".format(total))




def walidator(row):

        print(row)
        try:
            insert_into_offers = offers.insert()
            insert_into_offers.execute(uuid=row[0],lokacja = row[1], cena = row[2],tytul = row[3],foto = row[4])
            print("OK - ogłoszenie weszło do bazy")
        except Exception as error:
            try:
                print(error)
                print("Błąd")
            except Exception as error:
                print(error)





