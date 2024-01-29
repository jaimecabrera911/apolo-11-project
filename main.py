from src.services.generate_data import GenerateData

'''
Este script principal tiene la función de generar datos esenciales para el proyecto. Utiliza la clase 'GenerateData'
para crear información relevante sobre misiones y dispositivos. Estos datos son fundamentales para el funcionamiento
completo de la interfaz, ya que permiten la generación de informes y estadísticas de manera precisa.

Al ejecutar el método 'execute()' de 'GenerateData', se inicia el proceso de generación de datos, asegurando que
la interfaz tenga acceso a la información necesaria para proporcionar funcionalidades de reportes y estadísticas.

Este script sirve como punto de partida crucial para preparar los datos y garantizar que la interfaz pueda desempeñar
su papel de manera efectiva al facilitar la creación de informes y estadísticas en el proyecto.
'''


def main():
    GenerateData.execute()


if __name__ == '__main__':
    main()
