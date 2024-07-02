from datos import lista
from biblioteca_juego import *
import pygame

# INICIA PYGAME
pygame.init()
pygame.mixer.init()

# ESTABLECE Y SEPARA LISTAS
lista_pregunta = []
lista_opcion = []
lista_respuesta = []
separar_lista(lista, lista_pregunta, lista_opcion, lista_respuesta)
lista_indices = [{'pregunta': 0}, {'opcion': 0}, {'respuesta': 0}]
lista_mejor_puntuacion = cargar_archivo_json()

# NOMBRE DE VENTANA
pygame.display.set_caption("Preguntados")

# TAMAÑO DE VENTANA
config_pantalla = [1280, 720]
screen = pygame.display.set_mode(config_pantalla)

# RECTANGULOS (OBJETO)
rect_boton_jugar = pygame.Rect(850, 350, 280, 70)
rect_boton_puntaje = pygame.Rect(850, 450, 280, 70)
rect_boton_salir = pygame.Rect(850, 550, 280, 70)
rect_boton_mutear_desmutear = pygame.Rect(10, 600, 280, 70)

rect_boton_pregunta = pygame.Rect(490, 50, 280, 70)
rect_boton_reiniciar = pygame.Rect(490, 600, 280, 70)
rect_boton_opcion_a = pygame.Rect(100, 400, 270, 50)
rect_boton_opcion_b = pygame.Rect(390, 400, 240, 50)
rect_boton_opcion_c = pygame.Rect(650, 400, 320, 50)

rect_boton_mute_desmute = pygame.Rect(1, 620, 100, 100)

rect_tabla_puntajes = pygame.Rect(200, 100, 900, 500)

rect_boton_volver_menu = pygame.Rect(950, 625, 320, 75)

# IMAGEN CON REESCALADO
imagen_preguntados = pygame.image.load("D:/Material de universidad/programacion/Programacion 1/Clases/Pygame/juego_p/imagen_juego/png-transparent-trivia-crack-no-ads-quiz-logo-game-android-game-smiley-crack.png")
imagen_preguntados = pygame.transform.scale(imagen_preguntados, (480, 200))

imagen_fondo_menu = pygame.image.load("D:/Material de universidad/programacion/Programacion 1/Clases/Pygame/juego_p/imagen_juego/698800preguntados-22png.png")
imagen_fondo_menu = pygame.transform.scale(imagen_fondo_menu, (1280, 720))

imagen_sonido_desmuteado = pygame.image.load("D:/Material de universidad/programacion/Programacion 1/Clases/Pygame/juego_p/imagen_juego/Desmuteado.png")
imagen_sonido_desmuteado = pygame.transform.scale(imagen_sonido_desmuteado, (100, 100))

imagen_sonido_mute = pygame.image.load("D:/Material de universidad/programacion/Programacion 1/Clases/Pygame/juego_p/imagen_juego/Muteado.png")
imagen_sonido_mute = pygame.transform.scale(imagen_sonido_mute, (100, 100))

# Sonido
pygame.mixer.music.load("D:/Material de universidad/programacion/Programacion 1/Clases/Pygame/juego_p/audios_juego/Musica_fondo.mp3")
pygame.mixer.music.play(-1)


sonido_fallar_pregunta = pygame.mixer.Sound("D:/Material de universidad/programacion/Programacion 1/Clases/Pygame/juego_p/audios_juego/Fallar_respuesta.mp3")
sonido_fallar_pregunta.set_volume(0.5)

sonido_acertar_pregunta = pygame.mixer.Sound("D:/Material de universidad/programacion/Programacion 1/Clases/Pygame/juego_p/audios_juego/Acertar_respuesta.mp3")
sonido_acertar_pregunta.set_volume(0.5)

# COLORES
color_blanco = (250, 250, 250)
color_negro = (0, 0, 0)
color_verde = (80, 200, 120)
color_gris = (128, 128, 128)
color_celeste = (173, 216, 230)
color_violeta = (238, 130, 238)

# FUENTE DE LETRAS
font = pygame.font.SysFont("Arial Narrow", 50)

# TEXTOS
text_posicion = font.render("POSICION", True, color_negro)
text_posicion_uno = font.render("1", True, color_negro)
text_posicion_dos = font.render("2", True, color_negro)
text_posicion_tres = font.render("3", True, color_negro)
text_nombre = font.render("NOMBRES", True, color_negro)
texto_puntajes = font.render("PUNTAJES", True, color_negro)

