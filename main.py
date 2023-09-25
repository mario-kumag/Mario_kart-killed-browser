# %%
from rpg import *

personaje_1 = Personaje("Mario.kart", salud=100, energia=50, ataque_basico=10, probabilidad_critico=10)

enemigo = Enemigo("Browser", salud=50, energia=30, ataque_basico=8, probabilidad_critico=5, experiencia_otorgada=20, dinero_otorgado=10, objeto_otorgado=None)

habilidad_1 = Habilidad("Golpe destroza caparazon", ataque=20, energia_requerida=15)
personaje_1.aprender_habilidad(habilidad_1)

personaje_1.atacar(enemigo)

personaje_1.usar_habilidad(habilidad_1, enemigo)

personaje_1.descansar()

espada = Objeto("Espada afilada", "Una espada afilada para cortar Tortugas", precio=15)
personaje_1.obtener_objeto(espada)

tienda = Tienda()
tienda.vender_objeto(personaje_1, espada)

personaje_1.derrotar_enemigo(enemigo)

pocion_salud = Pocion("Poción de salud", "Restaura 30 puntos de salud", tipo="salud", nivel=3, precio=10)
personaje_1.obtener_objeto(pocion_salud)
personaje_1.usar_pocion(pocion_salud)

personaje_1.recibir_experiencia(300)

personaje_1.olvidar_habilidad(habilidad_1)

# %%
