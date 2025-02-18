#!/usr/bin/env python
import sys
import warnings
from datetime import datetime

from seo_blog_posts.crew import SeoBlogPosts

warnings.filterwarnings("ignore", category=SyntaxWarning)

def get_tone_input():
    """Exibe menu interativo para seleção do tom"""
    print("\nSelecione o tom do conteúdo:")
    print("1 - Profissional")
    print("2 - Descontraído")
    print("3 - Técnico")
    print("4 - Persuasivo")
    
    while True:
        choice = input("Digite o número correspondente (1-4): ")
        tones = {
            "1": "Profissional",
            "2": "Descontraído",
            "3": "Técnico",
            "4": "Persuasivo"
        }
        if choice in tones:
            return tones[choice]
        print("Opção inválida. Tente novamente.")

def run():
    """
    Run the crew with dynamic user input.
    """
    # Coletar inputs do usuário
    print("\n" + "="*50)
    print(" SEO Blog Post Generator - Configuração ".center(50, "="))
    print("="*50)
    
    topic = input("\nDigite o tópico principal do post: ")
    tone = get_tone_input()
    keywords = input("Palavras-chave adicionais (opcional, separadas por vírgula): ")
    
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # Preparar inputs para o crew
    inputs = {
        "topic": topic,
        "current_date": current_date,
        "tone": tone,
        "keywords": keywords.strip() if keywords else ""
    }

    # Executar o crew
    print("\n" + "="*50)
    print(" Iniciando processo de criação... ".center(50, "="))
    SeoBlogPosts().crew().kickoff(inputs=inputs)
    print("\nProcesso concluído com sucesso! Verifique o arquivo blog_post.md")

if __name__ == "__main__":
    run()