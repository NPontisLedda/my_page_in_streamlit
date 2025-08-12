# En caso de que no tengamos streamlit instalado, estos son los pasos para tener el combo completo.

# 1° pip install streamlit
# 2° pip install pillow -> para trabajar con imágenes
# 3° pip install streamlit-lottie -> para trabajar con animaciones 

# Una vez que tengamos armado un poco el formato, si queremos ver cómo va quedando la página, ponemos en la terminal
# streamlit run (nombre del archivo .py donde tengamos el proyecto)
# y para pararlo, usamos Ctrl + c
# https://www.youtube.com/watch?v=mAhJ_mQEoO4 -> video explicativo
# https://lottiefiles.com/search?q=chef+&category=animations&page=3 -> pagina animaciones
# https://www.webfx.com/tools/emoji-cheat-sheet/ -> pagina emojis


import streamlit as st
from PIL import Image # ->esto es pillow
import requests
from streamlit_lottie import st_lottie
from io import BytesIO


st.set_page_config(page_title="ButterSweet", page_icon="🍪", layout="wide")
email_contact = "emaildecontacto@gmail.com"

def css_load(css_file):
    with open(css_file) as file:
        st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)
css_load("style/main.css")

# Función para cargar animaciones Lottie
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# URL de las animaciones Lottie
url_lottie1 = "https://lottie.host/19376a64-ea20-498b-a0b6-e15b750107a3/dCB2IRN4sX.json"
url_lottie2 = "https://lottie.host/28951b72-62b2-4132-a375-9a49a2b5426e/v4fStwpLnh.json"
url_lottie3 = "https://lottie.host/374bb9de-3f20-474b-9bef-0fb6d96f5694/ZMKpKLjTDk.json"
url_lottie4 = "https://lottie.host/51744992-b4e9-47b5-86eb-a996b50a04f4/xqnTmzqRp7.json"

lottie1 = load_lottie(url_lottie1)
lottie2 = load_lottie(url_lottie2)
lottie3 = load_lottie(url_lottie3)
lottie4 = load_lottie(url_lottie4)

# Intro
def pagina_bienvenida():
    st.title("🍪Hola! Somos ButterSweet 👋🍰")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with text_column:
        st.subheader("ButterSweet")
        st.write(
            """
            Nace de la idea de poder darle a la gente, 
            ese gustito de algo dulce después de comer y que no tengan que si o si comprar una torta gigante 
            para comer algo clásico y rico
            """
        )
        st.write("##")
        st.write("Te invitamos a seguirnos en instagram y que puedas ver nuestros productos!! Y ayudarnos a crecer 📲 ")
        st.write("[Instagram >](https://www.instagram.com/buttersweet.1?igsh=Ym5vOXQ5eHZpcHFv/)")
    with image_column:
        image_url = "https://raw.githubusercontent.com/NPontisLedda/my_page_in_streamlit/main/imagenes/image.png"
        image_response = requests.get(image_url)
        image = Image.open(BytesIO(image_response.content))
        st.image(image, use_column_width=True)

# Servicios
def servicios():
    st.write("---")
    st.header("Servicios 🛠")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        image_url = "https://raw.githubusercontent.com/NPontisLedda/my_page_in_streamlit/main/imagenes/Collage%20de%20fotos%20neutro%20minimalista%20aesthetic.png"
        image_response = requests.get(image_url)
        image = Image.open(BytesIO(image_response.content))
        st.image(image, use_column_width=True)
    with text_column:
        st.subheader("Estos son algunos de nuestros productos que tendrás a tu disposición para pedir")
        st.write(
            """
            Contamos con:
            - Cheesecake
            - Lemon pie
            - Tiramisú
            - Alfajores de chocolate y dulce de leche
            - Conos de dulce de leche
            - E INCLUSIVE ARMAMOS DESAYUNOS!!🎉🎈 
            """
        )
        st.write("[Más Servicios >]()")

