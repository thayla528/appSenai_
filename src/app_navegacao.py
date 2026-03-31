import asyncio

import flet
from flet import ThemeMode, View, Colors, Button


def main(page: flet.Page):
    # configurações
    page.title = "Primeira api"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

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
                    Button("Ir para segunda tela", on_click= lambda: navegar("/segunda_tela"))
                ]

            )
        )
        if page.route == "/segunda_tela":
            page.views.append(
                View(
                    route="/segunda_tela",
                    controls=[
                        flet.AppBar(
                            title="Segunda página",
                        )
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




    #eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()




flet.run(main)
