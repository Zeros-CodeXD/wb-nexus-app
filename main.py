import flet as ft

def main(page: ft.Page):
    # This ensures the app doesn't hang waiting for resources
    page.title = "WB-NEXUS"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = "auto"
    
    # Simple check to see if the app is alive
    page.add(
        ft.Container(
            content=ft.Text("WB-NEXUS Loaded Successfully!", size=20, color="green"),
            alignment=ft.alignment.center,
            padding=20
        )
    )

    def open_link(e):
        page.launch_url(e.control.data)

    # Hardcoded data to avoid JSON loading crashes
    DATABASE = {
        "Books": [
            {"title": "Class 10 Science", "link": "https://wbbse.wb.gov.in"},
        ]
    }

    for section, items in DATABASE.items():
        page.add(ft.Text(section, size=24, weight="bold"))
        for item in items:
            page.add(
                ft.ListTile(
                    title=ft.Text(item["title"]),
                    on_click=open_link,
                    data=item["link"]
                )
            )

if __name__ == "__main__":
    # The 'assets_dir' parameter is safer to define here
    ft.app(target=main, assets_dir="assets")