# Sobre mí
def sobre_mi():
    st.write("---")
    text_column, animation_column = st.columns(2)
    with text_column:
        st.header("Sobre mí 🔍")
        st.write(
            """
            Hola, soy Nico y nací el 2 de abril de 1998 en Mendoza, Argentina. Desde una edad temprana, sentí una profunda pasión por la gastronomía, lo que me llevó a iniciar mis estudios en el Instituto Gastronómico de las Américas en 2019. Esta decisión marcó el comienzo de un emocionante viaje profesional en el mundo de la cocina.

            A los pocos meses de comenzar mis estudios, tuve la suerte de encontrar mi primer trabajo en la bodega Clos de Chacras. Pasé un año en esta prestigiosa bodega, donde adquirí valiosa experiencia y habilidades en el sector. Sin embargo, debido a la pandemia, me vi obligado a dejar mi puesto en Clos de Chacras. Durante ese tiempo, también trabajé como pasante en la bodega Norton, lo que me permitió explorar aún más el fascinante mundo de la gastronomía.

            En junio de 2021, decidí ampliar mis horizontes y viajé a España para realizar la temporada de verano en un hotel en Matalascañas. Esta experiencia internacional no solo enriqueció mi carrera profesional, sino que también me brindó una perspectiva global sobre la gastronomía.

            A mi regreso a Argentina, continué mi trayectoria en el campo culinario trabajando en la pastelería Alcayota. Mi carrera tomó un giro interesante cuando comencé a enseñar gastronomía y pastelería profesional en el mismo instituto donde había estudiado. Esta oportunidad me permitió compartir mi conocimiento y pasión por la cocina con futuros chefs y pasteleros.

            Tras cuatro años de intensa dedicación en el rubro gastronómico, decidí emprender un nuevo camino en el sector IT. Mi interés por los datos y la tecnología me llevó a estudiar Ciencia de Datos, y hoy en día me desempeño como analista de datos en mi primer empleo en el sector tecnológico. Este cambio de rumbo ha sido una aventura en sí misma, llena de nuevos desafíos y aprendizajes.

            En resumen, mi trayectoria profesional ha sido una combinación de experiencias enriquecedoras en la gastronomía y una emocionante transición al mundo de los datos y la tecnología. Cada etapa de mi carrera me ha brindado valiosas lecciones y ha contribuido a mi crecimiento personal y profesional. Estoy entusiasmado por el futuro y por las nuevas oportunidades que se presenten en mi camino.
            """
        )
        
    with animation_column:
        st_lottie(lottie1, height=300)
        st_lottie(lottie3, height=300)
        st_lottie(lottie4, height=300)

# contacto con la empresa

def contacto():
    st.write("---")
    st.header("Contacta con la empresa 📧")
    
    # URL del formulario de Google
    google_form_url = "https://docs.google.com/forms/d/e/1FAIpQLSdV5pG-VqvyrJnd2v26qyWngFNkZYBD5h4-DoPHWBlLJRf74Q/viewform?usp=sf_link"

    # Incrustar el formulario de Google usando un iframe
    google_form_iframe = f"""
    <iframe src="{google_form_url}" width="600" height="450" frameborder="0" marginheight="0" marginwidth="0">Cargando…</iframe>
    """

    left_column,center_column, right_column = st.columns(3)
    with left_column:
        st.markdown(google_form_iframe, unsafe_allow_html=True)
    with center_column:
        st.empty()
    with right_column: #-> parte de animación
        st_lottie(lottie2, height=600)






# Barra de navegación lateral

st.sidebar.title("Navegación") 
pagina = st.sidebar.selectbox("Selecciona una página", ["Página de bienvenida", "Servicios", "Sobre mí", "Contacto"])



if pagina == "Página de bienvenida":
    pagina_bienvenida()

if pagina == "Servicios":
    servicios()

if pagina == "Sobre mí":
    sobre_mi()


if pagina == "Contacto":
    contacto()