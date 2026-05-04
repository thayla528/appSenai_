import asyncio
import flet
from flet import ThemeMode, View, Colors, Button, Text, TextField, FloatingActionButton, Icons, \
    ListView, Icon, ListTile, PopupMenuButton, PopupMenuItem, Dropdown, dropdown


def main(page: flet.Page):
    # configurações
    page.title = "Primeira api"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    lista_dados = []

    def navegar(route):
        asyncio.create_task(page.push_route(route))

    def montar_lista_padrao():
        list_view.controls.clear()

        for item in lista_dados:
            # Lógica para mudar o ícone dependendo do gênero
            icone_genero = Icons.PERSON  # Padrão
            if item["genero"] == "Masculino":
                icone_genero = Icons.MAN
            elif item["genero"] == "Feminino":
                icone_genero = Icons.WOMAN

            list_view.controls.append(
                ListTile(
                    leading=Icon(icone_genero),  # Usa o ícone definido acima
                    title=Text(item["nome"]),
                    subtitle=Text(f"{item['profissao']} - {item['genero']}"),
                    trailing=PopupMenuButton(
                        icon=Icons.MORE_VERT,
                        items=[
                            PopupMenuItem("ver detalhes", icon=Icons.REMOVE_RED_EYE),
                            PopupMenuItem("Excluir", icon=Icons.DELETE, on_click=lambda _, i=item: excluir(i)),
                        ]
                    )
                )
            )
        page.update()

    def excluir(item):
        lista_dados.remove(item)
        montar_lista_padrao()

    def salvar_dados():
        nome = input_nome.value.strip()
        profissao = input_profissao.value.strip()
        genero = input_genero.value  # Pega o valor do Dropdown

        if nome and profissao and genero:
            # Salva nome, profissão e gênero no dicionário
            lista_dados.append({
                "nome": nome,
                "profissao": profissao,
                "genero": genero
            })

            # Limpa os campos
            input_nome.value = ""
            input_profissao.value = ""
            input_genero.value = None

            montar_lista_padrao()
            navegar("/lista_padrao")
        else:
            if not nome: input_nome.error_text = "campo obrigatório"
            if not profissao: input_profissao.error_text = "campo obrigatório"
            if not genero: input_genero.error_text = "selecione um gênero"

        page.update()

    def route_change():
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    flet.AppBar(title="Exemplo de listas", bgcolor=Colors.PURPLE_300),
                    Button("Lista padrão android", on_click=lambda _: navegar("/lista_padrao")),
                ]
            )
        )

        if page.route == "/lista_padrao":
            montar_lista_padrao()
            page.views.append(
                View(
                    route="/lista_padrao",
                    controls=[
                        flet.AppBar(title="Lista padrão android"),
                        list_view
                    ],
                    floating_action_button=FloatingActionButton(
                        icon=Icons.ADD,
                        on_click=lambda _: navegar("/form_cadastro")
                    )
                )
            )

        elif page.route == "/form_cadastro":
            page.views.append(
                View(
                    route="/form_cadastro",
                    controls=[
                        flet.AppBar(title="Formulário de cadastro"),
                        input_nome,
                        input_profissao,
                        input_genero,  # Adiciona o seletor na tela
                        btn_salvar
                    ]
                )
            )
        page.update()

    async def view_pop(e):
        if e.view is not None:
            page.views.remove(e.view)
            top_view = page.views[-1]
            await page.push_route(top_view.route)
            page.update()

    # componentes
    input_nome = TextField(label="Nome", hint_text="Digite seu nome")
    input_profissao = TextField(label="Profissão", hint_text="Digite sua profissão")

    # Dropdown para selecionar o gênero
    input_genero = Dropdown(
        label="Gênero",
        hint_text="Escolha o gênero",
        options=[
            dropdown.Option("Masculino"),
            dropdown.Option("Feminino"),
            dropdown.Option("Outro"),
        ],
    )

    list_view = ListView(height=500)
    btn_salvar = Button("Salvar", width=400, on_click=lambda _: salvar_dados())

    # eventos
    page.on_route_change = lambda _: route_change()
    page.on_view_pop = view_pop

    route_change()


flet.run(main)
