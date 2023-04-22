from pathlib import Path
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

# Configurações estruturais

diretorio = Path(__file__).parent if "__file__" in locals() else Path.cwd()

arquivo_css = diretorio / "style" / "geral.css" 
arquivo_pdf = diretorio / "assets" / "Curriculum.pdf"
arquivo_img = diretorio / "assets" / "Foto.jpg"


TITULO = "Curriculum | Jonatha Weydson da Silva"
NOME = 'Jonatha Weydson da Silva'
DESCRICAO = """
    Analista de Dados experiente em Python, especializado em análise, modelagem e visualização de dados. Habilidade em solucionar problemas de negócios, gerenciar projetos e comunicar insights. 
"""
EMAIL = "jonathaweydson@gmail.com"

MIDIA_SOCIAL = {
    "Linkedin":"https://www.linkedin.com/in/jonatha-weydson-261680a5/",
    "GitHub":"https://github.com/Jhow3D"
}

CURSOS = {
    "🎯 Ciências Contábeis - Faculdade Santa Helena":'Bachalerado',
    "🎯 Python Starter - Asimov Academy":"https://drive.google.com/file/d/1Egg711occm8UfYU2asNcCzcXo72cDqdD/view?usp=sharing",
    "🎯 Analisando Dados com Pandas & SQL - Asimov Academy":"https://drive.google.com/file/d/1JIFfyhjwc7S1CoqDi8m7Qwpjyuh8n45a/view?usp=share_link",
    "🎯 Python para Análise de Dados - Data Viking":"https://www.udemy.com/certificate/UC-8c61024a-a8b2-4a2b-ac8c-cdc60d9d8787/",
    "🎯 Fundamentos de Power BI - Empowerdata":"https://drive.google.com/file/d/15lzGruC2GiExcBfp9VXfPMZB4gYQ71id/view?usp=share_link",
    "🎯 Python Basics - Santader Coders":"https://drive.google.com/file/d/1IRKapp8VUKcNVWUiI4-Omjz6xo_RhBWF/view?usp=share_link",
    "🎯 Dashboard Analítico em STREAMLIT e Python - Udemy":"https://www.udemy.com/certificate/UC-00a7d2e7-7696-49a4-80cf-0a119609c8bb/"
}

st.set_page_config(
    page_title=TITULO
)

# Carregando Assents # 

with open(arquivo_css) as c:
    st.markdown("<style>{}</style>".format(c.read()),unsafe_allow_html=True)

with open(arquivo_pdf,'rb') as arquivo_pdf:
    pdfleitura = arquivo_pdf.read()
    
imagem = Image.open(arquivo_img)

def Home():
    col1,col2 = st.columns(2,gap="small")
    with col1:
        st.image(imagem,width=200)
        
    with col2:
        st.title(NOME)
        st.write(DESCRICAO) 
        st.download_button(
            label="Download Currículo",
            data=pdfleitura,
            file_name="Currículo_Jonatha.pdf",
            mime="application/octet-stream"
        )
        st.write("✉️",EMAIL)

    # MIDIAS SÓCIAIS # 

    st.write("#")

    colunas = st.columns(len(MIDIA_SOCIAL))
    for indices, (plataforma,link) in enumerate(MIDIA_SOCIAL.items()):
        colunas[indices].write(f'[{plataforma}]({link})')
        
    # EXPERIENCIAS # 

    st.write("#")
    st.write("---")
    st.subheader("Experiências")

    st.write("""
            
            -💹 5 anos de experiência na área contábil.
            
            -💹 Análise de dados com Python, Excel e Power Bi.
            
            -💹 Desenvolvimento Web com Streamlit.
            
            """)

    # Skills # 

    st.write("#")
    st.write("---")
    st.subheader("Skills")
    st.write("""
            
            - 🐍 Programação em Python
            - 📊Visualização de Dados
            - 📉Análise de Demonstrações Contábeis
            - 🏼 Análise de dados em Excel.
            """)

    # Histórico de Trabalho # 

    st.write("#")
    st.write("---")
    st.subheader("Históricos de Trabalhos")

    st.write("👨‍💻","**Professor de Python Módulo I | Fuctura**")
    st.write("06/2022 - Até o momento")
    st.write(
        """
        - Ministrada disciplinas de introdução a Python: 
            - Variáveis
            - Tipos de dados
            - Tipos de dados Estruturados
            - Condicionais
            - Loops
            - Funções
            - Bibliotecas
            - Try e Exception
            - Orientação a Objeto.
        """ 
    )

    st.write("👨‍💻","**Auxiliar Contábil | Tech Leader| Gerencial Consultores**")
    st.write("08/2023 - Até o momento")
    st.write(
        """
        - Processamento de Dados Contábeis
        - Análise das Demonstrações Contábeis
        - Criação de Relatórios Gerenciais e Visualização de Dados
        - Responsável por capacitar a equipe e ajudar a desenvolver um setor focado em tecnologia.
        - Responsável por criar novas soluções tecnólogicas para processamento de dados e automação de processos em Python.
        """ 
    )

    st.write("👨‍💻","**Análista Contábil | Construtora Andrade Guedes**")
    st.write("08/2020 - Até o momento")
    st.write(
        """
        - Processamento de Dados Contábeis
        - Análise das Demonstrações Contábeis
        - Responsável por envio de declarações acessórias (EFD,DCTF,DS)
        - Responsável por elaboração de relátorios gerencias para agentes internos e externos.
        """ 
    )

    # Cursos

    st.write("#")
    st.write("---")
    st.subheader("Cursos")
    for curso, link in CURSOS.items():
        st.write(f"[{curso}]({link})")
        
