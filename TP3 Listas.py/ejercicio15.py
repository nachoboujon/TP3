entrenadores = [
    ["Ash", 5, 10, 50, [
        ["Pikachu", 35, "Eléctrico", None],
        ["Charizard", 40, "Fuego", "Volador"],
        ["Bulbasaur", 20, "Planta", "Veneno"]
    ]],
    ["Misty", 3, 5, 30, [
        ["Starmie", 25, "Agua", "Psíquico"],
        ["Psyduck", 15, "Agua", None]
    ]],
    ["Brock", 4, 3, 25, [
        ["Onix", 30, "Roca", "Tierra"],
        ["Geodude", 20, "Roca", "Tierra"]
    ]],
    ["Gary", 2, 2, 20, [
        ["Eevee", 22, "Normal", None],
        ["Blastoise", 36, "Agua", None]
    ]]
]


def cantidad(nombreEntrenador):
    for entrenador in entrenadores:
        if entrenador[0] == nombreEntrenador:
            return len(entrenador[4])
    return 0

def entrenadoresCon3():
    return [entrenador[0] for entrenador in entrenadores if entrenador[1] > 3]

def mayorNivelPokemon():
    torneosMax = -1
    entrenadorConMasTorneos = None
    for entrenador in entrenadores:
        if entrenador[1] > torneosMax:
            torneosMax = entrenador[1]
            entrenadorConMasTorneos = entrenador
    if entrenadorConMasTorneos:
        return max(entrenadorConMasTorneos[4], key=lambda p: p[1])
    return None

def datosEntrenador(nombreEntrenador):
    for entrenador in entrenadores:
        if entrenador[0] == nombreEntrenador:
            return entrenador
    return None

def mayorBatallasGanadas():
    resultado = []
    for entrenador in entrenadores:
        totalBatallas = entrenador[2] + entrenador[3]
        if totalBatallas > 0:
            porcentajeVictorias = (entrenador[3] / totalBatallas) * 100
            if porcentajeVictorias > 79:
                resultado.append(entrenador[0])
    return resultado

def pokemonesTipos():
    resultado = []
    for entrenador in entrenadores:
        for pokemon in entrenador[4]:
            if (pokemon[2] == "Fuego" and pokemon[3] == "Planta") or (pokemon[2] == "Agua" and pokemon[3] == "Volador"):
                resultado.append(entrenador[0])
                break
    return resultado

def promediosPokemons(nombreEntrenador):
    for entrenador in entrenadores:
        if entrenador[0] == nombreEntrenador:
            total_nivel = sum(pokemon[1] for pokemon in entrenador[4])
            return total_nivel / len(entrenador[4])
    return 0

def cantEntrenadoresPokemon(nombrePokemon):
    contador = 0
    for entrenador in entrenadores:
        if any(pokemon[0] == nombrePokemon for pokemon in entrenador[4]):
            contador += 1
    return contador

def pokemonRepetido():
    resultado = []
    for entrenador in entrenadores:
        nombrePokemon = [pokemon[0] for pokemon in entrenador[4]]
        if len(nombrePokemon) != len(set(nombrePokemon)):
            resultado.append(entrenador[0])
    return resultado

def pokemonEspecifico(pokemonEspecific):
    resultado = []
    for entrenador in entrenadores:
        if any(pokemon[0] in pokemonEspecific for pokemon in entrenador[4]):
            resultado.append(entrenador[0])
    return resultado

def entrenadorPokemon(nombreEntrenador, nombrePokemon):
    for entrenador in entrenadores:
        if entrenador[0] == nombreEntrenador:
            for pokemon in entrenador[4]:
                if pokemon[0] == nombrePokemon:
                    return entrenador, pokemon
    return None, None

# Pruebas de las funciones
print(cantidad("Ash"))
print(entrenadoresCon3())
print(mayorNivelPokemon())
print(datosEntrenador("Misty"))
print(mayorBatallasGanadas())
print(pokemonesTipos())
print(promediosPokemons("Brock"))
print(cantEntrenadoresPokemon("Pikachu"))
print(pokemonRepetido())
print(pokemonEspecifico(["Tyrantrum", "Terrakion", "Wingull"]))
print(entrenadorPokemon("Ash", "Pikachu"))
