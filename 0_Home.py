import streamlit as st

st.set_page_config(
    page_title="Dashboard OpenFace",
    page_icon="🤖",
    layout="wide"
)

st.title("Bem-vindo ao Sistema de Análise de AUs")
st.write("Utilize o menu lateral esquerdo para navegar entre as diferentes análises do projeto.")
st.write("---")

st.markdown("""
###  Contexto da Pesquisa
A transferência de expressões faciais de humanos reais para humanos virtuais (Avatares/CG) frequentemente esbarra no chamado **Domain Gap** (Abismo de Domínio). Durante o processo de captura e *retargeting*, nuances cruciais das **micro e macroexpressões** tendem a perder intensidade e variância. Isso resulta em animações que sofrem um efeito de "suavização", tornando as reações virtuais mais engessadas, o que impacta diretamente a percepção emocional e pode agravar o efeito de *Uncanny Valley*.

Este sistema foi desenvolvido para **quantificar matematicamente essa perda**. Através da extração de dados faciais (Action Units) via OpenFace de vídeos de um dataset pré-selecionado, o painel compara frame a frame a dinâmica orgânica do ator original contra a resposta do motor gráfico.

###  Metodologia Analítica
O pipeline de engenharia de dados consolida as leituras de expressões reais e virtuais, aplicando rigor estatístico para avaliar a fidelidade da transferência:
* **Suavização Percentual:** Mede o achatamento direto da curva de força (Mediana) em músculos focais, evidenciando quais regiões do rosto (Upper vs. Lower Face) sofrem maior compressão de dados.
* **Dispersão e Variância:** Comprova visualmente e matematicamente a perda das micro-oscilações orgânicas — os pequenos tremores naturais da musculatura humana que o avatar não consegue reproduzir.
* **Correlação de Pearson:** Avalia a sincronia temporal, respondendo se o modelo virtual acompanha o ritmo da contraparte humana ou se apresenta atrasos (delay) no ápice da expressão.

###  Pipeline e Tecnologias
A arquitetura do estudo envolve ferramentas padrão da indústria para captura e animação, como **MediaPipe** e **LiveLink**, com renderização no ambiente da **Unreal Engine 4**. A camada de processamento de dados e visualização científica é construída inteiramente em Python (Pandas, SciPy, Seaborn e Streamlit).

---
**Equipe de Pesquisa e Desenvolvimento:**
* Francesco Pasa
* Gabriel Bremm
* Lucas Zwetsch
* Vinícius Ross
""")