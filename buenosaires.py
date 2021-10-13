import folium
import branca
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="GoogleMaps")

import matplotlib.pyplot as plt

 

#mi_mapa = folium.Map(location=(-34.5459451, -58.7535187), zoom_start=5,  tiles= "Stamen Toner")
mi_mapa = folium.Map(location=(-34.9205, -57.9536), zoom_start=6,  tiles="Stamen Toner")

html1 = "<h2>CIUDAD DE SAN NICOLAS</h2>"
iframe1 = branca.element.IFrame(html=html1, width=250, height=150)



html2 = "<h1>CIUDAD DE TANDIL</h1><h2>'La ciudad de las diagonales'</h2>"
iframe2 = branca.element.IFrame(html=html2, width=250, height=150)

html3 = "<h1>BAHIA BLANCA</h1>"
iframe3 = branca.element.IFrame(html=html3, width=250, height=150)

html4 = "<h3>CIUDAD AUTÒNOMA DE BUENOS AIRES</h3>"
iframe4 = branca.element.IFrame(html=html4, width=250, height=150)



html5 = "<h1>CIUDAD DE LA PLATA</h1><h2>'La ciudad de las diagonales'</h2>"
iframe5 = branca.element.IFrame(html=html5, width=250, height=150)

html6 = "<h1>MAR DEL PLATA</h1>"
iframe6 = branca.element.IFrame(html=html6, width=250, height=150)



sannicolas = folium.Marker(location=(-33.3335, -60.2110),   popup=folium.Popup(iframe1, max_width=500),
    icon=folium.Icon(color="purple",icon= "info", icon_shape ="circle"))
sannicolas.add_to(mi_mapa)

tandil = folium.Marker(location=(-37.3288, -59.1367),   popup=folium.Popup(iframe2, max_width=500),
    icon=folium.Icon(color="red",icon= "info"))
tandil.add_to(mi_mapa)

bblanca = folium.Marker(location=(-38.7183, -62.2663),   popup=folium.Popup(iframe3, max_width=500),
    icon=folium.Icon(color="blue",icon= "info"))
bblanca.add_to(mi_mapa)

buenosaires = folium.Marker(location=(-34.61315, -58.37723),   popup=folium.Popup(iframe4, max_width=500),
    icon=folium.Icon(color='cadetblue',spin= "True"))
buenosaires.add_to(mi_mapa)

laplata = folium.Marker(location=(-34.9205, -57.9536),   popup=folium.Popup(iframe5, max_width=500),
    icon=folium.Icon(color="green"))
laplata.add_to(mi_mapa)

marplata = folium.Marker(location=(-38.0055,-57.5426),   popup=folium.Popup(iframe6, max_width=500),
    icon=folium.Icon(color="black"))
marplata.add_to(mi_mapa)



mi_mapa.save("baires.html")