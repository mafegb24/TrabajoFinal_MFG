# -*- coding: utf-8 -*-
"""
Created on Fri May 10 17:36:41 2024

@author: mafer
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 08:18:37 2024
For: Algoritmos Pregrado Ingenieria Industrial
@author: 21-407-JAC
"""
# region Importaciones
import os
import random as rnd
import pandas as pd
import time
import datetime
import logging
import tqdm
import warnings
warnings.filterwarnings('ignore')
# endregion Importaciones

# region funciones
def GenerarNombre(Nombres: list, Apellidos: list) -> str:
    Nombre = rnd.choice(Nombres)
    Apellido = rnd.choice(Apellidos)
    return f'{Nombre} {Apellido}'
def GenerarEdad() -> int:
    r = rnd.random()
    if r < 0.5:
        return rnd.randint(16, 25)
    elif r < 0.75:
        return rnd.randint(26, 33)
    elif r < 0.9:
        return rnd.randint(34, 40)
    else:
        return rnd.randint(41, 85)
def GenerearSemestre() -> int:
    r = rnd.random()
    if r < 0.14:
        return 1
    elif r < 0.27:
        return 2
    elif r < 0.39:
        return 3
    elif r < 0.5:
        return 4
    elif r < 0.6:
        return 5
    elif r < 0.7:
        return 6
    elif r < 0.79:
        return 7
    elif r < 0.87:
        return 8
    elif r < 0.94:
        return 9
    else:
        return 10
