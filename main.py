import requests

pregunta = input("Título de la película")

API_KEY = "da22215a"

direccion = "http://www.ombapi.com/?apikey={}&s={}".format(API_KEY, pregunta)

respuesta = requests.get(direccion)

if respuesta.status_code = 200
    datos = respuesta.json()
    if datos['Response']== "False":
        print(datos["Error"])
    else:
        primera_peli = datos['search'][0]
        clave = primera_peli['imdbID']

        otra_direccion = direccion = "http://www.ombapi.com/?apikey={}&i={}".format(API_KEY, clave)
        nueva_respuesta = requests.get(otra_direccion)
        if nueva_respuesta.status_code == 200:
            datos = nueva_respuesta.json()
            if datos ['Response'] == "False":
                print(datos["Error"])
            else:
                titulo = datos['Title']
                agno = datos['Year']
                director = datos['Director']
                print("la peli {}, estrenada el año {}, fue dirigida por {}".format(titulo, agno, director))
            else:
                print("error en consulta por id", nueva_respuesta.status_code)
else:
    print("error en consulta en búsqueda", nueva_respuesta.status_code)
            
