import json

def separar_lista(lista: list, lista_pregunta: list, lista_opcion: list, lista_respuesta: list):
    '''
    Recibe 4 listas y se encarga de agragar datos de la primer lista entre las demas, no retorna nada\n
    Recibe 4 lista de tipo list\n
    No retorna nada
    '''
    for pregunta in lista:
        lista_pregunta.append(pregunta['pregunta'])
        lista_opcion.append(pregunta['a'])
        lista_opcion.append(pregunta['b'])
        lista_opcion.append(pregunta['c'])
        lista_respuesta.append(pregunta['correcta'])

def reiniciar_pasar_pregunta(lista: list, reiniciar: bool = False):
    '''
    Recibe una lista y un bool, aumenta los valores dentro de la lista en caso de que el bool sea False, en caso contrario los pone en cero, no retorna nadan\n
    Recibe una lista de tipo list y un reiniciar de tipo bool\n
    No retorna nada
    '''
    if reiniciar == False:
        lista[0]['pregunta'] += 1
        lista[1]['opcion'] += 3
        lista[2]['respuesta'] += 1
    else:
        lista[0]['pregunta'] = 0
        lista[1]['opcion'] = 0
        lista[2]['respuesta'] = 0

def resetear_sumar_score(score, font, sumar: bool = True):
    '''
    Recibe un score, un font y un sumar, si sumar es True el score se incrementa en 10 y se crea un texto, caso contrario el score se pone en 0 y se crea un texto, retorna el texto y el score\n
    Recibe un score de tipo str, un font de tipo font y un sumar de tipo bool\n
    Retorna un text_score_num de tipo surface y un score de tipo int 
    '''
    if sumar == True:
        score = int(score) + 10
        text_score_num = font.render(str(score), True, (255, 255, 255))
    else:
        score = 0
        text_score_num = font.render(str(score), True, (255, 255, 255))
    return text_score_num, score

def guardar_json(lista: dict):
    '''
    Recibe una lista , se encarga de pedir el nombre del archivo a crear, lo crea haciendo que sea de tipo json y muestra por consola un mensaje de que se creo el archivo\n
    Recibe una lista de tipo list\n
    No retorna nada
    '''
    with open(f"D:\Material de universidad\programacion\Programacion 1\Clases\Pygame\juego_p\mayores_puntajes.json", "w") as archivo:
        json.dump(lista,archivo,indent=4,ensure_ascii=False)

def cargar_archivo_json() ->dict:
    '''
    No recibe nada, se encarga de cargar un archivo de tipo json, retorna una lista \n
    No recibe nada\n
    Retorna una lista con los datos del archivo
    '''
    with open("D:\Material de universidad\programacion\Programacion 1\Clases\Pygame\juego_p\mayores_puntajes.json") as archivo:
        datos = json.load(archivo)
    return datos

def ordenar_lista_burbujeo(lista: list, criterio: str):
    '''
    Recibe una lista y un criterio, ordena el diccionario de acuerdo al criterio\n
    Recibe una lista de tipo list y un criterio de tipo str\n
    No retorna nada
    '''
    criterio = criterio.upper()
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if (criterio == "ASC" and lista[i]['score'] > lista[j]['score']) or (criterio == "DESC" and lista[i]['score'] < lista[j]['score']):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

def agregar_a_lista(lista: list, score_nuevo: int, nombre_nuevo: str):
    '''
    Recibe una lista, un score_nuevo y un nombre_nuevo, si en el indice 2 de la lista el score anterior es menor al score_nuevo se remplaza el score y el nombre\n
    Recibe una lista de tipo list, un score_nuevo de tipo int y un nombre_nuevo de tipo str\n
    No retorna nada
    '''
    if int(lista[2]['score']) < score_nuevo:
        lista[2]['score'] = score_nuevo
        lista[2]['nombre'] = nombre_nuevo