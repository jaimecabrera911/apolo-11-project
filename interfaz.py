from src.services.menu import Menu

'''
Este archivo es responsable de ejecutar la interfaz de usuario. Aquí, el menú presenta diversas opciones que permiten
al usuario generar informes de manera sencilla.

El objeto 'Menu' se instancia como 'app', y luego se ejecuta la aplicación utilizando el método 'execute_app()' para
iniciar la interacción con el usuario y procesar sus elecciones.

Este script actúa como el punto de entrada secundaria para la aplicación, permitiendo a los usuarios navegar y utilizar
las funciones de generación de informes de manera eficiente.
'''


def main():
    app = Menu()
    app.execute_app()


if __name__ == '__main__':
    main()
