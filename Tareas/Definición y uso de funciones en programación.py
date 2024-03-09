# Calcular la temperatura promedio usando declaración de funciones def
# Para lo cual se utilizara la misma matriz 3D que representa los datos e temperaturas
print('Hola bienvenidos')
print('¿Deseas conocer las temperaturas promedio de Quito, Guayaquil y Cuenca utilizando funciones de Python?')
nombre=input('Antes de iniciar ayudanos con tu nombre: ')
print(f"Un gusto conocerte {nombre}")
print("A continuación veamos las temperaturas promedios: ")
# Primero declararemos  la variable por medio de funciones def
def temperatura_promedio (cuidades_temperaturas):
    temperaturas_promedio = {}
    for ciudad, temperaturas in cuidades_temperaturas.items () :
        promedio = sum(temperaturas) / len(temperaturas)
        temperaturas_promedio [ciudad] = promedio
        return temperaturas_promedio
ciudades_temperaturas = {
    "Quito" :[ 14, 10, 11, 8, 12, 14, 15],
    "Guayaquil" :[ 25, 28, 31, 28, 25, 24, 55],
    "Cuenca" :[ 14, 10, 11, 8, 12, 14, 15],
    "Ambato" :[ 15, 11, 12, 9, 13, 15, 16],
}
#  Segundo realizamos las operaciones suma y promedio
temperaturas_promedio = temperatura_promedio (ciudades_temperaturas)
print("Temperaturas promedio por ciudad: ")
for ciudad, promedio in temperaturas_promedio.items():
    print(f"{ciudad}: {promedio: 2f} C")
print("Espero que te haya gustado, antes de terminar ¿Puedes decirnos qué tal te pareció?")
B=input('Puedes escibir si fue excelente, más o menos o pésimo: ')
print(f"Te parecio {B} gracias por tus comentarios")
