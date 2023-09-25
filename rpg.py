import random

 
class Entidad:
    def __init__(self, nombre, salud, energia, ataque_basico, probabilidad_critico):
        self.nombre = nombre
        self.salud = salud
        self.energia = energia
        self.salud_maxima = salud
        self.energia_maxima = energia
        self.ataque_basico = ataque_basico
        self.probabilidad_critico = probabilidad_critico

    def atacar(self, objetivo):
        if self.salud <= 0:
            print(f"{self.nombre} el personaje no puede atacar porque murio")
            return

        dano_critico = 2 if random.randint(1, 100) <= self.probabilidad_critico else 1

        dano = dano_critico * self.ataque_basico
        objetivo.recibir_dano(dano)

        print(f"{self.nombre} a atacado a {objetivo.nombre} y le infringio {dano} de dano")


    def recibir_dano(self, cantidad_dano):
        self.salud -= cantidad_dano
        if self.salud <= 0:
            print(f"{self.nombre} fue derrotado")
            self.salud = 0
        else:
            print(f"{self.nombre} fue atacado y recibio {cantidad_dano} de dano")


    def usar_habilidad(self, habilidad, objetivo):
        if self.salud <= 0:
            print(f"{self.nombre} no puede usar habilidades porque ha muerto")
            return

        if self.energia >= habilidad.energia_requerida:
            print(f"{self.nombre} uso habilidad {habilidad.nombre} contra {objetivo.nombre}")
            objetivo.recibir_dano(habilidad.ataque)
            self.energia -= habilidad.energia_requerida

        else:
            print(f"{self.nombre} no tiene energía necesaria para usar {habilidad.nombre}")


    def descansar(self):
        if self.salud <= 0:
            print(f"{self.nombre} no puede descansar cuando se muere")

        else:
            salud_recuperada = self.salud_maxima * 0.15
            energia_recuperada = self.energia_maxima * 0.15

            self.salud += salud_recuperada
            self.energia += energia_recuperada

            if self.salud > self.salud_maxima:
                self.salud = self.salud_maxima

            if self.energia > self.energia_maxima:
                self.energia = self.energia_maxima

            print(f"{self.nombre} ha descansado y se a recuperado un 15 % de su salud y tambien 15 % de energía")


