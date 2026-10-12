import flet as ft

def main(page: ft.Page):
    page.title = "My First App"
    
    # This centers everything on the screen
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Add some styled text and a button
    page.add(
        ft.Text("Hello from Flet!", size=30, weight=ft.FontWeight.BOLD),
        ft.ElevatedButton("Click Me!", on_click=lambda e: print("Button clicked!"))
    )

ft.run(main)