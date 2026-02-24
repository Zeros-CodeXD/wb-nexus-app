import flet as ft

# Data is inside the script so the app doesn't crash looking for files
DATABASE = {
    "books_class_8": [
        {"title": "Class 8 Science", "link": "https://drive.google.com/file/d/18BUfpM6iwruuXPcOyNTpYpIsifrwypPN/view?usp=sharing"},
        {"title": "Class 8 Mathematics", "link": "https://wbbse.wb.gov.in"},
    ],
    # ... (Keep all your other data here)
}

def main(page: ft.Page):
    page.title = "WB-NEXUS"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = "auto"
    
    def open_link(e):
        page.launch_url(e.control.data)

    # Simplified UI to ensure it loads fast
    lv = ft.ListView(expand=1, spacing=10, padding=20)
    
    for section, items in DATABASE.items():
        lv.controls.append(ft.Text(section.replace("_", " ").upper(), size=20, weight="bold", color="orange"))
        for item in items:
            lv.controls.append(
                ft.ListTile(
                    leading=ft.Icon(ft.icons.BOOK),
                    title=ft.Text(item["title"]),
                    subtitle=ft.Text("Tap to open link"),
                    on_click=open_link,
                    data=item["link"],
                )
            )
    
    page.add(lv)

# CRITICAL: This is what prevents the black screen
if __name__ == "__main__":
    ft.app(target=main)
