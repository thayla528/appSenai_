import asyncio

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
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    def digite_name():
        # Validação simples para verificar se os campos estão vazios
        res_nome.value = f'Olá, {input_nome.value}'
        res_cpf.value = f'CPF: {input_cpf.value}'
        res_email.value = f'E-mail: {input_email.value}'
        res_salario.value = f'Salário: R$ {input_salario.value}'


        navegar("/msg")

        page.update()



        if input_nome.value:
            input_nome.error = None
        else:

            input_nome.error = "Campo obrigatorio"

        if input_cpf.value:
            input_cpf.error = None
        else:

            input_cpf.error = "Campo obrigatorio"

        if input_email.value:
            input_email.error = None
        else:

            input_email.error = "Campo obrigatorio"

        if input_salario.value:
            input_salario.error = None
        else:

            input_salario.error = "Campo obrigatorio"

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
                    input_cpf,
                    input_email,
                    input_salario,
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
                        input_cpf,
                        input_email,
                        input_salario,


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
    input_cpf = TextField(label="CPF")
    input_email = TextField(label="E-mail")
    input_salario = TextField(label="R$ ""Salário")

    # Campos de saída (Labels da segunda tela)
    res_nome = Text()
    res_cpf = Text()
    res_email = Text()
    res_salario = Text()
    btn_salvar_nome = Button("Salvar", on_click=digite_name, )



    page.on_route_change = route_change
    page.on_view = view_pop

    route_change()


flet.run(main)
