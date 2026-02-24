import flet as ft
import traceback

# Keep the database here
DATABASE = {
    "books_class_10": [{"title": "Class 10 Bengali", "link": "https://wbbse.wb.gov.in"}],
    "books_class_9": [{"title": "Class 9 Bengali", "link": "https://wbbse.wb.gov.in"}]
}

def main(page: ft.Page):
    try:
        # 1. Setup Page
        page.title = "WB-NEXUS"
        page.theme_mode = ft.ThemeMode.DARK
        page.scroll = ft.ScrollMode.ADAPTIVE
        
        # 2. Tell us it started
        page.add(ft.Text("SYSTEM BOOTING...", color="yellow", weight="bold"))
        page.update()

        def open_link(e):
            page.launch_url(e.control.data)

        # 3. Build the UI
        content = ft.Column()
        content.controls.append(ft.Text("WB-NEXUS", size=30, weight="bold", color="orange"))

        for section, items in DATABASE.items():
            content.controls.append(ft.Text(section.upper(), color="blue", weight="bold"))
            for item in items:
                content.controls.append(
                    ft.ListTile(
                        title=ft.Text(item["title"]),
                        on_click=open_link,
                        data=item["link"]
                    )
                )

        # 4. Clear the booting message and show the app
        page.controls.clear()
        page.add(content)
        page.update()

    except Exception as e:
        # IF ANYTHING CRASHES, IT WILL SHOW UP HERE INSTEAD OF A BLACK SCREEN
        error_text = traceback.format_exc()
        page.controls.clear()
        page.add(
            ft.Text("APP CRASHED!", size=25, color="red", weight="bold"),
            ft.Text(error_text, color="red", selectable=True)
        )
        page.update()

if __name__ == "__main__":
    # Wrap the app launch in a try-except just in case the crash happens before main()
    try:
        ft.app(target=main)
    except Exception as core_error:
        print(f"Core Engine Error: {core_error}")
