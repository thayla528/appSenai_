import asyncio

import flet
from flet import ThemeMode, View, Colors, Button, Text, TextField, OutlinedButton


def main(page: flet.Page):
    # configurações
    page.title = "Primeira api"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    # caixas de texto
    res_nome = Text()

    # funções
    # navegar

    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    # gerenciar as telas



    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title="Primeira página",
                        bgcolor=Colors.PURPLE_300


                    ),
                    input_nome,
                    input_sobrenome,
                    Button("Ir para segunda tela",  on_click= lambda: navegar("/segunda_tela"))
                ]

            )
        )
        if page.route == "/segunda_tela":
            res_nome.value = f'Olá {input_nome.value} {input_sobrenome.value}'

            page.views.append(
                View(
                    route="/segunda_tela",
                    controls=[
                        flet.AppBar(
                            title="Segunda página",

                        ),
                        res_nome,
                    ]
                )
            )

    # voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    #componentes
    input_nome = TextField(label="Nome")
    input_sobrenome = TextField(label="Sobrenome")

    #botoes


    #eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()




flet.run(main)
