# ----------------------------------------------------- Importación de librerías --------------------------------------------------------- 
import tkinter              # GUI
from tkinter import ttk     # GUI
import math                 # FUNCIONES MATEMATICAS
import numpy as np          # FUNCIONES MATEMATICAS

# ----------------------------------------------- Creación e implementación de Widgets ---------------------------------------------------
# VENTANA PRINCIPA;
main_Window = tkinter.Tk()
main_Window.geometry("600x500")
main_Window.resizable(False, False)

# TABLA DE DATOS
tabla = tkinter.Canvas(main_Window)
tabla.columnconfigure(0)

# SELECCION DE FUNCION
opcion = "                              Seleccione una opción                                 "
opcionGrosor = "         Cálculo de grosor final de óxido en oblea de silicio      "
opcionOxido = "Cálculo de tiempo de oxidación para una película de óxido"
lista = [opcion, opcionGrosor, opcionOxido]
entrada_var = tkinter.StringVar(tabla)
entrada_var.set(lista[0])
entrada = ttk.OptionMenu(tabla, entrada_var, *lista)
entrada.grid(row = 1, column = 1, columnspan = 2)

# GROSOR INICIAL
grosorInicial_label = ttk.Label(tabla, text = "Grosor Inicial     ")
grosorInicial_label.grid(row = 3, column = 0, sticky = 'e')
grosorInicial = ttk.Entry(tabla, justify = 'center')
grosorInicial.grid(row = 3, column = 1, sticky = 'w')

# GROSOR FINAL
grosorFinal_label = ttk.Label(tabla, text = "Grosor Final     ")
grosorFinal_label.grid(row = 4, column = 0, sticky = 'e')
grosorFinal = ttk.Entry(tabla, justify = 'center')
grosorFinal.grid(row = 4, column = 1, sticky = 'w')

# TIEMPO DE OXIDACION
tiempoOxidacion_label = ttk.Label(tabla, text = "Tiempo de oxidacion     ")
tiempoOxidacion_label.grid(row = 5, column = 0, sticky = 'e')
tiempoOxidacion = ttk.Entry(tabla, justify = 'center')
tiempoOxidacion.grid(row = 5, column = 1, sticky = 'w')

# TEMPERATURA DE OXIDACION
temperaturaOxidacion_label = ttk.Label(tabla, text = "Temperatura de oxidacion     ")
temperaturaOxidacion_label.grid(row = 6, column = 0, sticky = 'e')
temperaturaOxidacion = ttk.Entry(tabla, justify = 'center')
temperaturaOxidacion.grid(row = 6, column = 1, sticky = 'w')

# TIPO DE PROCESO
proceso_label = ttk.Label(tabla, text = "Tipo de proceso     ")
proceso_label.grid(row = 7, column = 0, sticky = 'e')
procesos = ["                               ", "        Húmedo        ","            Seco           "]
procesos_var = tkinter.StringVar(tabla)
procesos_var.set(procesos[0])
proceso = ttk.OptionMenu(tabla, procesos_var, *procesos)
proceso.grid(row = 7, column = 1, sticky = 'w')


proceso = ttk.Entry(tabla, justify = 'center')

# ORIENTACION DE LA OBLEA
orientacion_label = ttk.Label(tabla, text = "Orientación     ")
orientacion_label.grid(row = 8, column = 0, sticky = 'e')
orientacionOblea = ["                               ", "              100             ", "              111             "]
orientacion_var = tkinter.StringVar(tabla)
orientacion_var.set(orientacionOblea[0])
orientacion = ttk.OptionMenu(tabla, orientacion_var, *orientacionOblea)
orientacion.grid(row = 8, column = 1, sticky = 'w')


tabla.place(x = 45, y = 40)

resultadoFrame = tkinter.Frame(main_Window)
resultadoFrame.place(x = 45, y = 450)
conversion_text = ttk.Label(resultadoFrame, text = "Resultado → ")
conversion_text.grid(row = 0, column = 0)
resultado_final = ttk.Label(resultadoFrame, text = "")
resultado_final.grid(row = 0, column = 1)
resultadoLabel = ttk.Label(resultadoFrame, text = "")
resultadoLabel.grid(row = 0, column = 2)


start = ttk.Button(main_Window, text = "Convertir", command = lambda: startFunction())
start.place(x = 280, y = 200)

exit_Button = ttk.Button(main_Window, text = "Salir", command = main_Window.destroy)
exit_Button.place(x = 500, y = 450)


# ------------------------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------- Creación e implementación de funciones ---------------------------------------------

# Lectura de parámetros y número a convertir
def startFunction ():
    # Principales
    global entrada_var, opcion, opcionGrosor, opcionOxido
    k = 8.617*10**-5
    # Selectores
    global procesos_var, orientacion_var
    # Label de resultado
    global  resultado_final, resultadoLabel

    # Valores
    global temperaturaOxidacion, tiempoOxidacion, grosorInicial, grosorFinal
    temperatura = float(temperaturaOxidacion.get())
    grosor = float(grosorInicial.get())
    temperatura = temperatura + 273.15

  
    # Selección de tipo de oblea y tipo de proceso
    if(procesos_var.get() == "        Húmedo        "):
        if(orientacion_var.get() == "              100             "):
            BADo = 9.7*10**7
            BDo = 386
            BAEa = 2.05
            BEa = .78
        elif(orientacion_var.get() == "              111             "):
            BADo = 1.63*10**8
            BDo = 386
            BAEa = 2.05
            BEa = .78
    elif(procesos_var.get() == "            Seco           "):
        if(orientacion_var.get() == "              100             "):
            BADo = 3.71*10**6
            BDo = 772
            BAEa = 2
            BEa = 1.23
        elif(orientacion_var.get() == "              111             "):
            BADo = 6.23*10**6
            BDo = 772
            BAEa = 2
            BEa = 1.23

    # Selección e implementación de fórmulas
    seleccion = entrada_var.get()
    if(seleccion != opcion):
        a = 0
        BA = BADo * math.exp(-BAEa/(k*temperatura))
        B = BDo * math.exp(-BEa/(k*temperatura))
        tao = (grosor**2)/B + grosor/BA
        # Calcular grosor
        resultadoLabel.destroy()
        resultadoLabel = ttk.Label(resultadoFrame, text = "")
        resultadoLabel.grid(row = 0, column = 2)
        if(seleccion == opcionGrosor):
            tiempo = float(tiempoOxidacion.get())    
            coef = [1/B, 1/BA, (-tiempo-tao)]
            temp = np.roots(coef)
            resultado = np.amax(temp)            
            resultado_final.configure(text = resultado)
            resultadoLabel.configure(text = "uM")

        # Calcular tiempo
        if(seleccion == opcionOxido):
            grosorF = float(grosorFinal.get())

            resultado = (grosorF**2)/B + (grosorF/BA) -tao
            resultado_final.configure(text = resultado)
            resultadoLabel.configure(text = "Horas")


        print(resultado)

    else:
        print("Por favor seleccione una opción")

# ----------------------------------------------- Inicio de loop principal para GUI --------------------------------------------------

main_Window.mainloop()

# ------------------------------------------------------------------------------------------------------------------------------------