text_jugar = font.render("JUGAR", True, color_blanco)
text_puntaje = font.render("VER PUNTAJE", True, color_blanco)
text_salir = font.render("SALIR", True, color_blanco)

text_pregunta = font.render("Pregunta", True, color_blanco)
text_reiniciar = font.render("Reiniciar", True, color_blanco)
text_score_txt = font.render("SCORE: ", True, color_blanco)
text_volver_menu = font.render("VOLVER A MENU", True, color_negro)

texto_preguntar_nombre = font.render("INGRESE SU NOMBRE (COMO MAXIMO 20 caracteres): ", True, color_blanco)
text_pedir_nombre_valido = font.render("# PORFAVOR INGRESE UN NOMBRE QUE NO ESTE VACIO", True, color_verde)

# SCORE Y SU TEXTO
score = 0
text_score_num = font.render(str(score), True, color_blanco)

# VARIABLES DE CONTROL
corriendo = True
ventana_menu = True
ventana_puntaje = False
ventana_juego = False
muteado = False
ver_preguntas = False
ocultar_a = False
correcta_a = False
ocultar_b = False
correcta_b = False
ocultar_c = False
correcta_c = False
termino_texto_nombre = False
nombre_vacio = False
nombre_jugador = ""
contador_fallas = 0
contador_tiempo = 0

