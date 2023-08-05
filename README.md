# UNIRIO Cardápio Bot

Um bot Python que realiza web scraping do site da UNIRIO para obter o cardápio da semana do bandejão e envia a imagem para um bot no Telegram.

## Como funciona

O bot Python realiza web scraping do site da UNIRIO para extrair a imagem do cardápio da semana do bandejão. Em seguida, utiliza a API do Telegram para enviar a imagem para um bot previamente configurado no Telegram.

## Configuração

Antes de executar o projeto, você precisa configurar o arquivo `config.py` com as seguintes variáveis:

```python
# config.py

# Token de acesso do seu bot no Telegram
bot_token = "SEU_TOKEN_DO_BOT"

# ID do chat ou grupo para onde deseja enviar a imagem
chat_id = "SEU_CHAT_ID"
```

Substitua `SEU_TOKEN_DO_BOT` pelo token de acesso do seu bot no Telegram e `SEU_CHAT_ID` pelo ID do chat ou grupo para onde deseja enviar a imagem.

## Instalação

Para executar o projeto, siga os passos abaixo:

1. Crie um ambiente virtual:

```
python -m venv venv
```

2. Ative o ambiente virtual:

No Windows:

```
venv\Scripts\activate
```

No Linux ou macOS:

```
source venv/bin/activate
```

3. Instale as dependências:

```
pip install -r requirements.txt
```

## Execução

Para executar o projeto, execute o seguinte comando:

```
python seu_codigo.py
```

Substitua `seu_codigo.py` pelo nome do arquivo que contém o código de web scraping (o arquivo que você forneceu anteriormente).

## Contribuição

Contribuições são bem-vindas! Se você quiser colaborar com melhorias, correções de bugs ou adicionar novos recursos, sinta-se à vontade para abrir uma pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Contato

Se você tiver alguma dúvida ou precisar de ajuda, sinta-se à vontade para entrar em contato comigo através do meu perfil do GitHub.

---
