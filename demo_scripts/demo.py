import flet as ft

from flet import TextField
from flet import TextButton
from flet import IconButton
from flet import FilledButton
from flet import icons
from flet import Page
from flet_core.control_event import ControlEvent



def main( page : ft.Page) -> None:
    page.title = 'Increment Title'
    page.vertical_alignment = ft.MainAxisAlignment.START
    
    page.theme_mode = 'light'
    page.window_width = 400
    page.window_height = 300
    # page.window_frameless = True
    page.window_resizable = True
    
    def onfocus_text(e):
        # textnumber.clean()
        textnumber.value = str("")
        page.update()
        
    
    textnumber : TextField = TextField(value='Enter Text',text_align=ft.TextAlign.START , width=200 , on_focus=lambda e : onfocus_text(e))
    add_button : TextButton = TextButton(text="Add Data")
    plus_icon : IconButton =IconButton(icons.ADD)
    page.add(
        ft.Row([textnumber , plus_icon])
    )
    


if __name__ == '__main__':
    ft.app(target=main)