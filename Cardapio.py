import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from config import bot_token, chat_id



link = "http://www.unirio.br/prae/nutricao-prae-1/cardapios-anteriores-re/cardapios-restaurante-escola-2023"
requisição = requests.get(link)
print(requisição)


site = BeautifulSoup(requisição.text, "html.parser")



listas_cardapio = site.find('div',id='parent-fieldname-text-cac82a45c8944a18b462cf8a0d5addd9' )
links = listas_cardapio.find_all('a')

if links:
    # Obter o último link (href) da lista de links
    last_link = links[-5]
    last_href = last_link['href']
    print(f"Último link (href): {last_href}")

     # Exibir o texto do último link
    last_text = last_link.get_text()
    print(f"Titulo: {last_text}")

    # Fazer o download da imagem
    response = requests.get(last_href)

    # Verificar se o download foi bem-sucedido
    if response.status_code == 200:
        # Abrir a imagem usando a biblioteca PIL (Pillow)
        img = Image.open(BytesIO(response.content))

        # Exibir a imagem no console
            #plt.imshow(img)
            #plt.axis('off')  # Remover os eixos do gráfico (opcional)
            #plt.show()
            
    else:
        print(f"Não foi possível baixar a imagem do link: {last_href}. ERRO: {response.status_code}")

else:
    print("Nenhum link encontrado dentro da div.")



# Função para enviar mensagem (texto ou imagem)
def enviar_mensagem(chat_id, texto=None, imagem=None):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage" if texto else f"https://api.telegram.org/bot{bot_token}/sendPhoto"
    parametros = {"chat_id": chat_id}
    if texto:
        parametros["text"] = texto
    if imagem:
        files = {"photo": ("imagem.jpg", imagem)}
        response = requests.post(url, params=parametros, files=files)
    else:
        response = requests.post(url, params=parametros)
    return response


# Download da imagem
response = requests.get(last_href)
if response.status_code == 200:
    imagem = BytesIO(response.content)
else:
    print("Não foi possível baixar a imagem.")
    exit()


try:
    # Enviar a mensagem de texto
    enviar_mensagem(chat_id, texto=last_text)

    # Enviar a imagem
    enviar_mensagem(chat_id, imagem=imagem)
    print("Arquivo e texto enviados com sucesso!")
except requests.RequestException as e:
    print("Erro ao enviar a mensagem:", e)
