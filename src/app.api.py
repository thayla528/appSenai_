import asyncio

import flet
from flet import ThemeMode, View, Colors, ListView, Icons, ListTile, Image, Column, Text, \
    Pagelet, NavigationBar, NavigationBarDestination, ScrollMode, FontWeight, TextOverflow, Card, Container, Row, \
    ProgressBar
from markdown_it.rules_block import lheading

from src.api_endpoints import get_planetas, get_personagens


def main(page: flet.Page):
    # Configurações
    page.title = "Exemplo de API"
    page.theme_mode = ThemeMode.LIGHT  # ou ThemeMode.Light
    page.window.width = 400
    page.window.height = 700

    # Funções
    # Navegar
    def navegar(route):
        asyncio.create_task(
            page.push_route(route)
        )

    def montar_lista_personagens():
        list_view.controls.clear()
        lista_dados1 = get_personagens()

        for item in lista_dados1["items"]:
            # --- LÓGICA DE CORES POR RAÇA ---
            raca = item["race"].lower()
            cor_badge = Colors.GREY_400  #--> Cor padrão
            #----- Cores ------
            if "saiyan" in raca:
                cor_badge = Colors.ORANGE_700
            elif "namekian" in raca:
                cor_badge = Colors.GREEN_700
            elif "frieza" in raca:
                cor_badge = Colors.PURPLE_400
            elif "human" in raca:
                cor_badge = Colors.BLUE_400

            #-------- tratamento de erros---------
            #-------- Barra de ki ----------------


            try:
                ki_limpo = float(item["ki"].replace(".", ""))
                progresso = ki_limpo / 60000000
                if progresso > 1: progresso = 1.0
            except:
                progresso = 0

            #--------- troquei o listitle por row ----------
            list_view.controls.append(
                Card(
                    content=Container(
                        height=160,
                        padding=15,
                        bgcolor=Colors.BLUE_50,  # Um azul mais suave de fundo
                        content=Row([
                            Image(src=item["image"], width=70),
                            Column([
                                # Linha com Nome e a Badge da Raça
                                Row([
                                    flet.TextButton(
                                        content=Text(item["name"], weight=FontWeight.BOLD, color=Colors.BLUE_900,
                                                     size=16),
                                        on_click=lambda e, personagem=item: ir_para_detalhes(personagem)
                                        ),
                                    Container(
                                        content=Text(item["race"], size=10, color=Colors.WHITE, weight=FontWeight.BOLD),
                                        bgcolor=cor_badge,
                                        padding=5,
                                        border_radius=5
                                    )
                                ], alignment="spaceBetween"),

                                # Barra de Poder
                                Column([
                                    Text(f"Ki inicial: {item['ki']}", size=11, weight=FontWeight.W_500),
                                    ProgressBar(value=progresso, color=Colors.ORANGE_700, bgcolor=Colors.GREY_300),
                                ], spacing=2),

                                Text(f"Max Ki: {item['maxKi']}", size=12, color=Colors.BLACK54),
                            ], expand=True, spacing=10)
                        ])
                    )
                )
            )

    def ir_para_detalhes(personagem):
        # Criamos uma nova visualização para o personagem específico
        page.views.append(
            View(
                route="/detalhes",
                controls=[
                    flet.AppBar(
                        title=Text(f"Detalhes: {personagem['name']}"),
                        bgcolor=Colors.ORANGE,
                    ),
                    Column([
                        Image(src=personagem["image"], width=200, height=200),
                        Text(personagem["name"], size=30, weight=FontWeight.BOLD),
                        Text(f"Raça: {personagem['race']}", size=20),
                        Text(f"Descrição: {personagem.get('description', 'Sem descrição disponível.')}"),
                        # Adicione aqui qualquer outro campo que sua API retorne
                    ], horizontal_alignment="center", spacing=20)
                ],
                scroll=ScrollMode.AUTO
            )
        )
        page.update()

    def montar_lista_planetas():
        list_view.controls.clear()

        # chamar a função que busca na api
        lista_dados = get_planetas()

        # item é um apelido para o objeto que esta vindo da api
        for item in lista_dados["items"]:
            list_view.controls.append(
                ListTile(
                    leading=Image(src=item["image"],width=60),
                    title=Text(item["name"],weight=FontWeight.BOLD,color=Colors.BLUE_900),
                    subtitle=Text(item["description"],max_lines=2, overflow=TextOverflow.ELLIPSIS,color=Colors.BLACK),
                )
            )

    def define_lista(e):
        # Muda a lista de acordo com o indice do NavigationBar
        return montar_lista_planetas() if e.data == 1 else montar_lista_personagens()

    # Gerenciar as telas(routes)
    def route_change():
        #carrega a primeira lista
        # montar_lista()
        montar_lista_personagens()

        page.views.clear()

        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(
                        title=Text("Dragon Ball Z", weight=FontWeight.BOLD),
                        bgcolor=Colors.ORANGE
                    ),
                    Column([
                        pagelet,
                    ])
                ],
                padding=0
            )
        )

    # Voltar
    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)

    # Componentes
    list_view = ListView(height=500)

    pagelet = Pagelet(
        navigation_bar=NavigationBar(
            destinations=[
                NavigationBarDestination(icon=Icons.MAN, label="Personagens"),
                NavigationBarDestination(icon=Icons.BLUR_ON, label="Planetas"),
            ],
            on_change=define_lista,
        ),
        content=Column([
            list_view,
        ],
            scroll=ScrollMode.HIDDEN,
            height=500
        ),
        height=600,
    )

    #  eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    route_change()


flet.run(main)