def projetos():
    pass

with st.sidebar:
    selected = option_menu(
            menu_title = 'Menu Principal',
            options=['Currículo','Projetos'],
            icons=[],
            menu_icon='cast',
            default_index=0
        )

if selected == 'Currículo':
    Home()    
    
elif selected == 'Projetos':
    coluns1 , coluns2 = st.columns(2)
    with coluns1: 
        proj = st.selectbox('Selecione o tipo de projeto ',[' ','Análise de dados','Desenvolvimento de Software','Desenvolvimento Web'])
        
        if proj == ' ':
            pass
        
        elif proj == 'Análise de dados':
            projAnalise = st.selectbox("Escolha o projeto: ",['','Educação','Mercado Financeiro','Mercado de games','Empresas: Únicornios'])
            if projAnalise == ' ':
                pass
            elif projAnalise == 'Educação':
                st.write('Descrição: Esse projeto tem como objetivo fazer uma analise de uma fonte de dados em csv que consta informações referente a área de educação e o objetivo foi realizar uma análise'
                             ' para responder algumas perguntas. Para isso foi necessário fazer tratamentos dos dados e posteriormente realizar as análises descritivas. ')
                st.write('link do projeto: https://github.com/Jhow3D/Projetos---An-lise-de-dados/blob/main/Case_Educa%C3%A7%C3%A3o.ipynb')
            elif projAnalise == 'Mercado Financeiro':
                st.markdown('Descrição: Esse projeto tem como objetivo fazer uma análise dos dados das ações da empresa MAGALU, foram realizadas análises temporais para indentificar o volume de compra e vendas das mesmas.')
                st.write('link do projeto: https://github.com/Jhow3D/Projetos---An-lise-de-dados/blob/main/Case_Mercado_Financeiro.ipynb')
                
            elif projAnalise == 'Mercado de games':
                st.markdown('Descrição: Esse projeto consiste em analisar o mercado de jogos do PS4 afim de responder algumas pergutas, também foi utilizados gráficos para ilustrar as análises realizadas.')
                st.write('link do projeto: https://github.com/Jhow3D/Projetos---An-lise-de-dados/blob/main/Case_Mercado_de_games.ipynb')
            
            elif projAnalise == "Empresas: Únicornios":
                st.markdown('Descrição: Nesse projeto foram relizadas inúmeras análises sobre uma base de dados que constam dados financeiros e gerenciais de empresas chamadas de "Unicórnios", que são empresas que tiveram uma grande valorização no mercado.')
                st.write('link do projeto: https://github.com/Jhow3D/Projetos---An-lise-de-dados/blob/main/Case_Unic%C3%B3rnios.ipynb')
        
        elif proj == 'Desenvolvimento de Software':
            projDesenvol = st.selectbox('Selecione o projeto: ',[" ",'Assistente Virtual'])
            if projDesenvol == 'Assistente Virtual':
                st.markdown('Descrição: Esse projeto foi criado cria uma assistente virtual que recebe comandos atrás de voz e texto para realizar tarefas já configuradas.')
                st.write('link do projeto: https://github.com/Jhow3D/Assistente-Virtual')