from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)
# Create our database model
class Trip(db.Model):
    __tablename__ = "trip"
    id = db.Column(db.Integer, primary_key=True)
    area=db.Column(db.String)
    difficulty=db.Column( db.Integer)
    name = db.Column(db.String)
    info=db.Column(db.String)
    url=db.Column(db.String)
    classname=db.Column( db.String)

engine = db.create_engine('sqlite:///data.db')
db.drop_all()
db.create_all()

# if __name__ == '__main__':

    #save data
trip=Trip(area='Golan Heights',
    classname='North_TheGolanHeights_Banias',
    name='Banias',
    difficulty=2,
    url= '../static/pictures/GolanHeights_Banias.jpg', 
    info='''the Banias is the biggest waterfall in Israel, and one of the prettiest.\n
    It's an easy 3 km of lovely view trip which even fits families with little kids.\n
    The fairy tale tells that Phanes, the greek god of shepherds and forests, used to live in this area,
     and thanks that a temple has been constructed here for him.\n
    Years after, when the Arabs lived here, in their accent it was easy to think the place ,"Phanes", called "Banias". 
    The new name has stayed.''')
db.session.add(trip)

trip=Trip(area='Emek Izrael',
    classname='North_EmekIzrael_Zippori',
    url=' ../static/pictures/EmekIzraelNahalZippori.jpg ',
    name='Zippori river',
    difficulty=1,
    info=''' Zippori river is a 4 km circular trip which fits everyone any - time.\n
    The river is part from a bigger river, which deliver water from Nathareth to Zevulun valley. \n 
    Thanks that fact, there is always water in the river, which adds to the great expirience of traveling in the area. \n
    ''')
db.session.add(trip)

trip=Trip(area='Tzfat and Meron mountains',
    classname='North_TzfatMeron_Zalmon',
    url='../static/pictures/TzfatMeron_Zalmon.jpg',
    name='Zalmon river',
    difficulty=1,
    info= ''' Zalmon is a unique 2 km trip 
    who combines peaceful and calm with beautiful view. \n 
    The trip fits to all ages and even for bikes.''')
db.session.add(trip)

trip=Trip(area='Upper Galilee',
    classname='North_UpperGalilee_kziv',
    url='../static/pictures/UpperGalilee_Kziv.jpg',
    name='Kziv river',
    difficulty=3,
    info=''' This trip is an 8 km trip, and one of the best in the country for all acounts. \n
    In the trip you can find a stream which has water all the year long and crusader fortress 
    on the background of the Galilee green view. In conclusion- you can't miss this trip! \n
    ''')
db.session.add(trip)


trip=Trip(area='Golan Heights',
    classname='North_TheGolanHeights_Zavitan',
    url='../static/pictures/GolanHeights_Zavitan.jpg',
    name='Zavitan stream: upper',
    difficulty=4,
    info=''' Zavitan is a 8 km trip which fits everyone whose intrested and has the ambition of traveling. \n
    The trip includes a stream and nice pools. In it's begining you can also find
    an history and archeology pieces. ''')
db.session.add(trip)

trip=Trip(area='Haifa and Carmel mountain',
    classname='Center_Haifa_Hashofet',
    url='../static/pictures/Haifa_Hashofet.jpg',
    name='Hashofet stream',
    difficulty=1,
    info=''' It's an easy 2 km trip which includes a green, peaceful, water-full and unique view
    which make him to be one of the popular rivers in the country. \n
    The trip fits for all ages, families, and even for wheelchair in some places.\n
     ''')
db.session.add(trip)

trip=Trip(area='Haifa and Carmel mountain',
    classname='Center_Coastal-plain_SoreqAndPalmachim',
    url='../static/pictures/CoastalPlain_SoreqPalmachim.jpg',
    name='Little Switzerland',
    difficulty=2,
    info=''' One of the best trips in the Carmel mountain area. \n
    In 8 km of traveling you can find the area as almost hypnotist thanks for the amazing view. \n
    Fits for families who likes to travel, and even for dogs!
     ''')
db.session.add(trip)

