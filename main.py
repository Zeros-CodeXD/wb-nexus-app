import flet as ft
import webbrowser
import asyncio # New way to handle time without crashing

# --- DATA (EMBEDDED TO PREVENT CRASHES) ---
# We put the data right here so the phone doesn't have to search for a file
DATABASE = {
  "books_class_8": [
    {"title": "Class 8 Science (Poribesh O Bigyan)", "link": "https://drive.google.com/file/d/18BUfpM6iwruuXPcOyNTpYpIsifrwypPN/view?usp=sharing"},
    {"title": "Class 8 English (Blossoms)", "link": "https://drive.google.com/file/d/1ETK2c1uJ802-hOiy0AsYHcmt8imEv_Fw/view?usp=drive_link"},
    {"title": "Class 8 Bengali Text", "link": "https://drive.google.com/file/d/197KM-v4IG5Zq7SwebNJ1kXv4OuSCwVDF/view?usp=drive_link"},
    {"title": "Class 8 History", "link": "https://drive.google.com/file/d/1z9yFpVeblEDkqlOueifS5bOoL-It_y6t/view?usp=drive_link"},
    {"title": "Class 8 Geography", "link": "https://drive.google.com/file/d/117Pahy31xCyuCGBa_7y_G7OKIE01N4Ch/view?usp=drive_link"}
  ],
  "books_class_9": [
    {"title": "Class 9 Bengali Text", "link": "https://drive.google.com/file/d/1W1iXt6ba7cKGXK06wU0PdDAP9yq_BNdI/view?usp=drive_link"},
    {"title": "Class 9 Mathematics", "link": "https://drive.google.com/file/d/1bLVwDsYfENQPta5O6w6DQMOvFURorsJj/view?usp=drive_link"},
    {"title": "Class 9 English", "link": "https://drive.google.com/file/d/1MJfjJt_9UrG04iMAanWz2izBx_RaBsgc/view?usp=drive_link"}
  ],
  "books_class_10": [
    {"title": "Class 10 Bengali Text", "link": "https://drive.google.com/file/d/1iQAADSemG8pJCG2phDGwGEdrpNGG1_9m/view?usp=drive_link"},
    {"title": "Class 10 Mathematics", "link": "https://drive.google.com/file/d/11TITkwOSGAFYSz015YStiaxUOUExTkfa/view?usp=drive_link"},
    {"title": "Class 10 English", "link": "https://drive.google.com/file/d/1J8ACc0y2ftQ_wSjEqx-C0sA_d8ZjImkx/view?usp=drive_link"}
  ],
  "papers_2024": [
    {"title": "Madhyamik 2024 - Bengali", "link": "https://drive.google.com/file/d/1cIMbMTMDD0uam_Dpgbw_Pwq3wxaMNoOI/view?usp=drive_link"},
    {"title": "Madhyamik 2024 - English", "link": "https://drive.google.com/file/d/1Jy1Mje6v1VExMIs828UMIekf8m7NyXRu/view?usp=drive_link"},
    {"title": "Madhyamik 2024 - Math", "link": "https://drive.google.com/file/d/1K21V1xGZEAFGXsGjojFzTo74KqpDFmC-/view?usp=drive_link"},
    {"title": "Madhyamik 2024 - Phy Science", "link": "https://drive.google.com/file/d/1isrdJmWektP7UNi4heeYF52jcuzHHFqF/view?usp=drive_link"}
  ],
  "papers_2023": [
    {"title": "Madhyamik 2023 - All Papers", "link": "https://drive.google.com/drive/folders/YOUR_LINK"}
  ],
  "colleges": [
    {"name": "Jadavpur University", "stream": "Science", "seats": 15, "link": "https://jadavpuruniversity.in/"},
    {"name": "Presidency Univ", "stream": "Arts", "seats": 0, "link": "https://presiuniv.ac.in/"},
    {"name": "Scottish Church", "stream": "Physics", "seats": 8, "link": "https://www.scottishchurch.ac.in/"}
  ],
  "syllabus_2025": [
    {"title": "Madhyamik 2025 Syllabus", "link": "https://wbbse.wb.gov.in"}
  ]
}

