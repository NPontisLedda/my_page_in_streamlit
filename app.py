# En caso de que no tengamos streamlit instalado, estos son los pasos para tener el combo completo.

# 1° pip install streamlit
# 2° pip install pillow -> para trabajar con imágenes
# 3° pip install streamlit-lottie -> para trabajar con animaciones 

# Una vez que tengamos armado un poco el formato, si queremos ver cómo va quedando la página, ponemos en la terminal
# streamlit run (nombre del archivo .py donde tengamos el proyecto)
# y para pararlo, usamos Ctrl + c


import streamlit as st
from PIL import Image # ->esto es pillow

st.set_page_config(page_title= "Nicoapp", page_icon= "🐺", layout= "wide")
email_contact = "emaildecontacto@gmail.com"

def css_load(css_file):
    with open(css_file) as file:
        st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)
css_load("style/main.css")

#intro 
with st.container():
    st.header("Hola! Somos Nicoapp 👋")
    st.title("Soy un analista de datos, que está incursionando en el mundo del desarrollo con Python.🐍")
    st.write("Hola")
    st.write("[Saber más >](https://nicoapp.com/)")


#sobre nosotros
with st.container():
    st.write("---") #-> con esto colocamos la línea que aparece para dividir sectores
    text_column, animation_column = st.columns(2) #-> acá definimos que vamos a tener la pantalla divida en dos, una parte de solo texto, y otra parte con animaciones.
    with text_column: #-> parte de texto
        st.header("Sobre mí 🔍")
        st.write(
            """
        ***Mi objetivo es aprender a utilizar Streamlit.***
            """
        )
        st.write("[Más sobre mí >](https://nicoapp.com/about/)")
    with animation_column: #-> parte de animación
        st.empty()


#servicios
with st.container():
    st.write("---")
    st.header("Servicios 🛠")
    st.write("##") #-> esto indica que queremos dejar un espacio entre el titulo y el resto del contenido
    image_column, text_column = st.columns((1,2))
    with image_column:
        image = Image.open("imagenes/python.png")
        st.image(image, use_column_width= True)
    with text_column:
        st.subheader("Esto vendría siendo el Subtitulo del apartado Servicios")
        st.write(
            """
            Esto es texto que va a aparecer debajo del subtitulo que colocamos antes
            """
        )
        st.write("[Más Servicios >](https://nicoapp.com/services/)")

with st.container():
    st.write("---")
    st.write("##") #-> esto indica que queremos dejar un espacio entre el titulo y el resto del contenido
    image_column, text_column = st.columns((1,2))
    with image_column:
        image = Image.open("imagenes/mendoza.jpg")
        st.image(image, use_column_width= True)
    with text_column:
        st.subheader("Esta es una imágen muy representativa de Mendoza, provincia donde nací.")
        st.write(
            """
            Esta imágen en particular, representa una de las mejores vistas de la provincia.
            La coordillera de los Andes.
            """
        )
        st.write("[Más sobre Mendoza >](https://mendoza.tur.ar/)")


# contacto con la empresa

with st.container():
    st.write("---")
    st.header("Contacta con la empresa 📧")
    st.write("##")
    contact_form = """
    <form action="https://formsubmit.co/{email_contact}" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder = "Nombre completo" required>
     <input type="email" name="email" placeholder= "e-mail de contacto" required>
     <textarea type="message" name="message" placeholder= "Coloca aquí tu consulta" required></textarea>
     <button type="submit">Enviar</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty








#----------------------------------------------------------------------------------------------
#from fastapi import FastAPI, Depends, Query
#from sqlalchemy.orm import Session
#from typing import List, Optional

#app = FastAPI()

#def get_db():
#    db = SessionLocal()
#    try:
#        yield db
#    finally:
#        db.close()

#@app.get("/candidates", response_model=List[dict])
#def get_candidates(
#    recruiter: Optional[str] = Query(None),
#    stage: Optional[str] = Query(None),
#    db: Session = Depends(get_db)
#):
#    base_query = """
#    SELECT u.name AS recruiter, st.name AS etapa, COUNT(e.person_id) AS cantidad_de_candidatos
#    FROM event AS e
#    INNER JOIN stage AS s ON e.stage_id = s.id
#    INNER JOIN stage_type AS st ON s.stage_type_id = st.id
#    LEFT JOIN user AS u ON e.user_id = u.id
#    WHERE YEAR(e.event_date) = YEAR(CURDATE()) AND e.answer_id IN (1,2,3,4,5,6,22) AND e.event_type_id NOT IN (15,16)
#    """
#    filters = []
#    params = {}

#    if recruiter:
#        filters.append("u.name = :recruiter")
#        params["recruiter"] = recruiter
#    if stage:
#        filters.append("st.name = :stage")
#        params["stage"] = stage

#    if filters:
#        base_query += " AND " + " AND ".join(filters)

#    base_query += " GROUP BY recruiter, etapa ORDER BY etapa;"

#    result = db.execute(text(base_query), params).fetchall()
#    return [dict(row) for row in result]
#-----------------------------------------------------------------------------------------------












