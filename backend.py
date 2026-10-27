import asyncio
from nicegui import ui
TEXT = 'This is <strong>HTML</strong>.'


async def search(user_input, result):
    ui.notify('Hledám....')
    value = user_input.value
    await asyncio.sleep(2)
    print(value)
    result.content = TEXT
    ui.notify('hotovo')

