cidade = input('Digite o nome da sua cidade: ').strip()
cincoLetras = cidade[:5]
cincoLetrasM = cincoLetras.upper()
print('Acidade começa com a palavra SANTO?: ')
print('SANTO' in cincoLetrasM)