trip=Trip(area='Haifa and Carmel mountain',
    classname='Center_Haifa_IsraelNationalTrail',
    url='../static/pictures/Haifa_Yagur.jpg',
    name='Israel national trail: Kibbuts Yagur to Ein Hod ',
    difficulty=5,
    info=''' This trip is part from the national trail of Israel (part 11). 
    It's a 21 km trip which fits people who used to travel a lot. 
    A wonderful trip which shows the beauty of Carmel mountain through view of 
    streams, caves, ruins, sprrings and even cliffs. 
    Recommended during flowring seasons.
    ''')
db.session.add(trip)

trip=Trip(area='Coastal plain',
    classname='Center_Coastal-plain_SoreqAndPalmachim',
    url='../static/pictures/CoastalPlain_SoreqPalmachim.jpg',
    name='Soreq stream and Palmachim beach ',
    difficulty=3,
    info=''' An amazing trip which combines the calm traveling in the beautiful beach of Palmachim
    and a short trip in the national park of Soreq stream. 5 km of beauty and peace. ''')
db.session.add(trip)

trip=Trip(area='The Shomron',
    classname='Center_Shomron_Petzl',
    url='../static/pictures/Shomron_Pzal.jpg',
    name='Petzl river',
    difficulty=4,
    info='''It's rare to hear about a trip which is almost unknown and still amazing in it's beauty. \n
    It's 10 km trip of challenging, peacefull, calm, full of sprrings, captor traveling. \n
    More than recommended for people who like to travel! 
    ''')
db.session.add(trip)

trip=Trip(area='Jerusalem',
    classname='Center_Jerusalem_katlav',
    url='../static/pictures/Jerusalem_Katlav.jpg',
    name='katlav river',
    difficulty=3,
    info=''' The river combines a chilly traveling through the bush forest and the river's pools. \n
    5 km trips which fits to families throughout all the year.
    ''')
db.session.add(trip)

trip=Trip(area='Dead sea and Judaean desert',
    classname='south_judaean_tzeelim',
    url='../static/pictures/Judaean_Tzeelim.jpg',
    name='Tzeelim river',
    difficulty=5,
    info=''' Tze'elim is hard trip which fits to people who used to travel a lot. \n
    It is one of the best trips in Judean desert which uncludes:
    amazing desert view, hiden pools, spring flowering etc. \n
    All of those and more, are part of the recipe for perfect trip.
    ''')
db.session.add(trip)

trip=Trip(area='Dead sea and Judaean desert',
    classname='south_judaean_peres',
    url='../static/pictures/Judaean_peres.jpg',
    name='peres river',
    difficulty=3,
    info=''' The trip in the lower part of the Nahal,
     is a 6 km trip which considered as a required trip for families who used to travel. \n
     The traveling is magical and totally recommended!!
    ''')
db.session.add(trip)

trip=Trip(area='north of the Negev',
    classname='south_NegevNorth_Nitzana',
    url='../static/pictures/northnegev_nitzana.jpg',
    name='nitzana',
    difficulty=1,
    info='''nitzana is one of those places you'll never see unless you'll travel them. \n
    it's a short trip, 3 km, which shows as uniqe part in the area. \n
    Fits to everyone, any time. \n
    Recommended!!
    ''')
db.session.add(trip)
trip=Trip(area='Center of the Negev and craters',
    classname='south_NegevCenter_Havarim',
    url='../static/pictures/Negevcenter_havarim.jpg',
    name='Havarim river',
    difficulty=2,
    info=''' You said full-moon-night? you said Havarim river! \n
    The trip, which is 3 km, is a not hard at all night trip which is 
    an amazing expiriece for the average traveler \n
    Very recommended! 
    ''')
db.session.add(trip)

trip=Trip(area='Center of the Negev and craters',
    classname='south_NegevCenter_Masor',
    url='../static/pictures/Negevcenter_masor.jpg',
    name='Masor mountain',
    difficulty=3,
    info=''' A short but challenging circular trip which fits people who used to travel. \n
    Masor is 180 meter above the sea mountain. 
    amazing trip!
    ''')
db.session.add(trip)

trip=Trip(area='South of the Negev and Eilat',
    classname='south_Negevsouth_timna',
    url='../static/pictures/southnegev_timna.jpg',
    name='Timna valley',
    difficulty=3,
    info=''' Timna park opens an unusual geological window which exposed us to beautiful rock formations.
    The breathtaking view of the drsert totally worth traveling.\n
    indeed recommended!
    ''')
db.session.add(trip)


db.session.commit()

print('Done')

