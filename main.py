from time import sleep
import urllib.request
from time import sleep
from pywhatkit import sendwhatmsg
from datetime import datetime


def identifica_preco(url):

    pagina = urllib.request.urlopen(url)
    texto = pagina.read().decode("utf-8")
    inicio = texto.find(">$") + 2
    fim = texto.find("</", inicio)
    preco = texto[inicio:fim]

    return float(preco)


def checa_preco():

    valor_minino = 4.70

    while True:
        cliente_comum = identifica_preco(
            "http://beans.itcarlow.ie/prices-loyalty.html")
        cliente_fidelidade = identifica_preco(
            "http://beans.itcarlow.ie/prices.html")

        menor_valor = (
            cliente_comum if cliente_comum <= cliente_fidelidade else cliente_fidelidade
        )

        pagina = (
            "cliente comum" if menor_valor == cliente_comum else "cliente fidelidade"
        )

        if cliente_comum >= valor_minino and cliente_fidelidade >= valor_minino:
            print("\nEspere...")
            print(
                f"\033[31mPreço Fidelidade: U${cliente_fidelidade:.2f}\033[m")
            print(f"\033[31mPreço Comum: U${cliente_comum:.2f}\033[m\n\033[m")
            sleep(4)

        else:
            print(f"\nCompre agora na pagina do {pagina}.")
            print(f"\033[32mPreço: U${menor_valor:.2f}\033[m\n")
            break

    return f"Preço Baixou!! - Preço: U${menor_valor:.2f} - Acesse a página do {pagina}."


def msg_whatsapp(mensagem):

    agora = datetime.now()
    hora = agora.hour
    minuto = agora.minute + 1

    sendwhatmsg("+55479200-5685", mensagem, hora, minuto, 20, True, 2)
    print("\033[32mMensagem enviada no whatsapp\033[m")


if __name__ == "__main__":
    mensagem = checa_preco()
    msg_whatsapp(mensagem)