# --- MAIN APP (ASYNC MODE) ---
# We use 'async' to make the splash screen smooth without freezing
async def main(page: ft.Page):
    # 1. CONFIG
    page.title = "WB Nexus"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.spacing = 0
    page.theme = ft.Theme(color_scheme_seed="cyan", use_material3=True)

    # 2. UTILS
    def handle_click(e):
        if e.control.data: webbrowser.open(e.control.data)

    # 3. CARD CREATORS
    def create_card(title, link, icon_name, color):
        return ft.Container(
            content=ft.Row([
                ft.Icon(icon_name, color=color, size=24),
                ft.Column([
                    ft.Text(title, size=14, weight="bold", max_lines=1, overflow="ellipsis", color="white"),
                    ft.Text("Tap to Open", size=10, color="grey"),
                ], expand=True, spacing=2),
                ft.IconButton(ft.icons.DOWNLOAD, icon_color=color, data=link, on_click=handle_click)
            ], alignment="spaceBetween"),
            padding=10, margin=ft.margin.only(bottom=5),
            bgcolor="#1f1f1f", border_radius=12,
            on_click=handle_click, data=link # Make whole card clickable
        )

    def create_college_card(item):
        status_col = "green" if item['seats'] > 0 else "red"
        status_txt = f"{item['seats']} LEFT" if item['seats'] > 0 else "FULL"
        return ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Text(item['name'], size=16, weight="bold", expand=True),
                    ft.Container(content=ft.Text(status_txt, size=10, color="black", weight="bold"), 
                                 bgcolor=status_col, padding=5, border_radius=5)
                ]),
                ft.Divider(height=5, color="grey"),
                ft.Row([
                    ft.Text(item['stream'], size=12, color="grey"),
                    ft.ElevatedButton("Apply", height=30, style=ft.ButtonStyle(bgcolor="blue", color="white"), 
                                      data=item['link'], on_click=handle_click)
                ], alignment="spaceBetween")
            ]),
            padding=15, margin=ft.margin.only(bottom=10), bgcolor="#252525", border_radius=15
        )

    # 4. SPLASH SCREEN (THE SAFE WAY)
    logo = ft.Icon(name=ft.icons.SHIELD_MOON, size=0, color="cyan")
    txt = ft.Text("WB NEXUS", size=0, weight="bold", opacity=0)
    
    splash = ft.Container(
        content=ft.Column([logo, txt], alignment="center", horizontal_alignment="center"),
        alignment=ft.alignment.center, expand=True, bgcolor="#000000"
    )
    
    page.add(splash)
    
    # Animate
    logo.size = 80
    logo.update()
    await asyncio.sleep(0.3)
    txt.size = 30
    txt.opacity = 1
    txt.update()
    await asyncio.sleep(1.5) # Wait for 1.5 seconds
    
    # Clear Splash
    page.clean()

    # 5. LOAD DASHBOARD
    content_area = ft.Column(expand=True, scroll="auto", spacing=10)
    current_tab = [0]

    def update_view():
        content_area.controls.clear()
        idx = current_tab[0]
        
        # Banner
        content_area.controls.append(
            ft.Container(
                content=ft.Row([ft.Icon(ft.icons.CAMPAIGN, color="black"), ft.Text("News: 2025 Routine Out!", color="black")]),
                bgcolor="amber", padding=10, border_radius=5, margin=ft.margin.only(bottom=10)
            )
        )

        if idx == 0: # Books
            for k in ["books_class_10", "books_class_9", "books_class_8"]:
                content_area.controls.append(ft.Text(k.replace("books_", "CLASS ").upper(), color="orange", weight="bold"))
                for x in DATABASE.get(k, []): content_area.controls.append(create_card(x['title'], x['link'], ft.icons.BOOK, "orange"))

        elif idx == 1: # Papers
            for k in ["papers_2024", "papers_2023", "papers_2022"]:
                content_area.controls.append(ft.Text(k.replace("papers_", "YEAR ").upper(), color="cyan", weight="bold"))
                for x in DATABASE.get(k, []): content_area.controls.append(create_card(x['title'], x['link'], ft.icons.DESCRIPTION, "cyan"))

        elif idx == 2: # Syllabus
            content_area.controls.append(ft.Text("SYLLABUS", color="purple", weight="bold"))
            for x in DATABASE.get("syllabus_2025", []): content_area.controls.append(create_card(x['title'], x['link'], ft.icons.LIST_ALT, "purple"))

        elif idx == 3: # Colleges
            content_area.controls.append(ft.Text("SEAT TRACKER", color="green", weight="bold"))
            for x in DATABASE.get("colleges", []): content_area.controls.append(create_college_card(x))

        page.update()

    def on_nav_change(e):
        current_tab[0] = e.control.selected_index
        update_view()

    # App Bar
    app_bar = ft.Container(
        content=ft.Row([ft.Icon(ft.icons.SHIELD, color="cyan"), ft.Text("WB NEXUS", size=20, weight="bold")]),
        padding=ft.padding.only(top=40, left=20, bottom=10), bgcolor="#111"
    )

    # Nav Bar
    nav = ft.NavigationBar(
        selected_index=0,
        on_change=on_nav_change,
        bgcolor="#111",
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.BOOK, label="Books"),
            ft.NavigationBarDestination(icon=ft.icons.DESCRIPTION, label="Papers"),
            ft.NavigationBarDestination(icon=ft.icons.LIST, label="Syllabus"),
            ft.NavigationBarDestination(icon=ft.icons.SCHOOL, label="Colleges"),
        ]
    )

    page.add(app_bar, ft.Container(content=content_area, expand=True, padding=10), nav)
    update_view()

# Use asyncio to run the app
if __name__ == "__main__":
    ft.app(target=main)