# endregion funciones
# region Inicializacion de fechas y log
print('*'*100)
print(f'{"Inicio del proceso":>15}')
inicio = time.time() #Inicio contador de ejecucion
hoy = datetime.date.today().strftime('%Y%m%d') #Captura de fecha de ejecucion
nombre_archivo_log = f"log_{hoy}.log" # Inicializacion del log
#Configuracion de almacenamiento y niveles del log
logging.basicConfig(filename=nombre_archivo_log, level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#Primer registro del log
logging.info("Iniciando el proceso, por MFG SOLUTIONS✔✔✔")
# endregion Inicializacion de fechas y log

# region Gestion de archivos y ubicaciones
#Creamos el directorio (carpeta) en donde se crearan los archivos
DirectorioActual = os.getcwd()
textemp = f'El directorio actual de trabajo es: \n\t--> {DirectorioActual}, \nEsta carpeta contendrá los archivos del trabajo final'
print(textemp)
logging.info(textemp)
#Creamos una carpeta donde almacenamos los resultados
CarpetaNueva = "CarpetaArchivosTrabajoFinal"
os.makedirs(CarpetaNueva, exist_ok=True)
logging.info("Se crea el directorio {}".format(CarpetaNueva))
print(f"'{CarpetaNueva}' La carpeeta ha sido creada.")
# Nombre de la carpeta donde se crearán los archivos
carpeta = os.path.join(DirectorioActual, "CarpetaArchivosTrabajoFinal")
logging.info("La ruta de trabajo será {}".format(carpeta))
RutaNombres = r'NombresArgentina.csv'
RutaApellidos = r'ApellidosArgentina.csv'
RutaNombres = os.path.join(DirectorioActual, RutaNombres)
RutaApellidos = os.path.join(DirectorioActual, RutaApellidos)
logging.info("Cargando CSV con nombres")
dfNombres = pd.read_csv(RutaNombres, encoding='ISO-8859-1')
Nombres = dfNombres['name'].tolist()
logging.info("Reemplazando nombres y detalles del documento")
for i in tqdm.trange(len(Nombres)):
    if ' ' in Nombres[i]:
        Nombres[i]=Nombres[i].replace(' ', '_')
logging.info("Cargando CSV con apellidos")
dfApellidos = pd.read_csv(RutaApellidos, encoding='ISO-8859-1')
Apellidos = dfApellidos['lastname'].tolist()
logging.info("Reemplazando apellidos y detalles del documento")
for i in tqdm.trange(len(Apellidos)):
    if ' ' in Apellidos[i]:
        Apellidos[i]=Apellidos[i].replace(' ', '_')
logging.info("Finalizado proceso de gestion de nombres y apellidos")
# endregion Gestion de archivos y ubicaciones
logging.info("Creando DataFrame con datos de estudiantes")
#region Generar datos filas.
df = pd.DataFrame(columns=['Nombre', 'Semestre', 'Edad', 'Fecha'])
for i in tqdm.trange(1000):
    vector = []
    nombre = GenerarNombre(Nombres, Apellidos).upper()
    semestre = GenerearSemestre()
    edad = GenerarEdad()
    fecha = datetime.date.today().strftime('%Y-%m-%d')
    vector = [nombre, semestre, edad, fecha]
    df.loc[len(df)] = vector
#endregion Generar datos filas.
logging.info("Exportando a Excel")
excel = 'Estudiantes.xlsx'
RutaExcel = os.path.join(DirectorioActual, excel)
df.to_excel(RutaExcel, index=False)
logging.info("Finalizado el proceso")
print(f"El archivo {excel} ha sido creado en la carpeta {DirectorioActual}")
print('FIN DEL PROCESO')
print('*'*100)


## COMIENZO CODIGO MAFE##

logging.info("Se hace funcion para definir las HTD y HTI  segun los creditos")
def creditaje(creditos):
    if creditos == 1:
        return 16, 32
    elif creditos == 2:
        return 32, 64
    elif creditos == 3:
        return 64, 80
    else:
        return 96, 120

logging.info("Se hace la clasificacion por semestre")
Cps = []

for i in range(1, 9):  
    Cps.append(df[df['Semestre']==i])
    
logging.info("Se almacena toda la informacion de las asignaturas y sus respectivos creditos en un diccionario")
asignaturas_por_semestre = {
    1: [
        {'nombre': 'Algebra y Trigonometria', 'creditos': 3},
        {'nombre': 'Calculo Diferencial', 'creditos': 3},
        {'nombre': 'Geometria Vectorial y Analitica', 'creditos': 3},
        {'nombre': 'Vivamos la Universidad', 'creditos': 1},
        {'nombre': 'Ingles 1', 'creditos': 1},
        {'nombre': 'Lectoescritura', 'creditos': 3},
        {'nombre': 'Introduccion a la Ingenieria Industrial', 'creditos': 1}
    ],
    2: [
        {'nombre': 'Gestion de las Organizaciones', 'creditos': 3},
        {'nombre': 'Habilidades Gerenciales', 'creditos': 3},
        {'nombre': 'Algebra Lineal', 'creditos': 3},
        {'nombre': 'Calculo Integral', 'creditos': 3},
        {'nombre': 'Descubriendo la fisica', 'creditos': 3},
        {'nombre': 'Ingles 2', 'creditos': 1}
    ],   
    3: [
        {'nombre': 'Gestion Contable', 'creditos': 3},
        {'nombre': 'Fisica Mecanica', 'creditos': 3},
        {'nombre': 'Ingles 3', 'creditos': 1},
        {'nombre': 'Algoritmia y Programacion', 'creditos': 3},
        {'nombre': 'Probabilidad e Inferencia Estadistica', 'creditos': 3},
        {'nombre': 'Teoria General de Sistemass', 'creditos': 3}
    ],
    4: [
        {'nombre': 'Ingenieria Economica', 'creditos': 3},
        {'nombre': 'Electiva en Fisica', 'creditos': 3},
        {'nombre': 'Ingles 4', 'creditos': 1},
        {'nombre': 'Diseño de experimentos y Analisis de Regresion', 'creditos': 3},
        {'nombre': 'Optimizacion', 'creditos': 3},
        {'nombre': 'Gestion de metodos y tiempos', 'creditos': 4}
    ],
    5: [
        {'nombre': 'Gestion Financiera', 'creditos': 3},
        {'nombre': 'Laboratorio Integrado de fisica', 'creditos': 1},
        {'nombre': 'Ingles 5', 'creditos': 1},
        {'nombre': 'Formacion ciudadana y constitucional', 'creditos': 1},
        {'nombre': 'Dinamica de Sistemas', 'creditos': 3},
        {'nombre': 'Muestreo y Series de Tiempo', 'creditos': 3},
        {'nombre': 'Procesos Estocasticos y Analisis de Decision', 'creditos': 3},
        {'nombre': 'Gestion por procesos', 'creditos': 3}
    ],
    6: [{'nombre': 'Gestion Tecnologica', 'creditos': 3},
        {'nombre': 'Legislacion', 'creditos': 3},
        {'nombre': 'Electiva en Humanidades 1', 'creditos': 3},
        {'nombre': 'Ingles 6', 'creditos': 1},
        {'nombre': 'Simulacion Discreta', 'creditos': 3},
        {'nombre': 'Formulacion de proyectos de Investigacion', 'creditos': 3},
        {'nombre': 'Normalizacion y control de la calidad', 'creditos': 3}
    ],
    7: [
        {'nombre': 'Formulacion y evaluacion de Proyectos de Inversion', 'creditos': 3},
        {'nombre': 'Emprendimiento', 'creditos': 2},
        {'nombre': 'Electiva en humanidades 2', 'creditos': 3},
        {'nombre': 'Enfasis Profesional 1', 'creditos': 3},
        {'nombre': 'Electiva Complementaria 1', 'creditos': 3},
        {'nombre': 'Diseños de sistemas productivos', 'creditos': 3}
    ],
    8: [
        {'nombre': 'Gestion de Proyectos', 'creditos': 3},
        {'nombre': 'Elecitiva en humanidades 3', 'creditos': 3},
        {'nombre': 'Enfasis profesional 1', 'creditos': 3},
        {'nombre': 'Electiva Complementaria 1', 'creditos': 3},
        {'nombre': 'Administracion de la Produccion y del Servicio', 'creditos': 3}
        ],
    9: [
        {'nombre': 'Electiva en Humanidades 4', 'creditos': 3},
        {'nombre': 'Enfasis Profesional 1', 'creditos': 3},
        {'nombre': 'Electiva Complementaria 1', 'creditos': 3},
        {'nombre': 'Gestion de la cadena de abastecimiento', 'creditos': 3},
        {'nombre': 'Ingenieria del mejoramiento continuo', 'creditos': 3}]

}

logging.info("Se crea lista vacia data, para almacenar la informacion")
data = []
logging.info("Se obtienen los estudiantes correspondientes al semestre actual")
for semestre in range(1, 9):

    estudiantes_semestre = Cps[semestre - 1]
    
    for index, estudiante in estudiantes_semestre.iterrows():
        nombre_estudiante = estudiante['Nombre']
        logging.info("Se hace la clasificacion de las asignaturas y credito por semestre")        
        for asignatura in asignaturas_por_semestre[semestre]:
            nombre_asignatura = asignatura['nombre']
            creditos = asignatura['creditos']
            HTD, HTI = creditaje(creditos)
            
            logging.info("Se crea un diccionario para designar las columnas en el dataframe")
            row = {
                'Nombre': nombre_estudiante,
                'Semestre': semestre,
                'Asignatura': nombre_asignatura,
                'CodigoAsignatura': f"{nombre_asignatura[:3].upper()}{semestre}{creditos}{1}",
                'Creditos': creditos,
                'HTD': HTD,
                'HTI': HTI
            }
            
            logging.info("Se agrega el diccionario a la lista")
            data.append(row)

logging.info("Se crea el dataframe a partir de la lista de diccionarios y se nombra df_completo")
df_completo = pd.DataFrame(data)

logging.info("Se muestra el dataframe final")
print(df_completo)
df_completo.head()
logging.info("Exportando a Excel y CSV")
df_completo.to_excel('06062024-LISTADO COMPLETO-5585.xlsx')
df_completo.to_csv('06062024-LISTADO COMPLETO-5585.csv')

logging.info("Se finaliza el proceso")
print('FIN DEL PROCESO')
print('*'*100)
