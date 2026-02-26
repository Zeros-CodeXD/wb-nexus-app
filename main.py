import flet as ft
import time

# --- DATABASE (Same as before) ---
DATABASE = {
  "books_class_10": [
    {"title": "Class 10 Bengali", "link": "https://drive.google.com/file/d/1iQAADSemG8pJCG2phDGwGEdrpNGG1_9m/view?usp=drive_link"},
    {"title": "Class 10 Math", "link": "https://drive.google.com/file/d/11TITkwOSGAFYSz015YStiaxUOUExTkfa/view?usp=drive_link"},
    {"title": "Class 10 English", "link": "https://drive.google.com/file/d/1J8ACc0y2ftQ_wSjEqx-C0sA_d8ZjImkx/view?usp=drive_link"}
  ],
  "papers_2024": [
    {"title": "2024 Bengali Paper", "link": "https://drive.google.com/file/d/1cIMbMTMDD0uam_Dpgbw_Pwq3wxaMNoOI/view?usp=drive_link"},
    {"title": "2024 English Paper", "link": "https://drive.google.com/file/d/1Jy1Mje6v1VExMIs828UMIekf8m7NyXRu/view?usp=drive_link"}
  ],
  "colleges": [
    {"name": "Jadavpur Univ", "stream": "Science", "seats": 15, "link": "https://jadavpuruniversity.in/"},
    {"name": "Presidency Univ", "stream": "Arts", "seats": 0, "link": "https://presiuniv.ac.in/"}
  ]
}

def main(page: ft.Page):
    # 1. SETUP (Keep it simple)
    page.title = "WB Nexus"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.spacing = 0
    
    # --- PHASE 1: SHOW LOADING SCREEN IMMEDIATELY ---
    # This prevents the black screen. Android sees this and is happy.
    loader = ft.Column(
        [
            ft.ProgressRing(),
            ft.Text("Starting WB Nexus...", color="cyan")
        ], 
        alignment="center", horizontal_alignment="center", expand=True
    )
    
    page.add(ft.Container(content=loader, alignment=ft.alignment.center, expand=True))
    page.update()
    
    # --- PHASE 2: DEFINE THE APP (But don't show it yet) ---
    
    def open_link(e):
        page.launch_url(e.control.data)

    def make_card(title, link, icon, color):
        return ft.Container(
            content=ft.Row([
                ft.Icon(icon, color=color),
                ft.Column([
                    ft.Text(title, weight="bold", size=14, color="white"),
                    ft.Text("Download PDF", size=10, color="grey")
                ], expand=True),
                ft.IconButton(ft.icons.DOWNLOAD, icon_color=color, data=link, on_click=open_link)
            ]),
            bgcolor="#1f1f1f", padding=10, border_radius=10, margin=5,
            on_click=open_link, data=link
        )

    # Prepare Views (This happens in background while loader is showing)
    books_view = ft.ListView(expand=True, padding=10)
    for x in DATABASE["books_class_10"]:
        books_view.controls.append(make_card(x['title'], x['link'], ft.icons.BOOK, "orange"))

    papers_view = ft.ListView(expand=True, padding=10)
    for x in DATABASE["papers_2024"]:
        papers_view.controls.append(make_card(x['title'], x['link'], ft.icons.DESCRIPTION, "cyan"))

    college_view = ft.ListView(expand=True, padding=10)
    for x in DATABASE["colleges"]:
        col = "green" if x['seats'] > 0 else "red"
        college_view.controls.append(
            ft.Container(
                content=ft.Row([
                    ft.Text(x['name'], weight="bold", size=16),
                    ft.Container(content=ft.Text(f"{x['seats']} Seats", color="black", size=10), bgcolor=col, padding=5, border_radius=5)
                ], alignment="spaceBetween"),
                bgcolor="#252525", padding=15, border_radius=10, margin=5,
                on_click=open_link, data=x['link']
            )
        )

    # --- PHASE 3: SWAP LOADER FOR APP ---
    # We sleep 1 second to ensure the UI thread is ready
    time.sleep(0.5) 
    
    page.clean() # Remove loader

    # Add Navigation
    def nav_change(e):
        idx = e.control.selected_index
        if idx == 0: body.content = books_view
        elif idx == 1: body.content = papers_view
        elif idx == 2: body.content = college_view
        page.update()

    nav = ft.NavigationBar(
        selected_index=0,
        on_change=nav_change,
        destinations=[
            ft.NavigationDestination(icon=ft.icons.BOOK, label="Books"),
            ft.NavigationDestination(icon=ft.icons.DESCRIPTION, label="Papers"),
            ft.NavigationDestination(icon=ft.icons.SCHOOL, label="Colleges"),
        ]
    )

    header = ft.Container(
        content=ft.Text("WB NEXUS", size=22, weight="bold", color="cyan"),
        padding=15, bgcolor="#111", alignment=ft.alignment.center
    )

    body = ft.Container(content=books_view, expand=True)

    page.add(header, body, nav)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
