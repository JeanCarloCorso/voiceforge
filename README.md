# 🎙️ VoiceForge

VoiceForge é uma API de **Text-to-Speech (TTS)** construída em **Python** utilizando **FastAPI**, com suporte a múltiplas vozes (speakers) e geração de arquivos de áudio.

O projeto foi pensado para ser simples de iniciar, escalável e fácil de integrar com aplicações web.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.11**
- **FastAPI**
- **Uvicorn**
- **Coqui TTS**
- **HTML / CSS / JavaScript** (frontend simples)
- **Linux (ambiente de desenvolvimento)**

---

## 📦 Requisitos

Antes de iniciar, certifique-se de ter instalado:

- **Python 3.11.x**
- **pip (atualizado)**
- **git**
- Sistema Linux (Ubuntu/Debian recomendad

# Configuração do Ambiente

## Criar o ambiente virtual (Python 3.11)

~~~
python3.11 -m venv venv
~~~

## Ativar o ambiente virtual

~~~
source venv/bin/activate
~~~

Verifique se o Python correto está ativo:

~~~
python --version
~~~

Saída esperada:

~~~
Python 3.11.x
~~~

## Atualizar o pip

~~~
pip install --upgrade pip
~~~

## Instalar as dependências do projeto

~~~
pip install -r requirements.txt
~~~

## Executando o Projeto

Com o ambiente virtual ativado, execute o servidor FastAPI com:

~~~
uvicorn app.main:app --reload
~~~

## Dependências do Sistema (Linux)

Algumas dependências do Coqui TTS exigem bibliotecas adicionais do sistema.
Execute o comando abaixo antes ou caso ocorra erro na instalação:

~~~
sudo apt install -y build-essential libsndfile1 ffmpeg
~~~