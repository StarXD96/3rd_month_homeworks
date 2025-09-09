import flet as ft

from datetime import datetime

def main(page: ft.Page):
    page.title = 'Моё первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text(value='Hello World')

    greeting_history = []
    history_text = ft.Text('История приветствий:')


    def on_button_click(_):
        name = name_input.value.strip()
        print(name)

        if name:
            
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            greeting_text.value = f'Hello {name}! ({now})'
            print(greeting_text)
            name_input.value = ''

            greeting_history.append(f'{name} - {now}')
            history_text.value = 'История приветствий:\n' + '\n'.join(greeting_history)
        else:
            greeting_text.value = 'Пожалуйста, введите имя!'

        page.update()

    def clear_history(_):
        greeting_history.clear()
        history_text.value = "История приветствий"
        page.update()

    def theme_change(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click)
    name_button = ft.ElevatedButton(text='SEND', on_click=on_button_click)
    clear_history_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)
    theme_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=theme_change, tooltip='Сменит тему')

    page.add(greeting_text, name_input, name_button, clear_history_button, theme_button, history_text)


ft.app(target=main, view=ft.WEB_BROWSER)