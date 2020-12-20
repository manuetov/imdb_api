direccion = "http://www.omdbapi.com/?apikey=da22215a&i=tt3896198" #url a la que voy a llamar

# hacer peticion http y se guarda en respuesta
respuesta = requests.get(direccion) 

if respuesta.status_code == 200:
    print(respuesta.text)
    datos = respuesta.json() # guarda la respuesta de la petición en la variable datos
    print(datos)
else:
    print("se ha producido un error", respuesta.status_code)