import folium
import branca
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="GoogleMaps")

import matplotlib.pyplot as plt

 

 
'''
location1 = geolocator.geocode("General Pinto 3974, Jose C Paz")
location2 = geolocator.geocode("Craig 1865, Merlo")
location3 = geolocator.geocode(" Villa Sanagasta")
print(location1.address)
print((location1.latitude, location1.longitude))
print((location2.latitude, location2.longitude))
print((location3.latitude, location3.longitude))
print(location1.raw)
'''
#mi_mapa = folium.Map(location=(-34.5459451, -58.7535187), zoom_start=5,  tiles= "Stamen Toner")
mi_mapa = folium.Map(location=(-34.5459451, -58.7535187), zoom_start=5,  tiles="Stamen Terrain")
html = "<p>primera geolocalizacion</p><p>CASA DE MARIA MACHACA</p>"
iframe1 = branca.element.IFrame(html=html, width=250, height=150)


html2 = "<h1>NUESTRA CASA</h1><h2> esto es un subtitulo</h2>"
iframe2 = branca.element.IFrame(html=html2, width=250, height=150)

html3 = "<h1>Villa Sanagasta</h1><h2> CASA DE CLAUDIA</h2><img src='img2.png'>"
iframe3 = branca.element.IFrame(html=html3, width=250, height=150)

html4 = "<h1>PROVINCIA DE BUENOS AIRES</h1>"
iframe4 = branca.element.IFrame(html=html4, width=250, height=150)

html5 = "<h1>PROVINCIA DE CORDOBA</h1>"
iframe5 = branca.element.IFrame(html=html5, width=250, height=150)

html6 = "<h1>PROVINCIA DE SANTA FE</h1>"
iframe6 = branca.element.IFrame(html=html6, width=250, height=150)

html7 = "<h1>PROVINCIA DE MENDOZA</h1>"
iframe7 = branca.element.IFrame(html=html7, width=250, height=150)

html8 = "<h1>PROVINCIA DE TUCUMAN</h1>"
iframe8 = branca.element.IFrame(html=html8, width=250, height=150)

html9 = "<h1>PROVINCIA DE SALTA </h1>"
iframe9 = branca.element.IFrame(html=html9, width=250, height=150)

html10 = "<h1>PROVINCIA DE SAN JUAN </h1>"
iframe10 = branca.element.IFrame(html=html10, width=250, height=150)

html11 = "<h1>PROVINCIA DE CHACO</h1>"
iframe11 = branca.element.IFrame(html=html11, width=250, height=150)

html12 = "<h1>PROVINCIA DE SANTIAGO DEL ESTERO</h1>"
iframe12 = branca.element.IFrame(html=html12, width=250, height=150)

html13 = "<h1>PROVINCIA DE MISIONES</h1>"
iframe13 = branca.element.IFrame(html=html13, width=250, height=150)

html14 = "<h1>PROVINCIA DE  JUJUY</h1>"
iframe14 = branca.element.IFrame(html=html14, width=250, height=150)

html15 = "<h1>PROVINCIA DE  LA PAMPA</h1>"
iframe15 = branca.element.IFrame(html=html15, width=250, height=150)

html16 = "<h1>PROVINCIA DE  SAN LUIS</h1>"
iframe16 = branca.element.IFrame(html=html16, width=250, height=150)

html17 = "<h1>PROVINCIA DE  LA RIOJA</h1>"
iframe17 = branca.element.IFrame(html=html17, width=250, height=150)

html18 = "<h1>PROVINCIA DE  CORRIENTES</h1>"
iframe18 = branca.element.IFrame(html=html18, width=250, height=150)

html19 = "<h1>PROVINCIA DE FORMOSA</h1>"
iframe19 = branca.element.IFrame(html=html19, width=250, height=150)

html20 = "<h1>PROVINCIA DE  ENTRE RIOS</h1>"
iframe20 = branca.element.IFrame(html=html20, width=250, height=150)

html21 = "<h3>PROVINCIA DE  TIERRA DE FUEGO</h3>"
iframe21 = branca.element.IFrame(html=html21, width=250, height=150)

html22 = "<h1>PROVINCIA DE  RIO NEGRO </h1>"
iframe22 = branca.element.IFrame(html=html22, width=250, height=150)

html23 = "<h1>PROVINCIA DE  NEUQUEN</h1>"
iframe23 = branca.element.IFrame(html=html23, width=250, height=150)

html24 = "<h1>PROVINCIA DE CHUBUT</h1>"
iframe24 = branca.element.IFrame(html=html24, width=250, height=150)




marcador1 = folium.Marker(location=(-34.5459400, -58.7535187),   popup=folium.Popup(iframe2, max_width=500),
    icon=folium.Icon(color="purple",spin= "True",icon= "home", icon_shape ="circle"))
marcador1.add_to(mi_mapa)

