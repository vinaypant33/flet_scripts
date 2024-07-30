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
    current_opeartion = ''
    global comparable_text
    comparable_text = ""
    
    
    def text_value(event ,  value):
        # display_text.disabled = False
        global comparable_text
        
        if comparable_text  == "":
            comparable_text = str(value)
        else:
            comparable_text = str(comparable_text) + str(value)
        
        display_text.value  =  comparable_text
        page.update()
        
        # display_text.disabled = True
        
    def opeartion_value(event , operation):
        global middle_value
        global third_value
        global comparable_text
        global current_opeartion
        current_opeartion = str(operation)
        middle_value = comparable_text
        comparable_text = ""
        
    def equals_operation(event):
        global current_opeartion
        global middle_value
        global comparable_text
        if current_opeartion == '+':
            temp_value = int(comparable_text) + int(middle_value)
            display_text.value = str(temp_value)
        elif current_opeartion == '/':
            temp_value = int(comparable_text) / int(middle_value)
            display_text.value = str(temp_value)
        elif current_opeartion == 'X':
            temp_value = int(comparable_text) * int(middle_value)
            display_text.value = str(temp_value)
        elif current_opeartion == '%':
            temp_value = int(comparable_text) // int(middle_value)
            display_text.value = str(temp_value)
        elif current_opeartion == '-':
            temp_value = int(comparable_text) - int(middle_value)
            display_text.value = str(temp_value)
        
        
        page.update()
        comparable_text = ''
        middle_value = ''
        current_opeartion = ''


    def ac_clicked(event):
        global comparable_text
        comparable_text = ''
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
    percentage_button : IconButton = IconButton(icon=icons.PERCENT , on_click=lambda e : opeartion_value(e , '%'))
    backspace_button : IconButton  = IconButton(icon = icons.CLOSE)
    divide_button  :  IconButton = IconButton(content=ft.Text("÷") , style=ft.ButtonStyle(bgcolor=ft.colors.BLUE_100 , color=ft.colors.BLUE), on_click=lambda e : opeartion_value(e , '/'))
    
    seven_key : IconButton = IconButton(content=ft.Text('7') , on_click=lambda e : text_value(event=e , value=str('7')))
    eight_key : IconButton = IconButton(content=ft.Text('8') , on_click=lambda e : text_value(event=e , value=str('8')))
    nine_key  :  IconButton = IconButton(content=ft.Text('9') , on_click=lambda e : text_value(event=e , value=str('9')))
    cross_button  :  IconButton = IconButton(icon=icons.CLOSE_ROUNDED ,style=ft.ButtonStyle(bgcolor=ft.colors.BLUE_100 , color=ft.colors.BLUE) , on_click=lambda e : opeartion_value(e , 'X'))
    
    four_button :  IconButton = IconButton(content=ft.Text('4') , on_click=lambda e : text_value(event=e , value=str('4')))
    five_button :  IconButton = IconButton(content=ft.Text('5') , on_click=lambda e : text_value(event=e , value=str('5')))
    six_button :  IconButton = IconButton(content=ft.Text('6') , on_click=lambda e : text_value(event=e , value=str('6')))
    minus_button  :  IconButton = IconButton(icons.MINIMIZE_ROUNDED , style=ft.ButtonStyle(bgcolor=ft.colors.BLUE_100 , color=ft.colors.BLUE) , on_click=lambda e : opeartion_value(e , '-'))
    
    
    one_key  :  IconButton = IconButton(content=ft.Text('1') , on_click=lambda e : text_value(event=e , value=str('1')))
    two_key : IconButton = IconButton(content=ft.Text('2') , on_click=lambda e : text_value(event=e , value=str('2')))
    three_key  : IconButton = IconButton(content=ft.Text('3') , on_click=lambda e : text_value(event=e , value=str('3')))
    add_key :  IconButton = IconButton(icons.ADD , style=ft.ButtonStyle(bgcolor=ft.colors.BLUE_100 , color=ft.colors.BLUE) , on_click=lambda e : opeartion_value(e , '+'))
    
    double_zero : IconButton = IconButton(content=ft.Text('00') , on_click=lambda e : text_value(event=e , value=str('00')))
    zero : IconButton = IconButton(content=ft.Text('0') , on_click=lambda e : text_value(event=e , value=str('0')))
    dot_button : IconButton = IconButton(content=ft.Text('.'))
    equal_button : IconButton = IconButton(content=ft.Text('=') ,style=ft.ButtonStyle(bgcolor=ft.colors.BLUE_100 , color=ft.colors.BLUE) , on_click=lambda e : equals_operation(e))
    
    
    
    
    page.add(ft.Row([display_text]) , 
             ft.Row([ac_button , percentage_button , backspace_button , divide_button] , ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Row([seven_key , eight_key , nine_key , cross_button] , ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Row([four_button,five_button,six_button,minus_button] , ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Row([one_key,two_key,three_key,add_key] , ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Row([double_zero,zero,dot_button,equal_button]  , ft.MainAxisAlignment.SPACE_BETWEEN))
    
    


if __name__ == '__main__':
    ft.app(target=main)