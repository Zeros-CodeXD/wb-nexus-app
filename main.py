import flet as ft
import json
import os

# --- HARDCODED DATABASE ---
DATABASE = {
    "books_class_10": [
        {"title": "Class 10 Bengali Text", "link": "https://drive.google.com/file/d/1iQAADSemG8pJCG2phDGwGEdrpNGG1_9m/view?usp=drive_link"},
        {"title": "Class 10 Mathematics", "link": "https://drive.google.com/file/d/11TITkwOSGAFYSz015YStiaxUOUExTkfa/view?usp=drive_link"},
    ],
    "books_class_9": [
        {"title": "Class 9 Bengali Text", "link": "https://drive.google.com/file/d/1W1iXt6ba7cKGXK06wU0PdDAP9yq_BNdI/view?usp=drive_link"},
    ],
    "books_class_8": [
        {"title": "Class 8 Science", "link": "https://drive.google.com/file/d/18BUfpM6iwruuXPcOyNTpYpIsifrwypPN/view?usp=sharing"},
    ],
    "papers_2024": [
        {"title": "Madhyamik 2024 - Bengali", "link": "https://drive.google.com/file/d/1cIMbMTMDD0uam_Dpgbw_Pwq3wxaMNoOI/view?usp=drive_link"},
    ],
    "colleges": [
        {"name": "Jadavpur University", "stream": "Science", "seats": 15, "link": "https://jadavpuruniversity.in/"},
    ]
}

def main(page: ft.Page):
    page.title = "WB-NEXUS"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = "auto"

    # --- JSON LOADING (ANDROID COMPATIBLE) ---
    external_data = []
    
    # In Flet, assets are referenced relative to the assets root
    # If your file is assets/data.json, use "data.json"
    try:
        # This is the most reliable way for Flet 0.80+
        with open("assets/your_file.json", "r", encoding="utf-8") as f:
            external_data = json.load(f)
    except Exception as e:
        print(f"Could not load JSON: {e}")

    def open_link(e):
        url = e.control.data
        if url: page.launch_url(url)

    def create_card(title, link, icon, color):
        return ft.Container(
            content=ft.Row([
                ft.Icon(icon, color=color),
                ft.Column([
                    ft.Text(title, weight="bold", size=14, width=220, overflow=ft.TextOverflow.ELLIPSIS),
                    ft.Text("Tap to Open PDF", size=10, color="grey")
                ], expand=True),
                ft.Icon(ft.icons.CHEVRON_RIGHT, color="grey")
            ]),
            bgcolor="#1A1A1A", padding=15, border_radius=12,
            on_click=open_link, data=link, margin=ft.margin.only(bottom=10)
        )

    # UI Construction
    books_view = ft.Column(scroll="auto")
    for section in ["books_class_10", "books_class_9", "books_class_8"]:
        books_view.controls.append(ft.Text(section.replace("_", " ").upper(), color="orange", weight="bold"))
        for item in DATABASE[section]:
            books_view.controls.append(create_card(item['title'], item['link'], ft.icons.BOOK, "orange"))

    papers_view = ft.Column(scroll="auto")
    for section in ["papers_2024"]:
        papers_view.controls.append(ft.Text("2024 PAPERS", color="cyan", weight="bold"))
        for item in DATABASE[section]:
            papers_view.controls.append(create_card(item['title'], item['link'], ft.icons.DESCRIPTION, "cyan"))

    page.add(
        ft.Container(
            content=ft.Text("WB-NEXUS", size=30, weight="bold", color="cyan"),
            alignment=ft.alignment.center, padding=20
        ),
        ft.Tabs(
            selected_index=0,
            expand=1,
            tabs=[
                ft.Tab(text="Books", icon=ft.icons.BOOK, content=books_view),
                ft.Tab(text="Papers", icon=ft.icons.HISTORY, content=papers_view),
            ]
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
