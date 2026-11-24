import streamlit as st
from PIL import Image
from streamlit_cropper import st_cropper

st.set_page_config(page_title="Corta Imagem", layout="wide")
st.title("Corta Imagem")

# ---- Controles na barra lateral ----
img_file = st.sidebar.file_uploader(label="Envie uma Imagem", type=["png", "jpg", "jpeg"])
realtime_update = st.sidebar.checkbox("Atualização em Tempo Real", value=True)
box_color = st.sidebar.color_picker(label="Cor da caixa", value="#0000FF")
aspect_choice = st.sidebar.radio(
    label="Proporção da Tela", options=["Livre", "1:1", "16:9", "4:3"]
)

aspect_dict = {
    "Livre": None,
    "1:1": (1, 1),
    "16:9": (16, 9),
    "4:3": (4, 3),
}
aspect_ratio = aspect_dict[aspect_choice]

# ---- Recorte ----
if not img_file:
    st.info("Envie uma imagem pela barra lateral para começar.")
else:
    img = Image.open(img_file)

    if not realtime_update:
        st.write("Dê um duplo clique para cortar a imagem")

    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.subheader("Selecione a área")
        imagem_cortada = st_cropper(
            img,
            realtime_update=realtime_update,
            box_color=box_color,
            aspect_ratio=aspect_ratio,
        )
    with coluna2:
        st.subheader("Prévia do recorte")
        st.image(imagem_cortada)
        st.caption(f"Tamanho: {imagem_cortada.width} × {imagem_cortada.height} px")