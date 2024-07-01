import json


def separar_lista(lista: list, lista_pregunta, lista_opcion, lista_respuesta):
    for pregunta in lista:
        lista_pregunta.append(pregunta['pregunta'])
        lista_opcion.append(pregunta['a'])
        lista_opcion.append(pregunta['b'])
        lista_opcion.append(pregunta['c'])
        lista_respuesta.append(pregunta['correcta'])

def reiniciar_pasar_pregunta(lista: list, reiniciar: bool = False):
    if reiniciar == False:
        lista[0]['pregunta'] += 1
        lista[1]['opcion'] += 3
        lista[2]['respuesta'] += 1
    else:
        lista[0]['pregunta'] = 0
        lista[1]['opcion'] = 0
        lista[2]['respuesta'] = 0

def resetear_sumar_score(score, font, sumar: bool = True):
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
    No recibe nada, se encarga de cargar un archivo de tipo json, retorna un diccionario \n
    No recibe nada\n
    Retorna un diccionario con los datos del archivo
    '''
    with open("D:\Material de universidad\programacion\Programacion 1\Clases\Pygame\juego_p\mayores_puntajes.json") as archivo:
        datos = json.load(archivo)
    return datos

def ordenar_lista_burbujeo(lista: list, criterio: str):
    '''
    Recibe un diccionario y un criterio, ordena el diccionario de acuerdo al criterio\n
    Recibe un diccionario de tipo dict y un criterio de tipo str\n
    No retorna nada
    '''
    criterio = criterio.upper()
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if (criterio == "ASC" and lista[i]['score'] > lista[j]['score']) or (criterio == "DESC" and lista[i]['score'] < lista[j]['score']):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

def agregar_a_lista(lista, score_nuevo, nombre_nuevo):
    '''
    
    '''
    if int(lista[2]['score']) < score_nuevo:
        lista[2]['score'] = score_nuevo
        lista[2]['nombre'] = nombre_nuevo

