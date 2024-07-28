import flet as ft

from flet import TextField
from flet_core.control_event import ControlEvent



def main( page : ft.Page) -> None:
    page.title = 'Increment Title'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    page.theme_mode = 'dark'
    
    textnumber : TextField = TextField(value='0' , 
                                       text_align=ft.TextAlign.CENTER , width=100)

    page.add(
        ft.Row(
            [textnumber]
        )
    )
    


if __name__ == '__main__':
    ft.app(target=main)