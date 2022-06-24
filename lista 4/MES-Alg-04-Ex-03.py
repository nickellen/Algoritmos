# Tabela de conversão de temperaturas
print('Celsius:\tFahrenheit:')

for celsius in range(0,101,10):
    faren= (celsius*1.8)+32
    print(f'{celsius}°C\t\t{faren}°F')