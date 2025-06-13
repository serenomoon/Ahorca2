from datos import *
import random

def obtener_lista_palabras(datos,categoria) -> list:
    palabras = []
    for i in datos:
        if i["Tematica"] == categoria:
            palabras.append(i["Palabra a descubrir"])
    return palabras


def seleccionar_categoria(datos: list):
    lista_categoria = obtener_categorias(datos)
    categoria = lista_categoria[random.randint(0,len(lista_categoria) -1)]
    return categoria


def obtener_categorias(datos):
    tematicas = []
    for tematica in datos:
        tematicas.append(tematica["Tematica"])
    datos = set(tematicas)
    return list(datos)


def seleccionar_palabra(palabras):
    la_palabra = palabras[random.randint(0,len(palabras) -1)]
    return la_palabra


def mostrar_palabra_oculta(la_palabra):
    palabra_guiones = ""
    
    for i in range(len(la_palabra)):
            letra = la_palabra[i]
            if la_palabra >= 'a' and letra <= 'z':
                palabra_guiones += "_"
            else:
                palabra_guiones += letra
                
    return palabra_guiones 


def actualizar_palabra_oculta(la_palabra , letra):
    palabra_semi_oculta = ""
    
    for i in range(len(la_palabra)):
        if la_palabra[i] == letra:
            palabra_semi_oculta += la_palabra[i]   
        else:
            palabra_semi_oculta += "_"
            
    return palabra_semi_oculta        
            
                      
def obtener_elemento_aleatorio(lista_elementos:list)->any:
    pass

def guardar_puntuacion()->bool:
    pass

def ingresar_nombre_usuario(mensaje:str, mensaje_error:str, minimo_len:int, maximo_len:int)->str:
    pass

def verificar_estado_juego(diccionario_juego:dict)->bool:
    pass  

def calcular_puntuacion_final():
    
    pass

    
