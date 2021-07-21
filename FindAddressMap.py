import gmplot
import googlemaps
import json

APIKey_Addr = "/home/matanya/Documents/GitHub/Google_API_key.txt"
f = open(APIKey_Addr)
apikey = f.read()
f.close()
print("API Key retrived as: " + apikey)

def make_map(addr_str):
    
    gmaps = googlemaps.Client(key=apikey)

    # address_string = '6015 East Bayaud Ave'
    address_string = addr_str

    geocode_result = gmaps.geocode(address_string)

    lat = geocode_result[0]['geometry']['location']['lat']
    lng = geocode_result[0]['geometry']['location']['lng']

    gmplot_obj = gmplot.GoogleMapPlotter(lat, lng, 17, apikey=apikey, map_type='hybrid')

    gmplot_obj.marker(lat, lng, color='yellow')

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

    gmplot_obj.polygon(*polygon_greeley, face_color='pink', edge_color='cornflowerblue', edge_width=5)

    html_map = gmplot_obj.get()
    head_index = html_map.find('<head>')
    html_finished = html_map[:(head_index + 7)] + '<script type="text/javascript" src="https://livejs.com/live.js"></script>\n' + html_map[(head_index + 7):]
    current_view = open("address_map_live.html", "w")
    current_view.write(html_finished)
    current_view.close

    return None

# python3 -m http.server