marcador2 = folium.Marker(location=(-34.6935665, -58.6596387),   popup=folium.Popup(iframe1, max_width=500),
    icon=folium.Icon(color="red",icon= "cloud"))


marcador3 = folium.Marker(location=(-29.2860467, -67.0206767),   popup=folium.Popup(iframe3, max_width=500),
    icon=folium.Icon(color="green",icon= "camera"))
buenosaires = folium.Marker(location=(-34.61315, -58.37723),   popup=folium.Popup(iframe4, max_width=500),
    icon=folium.Icon(color="blue"))
buenosaires.add_to(mi_mapa)
cordoba = folium.Marker(location=(-31.4135, -64.18105),   popup=folium.Popup(iframe5, max_width=500),
    icon=folium.Icon(color="blue"))
cordoba.add_to(mi_mapa)

santafe = folium.Marker(location=(-32.94682, -60.63932),   popup=folium.Popup(iframe6, max_width=500),
    icon=folium.Icon(color="blue"))
santafe.add_to(mi_mapa)
mendoza = folium.Marker(location=(-32.89084, -68.82717),   popup=folium.Popup(iframe7, max_width=500),
    icon=folium.Icon(color="blue"))
mendoza.add_to(mi_mapa)
tucuman = folium.Marker(location=(-26.82414, -65.2226),   popup=folium.Popup(iframe8, max_width=500),
    icon=folium.Icon(color="blue"))
tucuman.add_to(mi_mapa)
salta = folium.Marker(location=(-24.7859, -65.41166),   popup=folium.Popup(iframe9, max_width=500),
    icon=folium.Icon(color="blue"))
salta.add_to(mi_mapa)
sanjuan = folium.Marker(location=(-31.5375, -68.53639),   popup=folium.Popup(iframe10, max_width=500),
    icon=folium.Icon(color="blue"))
sanjuan.add_to(mi_mapa)
chaco = folium.Marker(location=(-27.46056, -58.98389),   popup=folium.Popup(iframe11, max_width=500),
    icon=folium.Icon(color="blue"))
chaco.add_to(mi_mapa)
santiago  = folium.Marker(location=(-27.79511, -64.26149),   popup=folium.Popup(iframe12, max_width=500),
    icon=folium.Icon(color="blue"))
santiago.add_to(mi_mapa)
misiones = folium.Marker(location=(-27.36708, -55.89608),   popup=folium.Popup(iframe13, max_width=500),
    icon=folium.Icon(color="blue"))
misiones.add_to(mi_mapa)
jujuy = folium.Marker(location=(-24.19457, -65.29712),   popup=folium.Popup(iframe14, max_width=500),
    icon=folium.Icon(color="blue"))
jujuy.add_to(mi_mapa)

lapampa= folium.Marker(location=(-38.4161 , -63.6167),   popup=folium.Popup(iframe15, max_width=500),
    icon=folium.Icon(color="blue"))
lapampa.add_to(mi_mapa)
sanluis = folium.Marker(location=(-33.3017 , -66.3378),   popup=folium.Popup(iframe16, max_width=500),
    icon=folium.Icon(color="blue"))
sanluis.add_to(mi_mapa)
larioja = folium.Marker(location=(-29.4135, -66.8565),   popup=folium.Popup(iframe17, max_width=500),
    icon=folium.Icon(color="blue"))
larioja.add_to(mi_mapa)
corrientes = folium.Marker(location=(-27.4692, -58.8306),   popup=folium.Popup(iframe18, max_width=500),
    icon=folium.Icon(color="blue"))
corrientes.add_to(mi_mapa)
formosa = folium.Marker(location=(-26.1858, -58.1756),   popup=folium.Popup(iframe19, max_width=500),
    icon=folium.Icon(color="green"))
formosa.add_to(mi_mapa)
entrerios = folium.Marker(location=(-31.7413, -60.5115),   popup=folium.Popup(iframe20, max_width=500),
    icon=folium.Icon(color="green"))
entrerios.add_to(mi_mapa)
tdelfuego = folium.Marker(location=(-54.8019,-68.3030),   popup=folium.Popup(iframe21, max_width=500),
    icon=folium.Icon(color="green"))
tdelfuego.add_to(mi_mapa)
rionegro = folium.Marker(location=(-40.8119, -62.9962),   popup=folium.Popup(iframe22, max_width=500),
    icon=folium.Icon(color="green"))
rionegro.add_to(mi_mapa)
neuquen = folium.Marker(location=(-38.9517, -68.0592),   popup=folium.Popup(iframe23, max_width=500),
    icon=folium.Icon(color="green"))
neuquen.add_to(mi_mapa)
chubut = folium.Marker(location=(-43.2999, -65.0995),   popup=folium.Popup(iframe24, max_width=500),
    icon=folium.Icon(color="green"))
chubut.add_to(mi_mapa)
  
marcador1.add_to(mi_mapa)
marcador2.add_to(mi_mapa)
marcador3.add_to(mi_mapa)


mi_mapa.save("mapa4.html")