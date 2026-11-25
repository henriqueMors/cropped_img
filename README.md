# Corta Imagem: Recorte de Imagens com Streamlit

Aplicação web feita em **Python** com **Streamlit** e o componente **streamlit-cropper** para **recortar imagens com o mouse**: você arrasta uma caixa sobre a imagem e vê, ao lado, a prévia do recorte.

## Funcionalidades

- **Upload de imagem** nos formatos PNG, JPG e JPEG
- **Caixa de recorte** que pode ser arrastada e redimensionada sobre a imagem
- **Prévia do recorte** ao lado da imagem original, com o tamanho em pixels
- **Proporção da caixa**: livre, 1:1 (quadrado), 16:9 (widescreen) ou 4:3
- **Cor da caixa** escolhida pelo usuário (seletor de cores)
- **Atualização em tempo real** (liga/desliga):
  - **ligada**: o recorte atualiza enquanto você arrasta a caixa
  - **desligada**: você posiciona a caixa e confirma com **duplo clique**, o que é mais leve para imagens grandes

## Código

```python
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
```

## Como executar

```bash
# criar e ativar o ambiente virtual
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Linux/macOS

# instalar as dependências
pip install streamlit streamlit-cropper pillow

# rodar o app
streamlit run app.py
```

O app abre no navegador em `http://localhost:8501`.

> O nome no `pip` usa **hífen** (`streamlit-cropper`), e no `import` usa **underline** (`from streamlit_cropper import st_cropper`).

## Parâmetros do `st_cropper`

| Parâmetro | O que faz |
|---|---|
| `realtime_update` | `True` atualiza enquanto arrasta; `False` só com duplo clique |
| `box_color` | cor da caixa de seleção (ex.: `"#0000FF"`) |
| `aspect_ratio` | trava a proporção: `(1, 1)`, `(16, 9)`, `(4, 3)`; `None` deixa livre |
| `return_type` | `"image"` (padrão) devolve a imagem recortada; `"box"` devolve só as coordenadas (esquerda, topo, largura, altura) |

## O que aprendi neste projeto

- **Componentes da comunidade**: o Streamlit pode ser ampliado com componentes feitos por outras pessoas, instalados via `pip`. É assim que ele ganha recursos como o recorte com o mouse.
- **Dicionário para traduzir escolhas**: o `aspect_dict` converte o texto escolhido no rádio (`"16:9"`) no valor que a função espera (`(16, 9)`).
- **Imagens com Pillow**: o recorte devolve uma imagem do Pillow (`PIL.Image`), com `.width` e `.height`, que pode ser salva, exibida ou convertida para NumPy (`np.array(imagem)`) para ser usada com o OpenCV.
- **Layout em colunas**: `st.columns(2)` coloca a seleção e a prévia lado a lado.
- **Ajustes em relação ao código da aula**: incluir a opção de proporção livre, passar o `aspect_ratio` para o `st_cropper` (calculado no código da aula, mas não usado), aceitar `.jpeg` e exibir a prévia do recorte.

## Ideias de evolução

- **Botão de download** do recorte (`st.download_button`)
- **Integração com o projeto de OpenCV**: recortar primeiro e aplicar filtros só na área escolhida
- **Proporções extras** (ex.: 9:16 para stories, 3:2 para fotos)

## Tecnologias

- Python 3
- Streamlit
- streamlit-cropper
- Pillow