import flet as ft

def main(pagina):

    texto=ft.Text("hashsap")
    #Campo pro usuario digitar
    nome_usuario=ft.TextField(label="Escreva sêu nome")
    
    chat=ft.Column()

    def emviar_mensagem_tunel(informacoes):
    #Criando tunel
        print(informacoes)
        chat.controls.append(ft.Text(informacoes))
        pagina.update()

    pagina.pubsub.subscribe(emviar_mensagem_tunel)

    campo_mensagem=ft.TextField(label="Escreva sua mensagem aqui")

    def emviar_mensagem(evento):
        #Colocar o nome do usuario na mensagem
        texto_campo_mensagem=f"{nome_usuario.value}: {campo_mensagem.value}"
        #Adicionando mensagem
        pagina.pubsub.send_all(texto_campo_mensagem)
        #Limpa o campo mensagem
        campo_mensagem.value=""
        pagina.update()

    campo_emviar=ft.ElevatedButton("Emviar",on_click=emviar_mensagem)

    def entra_chat(evento):
        #Fechar o popap
        popup.open=False
        #Tirar o botão iniciar chat da tela
        pagina.remove(botoa_iniciar)
        #Adicionar chat
        pagina.add(chat)
        #Criar o campo de emviar mensagem
        linha_mensagem=ft.Row(
            [campo_mensagem,campo_emviar]
        )
        pagina.add(linha_mensagem)
        #Botão de emviar mensagem
        texto=f"{nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto)

        pagina.update()

    #Criando popup                         
    popup=ft.AlertDialog(
        open=False,
        modal=True, 
        title=ft.Text("Bem vindo ao hashsap"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar",on_click=entra_chat)]
        )

    def iniciar_chat(evento):
        #Abrindo popup
        pagina.dialog=popup
        popup.open=True
        pagina.update()
    
    botoa_iniciar=ft.ElevatedButton("Iniciar chat",on_click=iniciar_chat)
    #Adicionando elementos na pagina
    pagina.add(texto)
    pagina.add(botoa_iniciar)

#Chamando o app
#ft.app(main)
ft.app(main,view=ft.WEB_BROWSER)

#FORMATO SITE=WEB_BROWSER
