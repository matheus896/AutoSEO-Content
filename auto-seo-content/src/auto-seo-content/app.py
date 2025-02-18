

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from datetime import datetime
from seo_blog_posts.crew import SeoBlogPosts
from dotenv import load_dotenv

# Configuração inicial do Streamlit
st.set_page_config(
    page_title="AutoSEO Content Factory",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Carregar variáveis de ambiente
load_dotenv()

# Logo e cabeçalho
st.logo(
    "https://cdn.prod.website-files.com/66cf2bfc3ed15b02da0ca770/66d07240057721394308addd_Logo%20(1).svg",
    link="https://www.crewai.com/"
)

# Layout principal
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.title("📝 AutoSEO Content Factory", anchor=False)
    st.caption("Criação automatizada de posts otimizados para SEO")

# Verificar chaves de API necessárias
if not os.environ.get("SERPER_API_KEY"):
    st.warning("⚠️ Configure sua chave SERPER_API_KEY no arquivo .env")
    st.stop()

# Seção de entrada de dados
with st.form(key="blog_config"):
    topic = st.text_input(
        "Tópico principal do post:",
        placeholder="Ex: Inteligência Artificial em Marketing Digital"
    )
    
    col1, col2 = st.columns(2)
    with col1:
        tone = st.selectbox(
            "Tom do conteúdo:",
            ("Profissional", "Descontraído", "Técnico", "Persuasivo")
        )
    with col2:
        keywords = st.text_input(
            "Palavras-chave adicionais (opcional):",
            placeholder="Ex: IA, automação, leads"
        )
    
    generate = st.form_submit_button("🚀 Gerar Post Blog")

if generate and topic:
    with st.status("🔍 Iniciando processo de criação...", expanded=True) as status:
        try:
            # Configurar inputs
            inputs = {
                "topic": topic,
                "current_date": datetime.now().strftime("%Y-%m-%d"),
                "tone": tone,
                "keywords": keywords
            }

            # Executar o crew
            SeoBlogPosts().crew().kickoff(inputs=inputs)
            
            # Ler arquivo gerado
            with open("blog_post.md", "r") as file:
                content = file.read()
            
            status.update(label="✅ Post gerado com sucesso!", state="complete")
            
            # Exibir preview
            st.subheader("Pré-visualização do Post")
            st.markdown(content)
            
            # Botão de download
            st.download_button(
                label="📥 Baixar Post em Markdown",
                data=content,
                file_name="blog_post.md",
                mime="text/markdown"
            )

        except Exception as e:
            status.update(label="❌ Erro na geração", state="error")
            st.error(f"Erro: {str(e)}")

# Footer
st.divider()
st.caption("Desenvolvido com ❤️ usando [CrewAI](https://crewai.com) e [Streamlit](https://streamlit.io)")