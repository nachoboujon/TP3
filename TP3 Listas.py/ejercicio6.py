superHeroes = [
    {"nombre": 'Linterna Verde', "aparicion": 1940, "casa": 'DC', "biografia": 'Superhéroe con un anillo de poder.'},
    {"nombre": 'Wolverine', "aparicion": 1974, "casa": 'Marvel', "biografia": 'Mutante con garras retráctiles y factor de curación.'},
    {"nombre": 'Dr. Strange', "aparicion": 1963, "casa": 'DC', "biografia": 'Hechicero Supremo del Universo Marvel.'},
    {"nombre": 'Mujer Maravilla', "aparicion": 1941, "casa": 'DC', "biografia": 'Princesa amazona con habilidades de combate.'},
    {"nombre": 'Flaheroe', "aparicion": 1940, "casa": 'DC', "biografia": 'El hombre más rápido del mundo.'},
    {"nombre": 'Star lord', "aparicion": 1976, "casa": 'Marvel', "biografia": 'Aventurero espacial y líder de los Guardianes de la Galaxia.'}
]


def eliminarLV (superHeroes, nombre):
    return [heroe for heroe in superHeroes if heroe["nombre"] != nombre]
        

def año(superHeroes, nombre):
    for heroe in superHeroes:
        if heroe["nombre"] == nombre:
            return heroe["aparicion"]
    return None


def cambiar (superHeroes, nombre, nuevaCasa):
    for heroe in superHeroes:
        if heroe["nombre"] == nombre:
            heroe["casa"] = nuevaCasa

def buscarbiografia(superHeroes, palabras):
    resultado = []
    for heroe in superHeroes:
        if any(palabra in heroe["biografia"] for palabra in palabras):
            resultado.append(heroe["nombre"])
    return resultado

def aparicion(superheroes, año):
    resultado = []
    for heroe in superheroes:
        if heroe["aparicion"] < año:
            resultado.append((heroe["nombre"], heroe["casa"]))
    return resultado

def casaSuperHeroes(superheroes, nombres):
    resultado = {}
    for heroe in superheroes:
        if heroe["nombre"] in nombres:
            resultado[heroe["nombre"]] = heroe["casa"]
    return resultado

def infoSuperHeroes(superheroes, nombres):
    resultado = []
    for heroes in superheroes:
        if heroes["nombre"] in nombres:
            resultado.append(heroes)
    return resultado

def listar(superheroes, letras):
    resultado = []
    for heroes in superheroes:
        if heroes["nombre"][0] in letras:
            resultado.append(heroes["nombre"])
    return resultado


def contarCasas(superheroes):
    conteo = {"Marvel": 0, "DC": 0}
    for heroes in superheroes:
        if heroes["casa"] in conteo:
            conteo[heroes["casa"]] += 1
    return conteo


superHeroes = eliminarLV(superHeroes, "Linterna Verde")
for lista in superHeroes:
    print (lista)


print(año (superHeroes, "Wolverine"))


cambiar(superHeroes, "Dr. Strange", "Marvel")


for lista in superHeroes:
    print (lista)
    


print(buscarbiografia(superHeroes, ["traje", "armadura"]))


print(aparicion (superHeroes, 1963))


print(casaSuperHeroes(superHeroes, ["Capitana Marvel", "Mujer Maravilla"]))


print(infoSuperHeroes(superHeroes, ["Flaheroes", "Star-Lord"]))


print(listar(superHeroes, ["B", "M", "S"]))


print(contarCasas(superHeroes))