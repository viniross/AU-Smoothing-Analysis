# Análise Quantitativa de Action Units em Expressões Faciais: Humanos Reais vs. Virtuais

Este projeto apresenta um sistema de análise e visualização de dados para quantificar a perda de intensidade e variância em expressões faciais transferidas de humanos reais para avatares virtuais. Utilizando dados de Action Units (AUs) extraídos com a ferramenta OpenFace, o sistema oferece uma análise estatística detalhada para investigar o "Domain Gap" (Abismo de Domínio) entre as expressões originais e as recriadas digitalmente.

## 📜 Contexto

A transferência de expressões faciais para avatares digitais frequentemente resulta em uma  "suavização". Isso pode levar a animações menos expressivas e impactar a percepção emocional, contribuindo para o efeito de *Uncanny Valley*. Este projeto foi desenvolvido para medir essa perda de forma objetiva, comparando a dinâmica das AUs de atores reais com as de seus avatares correspondentes.

## 🏗️ Estrutura do Projeto

O projeto está organizado da seguinte forma:

```
.
├── 0_Home.py                   # Página inicial da aplicação Streamlit
├── data
│   ├── processed
│   │   └── dataset_consolidado.csv # Dataset consolidado após o pré-processamento
│   └── raw
│       ├── real_human          # Dados brutos de expressões de humanos reais
│       └── virtual_human       # Dados brutos de expressões de humanos virtuais
├── pages
│   ├── 1_Estatisticas_Gerais.py # Análise de estatísticas descritivas
│   ├── 2_Analise_Temporal.py    # Análise da dinâmica temporal das AUs
│   ├── 3_Inspecao_Picos.py      # Inspeção dos picos de intensidade das AUs
│   ├── 4_Dispersao_e_Variancia.py # Análise da dispersão e variância
│   └── 5_Suavizacao_Severa.py   # Análise da suavização por AU
├── src
│   ├── analysis.py             # Funções para análise estatística
│   ├── data_loader.py          # Script para carregar e consolidar os dados
│   ├── plots.py                # Funções para a geração de gráficos
│   └── utils.py                # Funções utilitárias e constantes
├── requirements.txt            # Lista de dependências do projeto
└── README.md                   # Este arquivo
```

## 📚 Bibliotecas Utilizadas

O projeto utiliza as seguintes bibliotecas Python:

-   **pandas**: Para manipulação e análise de dados.
-   **numpy**: Para operações numéricas.
-   **scipy**: Para cálculos estatísticos, como a correlação de Pearson e o Teste-T.
-   **streamlit**: Para a criação do dashboard interativo.
-   **matplotlib** e **seaborn**: Para a visualização de dados e geração de gráficos.

Para instalar as dependências, execute o seguinte comando:

```bash
pip install -r requirements.txt
```

## 📊 Fórmulas e Análises

O sistema implementa as seguintes métricas e análises estatísticas:

### 1. Estatísticas Descritivas

Para cada Action Unit, são calculadas as seguintes estatísticas descritivas tanto para os dados de humanos reais quanto para os de avatares virtuais:

-   **Mediana**: Representa o valor central da intensidade da AU, sendo uma medida de tendência central robusta a outliers.
-   **Variância**: Mede a dispersão dos valores de intensidade em torno da média, indicando a variabilidade da expressão.
-   **Máximo**: O pico de intensidade registrado para a AU.

### 2. Suavização Percentual

A suavização quantifica a perda de intensidade da expressão ao ser transferida para o avatar. A fórmula é:

$$
\text{Suavização} (\%) = \frac{\text{Mediana}_{\text{Real}} - \text{Mediana}_{\text{Virtual}}}{\text{Mediana}_{\text{Real}}} \times 100
$$

Um valor positivo indica uma perda de intensidade (a expressão do avatar é mais fraca), enquanto um valor negativo sugere uma intensificação.

### 3. Correlação Temporal (Coeficiente de Pearson)

Para avaliar a sincronia temporal entre a expressão do humano real e a do avatar, é calculado o coeficiente de correlação de Pearson entre as séries temporais de cada AU.

$$
r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}}
$$

Onde:
-   $x_i$ e $y_i$ são as intensidades da AU nos frames $i$ para o real e o virtual, respectivamente.
-   $\bar{x}$ e $\bar{y}$ são as médias das intensidades.

Um valor próximo de 1 indica uma alta correlação positiva (o avatar acompanha o ritmo do humano), enquanto um valor próximo de 0 indica ausência de correlação.

### 4. Teste de Significância Estatística (Teste-T Independente)

Para verificar se a diferença de intensidade entre as expressões real e virtual é estatisticamente significativa, é aplicado um Teste-T para amostras independentes. A hipótese nula ($H_0$) é que não há diferença entre as médias de intensidade. Um p-valor inferior a 0.05 indica que a diferença é estatisticamente significativa.

## 🚀 Como Executar

1.  Certifique-se de que o Python e o pip estão instalados.
2.  Clone este repositório.

     ```bash
    git clone https://github.com/viniross/AU-Smoothing-Analysis.git
    cd AU-Smoothing-Analysis
    ```
3.  Instale as dependências: `pip install -r requirements.txt`.
4.  Se os dados brutos foram atualizados, execute o script de consolidação: `python src/data_loader.py`.
5.  Para iniciar a aplicação, execute o seguinte comando no terminal, na raiz do projeto:

    ```bash
    streamlit run 0_Home.py
    ```

    A aplicação será aberta no seu navegador padrão.