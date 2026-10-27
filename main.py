#!/usr/bin/env python
from nicegui import ui
import backend 



with ui.header().classes(replace='row items-center') as header:
    ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
    with ui.tabs() as tabs:
        ui.tab('A')
        ui.tab('B')

with ui.footer(value=False) as footer:
    ui.label('Footer')

with ui.left_drawer().classes('bg-blue-100') as left_drawer:
    ui.label('Výstupní formát')
    toggle1 = ui.toggle(['csv', 'json'], value='csv')
    ui.label('Výstupní soubor:')
    result = ui.label()

with ui.tab_panels(tabs, value='A').classes('w-full'):
    with ui.tab_panel('A'):
        ui.label('Content of A')
        with ui.row():
            user_input = ui.input(label='klíčové slovní spojení', placeholder='začněte psát',
              on_change=lambda e: result.set_text(  e.value),
              validation={'Příliš krátký text': lambda value: len(value) > 10}).on('keydown.enter', lambda: backend.search())
            search = ui.button('Hledej', on_click=lambda: backend.search(user_input, result))
            ui.button('Stáhnout', on_click=lambda: ui.notify('Stahuji ....'))
        with ui.row():
            result = ui.html('', sanitize=False)

    with ui.tab_panel('B'):
        ui.label('Content of B')

ui.run(title="gscrapper")