while corriendo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            corriendo = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if ventana_menu == True:
                if rect_boton_salir.collidepoint(event.pos): 
                    corriendo = False
                if rect_boton_jugar.collidepoint(event.pos): 
                    ventana_menu = False
                    ventana_juego = True
                if rect_boton_puntaje.collidepoint(event.pos):
                    ventana_menu = False
                    ventana_puntaje = True
                if rect_boton_mute_desmute.collidepoint(event.pos):
                    if muteado == False:
                        muteado = True
                        pygame.mixer.music.stop()
                    else:
                        muteado = False
                        pygame.mixer.music.play(-1)

            if ventana_puntaje == True:
                if rect_boton_volver_menu.collidepoint(event.pos):
                    ventana_puntaje = False
                    ventana_menu = True

            if ventana_menu == False and ventana_juego == True:
                if lista_indices[0]['pregunta'] < len(lista_pregunta):
                    if rect_boton_volver_menu.collidepoint(event.pos):
                        ventana_juego = False
                        ventana_menu = True
                        text_score_num, score = resetear_sumar_score(lista_indices, font, False)
                        reiniciar_pasar_pregunta(lista_indices, True)
                        ocultar_b = False
                        ocultar_a = False
                        ocultar_c = False
                        ver_preguntas = False

                    if rect_boton_pregunta.collidepoint(event.pos): 
                        if ver_preguntas == True:
                            reiniciar_pasar_pregunta(lista_indices)
                            ocultar_b = False
                            ocultar_a = False
                            ocultar_c = False
                        ver_preguntas = True
                    
                    if rect_boton_reiniciar.collidepoint(event.pos): 
                        text_score_num, score = resetear_sumar_score(lista_indices, font, False)
                        reiniciar_pasar_pregunta(lista_indices, True)
                        ocultar_b = False
                        ocultar_a = False
                        ocultar_c = False

                    if ver_preguntas == True:
                        if rect_boton_opcion_a.collidepoint(event.pos):
                            if lista_respuesta[lista_indices[2]['respuesta']] == 'a':
                                sonido_acertar_pregunta.play()
                                correcta_a = True
                                text_score_num, score = resetear_sumar_score(score, font)
                                reiniciar_pasar_pregunta(lista_indices)
                                ocultar_b = False
                                ocultar_a = False
                                ocultar_c = False
                                contador_fallas = 0
                            else:
                                sonido_fallar_pregunta.play()
                                ocultar_a = True
                                contador_fallas +=1

                        if rect_boton_opcion_b.collidepoint(event.pos):
                            if lista_respuesta[lista_indices[2]['respuesta']] == 'b':
                                sonido_acertar_pregunta.play()
                                correcta_b = True
                                text_score_num, score = resetear_sumar_score(score, font)
                                reiniciar_pasar_pregunta(lista_indices)
                                ocultar_b = False
                                ocultar_a = False
                                ocultar_c = False
                                contador_fallas = 0

                            else:
                                sonido_fallar_pregunta.play()
                                ocultar_b = True
                                contador_fallas +=1

                        if rect_boton_opcion_c.collidepoint(event.pos): 
                            if lista_respuesta[lista_indices[2]['respuesta']] == 'c':
                                sonido_acertar_pregunta.play()
                                correcta_c = True
                                text_score_num, score = resetear_sumar_score(score, font)
                                reiniciar_pasar_pregunta(lista_indices)
                                ocultar_b = False
                                ocultar_a = False
                                ocultar_c = False
                                contador_fallas = 0
                            else:
                                sonido_fallar_pregunta.play()
                                ocultar_c = True
                                contador_fallas +=1
                            
                        if contador_fallas == 2:
                            reiniciar_pasar_pregunta(lista_indices)
                            contador_fallas = 0
                            ocultar_b = False
                            ocultar_a = False
                            ocultar_c = False
        if event.type == pygame.KEYDOWN:
            if lista_indices[0]['pregunta'] >= len(lista_pregunta):
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    if nombre_jugador != "":
                        termino_texto_nombre = True
                        nombre_vacio = False
                    else:
                        nombre_vacio = True

                elif event.key == pygame.K_BACKSPACE:
                    nombre_jugador = nombre_jugador[:-1]
                else:
                    if len(nombre_jugador) < 20:
                        nombre_jugador += event.unicode

    if ventana_menu == True:
        screen.fill(color_gris)
        screen.blit(imagen_fondo_menu, (0, 0))

        pygame.draw.rect(screen, color_gris, rect_boton_salir, border_radius=15)
        pygame.draw.rect(screen, color_gris, rect_boton_jugar, border_radius=15)
        pygame.draw.rect(screen, color_gris, rect_boton_puntaje, border_radius=15)
        pygame.draw.rect(screen, color_blanco, rect_boton_mute_desmute, border_radius=15)

        if muteado == False:
            screen.blit(imagen_sonido_desmuteado, (1, 620))
        else:
            screen.blit(imagen_sonido_mute, (1, 620))

        screen.blit(text_jugar, (935, 370))
        screen.blit(text_puntaje, (875, 470))
        screen.blit(text_salir, (935, 570))

    elif ventana_puntaje == True:
        screen.fill(color_violeta)

        pygame.draw.rect(screen, color_blanco, rect_boton_volver_menu, border_radius=15)
        pygame.draw.rect(screen, color_negro, rect_boton_volver_menu, width=10, border_radius=15)
        pygame.draw.rect(screen, color_blanco, rect_tabla_puntajes, border_radius=15)
        pygame.draw.rect(screen, color_negro, rect_tabla_puntajes, width=10, border_radius=15)
        pygame.draw.line(screen, color_negro, (425, 100), (425, 590), width=10)
        pygame.draw.line(screen, color_negro, (835, 100), (835, 590), width=10)
        pygame.draw.line(screen, color_negro, (200, 225), (1090, 225), width=10)
        pygame.draw.line(screen, color_negro, (200, 335), (1090, 335), width=10)
        pygame.draw.line(screen, color_negro, (200, 450), (1090, 450), width=10)

        screen.blit(text_volver_menu, (975, 650))
        screen.blit(text_posicion, (225, 150))
        screen.blit(text_posicion_uno, (300, 250))
        screen.blit(text_posicion_dos, (300, 375))
        screen.blit(text_posicion_tres, (300, 500))
        screen.blit(text_nombre, (550, 150))
        screen.blit(texto_puntajes, (875, 150))

        if lista_mejor_puntuacion[0]['nombre'] != "":
            text_posicion_uno_nombre = font.render(lista_mejor_puntuacion[0]['nombre'], True, color_negro)
        else:
            text_posicion_uno_nombre = font.render("-"*31, True, color_negro)

        if lista_mejor_puntuacion[1]['nombre'] != "":
            text_posicion_dos_nombre = font.render(lista_mejor_puntuacion[1]['nombre'], True, color_negro)
        else:
            text_posicion_dos_nombre = font.render("-"*31, True, color_negro)

        if lista_mejor_puntuacion[2]['nombre'] != "":
            text_posicion_tres_nombre = font.render(lista_mejor_puntuacion[2]['nombre'], True, color_negro)
        else:
            text_posicion_tres_nombre = font.render("-"*31, True, color_negro)

        if lista_mejor_puntuacion[0]['score'] > -1:
            text_posicion_uno_num = font.render(str(lista_mejor_puntuacion[0]['score']), True, color_negro)
        else:
            text_posicion_uno_num = font.render("-", True, color_negro)

        if lista_mejor_puntuacion[1]['score'] > -1:
            text_posicion_dos_num = font.render(str(lista_mejor_puntuacion[1]['score']), True, color_negro)
        else:
            text_posicion_dos_num = font.render("-", True, color_negro)

        if lista_mejor_puntuacion[2]['score'] > -1:
            text_posicion_tres_num = font.render(str(lista_mejor_puntuacion[2]['score']), True, color_negro)
        else:
            text_posicion_tres_num = font.render("-", True, color_negro)
        
        screen.blit(text_posicion_uno_nombre, (450, 260))
        screen.blit(text_posicion_uno_num, (965, 260))
        screen.blit(text_posicion_dos_nombre, (450, 375))
        screen.blit(text_posicion_dos_num, (965, 375))
        screen.blit(text_posicion_tres_nombre, (450, 500))
        screen.blit(text_posicion_tres_num, (965, 500))


    elif ventana_juego == True and lista_indices[0]['pregunta'] < len(lista_pregunta):
        screen.fill(color_celeste)

        pygame.draw.rect(screen, color_gris, rect_boton_pregunta, border_radius=15)
        pygame.draw.rect(screen, color_gris, rect_boton_reiniciar, border_radius=15)
        pygame.draw.rect(screen, color_blanco, rect_boton_volver_menu, border_radius=15)
        pygame.draw.rect(screen, color_negro, rect_boton_volver_menu, width=10, border_radius=15)

        screen.blit(text_volver_menu, (975, 650))
        screen.blit(text_pregunta, (560, 70))
        screen.blit(text_reiniciar, (560, 620))
        screen.blit(imagen_preguntados, (0, 0))
        screen.blit(text_score_txt, (1050, 15))
        screen.blit(text_score_num, (1200, 15))

        if ver_preguntas == True:
            text_preguntas = font.render(lista_pregunta[lista_indices[0]['pregunta']], True, color_blanco) 
            text_opcion_a = font.render(lista_opcion[lista_indices[1]['opcion']], True, color_blanco)
            text_opcion_b = font.render(lista_opcion[lista_indices[1]['opcion'] + 1], True, color_blanco)
            text_opcion_c = font.render(lista_opcion[lista_indices[1]['opcion'] + 2], True, color_blanco)

            screen.blit(text_preguntas, (100, 330))

            if ocultar_a == False:
                pygame.draw.rect(screen, color_gris, rect_boton_opcion_a, border_radius=15)
                screen.blit(text_opcion_a, (110, 405))
                if correcta_a == True:
                    contador_tiempo += 1
                    pygame.draw.rect(screen, color_verde, rect_boton_opcion_a, border_radius=15, width=10)
                    if contador_tiempo > 30:
                        contador_tiempo = 0
                        correcta_a = False

            if ocultar_b == False:
                pygame.draw.rect(screen, color_gris, rect_boton_opcion_b, border_radius=15)
                screen.blit(text_opcion_b, (400, 405))
                if correcta_b == True:
                    contador_tiempo += 1
                    pygame.draw.rect(screen, color_verde, rect_boton_opcion_b, border_radius=15, width=10)
                    if contador_tiempo > 30:
                        contador_tiempo = 0
                        correcta_b = False

            if ocultar_c == False:
                pygame.draw.rect(screen, color_gris, rect_boton_opcion_c, border_radius=15)
                screen.blit(text_opcion_c, (660, 405))
                if correcta_c == True:
                    contador_tiempo += 1
                    pygame.draw.rect(screen, color_verde, rect_boton_opcion_c, border_radius=15, width=10)
                    if contador_tiempo > 30:
                        contador_tiempo = 0
                        correcta_c = False
    
    elif lista_indices[0]['pregunta'] >= len(lista_pregunta):
        
        texto_nombre_jugador = font.render(nombre_jugador, True, color_blanco)
        
        screen.fill(color_negro)

        screen.blit(texto_preguntar_nombre, (200, 200))
        screen.blit(texto_nombre_jugador, (350, 300))

        if nombre_vacio == True:
            screen.blit(text_pedir_nombre_valido, (200, 500))
        
        if termino_texto_nombre == True:
            agregar_a_lista(lista_mejor_puntuacion, int(score), nombre_jugador)
            ordenar_lista_burbujeo(lista_mejor_puntuacion, 'DESC')
            guardar_json(lista_mejor_puntuacion)
            
            ventana_menu = True
            ventana_juego = False
            termino_texto_nombre = False
            ver_preguntas = False
            nombre_jugador = ""
            text_score_num, score = resetear_sumar_score(lista_indices, font, False)
            reiniciar_pasar_pregunta(lista_indices, True)
            
    pygame.display.flip()
pygame.quit