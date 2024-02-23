import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from config import bot_token, chat_id
import pytz
import time
import schedule



def enviar_mensagem(chat_id, mensagem, imagem=None):
    url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
   
    parametros = {"chat_id": chat_id,
                  "caption": mensagem,
                  "parse_mode": "Markdown"}

    files = {"photo": ("imagem.jpg", imagem)}
    response = requests.post(url, params=parametros, files=files)

    if response is not None:
        if response.status_code == 200:
            print("Mensagem enviada com sucesso!")
        else:
            print(f"Erro ao enviar mensagem. Código de status: {response.status_code}")
    else:
        print("Não houve resposta da requisição.")
    
    return response



def main():
    link = "https://www.unirio.br/prae/nutricao-prae-1/cardapios-anteriores-re/cardapio-restaurante-escola-2024"
    #link = "http://www.unirio.br/prae/nutricao-prae-1/cardapios-anteriores-re/cardapios-restaurante-escola-2023"
    requisição = requests.get(link)

    print(f"Site da UNIRIO: {requisição}")

    site = BeautifulSoup(requisição.text, "html.parser")

    listas_cardapio = site.find('div', id='parent-fieldname-text-f155ab699e8147f0b2c6cc2583039df2')
    links = listas_cardapio.find_all('a')

    if links:
        last_link = links[-1]
        last_href = last_link['href']
        print(f"Último link (href): {last_href}")

        last_text = last_link.get_text()
        print(f"Título: {last_text}")

        response = requests.get(last_href)

        if response.status_code == 200:
            imagem = BytesIO(response.content)
        else:
            print(f"Não foi possível baixar a imagem do link: {last_href}. ERRO: {response.status_code}")
            return
    else:
        print("Nenhum link encontrado dentro da div.")
        return

    mensagem = "Coe galera! "
    mensagem += f"\nSegue o *{last_text.lower()}*🍴\n\nLembre-se:\nAlmoço: 11h às 14h\nJanta: 17h às 20h\n\nPreço: R$ 3,00"

    mensagem += "\n\nVerificar o perfil oficial do RE em caso de alterações no cardápio."
    mensagem += "\n[Insta do RE](https://www.instagram.com/restaurante_escola_unirio)\n\n-----------"



    try:
        enviar_mensagem(chat_id, mensagem, imagem=imagem)
        print("Arquivo e texto enviados com sucesso!")
    except requests.RequestException as e:
        print("Erro ao enviar a mensagem:", e)




#main()

# Executa a função main às segundas-feiras às 9h30 no fuso horário da América/São_Paulo
schedule.every().monday.at("10:30", "America/Sao_Paulo").do(main)
print("Aguardando agendamento")

while True:
    schedule.run_pending()
    time.sleep(1)
    