class Personaje(Entidad):
    def __init__(self, nombre, salud, energia,ataque_basico,probabilidad_critico,habilidades=[],dinero=0,nivel=1,experiencia=0):
        super().__init__(nombre,salud,energia,ataque_basico,probabilidad_critico)
        self.habilidades = habilidades
        self.inventario = []
        self.dinero = dinero
        self.nivel = nivel
        self.experiencia = experiencia

    def aprender_habilidad(self, habilidad):
        if len(self.habilidades) < 3:
            self.habilidades.append(habilidad)
            print(f"{self.nombre} aprendio la habilidad {habilidad.nombre}")
        else:
            print(f"{self.nombre} ya tiene 3 habilidades, no puede aprender otra")

    def olvidar_habilidad(self, habilidad_a_olvidar):
        if habilidad_a_olvidar in self.habilidades:
            self.habilidades.remove(habilidad_a_olvidar)
            print(f"{self.nombre} olvido {habilidad_a_olvidar.nombre}")
        else:
            print(f"{self.nombre} no tiene la habilidad {habilidad_a_olvidar.nombre} para ser olvidada")

    def recibir_experiencia(self, cantidad):
        print(f"{self.nombre} ha obtenido un total de :{cantidad} puntos de experiencia")
        self.experiencia += cantidad

        if self.experiencia >= self.nivel*100:
            self.subir_nivel()
            self.aumentar_atributos()

    def subir_nivel(self):
        self.nivel += 1
        self.experiencia = 0
        print(f"{self.nombre} subio al nivel:{self.nivel}")

    def aumentar_atributos(self):
        self.salud_maxima += 10
        self.energia_maxima += 5
        self.ataque_basico += 2
        print(f"{self.nombre} sus atributos mejoraron con el aumento de nivel")

    def obtener_objeto(self, objeto):
        if len(self.inventario) < 10:
            self.inventario.append(objeto)
            print(f"{self.nombre} obtuvo el objeto:{objeto.nombre} del enemigo")
        else:
            print(f"{self.nombre} El inventario está lleno")

    def eliminar_objeto(self, objeto):
        if objeto in self.inventario:
            self.inventario.remove(objeto)
            print(f"{self.nombre} elimino {objeto.nombre} del inventario")
        else:
            print(f"{self.nombre} no posees {objeto.nombre} en el inventario")

    def usar_pocion(self, pocion):
        if isinstance(pocion, Pocion):
            if pocion in self.inventario:
                if pocion.tipo == "salud":
                    cantidad_curacion = pocion.nivel * 10
                    self.salud += cantidad_curacion
                    if self.salud > self.salud_maxima:
                        self.salud = self.salud_maxima
                    print(f"{self.nombre} ha usado una poción de salud y se recupero un total de:{cantidad_curacion} puntos de salud")
                elif pocion.tipo == "energia":
                    cantidad_curacion = pocion.nivel * 5
                    self.energia += cantidad_curacion
                    if self.energia > self.energia_maxima:
                        self.energia = self.energia_maxima
                    print(f"{self.nombre} ha usado una poción de energía y se recupero un total de:{cantidad_curacion} puntos de energía")
                else:
                    print(f"{self.nombre} no puede usar esa poción en este momento")
            else:
                print(f"{self.nombre} no posee la pocion:{pocion.nombre} en el inventario")
        else:
            print(f"{self.nombre} no se puede usar ese objeto")

    def derrotar_enemigo(self, enemigo):
        if len (self.inventario) < 10:
            self.inventario.append(enemigo.objeto_otorgado)
        self.experiencia += enemigo.experiencia_otorgada
        self.dinero += enemigo.dinero_otorgado
        print(f"{self.nombre} ha derrotado a {enemigo.nombre}, recibio {enemigo.dinero_otorgado} monedas y un total de:{enemigo.experiencia_otorgada} de experiencia")

class Enemigo(Entidad):
    def __init__(self, nombre, salud, energia, ataque_basico, probabilidad_critico, experiencia_otorgada, dinero_otorgado, objeto_otorgado):
        super().__init__(nombre, salud, energia, ataque_basico, probabilidad_critico)
        self.experiencia_otorgada = experiencia_otorgada
        self.dinero_otorgado = dinero_otorgado
        self.objeto_otorgado = objeto_otorgado

class Habilidad:
    def __init__(self, nombre, ataque, energia_requerida):
        self.nombre = nombre
        self.ataque = ataque
        self.energia_requerida = energia_requerida

class Objeto:
    def __init__(self, nombre, descripcion, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

class Pocion(Objeto):
    def __init__(self, nombre, descripcion, tipo, nivel, precio):
        super().__init__(nombre, descripcion, precio)
        self.tipo = tipo
        self.nivel = nivel

class Tienda:
    def __init__(self):
        self.inventario_objetos = []
        self.inventario_pociones = []

    def agregar_objeto(self, objeto):
        self.inventario_objetos.append(objeto)

    def agregar_pocion(self, pocion):
        self.inventario_pociones.append(pocion)

    def vender_objeto(self, personaje, objeto):
        if objeto in self.inventario_objetos and personaje.dinero >= objeto.precio:
            personaje.dinero -= objeto.precio
            personaje.obtener_objeto(objeto)
            self.inventario_objetos.remove(objeto)
            print(f"{personaje.nombre} compro {objeto.nombre} al precio de:{objeto.precio} monedas")
        else:
            print(f"No tienes las monedas necesarias para comprar {objeto.nombre}")

    def vender_pocion(self, personaje, pocion):
        if pocion in self.inventario_pociones and personaje.dinero >= pocion.precio:
            personaje.dinero -= pocion.precio
            personaje.obtener_objeto(pocion)
            self.inventario_pociones.remove(pocion)
            print(f"{personaje.nombre} compro {pocion.nombre} al precio de:{pocion.precio} monedas")
        else:
            print(f"No tienes las monedas necesarias para comprar {pocion.nombre}")