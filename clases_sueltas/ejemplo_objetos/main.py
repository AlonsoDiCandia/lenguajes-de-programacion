from Equipo import Equipo
from Grupo import Grupo

equipos = ['Ñublense', 'Coquimbo Unido', 'Unión Española', 'Colo-Colo', 'Deportes Copiapó', 'O´Higgins', 'Cobreloa', 'Huachipato', 'Audax Italiano', 'Deportes Iquique', 'Unión La Calera', 'Universidad Católica', 'Everton', 'Palestino', 'Universidad de Chile', 'Cobresal']
grupos = []

for index, equipo in enumerate(equipos):
    if index < 4:
        g = Grupo(f'Grupo {index + 1}')
        grupos.append(g)

    e = Equipo(equipo)
    pos = index % 4

    grupos[pos].agregar_equipo(e)

for grupo in grupos:
    print(f"{10*'#'} {grupo.nombre} {10*'#'}")
    grupo.generar_partidos()



















# for index, equipo in enumerate(equipos):
#     if index < 4:
#         g = Grupo(f'Grupo {index + 1}')
#         grupos.append(g)

#     e = Equipo(equipo)

#     pos = index % 4

#     grupos[pos].agregar_equipo(e)

    # if pos == 0:
    #     grupos[pos].agregar_equipo(e)
    # elif pos == 1:
    #     grupos[pos].agregar_equipo(e)
    # elif pos == 2:
    #     grupos[pos].agregar_equipo(e)
    # elif pos == 3:
    #     grupos[pos].agregar_equipo(e)

# for grupo in grupos:
#     print(f"{10*'#'} {grupo.nombre} {10*'#'}")
#     grupo.generar_partidos()
