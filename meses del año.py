meses_del_ano = [
    'Enero',
    'Febrero',
    'Marzo',
    'Abril',
    'Mayo',
    'Junio',
    'Julio',
    'Agosto',
    'Septiembre',
    'Octubre',
    'Noviembre',
    'Diciembre'
]

# for mes in meses_del_ano:
#     print(mes)

mes_del_usuario = int(input('Digite número del mes, por favor: '))

if mes_del_usuario >= 1 and mes_del_usuario <= 12:
    print(f'El mes {mes_del_usuario} es {meses_del_ano[mes_del_usuario-1]}')
else:
    print('ERROR')
