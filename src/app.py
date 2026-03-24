import flet
from flet import ThemeMode, Text, TextField, OutlinedButton, Column, CrossAxisAlignment, Container, Colors, FontWeight
from flet.controls.border_radius import horizontal

from datetime import datetime, date
from dateutil.relativedelta import relativedelta

def main(page: flet.Page):
    # configurações
    page.title = "Primeira api"
    page.theme_mode = ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    # caixas de texto
    res_nome = Text()
    res_numero = Text()
    res_idade = Text()

    # funções

    def salvar_nome(e):
        res_nome.value = f'Olá {input_nome.value}  {input_sobrenome.value}'
        page.update()

    def salvar_numero(e):  # O argumento deve ser declarado aqui
        try:
            numero = int(int_numero.value)
            tipo = "par" if numero % 2 == 0 else "ímpar"
            res_numero.value = f'O número {numero} é {tipo}'
        except ValueError:
            res_numero.value = "Por favor, digite um número válido"
        page.update()

    def verificar_maioridade(e):
        try:
            # 1. Converte o texto digitado (DD/MM/AAAA) em uma data real
            nascimento = datetime.strptime(int_idade.value, "%d/%m/%Y")
            hoje = datetime.now()

            # 2. Cálculo da idade
            idade = hoje.year - nascimento.year

            # Ajuste: se ainda não fez aniversário este ano, subtrai 1
            fez_aniversario = (hoje.month, hoje.day) >= (nascimento.month, nascimento.day)
            if not fez_aniversario:
                idade -= 1

            # 3. Verifica maioridade
            if idade >= 18:
                res_idade.value = f"Você tem {idade} anos e é Maior de Idade!"
            else:
                res_idade.value = f"Você tem {idade} anos e é Menor de Idade!"

        except ValueError:
            res_idade.value = "Erro: Use o formato DD/MM/AAAA (ex: 20/05/1990)"

    # componentes
            #salvar
    input_nome = TextField(label="Nome")
    input_sobrenome = TextField(label="Sobrenome")
    int_numero = TextField(label="Numero")
    int_idade = TextField(label="Data de Nasc. (DD/MM/AAAA)", hint_text="Ex: 15/01/2000")

            #botões
    btn_idade = OutlinedButton("Verificar Maioridade", on_click=verificar_maioridade)
    btn_salvar= OutlinedButton("Salvar_nome", on_click=salvar_nome)
    btn_salvar1 = OutlinedButton("Salvar_número", on_click=salvar_numero)

    #construção de tala
    # ordem de como vai ficar visualmente
    page.add(
        Column([
            Container(
                Column(

                    [
                        Text("atividade 1", weight=FontWeight.BOLD, size=24),
                        input_nome,
                        input_sobrenome,
                        btn_salvar,
                        res_nome,
                    ],
                    horizontal_alignment = CrossAxisAlignment.CENTER,
                ),
                bgcolor = Colors.BLUE_400,
                padding = 15,
                border_radius=10,
                width = 400,


            ),

            Container(
                Column(

                    [
                        Text("atividade 2", weight=FontWeight.BOLD, size=24),
                        int_numero,
                        btn_salvar1,
                        res_numero,
                    ],
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                ),
                bgcolor=Colors.PURPLE_400,
                padding=15,
                border_radius=10,
                width=400,

            ),

            Container(
                Column(

                    [
                        Text("atividade 3", weight=FontWeight.BOLD, size=24),
                        int_idade,
                        btn_idade,
                        res_idade
                    ],
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                ),
                bgcolor=Colors.BLUE_800,
                padding=15,
                border_radius=10,
                width=400,

            ),
        ],
        width=400,
        horizontal_alignment = CrossAxisAlignment.CENTER

        )

    )

flet.run(main)


