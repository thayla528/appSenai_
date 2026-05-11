import flet as ft
import requests

def main(page: ft.Page):
    # Ajuste de Tema e Tamanho (Igual ao exemplo anterior)
    page.title = "Consulta CEP"
    page.theme_mode = ft.ThemeMode.DARK # Mudado para DARK
    page.window.width = 400
    page.window.height = 800

    # Opcional: Impede o usuário de esticar a tela e perder o formato
    page.window.resizable = False

    # Componentes com as cores do outro código
    input_cep = ft.TextField(
        label="Digite o CEP (apenas números)",
        border_color=ft.Colors.PURPLE_300,
        focused_border_color=ft.Colors.PINK_300
    )

    logradouro = ft.Text(size=18, color=ft.Colors.WHITE)
    bairro = ft.Text(size=18, color=ft.Colors.WHITE)
    cidade_uf = ft.Text(size=18, color=ft.Colors.WHITE)
    msg_erro = ft.Text(color=ft.Colors.RED_400)

    def buscar_cep(e):
        cep = input_cep.value.strip().replace("-", "").replace(".", "")
        msg_erro.value = ""

        if len(cep) != 8:
            msg_erro.value = "CEP inválido! Digite 8 números."
            page.update()
            return

        try:
            url = f"https://viacep.com.br/ws/{cep}/json/"
            response = requests.get(url)

            if response.status_code == 200:
                dados = response.json()
                if "erro" in dados:
                    msg_erro.value = "CEP não encontrado!"
                    logradouro.value = ""
                    bairro.value = ""
                    cidade_uf.value = ""
                else:
                    logradouro.value = f"Rua: {dados.get('logradouro')}"
                    bairro.value = f"Bairro: {dados.get('bairro')}"
                    cidade_uf.value = f"Cidade: {dados.get('localidade')} - {dados.get('uf')}"
            else:
                msg_erro.value = "Erro no servidor da API."
        except Exception:
            msg_erro.value = "Erro de conexão com a API."

        page.update()

    # Botão com a cor do estilo anterior
    btn_buscar = ft.ElevatedButton(
        "Consultar",
        on_click=buscar_cep,
        style=ft.ButtonStyle(bgcolor=ft.Colors.PURPLE_300, color=ft.Colors.WHITE)
    )

    page.add(
        ft.AppBar(title="Buscador de Endereço", bgcolor=ft.Colors.PURPLE_300),
        ft.Column(
            controls=[
                ft.Container(height=20), # Espaçamento
                input_cep,
                btn_buscar,
                msg_erro,
                ft.Divider(color=ft.Colors.PINK_300),
                logradouro,
                bairro,
                cidade_uf
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

# COMANDO DO PROFESSOR
ft.run(main)
