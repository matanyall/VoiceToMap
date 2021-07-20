import gmplot
import googlemaps
import json

APIKey_Addr = "/home/matanya/Documents/GitHub/Google_API_key.txt"
f = open(APIKey_Addr)
apikey = f.read()
f.close()
print("API Key retrived as: " + apikey)


def make_map(addr_str):
    
    # gmap = gmplot.GoogleMapPlotter(39.85703116, -104.67212234, 13, apikey=apikey, map_type='hybrid')
    gmaps = googlemaps.Client(key=apikey)

    # address_string = '7015 East Bayaud Ave'
    address_string = addr_str

    geocode_result = gmaps.geocode(address_string)

    #geocode = geocode_result.json()
    # geocode_dict = json.loads(geocode)
    # geocode_dict = { k[0]: k[1:] for k in geocode_result}

    # print(geocode_result[0]['geometry']['location']['lat'])

    lat = geocode_result[0]['geometry']['location']['lat']
    lng = geocode_result[0]['geometry']['location']['lng']

    gmap2 = gmplot.GoogleMapPlotter(lat, lng, 17, apikey=apikey, map_type='hybrid')

    gmap2.marker(lat, lng, color='yellow')

    polygon_greeley = zip(*[
        [40.421438131818945, -104.90689922760113], 
        [40.39264010682981, -104.90704357703802],
        [40.37768665590296, -104.87052316950425], 
        [40.377576691763664, -104.79445101626195],
        [40.3848339399258, -104.78463525478912],
        [40.3848339399258, -104.70134562970222],
        [40.39692761623743, -104.69109681968285],
        [40.39725741334982, -104.68546719164405],
        [40.385163796268856, -104.68763243319744], 
        [40.38528766701501, -104.66799532081751],
        [40.3989698462869, -104.64941849606247],
        [40.4109394726745, -104.67340505549893],
        [40.44233019425396, -104.68616386374667],
        [40.43759144538182, -104.71525394635309],
        [40.437513758188885, -104.78894882257916], 
        [40.42140372290265, -104.81339009550702],
        [40.421926461435596, -104.90694554618952]
    ])

    gmap2.polygon(*polygon_greeley, face_color='pink', edge_color='cornflowerblue', edge_width=5)



    # print(geocode_result)
    #gmap2.draw('map3.html')

    # gmap2.draw('map2.html')
    html_map = gmap2.get()
    head_index = html_map.find('<head>')
    html_finished = html_map[:(head_index + 7)] + '<script type="text/javascript" src="https://livejs.com/live.js"></script>\n' + html_map[(head_index + 7):]
    current_view = open("address_map_live.html", "w")
    current_view.write(html_finished)
    current_view.close

    return None

# marker_color="yellow"
# for runway in runway_coordinates:
#     gmap.marker(runway_coordinates[runway][0], runway_coordinates[runway][1], color=marker_color, title=runway, label=runway, info_window="RUNWAY %s" % (runway))

# gmap.marker(39.895833, -104.696167, color='yellow', title='16R', label='16R', info_window="RUNWAY 16R")
# gmap.marker(39.851833, -104.696667, color='yellow', title='34L', label='34L', info_window="RUNWAY 34L")
# gmap.marker(39.841, -104.726667, color='yellow', title='07', label='07', info_window="RUNWAY 07")
# gmap.marker(39.840667, -104.684, color='yellow', title='25', label='25', info_window="RUNWAY 25")
# gmap.marker(39.8775, -104.662167, color='yellow', title='08', label='08', info_window="RUNWAY 08")
# gmap.marker(39.877167, -104.6195, color='yellow', title='26', label='26', info_window="RUNWAY 26")
# gmap.marker(39.897, -104.686833, color='yellow', title='16L', label='16L', info_window="RUNWAY 16L")
# gmap.marker(39.864167, -104.687167, color='yellow', title='34R', label='34R', info_window="RUNWAY 34R")
# gmap.marker(39.865, -104.641333, color='yellow', title='17L', label='17L', info_window="RUNWAY 17L")
# gmap.marker(39.832, -104.641667, color='yellow', title='35R', label='35R', info_window="RUNWAY 35R")
# gmap.marker(39.861167, -104.660167, color='yellow', title='17R', label='17R', info_window="RUNWAY 17R")
# gmap.marker(39.828333, -104.6605, color='yellow', title='35L', label='35L', info_window="RUNWAY 35L")

# python3 -m http.server
