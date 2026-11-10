import mysql.connector 


import streamlit as st 

st.title("Conexión con base de datos MySQL") 

# Obtener las credenciales almacenadas en Streamlit Secrets 

host = st.secrets["mysql"]["host"] 

port = st.secrets["mysql"]["port"] 

user = st.secrets["mysql"]["user"] 

password = st.secrets["mysql"]["password"] 

database = st.secrets["mysql"]["database"] 

# Intentar establecer la conexión 

try: 

    conn = mysql.connector.connect( 

        host= bzu9t0krsi4i7ny79nb5-mysql.services.clever-cloud.com, 

        port="3306", 

        user="u2fzl9qh9s98elr8", 

        password="6DGwOB7FhWlIjx9IHDB7", 

        database="bzu9t0krsi4i7ny79nb5" 

    ) 

    # Verificar si la conexión fue exitosa 

    if conn.is_connected(): 

        st.success("Conexión exitosa a la base de datos MySQL.") 

    else: 

        st.error("No se pudo conectar a la base de datos.") 

except mysql.connector.Error as err: 

    # Mostrar el error si la conexión falla 

    st.error(f"Error al conectar con la base de datos: {err}") 

finally: 

    if "conn" in locals() and conn.is_connected(): 

        conn.close() 
