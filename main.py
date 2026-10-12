import flet as ft

def main(page: ft.Page):
    page.title = "My First App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # This variable will keep track of how many times you click
    click_count = 0

    # Create the text element first
    my_text = ft.Text("Hello from Flet!", size=30, weight=ft.FontWeight.BOLD)

    # This function runs every time the button is clicked
    def button_clicked(e):
        nonlocal click_count
        click_count += 1
        my_text.value = f"Button clicked {click_count} times!"
        page.update() # This tells the app to refresh the screen

    # Add the elements to the page
    page.add(
        my_text,
        ft.Button("Click Me!", on_click=button_clicked)
    )

ft.run(main)