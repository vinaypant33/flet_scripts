import flet as ft

from flet import TextField
from flet import TextButton
from flet import IconButton
from flet import FilledButton
from flet import icons
from flet import Page
from flet_core.control_event import ControlEvent



def main( page : ft.Page) -> None:
    page.title = 'Calculator'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    page.theme_mode = 'light'
    page.window.width = 330
    page.window.height = 400
    # page.window_frameless = True
    # page.window.resizable = False
    page.window.maximizable = False
    
    current_value  = 0
    middle_value  =  0
    third_value  =  0
    comparable_text = '0'
    
    def text_value(event ,  value):
        display_text.disabled = False
        comparable_text = str(comparable_text) + str(value)
        display_text.value = comparable_text
        display_text.disabled = True
        page.update()
        
        
        
    
    def ac_clicked(event):
        print("called from AC")
        display_text.clean()
        current_value = 0
        display_text.value = current_value
        page.update()
    
    display_text  : TextField = TextField(value = current_value , disabled=True)
    
    # Buttons for the first row : 
    # ac_button   : IconButton = IconButton(icon=icons.ABC , style=ft.ButtonStyle(
    #         bgcolor=ft.colors.BLUE,
    #         color=ft.colors.WHITE
    #     ))
    
    ac_button : IconButton = IconButton(icon=icons.ABC , on_click=ac_clicked)
    percentage_button : IconButton = IconButton(icon=icons.PERCENT)
    backspace_button : IconButton  = IconButton(icon = icons.CLOSE)
    divide_button  :  IconButton = IconButton(content=ft.Text("÷") , style=ft.ButtonStyle(bgcolor=ft.colors.BLUE_100 , color=ft.colors.BLUE))
    
    seven_key : IconButton = IconButton(content=ft.Text('7') , on_click=lambda e : text_value(event=e , value=7))
    eight_key : IconButton = IconButton(content=ft.Text('8'))
    nine_key  :  IconButton = IconButton(content=ft.Text('9'))
    cross_button  :  IconButton = IconButton(icon=icons.CLOSE_ROUNDED ,style=ft.ButtonStyle(bgcolor=ft.colors.BLUE_100 , color=ft.colors.BLUE))
    
    four_button :  IconButton = IconButton(content=ft.Text('4'))
    five_button :  IconButton = IconButton(content=ft.Text('5'))
    six_button :  IconButton = IconButton(content=ft.Text('6'))
    minus_button  :  IconButton = IconButton(icons.MINIMIZE_ROUNDED , style=ft.ButtonStyle(bgcolor=ft.colors.BLUE_100 , color=ft.colors.BLUE))
    
    
    one_key  :  IconButton = IconButton(content=ft.Text('1'))
    two_key : IconButton = IconButton(content=ft.Text('2'))
    three_key  : IconButton = IconButton(content=ft.Text('3'))
    add_key :  IconButton = IconButton(icons.ADD , style=ft.ButtonStyle(bgcolor=ft.colors.BLUE_100 , color=ft.colors.BLUE))
    
    double_zero : IconButton = IconButton(content=ft.Text('00'))
    zero : IconButton = IconButton(content=ft.Text('0'))
    dot_button : IconButton = IconButton(content=ft.Text('.'))
    equal_button : IconButton = IconButton(content=ft.Text('=') ,style=ft.ButtonStyle(bgcolor=ft.colors.BLUE_100 , color=ft.colors.BLUE))
    
    
    
    
    page.add(ft.Row([display_text]) , 
             ft.Row([ac_button , percentage_button , backspace_button , divide_button] , ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Row([seven_key , eight_key , nine_key , cross_button] , ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Row([four_button,five_button,six_button,minus_button] , ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Row([one_key,two_key,three_key,add_key] , ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Row([double_zero,zero,dot_button,equal_button]  , ft.MainAxisAlignment.SPACE_BETWEEN))
    
    


if __name__ == '__main__':
    ft.app(target=main)