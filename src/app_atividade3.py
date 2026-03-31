import asyncio

import flet as ft

import flet
from flet import ThemeMode, View, Colors, Button, Text, TextField



def main(page: flet.Page):
    # configuracoes
    page.title = "primeiro APP"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    # funçao
    # navegar
    def navegar_(route):
        asyncio.create_task(
            page.push_route(route)
        )

    def digite_name():
        # Validação simples para verificar se os campos estão vazios
        res_nome.value = f'Olá, {input_nome.value}'
        res_disciplina.value = f'Disciplina{input_disciplina}'
        res_salario.value = f'Salário: R$ {input_salario.value}'
        res_carga_horaria.value = f'Carga horaria{input_carga_horaria}'
        res_carga_horaria_minima.value = f'Carga horaria minima{input_carga_horaria_minima}'


        navegar_("/msg")

        page.update()



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


    # Gerenciar as telas(routes)
    def route_change():
        page.views.clear()

        page.views.append(
            View(
                route="/msg",
                controls=[
                    flet.AppBar(
                        title="Cadrastrar Funcionario",
                        bgcolor=Colors.PURPLE_300


                    ),
                    input_nome,
                    input_disciplina,
                    input_salario,
                    input_carga_horaria,
                    input_carga_horaria_minima,
                    btn_salvar_nome
                ]
            )
        )
        if page.route == "/msg":
            page.views.append(
                View(
                    route="/segunda_tela",
                    controls=[
                        flet.AppBar(
                            title="segunda pagina",
                        ),

                        text_msg,
                        input_nome,
                        input_disciplina,
                        input_salario,
                        input_carga_horaria,
                        input_carga_horaria_minima,


                    ]
                )
            )

    # Voltar

    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # componentes
    text_msg = Text()
    input_nome = TextField(label="Nome")
    input_disciplina = TextField(label="Disciplina")
    input_salario = TextField(label="Salario")
    input_carga_horaria = TextField(label="carga horaria")
    input_carga_horaria_minima = TextField(label="Carga horaria minima")

    # Campos de saída (Labels da segunda tela)
    res_nome = Text()
    res_disciplina = Text()
    res_salario = Text()
    res_carga_horaria = Text()
    res_carga_horaria_minima = Text()
    btn_salvar_nome = Button("Salvar", on_click=digite_name, )



    page.on_route_change = route_change
    page.on_view = view_pop

    route_change()


flet.run(main)
