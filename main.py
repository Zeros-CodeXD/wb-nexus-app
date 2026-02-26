import flet as ft

# --- DATABASE (Your Full Data is here) ---
DATABASE = {
  "books_class_10": [
    {"title": "Sahitya Sanchayan (Bengali)", "link": "https://drive.google.com/file/d/1iQAADSemG8pJCG2phDGwGEdrpNGG1_9m/view"},
    {"title": "Bliss (English)", "link": "https://drive.google.com/file/d/1J8ACc0y2ftQ_wSjEqx-C0sA_d8ZjImkx/view"},
    {"title": "Ganit Prakash (Math)", "link": "https://drive.google.com/file/d/11TITkwOSGAFYSz015YStiaxUOUExTkfa/view"},
    {"title": "Koni (Rapid Reader)", "link": "https://drive.google.com/file/d/1jJ-YJIkSyYFG7bSt9Ui9RLfZDWApLKDp/view"}
  ],
  "books_class_9": [
    {"title": "Sahitya Sanchayan", "link": "https://drive.google.com/file/d/1W1iXt6ba7cKGXK06wU0PdDAP9yq_BNdI/view"},
    {"title": "Bliss (English)", "link": "https://drive.google.com/file/d/1MJfjJt_9UrG04iMAanWz2izBx_RaBsgc/view"},
    {"title": "Ganit Prakash", "link": "https://drive.google.com/file/d/1bLVwDsYfENQPta5O6w6DQMOvFURorsJj/view"}
  ],
  "colleges": [
    {"name": "Jadavpur Univ", "dept": "Science", "seats": 15, "link": "https://jadavpuruniversity.in/"},
    {"name": "Presidency Univ", "dept": "Arts", "seats": 0, "link": "https://presiuniv.ac.in/"}
  ],
  "syllabus_2025": [
    {"title": "Madhyamik 2025 Syllabus", "link": "https://wbbse.wb.gov.in"}
  ]
}

def main(page: ft.Page):
    # 1. SETUP
    page.title = "WB Nexus"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.spacing = 0
    
    # --- PHASE 2: THE REAL APP ---
    def load_content(e):
        page.clean()
        
        # Link Handler
        def handle_link(e):
            if e.control.data: page.launch_url(e.control.data)

        # UI Builders (Inside function to delay processing)
        def create_card(title, link, icon, color):
            return ft.Container(
                content=ft.Row([
                    ft.Icon(icon, color=color),
                    ft.Column([
                        ft.Text(title, weight="bold", size=14, color="white"),
                        ft.Text("Download", size=10, color="grey")
                    ], expand=True),
                    ft.IconButton(ft.icons.DOWNLOAD, icon_color=color, data=link, on_click=handle_link)
                ]),
                bgcolor="#1f1f1f", padding=10, border_radius=10, margin=5,
                on_click=handle_link, data=link
            )

        def create_college_card(item):
            col = "green" if item.get('seats', 0) > 0 else "red"
            return ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Text(item['name'], weight="bold", size=16),
                        ft.Container(content=ft.Text(f"{item.get('seats',0)} SEATS", color="black", size=10), bgcolor=col, padding=5, border_radius=5)
                    ], alignment="spaceBetween"),
                    ft.ElevatedButton("Apply", height=30, style=ft.ButtonStyle(bgcolor="blue", color="white"), data=item['link'], on_click=handle_link)
                ]),
                bgcolor="#252525", padding=15, border_radius=10, margin=5
            )

        # Tabs
        books_view = ft.ListView(expand=True, padding=10)
        for k in ["books_class_10", "books_class_9"]:
            if k in DATABASE:
                for x in DATABASE[k]: books_view.controls.append(create_card(x['title'], x['link'], ft.icons.BOOK, "orange"))

        colleges_view = ft.ListView(expand=True, padding=10)
        for x in DATABASE["colleges"]: colleges_view.controls.append(create_college_card(x))

        body = ft.Container(content=books_view, expand=True)

        def on_nav(e):
            if e.control.selected_index == 0: body.content = books_view
            elif e.control.selected_index == 1: body.content = colleges_view
            page.update()

        nav = ft.NavigationBar(
            on_change=on_nav,
            destinations=[
                ft.NavigationDestination(icon=ft.icons.BOOK, label="Books"),
                ft.NavigationDestination(icon=ft.icons.SCHOOL, label="Colleges"),
            ]
        )

        page.add(
            ft.Container(content=ft.Text("WB NEXUS", size=22, weight="bold", color="cyan"), padding=20, alignment=ft.alignment.center),
            body, 
            nav
        )
        page.update()

    # --- PHASE 1: THE MANUAL START BUTTON ---
    # This screen requires ZERO processing power. It will load instantly.
    start_btn = ft.ElevatedButton(
        "CLICK TO START APP", 
        color="black", 
        bgcolor="cyan", 
        height=50, 
        width=200,
        on_click=load_content
    )

    page.add(
        ft.Container(
            content=start_btn,
            alignment=ft.alignment.center,
            expand=True,
            bgcolor="#0a0a0a"
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
