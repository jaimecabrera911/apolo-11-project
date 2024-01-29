from src.services.generate_report import GenerateReport

'''
Este módulo define la clase Menu, que representa un menú basado en texto para interactuar con la clase GenerateReport.

Clases:
    - Menu: Representa un menú con opciones para interactuar con la clase GenerateReport.

Métodos:
    - show_menu: Muestra las opciones disponibles del menú.
    - option_1: Ejecuta la opción 1 - Analizar Eventos.
    - option_2: Ejecuta la opción 2 - Gestión de desconexiones.
    - option_3: Ejecuta la opción 3 - Consolidación de misiones.
    - option_4: Ejecuta la opción 4 - Cálculo de porcentajes.
    - option_5: Ejecuta la opción 5 - Crear un backup.
    - execute_app: Ejecuta la aplicación del menú y maneja las entradas del usuario.

Uso:
    Para utilizar este módulo, importa la clase Menu y crea una instancia para ejecutar las opciones del menú.
'''


class Menu:
    generate_report = GenerateReport()

    @staticmethod
    def show_menu():
        print("\n======Menu======")
        print("1. Analizar Eventos")
        print("2. Gestión de desconexiones")
        print("3. Consolidación de misiones")
        print("4. Cálculo de porcentajes")
        print("5. Crear un backup")
        print("6. Salir")

    def option_1(self):
        self.generate_report.analyze_events()
        print("Reporte generado")

    def option_2(self):
        self.generate_report.manage_disconnections()
        print("Reporte generado")

    def option_3(self):
        self.generate_report.get_inoperable_devices()
        print("Reporte generado")

    def option_4(self):
        self.generate_report.calculate_data_percentages()
        print("Reporte generado")

    def option_5(self):
        self.generate_report.create_backup()
        print("Se han movido todos los archivos a la carpeta backup")

    def execute_app(self):
        while True:
            self.show_menu()
            option = input("Selecciona una opción: ")

            if option == "1":
                self.option_1()
            elif option == "2":
                self.option_2()
            elif option == "3":
                self.option_3()
            elif option == "4":
                self.option_4()
            elif option == "5":
                self.option_5()
            elif option == "6":
                print("Saliendo del programa. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, selecciona una opción del menú.")
