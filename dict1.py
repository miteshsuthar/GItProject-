room={'Amenities': ['Wheelchair access',
    'Car rental desk',
    'Non-smoking rooms (generic)',
    'Family Room',
    'Rollaway adult',
    'Business center',
    'Tennis court',
    'Golf',
    'Conference facilities',
    'Data port',
    'High speed internet access',
    'Interior corridors',
    'Executive floor',
    'Game room',
    'Health club',
    'Outdoor pool',
    'Pool',
    'Room service',
    'Dry cleaning'],
   'HotelAddress': '1111 S. Royal Poinciana Blvd',
   'HotelCode': '100045906',
   'HotelContact': {'Fax': '305-884-1881', 'Phone': '305-885-1941'},
   'HotelImages': ['http://vcmp-hotels.cert.sabre.com/image/upload/f_auto,q_auto:best/hotel/i/2467/csjihvgzxqkhqgdw0mtz.jpg'],
   'HotelLogo': 'http://vcmp-hotels.cert.sabre.com/image/upload/f_auto,q_auto:best,t_vcmp_logo/hotel/l/hi/HI.png',
   'HotelName': 'Holiday Inn - Intl Airport N',
   'HotelSabreRating': 3.0,
   'Latitude': '25.80877',
   'Longitude': '-80.26371',
   'SabreHotelCode': '100045906',
   'availableRoomQuantity0': 7,
   'availableRoomQuantity2': 6,
   'currencyCode0': 'USD',
   'currencyCode2': 'USD',
   'hotelDistance': 2.02,
   'roomRate0': 800.95,
   'roomRate2': 762.99,
   'roomType0': 'DOUBLE GUEST ROOM',
   'roomType2': 'King Room - Non-Smoking'}

l1=[]
d_item=room.items()
for i in d_item:
    if '0' in i[0]:
        l1.append(i)
    if '2' in i[0]:
        l1.append(i)
print(l1)