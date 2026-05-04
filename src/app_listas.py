import asyncio

import flet
from flet import ThemeMode, View, Colors, Button, Text, TextField, FloatingActionButton, Icons, \
    ListView, Card, Container, Row, Icon, ListTile, PopupMenuButton, PopupMenuItem
from markdown_it.rules_block import lheading


def main(page: flet.Page):
    # configurações
    page.title = "Primeira api"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    lista_dados = []

    # caixas de texto


    # funções
    # navegar

    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    def montar_lista_texto():
        list_view.controls.clear()
        for item in lista_dados:

            list_view.controls.append(
                Text(item)
            )

    def montar_lista_card():
        list_view.controls.clear()
        for item in lista_dados:
            list_view.controls.append(
                Card(
                    bgcolor=Colors.PINK_100,
                    content=Container(
                        Row(
                            [
                                Icon(Icons.PERSON),
                                Text(item)
                            ],
                            margin=8
                        )

                    )
                )
            )

    def montar_lista_padrao():
        list_view.controls.clear()

        for item in lista_dados:
            list_view.controls.append(
                ListTile(
                    leading=Icon(Icons.PERSON),
                    title=Text(item),
                    subtitle=Text("Subtitulo"),
                    trailing=PopupMenuButton(
                        icon=Icons.MORE_VERT,
                        items=[
                            PopupMenuItem("ver detalhes", icon=Icons.REMOVE_RED_EYE),
                            PopupMenuItem("Excluir", icon=Icons.DELETE, on_click=lambda: excluir(item)),
                        ]
                    )

                )
            )

    def excluir(item):
        lista_dados.remove(item)
        montar_lista_padrao()

    def salvar_dados():
        nome = input_nome.value.strip()

        if nome:
            lista_dados.append(nome)
            input_nome.error_text = None
            input_nome.value = ""
        else:
            input_nome.error = "campo obrigatório"

        montar_lista_texto()
        montar_lista_card()
        montar_lista_padrao()
        navegar("/lista_padrao")

        page.update()




    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title="Exemplo de listas",
                        bgcolor=Colors.PURPLE_300


                    ),

                    Button("Lista de texto",  on_click= lambda: navegar("/lista_texto")),
                    Button("Lista de card", on_click=lambda: navegar("/lista_card")),
                    Button("Lista padrão android", on_click=lambda: navegar("/lista_padrao")),
                ]

            )
        )
        if page.route == "/lista_texto":
            montar_lista_texto()
            page.views.append(
                View(
                    route="/lista_texto",
                    controls=[
                        flet.AppBar(
                            title="Lista de texto",

                        ),
                        input_nome,
                        btn_salvar,
                        list_view

                    ]
                )
            )


        elif page.route == "/lista_card":
            montar_lista_card()

            page.views.append(
                View(
                    route="/lista_card",
                    controls=[
                        flet.AppBar(
                            title="Lista de card",

                        ),
                        input_nome,
                        btn_salvar,
                        list_view
                    ]
                )
            )

        elif page.route == "/lista_padrao":
            montar_lista_padrao()

            page.views.append(
                View(
                    route="/lista_padrao",
                    controls=[
                        flet.AppBar(
                            title="Lista padrão android",

                        ),
                        list_view

                    ],
                    floating_action_button = FloatingActionButton(
                        icon = Icons.ADD,
                        on_click=lambda: navegar("/form_cadastro")
                    )
                )
            )

        elif page.route == "/form_cadastro":

            page.views.append(
                View(
                    route="/form_cadastro",
                    controls=[
                        flet.AppBar(
                            title="Formulário de cadastro",

                        ),
                        input_nome,
                        btn_salvar

                    ]
                )
            )

        page.update()

    # voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)
            page.update()

    #componentes

    input_nome = TextField(label="Nome", hint_text="Digite seu nome", on_submit=salvar_dados)


    list_view = ListView(height=500)


    #botoes

    btn_salvar = Button("Salvar", width=400, on_click=lambda: salvar_dados())

    #eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()




flet.run(main)
