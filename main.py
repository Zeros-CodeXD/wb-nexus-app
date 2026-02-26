import flet as ft

def main(page: ft.Page):
    page.bgcolor = "white"
    page.add(
        ft.Column([
            ft.Text("IT WORKS!", size=40, color="black", weight="bold"),
            ft.Text("The app is running.", color="blue"),
            ft.Icon(ft.icons.CHECK_CIRCLE, size=50, color="green")
        ], alignment="center", horizontal_alignment="center")
    )

if __name__ == "__main__":
    ft.app(target=main)
