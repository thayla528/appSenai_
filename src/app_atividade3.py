import asyncio  # Importa a biblioteca para lidar com tarefas paralelas (como a sua função de navegar)
import flet as ft  # Importa o Flet com o apelido de 'ft'
import flet  # Importa o Flet de forma direta
from flet import ThemeMode, View, Colors,Text, TextField  # Importa componentes específicos do Flet


def main(page: flet.Page):  # Função principal que carrega a janela/página do app
    # CONFIGURAÇÕES INICIAIS DA PÁGINA
    page.title = "primeiro APP"  # Define o título da janela do aplicativo
    page.theme_mode = ThemeMode.DARK  # Define o tema escuro como padrão
    page.window.width = 400  # Define a largura da janela
    page.window.height = 700  # Define a altura da janela

    # FUNÇÃO DE NAVEGAÇÃO
    def navegar_(route):
        # Cria uma tarefa assíncrona para mudar a rota atual da página
        asyncio.create_task(page.push_route(route))

    # FUNÇÃO DISPARADA AO CLICAR NO BOTÃO "SALVAR"
    def digite_name():
        # Captura o que foi digitado na tela 1 e salva formatado nas variáveis de texto
        res_nome.value = f"Olá, {input_nome.value}"
        res_disciplina.value = f"Disciplina{input_disciplina.value}"
        res_salario.value = f"Salário: R$ {input_salario.value}"
        res_carga_horaria.value = f"Carga horaria{input_carga_horaria.value}"
        res_carga_horaria_minima.value = (
            f"Carga horaria minima{input_carga_horaria_minima.value}"
        )

        # COPIA o que foi digitado na tela 1 para as caixas travadas (read_only) da tela 2
        p2_nome.value = input_nome.value
        p2_disciplina.value = input_disciplina.value
        p2_salario.value = input_salario.value
        p2_carga_horaria.value = input_carga_horaria.value
        p2_carga_horaria_minima.value = input_carga_horaria_minima.value

        # Chama a função para navegar até a rota '/msg'
        navegar_("/msg")

        # Atualiza a página para carregar as informações novas na tela
        page.update()

        # SISTEMA DE VALIDAÇÃO (Verifica se cada campo está preenchido ou vazio)
        # Se tiver texto, remove o erro. Se estiver vazio, exibe o texto de erro no campo.
        if input_nome.value:
            input_nome.error = None
        else:
            input_nome.error = "Campo obrigatorio"

        if input_disciplina.value:
            input_disciplina.error = None
        else:
            input_disciplina.error = "Campo obrigatorio"

        if input_salario.value:
            input_salario.error = None
        else:
            input_salario.error = "Campo obrigatorio"

        if input_carga_horaria.value:
            input_carga_horaria.error = None
        else:
            input_carga_horaria.error = "Campo obrigatorio"

        if input_carga_horaria_minima.value:
            input_carga_horaria_minima.error = None
        else:
            input_carga_horaria_minima.error = "Campo obrigatorio"

    # FUNÇÃO PARA MUDAR O TEMA (CLARO/ESCURO)
    def handle_switch_change():
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT  # Ativa o tema claro
            switch.thumb_icon = ft.Icons.LIGHT_MODE  # Muda o ícone do botão
        else:
            page.theme_mode = ft.ThemeMode.DARK  # Ativa o tema escuro
            switch.thumb_icon = ft.Icons.DARK_MODE  # Muda o ícone do botão

        page.update()  # Atualiza a interface para aplicar o novo tema

    # O botão de interruptor (Switch) para mudar o tema
    switch = ft.Switch(
        thumb_icon=ft.Icons.DARK_MODE, on_change=handle_switch_change
    )

    # SISTEMA QUE GERENCIA AS TELAS ATRAVÉS DAS ROTAS
    def route_change():
        page.views.clear()  # Limpa a pilha de visualizações para reconstruir do zero

        # CRIAÇÃO DA PRIMEIRA TELA (Rota /msg)
        page.views.append(
            View(
                route="/msg",
                controls=[
                    flet.AppBar(  # Barra superior da primeira tela
                        leading=ft.Icon(ft.Icons.PERSON_ADD),  # Ícone de adicionar pessoa
                        title="Cadastrar Funcionário",  # Título
                        bgcolor=Colors.PURPLE_300,  # Cor roxa de fundo
                        actions=[switch],  # Adiciona o botão de tema no topo
                    ),
                    # Campos onde o usuário digita os dados na primeira tela:
                    input_nome,
                    input_disciplina,
                    input_salario,
                    input_carga_horaria,
                    input_carga_horaria_minima,
                    btn_salvar_nome,  # Botão de salvar
                    ft.Container(  # Container transparente aplicando um tema rosa
                        theme=ft.Theme(
                            color_scheme=ft.ColorScheme(primary=ft.Colors.PINK)
                        ),
                    ),
                ],
            )
        )

        # CRIAÇÃO DA SEGUNDA TELA (Apenas se a rota atual for /msg)
        if page.route == "/msg":
            page.views.append(
                View(
                    route="/segunda_tela",
                    controls=[
                        flet.AppBar(  # Barra superior da segunda tela
                            leading=ft.Icon(ft.Icons.CHROME_READER_MODE),  # Ícone de leitura
                            title="Segunda Página",  # Título
                            actions=[switch],  # Botão de tema também aqui
                        ),
                        text_msg,  # Texto vazio criado nos componentes
                        # Abaixo estão as caixas clonadas da primeira tela
                        # Elas têm o mesmo design, mas o usuário não consegue digitar nelas
                        p2_nome,
                        p2_disciplina,
                        p2_salario,
                        p2_carga_horaria,
                        p2_carga_horaria_minima,
                        ft.ElevatedButton(  # Botão para voltar à primeira tela
                            "Voltar",
                            icon=ft.Icons.ARROW_BACK,
                            on_click=lambda _: navegar_("/")  # Chama a função navegar apontando pra raiz
                        ),
                    ],
                )
            )
        page.update()  # Desenha as telas configuradas na interface

    # FUNÇÃO DO BOTÃO VOLTAR NATIVO (Por exemplo, a seta de voltar do Android)
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)  # Remove a tela atual
            top_view = page.views[-1]  # Pega a tela anterior
            await page.push_route(top_view.route)  # Volta para a rota anterior

    # CRIAÇÃO DOS COMPONENTES (Controles de interface)
    text_msg = Text()  # Texto simples

    # Caixas de digitação originais da TELA 1 (Com rótulos e ícones laterais)
    input_nome = TextField(label="Nome", prefix_icon=ft.Icons.PERSON)
    input_disciplina = TextField(label="Disciplina", prefix_icon=ft.Icons.BOOK)
    input_salario = TextField(label="Salário", prefix_icon=ft.Icons.ATTACH_MONEY)
    input_carga_horaria = TextField(label="Carga horária", prefix_icon=ft.Icons.ACCESS_TIME)
    input_carga_horaria_minima = TextField(label="Carga horária mínima", prefix_icon=ft.Icons.TIMER_3)

    # Caixas de digitação idênticas para a TELA 2 (Com o 'read_only=True' que impede a edição)
    p2_nome = TextField(label="Nome", prefix_icon=ft.Icons.PERSON, read_only=True)
    p2_disciplina = TextField(label="Disciplina", prefix_icon=ft.Icons.BOOK, read_only=True)
    p2_salario = TextField(label="Salário", prefix_icon=ft.Icons.ATTACH_MONEY, read_only=True)
    p2_carga_horaria = TextField(label="Carga horária", prefix_icon=ft.Icons.ACCESS_TIME, read_only=True)
    p2_carga_horaria_minima = TextField(label="Carga horária mínima", prefix_icon=ft.Icons.TIMER_3, read_only=True)

    # Variáveis de texto de saída (Caso você queira usar textos simples ao invés de caixas travadas)
    res_nome = Text()
    res_disciplina = Text()
    res_salario = Text()
    res_carga_horaria = Text()
    res_carga_horaria_minima = Text()

    # Botão de salvar com ícone de disquete, disparando a função 'digite_name'
    btn_salvar_nome = ft.ElevatedButton("Salvar", icon=ft.Icons.SAVE, on_click=digite_name)

    # Vincula as funções criadas aos eventos de rota nativos do Flet
    page.on_route_change = route_change
    page.on_view = view_pop

    # Executa o gerenciador de rotas pela primeira vez para abrir o app
    route_change()


flet.run(main)  # Comando que bota o aplicativo para rodar
