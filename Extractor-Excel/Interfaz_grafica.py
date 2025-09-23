import pandas as pd
import smtplib, ssl
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from email.message import EmailMessage

def abrir_excel():
    ruta = filedialog.askopenfilename(
        title="Elige el archivo Excel.",
        filetypes=[("Excel (.xlsx)", "*.xlsx"), ("Excel (.xls)", "*.xls")]
    )
    
    
    if ruta:
        entry_archivo.delete(0, tk.END)
        entry_archivo.insert(0, tk. ruta)
        
def procesar_y_enviar():
    
    ruta = entry_archivo.get()
    
    if not ruta:
        messagebox.showerror("Error", "No se ha seleccionado ningun archivo")
        return
    columnas = [col.strip() for col in entry_columnas.get().split(',') if col.strip()]
    
    try:
        df = pd.read_excel(ruta)    # Lee el Excel en un DataFrame:contentReference[oaicite:3]{index=3}
    except KeyError as e:
        messagebox.showerror("Error", f"No se pudo leer el archivo {e}")
        return
    
    try:
        df_filtrado = df[columnas]
    except KeyError as e:
        messagebox.showerror("Error", f"No se pudo encontrar columna {e}")
        return
    
    archivo_filtrado = "datos_filtrados.xlsx"
    df_filtrado.to_excel(archivo_filtrado, index=False)
    # Luego llamaríamos a la función de envío usando archivo_filtrado y entry_email.get()

def enviar_correo(archivo_adj, destinatario):
    remitente           =   os.getenv("SMTP_USER")           # eJ. "usuario@example.com"
    password            =   os.getenv("SMTP_PASS")
    servidor            =   os.getenv("SMTP_SERVER", "smtp.example.com")
    puerto              =   int(os.getenv("SMTP_PORT", 465))
    
    msg                 =   EmailMessage()
    msg['Subject']      =   "Datos Extraidos de Excel"
    msg['From']         =   remitente
    msg['To']           =   destinatario
    msg.set_content("Adjunto archivo con las columnas solicitadas")

    # Adjutanmos el archivo
    with open(archivo_adj, 'rb') as f:
        datos = f.read()
        msg.add_attachment(datos, maintype='application', subtype='octet-stream', filename=archivo_adj)
    
    # Enviamos el correo usando SMTP.
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(servidor, puerto, context=context) as server:
        server.login(remitente, password)
        server.send_message(msg)
    
        
root = tk.Tk() # Se inicializa la interfaz grafica
root.title("Extraccion y Filtrado Excel")

tk.Label(root, text="Archivo Excel:").grid(row=0, column=0)
entry_archivo = tk.Entry(root, width=40)
entry_archivo.grid(row=0, column=1)
tk.Button(root, text="Seleccionar", command=abrir_excel).grid(row=0, column=2)

tk.Label(root, text="Columnas (Separadas por comas:)").grid(row=1, column=0)
entry_columnas = tk.Entry(root, width=40)
entry_columnas.grid(row=1, column=1)

tk.Label(root, text="Email destinario: ").grid(row=2, column=0)
entry_email = tk.Entry(root, width=40)
entry_email.grid(row=2, column=1)

tk.Button(root, text="Procesar y enviar", command=procesar_y_enviar).grid(row=3, column=1)
root.mainloop()


    