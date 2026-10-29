#!/usr/bin/env python
from nicegui import ui
import backend 



with ui.header().classes('items-center justify-between row') as header:
    ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
    ui.label('G-scrapper')
    ui.label('')

with ui.footer(value=False) as footer:
    ui.label('Footer')

with ui.left_drawer().classes('bg-blue-100') as left_drawer:
    ui.label('Výstupní formát')
    toggle1 = ui.toggle(['csv', 'json'], value='csv')
    ui.label('Výstupní soubor:')
    result = ui.label()

ui.label('Content of X')
with ui.row():
    user_input = ui.input(label='klíčové slovní spojení', placeholder='začněte psát',
      validation={'Příliš krátký text': lambda value: len(value) > 10}).on('keydown.enter',
      lambda: backend.search())
    search = ui.button('Hledej', on_click=lambda: backend.search(user_input, result))
    ui.button('Stáhnout', on_click=lambda: ui.notify('Stahuji ....'))
with ui.row():
    result = ui.html('', sanitize=False)


ui.run(title="gscrapper")


