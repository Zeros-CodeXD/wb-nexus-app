import flet as ft
import asyncio
import traceback

# --- 1. THE FULL EMBEDDED DATABASE (Safe & Crash-Proof) ---
DATABASE = {
  "books_class_8": [
    {"title": "Class 8 Science (Poribesh O Bigyan)", "link": "https://drive.google.com/file/d/18BUfpM6iwruuXPcOyNTpYpIsifrwypPN/view?usp=sharing"},
    {"title": "Class 8 English (Blossoms)", "link": "https://drive.google.com/file/d/1ETK2c1uJ802-hOiy0AsYHcmt8imEv_Fw/view?usp=drive_link"},
    {"title": "Class 8 Bengali Text (Sahitya Mela)", "link": "https://drive.google.com/file/d/197KM-v4IG5Zq7SwebNJ1kXv4OuSCwVDF/view?usp=drive_link"},
    {"title": "Class 8 Bengali Grammar", "link": "https://drive.google.com/file/d/1oVPMJrl6iYGF_tYeIzCYpwRBpxd9vLg3/view?usp=drive_link"},
    {"title": "Class 8 Rapid Reader", "link": "https://drive.google.com/file/d/1q_cJl8L5XLc96NZA2Cm5x9P_D52jIwNj/view?usp=drive_link"},
    {"title": "Class 8 History", "link": "https://drive.google.com/file/d/1z9yFpVeblEDkqlOueifS5bOoL-It_y6t/view?usp=drive_link"},
    {"title": "Class 8 Geography", "link": "https://drive.google.com/file/d/117Pahy31xCyuCGBa_7y_G7OKIE01N4Ch/view?usp=drive_link"}
  ],
  "books_class_9": [
    {"title": "Class 9 Bengali Text", "link": "https://drive.google.com/file/d/1W1iXt6ba7cKGXK06wU0PdDAP9yq_BNdI/view?usp=drive_link"},
    {"title": "Class 9 Rapid Reader", "link": "https://drive.google.com/file/d/1LdJle7dtqQnfdds_0ENfj3a6KmWACqu-/view?usp=drive_link"},
    {"title": "Class 9 Mathematics", "link": "https://drive.google.com/file/d/1bLVwDsYfENQPta5O6w6DQMOvFURorsJj/view?usp=drive_link"},
    {"title": "Class 9 English", "link": "https://drive.google.com/file/d/1MJfjJt_9UrG04iMAanWz2izBx_RaBsgc/view?usp=drive_link"}
  ],
  "books_class_10": [
    {"title": "Class 10 Bengali Text", "link": "https://drive.google.com/file/d/1iQAADSemG8pJCG2phDGwGEdrpNGG1_9m/view?usp=drive_link"},
    {"title": "Class 10 Rapid Reader", "link": "https://drive.google.com/file/d/1jJ-YJIkSyYFG7bSt9Ui9RLfZDWApLKDp/view?usp=drive_link"},
    {"title": "Class 10 Mathematics", "link": "https://drive.google.com/file/d/11TITkwOSGAFYSz015YStiaxUOUExTkfa/view?usp=drive_link"},
    {"title": "Class 10 English", "link": "https://drive.google.com/file/d/1J8ACc0y2ftQ_wSjEqx-C0sA_d8ZjImkx/view?usp=drive_link"}
  ],
  "papers_2024": [
    {"title": "Madhyamik 2024 - Bengali", "link": "https://drive.google.com/file/d/1cIMbMTMDD0uam_Dpgbw_Pwq3wxaMNoOI/view?usp=drive_link"},
    {"title": "Madhyamik 2024 - English", "link": "https://drive.google.com/file/d/1Jy1Mje6v1VExMIs828UMIekf8m7NyXRu/view?usp=drive_link"},
    {"title": "Madhyamik 2024 - Math", "link": "https://drive.google.com/file/d/1K21V1xGZEAFGXsGjojFzTo74KqpDFmC-/view?usp=drive_link"},
    {"title": "Madhyamik 2024 - Phy Sci", "link": "https://drive.google.com/file/d/1isrdJmWektP7UNi4heeYF52jcuzHHFqF/view?usp=drive_link"},
    {"title": "Madhyamik 2024 - Life Sci", "link": "https://drive.google.com/file/d/10uMrtr3cOujv_e07XkaliaEx16Gv9XGf/view?usp=drive_link"},
    {"title": "Madhyamik 2024 - History", "link": "https://drive.google.com/file/d/1i1C-plnjdPTpHN551J3xHlcxFzkHRQNE/view?usp=drive_link"},
    {"title": "Madhyamik 2024 - Geography", "link": "https://drive.google.com/file/d/1M3oyhEVcA_XW6_-X5L4l1eAhEJTPDh41/view?usp=drive_link"}
  ],
  "papers_2023": [
    {"title": "Madhyamik 2023 - Bengali", "link": "https://drive.google.com/file/d/1Eijq8S0kYZG6pZK3cwoO5pcNcIxslH_W/view?usp=drive_link"},
    {"title": "Madhyamik 2023 - English", "link": "https://drive.google.com/file/d/1XnGDf2ekn4ljc5LP4_kpRPFXkXrhDuHs/view?usp=drive_link"},
    {"title": "Madhyamik 2023 - Math", "link": "https://drive.google.com/file/d/1q8ev-LLr6Ry7jwIWY3M3n3oO3V2rehx-/view?usp=drive_link"},
    {"title": "Madhyamik 2023 - Phy Sci", "link": "https://drive.google.com/file/d/1GvH9M-sEWNIX9vDM2GOKmFx1OZyCHHlO/view?usp=drive_link"},
    {"title": "Madhyamik 2023 - Life Sci", "link": "https://drive.google.com/file/d/1LywHj2UH2mc2qrJD4KPPKvYbsfwAOTYx/view?usp=drive_link"},
    {"title": "Madhyamik 2023 - History", "link": "https://drive.google.com/file/d/1LSiZV1yY4QtUPq8Xu8HWFxCDOpScnO7y/view?usp=drive_link"},
    {"title": "Madhyamik 2023 - Geography", "link": "https://drive.google.com/file/d/1shP3OooAaWdeoM2oAnxWR92TEw5uU3QF/view?usp=drive_link"}
  ],
  "papers_2022": [
    {"title": "Madhyamik 2022 - Bengali", "link": "https://drive.google.com/file/d/1qiNdm9CJYefLZ-wF-qDLCQnMZNbR7ebU/view?usp=drive_link"},
    {"title": "Madhyamik 2022 - English", "link": "https://drive.google.com/file/d/1vuK6W9evHONNvHmk2nUOxvIYw6BdCCtr/view?usp=drive_link"},
    {"title": "Madhyamik 2022 - Math", "link": "https://drive.google.com/file/d/1XDwjyeTHDkRnXjJatqMjG-ZtFNEb3hBW/view?usp=drive_link"},
    {"title": "Madhyamik 2022 - Phy Sci", "link": "https://drive.google.com/file/d/1sYrcwl5gLVCNEFEcrR4QypBsBe78IQ9g/view?usp=drive_link"},
    {"title": "Madhyamik 2022 - Life Sci", "link": "https://drive.google.com/file/d/1zNaUAAEklNCKYdv_dRny_gyfotg5eGOM/view?usp=drive_link"},
    {"title": "Madhyamik 2022 - History", "link": "https://drive.google.com/file/d/1ZW4c3u6-G9gPXbMxAO1MQk6-_kh9r05g/view?usp=drive_link"},
    {"title": "Madhyamik 2022 - Geography", "link": "https://drive.google.com/file/d/19QWjSKary4IXrv9Bwa0oyADDTXmc3dPA/view?usp=drive_link"}
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

# --- USE ASYNC MAIN TO PREVENT UI FREEZE ---
async def main(page: ft.Page):
    # CRASH PROTECTION START
    try:
        # 1. CONFIGURATION
        page.title = "WB Nexus"
        page.theme_mode = ft.ThemeMode.DARK
        page.padding = 0
        page.spacing = 0
        page.window_width = 400
        page.window_height = 800
        page.theme = ft.Theme(color_scheme_seed="cyan", use_material3=True)

        # 2. LINK HANDLER (Android Compatible)
        def handle_link(e):
            url = e.control.data
            if url:
                print(f"Opening: {url}")
                page.launch_url(url)

        # 3. UI COMPONENTS
        def create_card(title, link, icon_name, color):
            return ft.Container(
                content=ft.Row([
                    ft.Container(
                        content=ft.Icon(icon_name, color=color, size=24),
                        padding=10, bgcolor=ft.colors.with_opacity(0.1, color), border_radius=10
                    ),
                    ft.Column([
                        ft.Text(title, size=14, weight="bold", max_lines=1, overflow=ft.TextOverflow.ELLIPSIS, color="white"),
                        ft.Text("Tap to Open", size=11, color="grey"),
                    ], expand=True, spacing=2),
                    ft.IconButton(ft.icons.OPEN_IN_NEW, icon_color=color, data=link, on_click=handle_link)
                ], alignment="spaceBetween"),
                padding=10, margin=ft.margin.only(bottom=5),
                bgcolor="#1f1f1f", border_radius=12,
                on_click=handle_link, data=link # Tapping anywhere works
            )

        def create_college_card(item):
            status_col = "green" if item['seats'] > 0 else "red"
            status_text = f"{item['seats']} LEFT" if item['seats'] > 0 else "FULL"
            return ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Text(item['name'], size=16, weight="bold", expand=True),
                        ft.Container(content=ft.Text(status_text, size=10, weight="bold", color="black"), 
                                     bgcolor=status_col, padding=5, border_radius=5)
                    ]),
                    ft.Divider(height=10, color="grey"),
                    ft.Row([
                        ft.Text(f"Stream: {item['stream']}", size=11, color="grey"),
                        ft.ElevatedButton("Apply", height=30, style=ft.ButtonStyle(bgcolor="blue", color="white"), 
                                          data=item['link'], on_click=handle_link)
                    ], alignment="spaceBetween")
                ]),
                padding=15, margin=ft.margin.only(bottom=10), bgcolor="#252525", border_radius=15
            )

        # 4. CONTENT BUILDERS
        def build_tab_content(tab_index):
            content = ft.Column(expand=True, scroll="auto", spacing=10, padding=15)
            
            # Notification Banner
            content.controls.append(
                ft.Container(
                    content=ft.Row([ft.Icon(ft.icons.CAMPAIGN, color="black"), ft.Text("News: 2025 Routine Released!", color="black", weight="bold")]),
                    bgcolor="amber", padding=10, border_radius=8, margin=ft.margin.only(bottom=10)
                )
            )

            if tab_index == 0: # BOOKS
                for k in ["books_class_10", "books_class_9", "books_class_8"]:
                    content.controls.append(ft.Text(k.replace("books_", "CLASS ").upper(), color="orange", weight="bold"))
                    for x in DATABASE[k]: content.controls.append(create_card(x['title'], x['link'], ft.icons.BOOK, "orange"))

            elif tab_index == 1: # PAPERS
                for k in ["papers_2024", "papers_2023", "papers_2022"]:
                    content.controls.append(ft.Text(k.replace("papers_", "YEAR ").upper(), color="cyan", weight="bold"))
                    for x in DATABASE[k]: content.controls.append(create_card(x['title'], x['link'], ft.icons.DESCRIPTION, "cyan"))

            elif tab_index == 2: # SYLLABUS
                content.controls.append(ft.Text("OFFICIAL SYLLABUS", color="purple", weight="bold"))
                for x in DATABASE["syllabus_2025"]: content.controls.append(create_card(x['title'], x['link'], ft.icons.LIST_ALT, "purple"))

            elif tab_index == 3: # COLLEGES
                content.controls.append(ft.Text("SEAT AVAILABILITY", color="green", weight="bold"))
                for x in DATABASE["colleges"]: content.controls.append(create_college_card(x))

            return content

        # 5. SPLASH SCREEN SEQUENCE
        logo_icon = ft.Icon(name=ft.icons.SHIELD_MOON, size=0, color="cyan")
        logo_text = ft.Text("WB NEXUS", size=0, weight="bold", opacity=0)
        
        splash = ft.Container(
            content=ft.Column([logo_icon, logo_text], alignment="center", horizontal_alignment="center"),
            alignment=ft.alignment.center, expand=True, bgcolor="#000000"
        )
        
        page.add(splash)
        
        # Safe Animation (Async)
        logo_icon.size = 80
        logo_icon.update()
        await asyncio.sleep(0.3)
        logo_text.size = 30
        logo_text.opacity = 1
        logo_text.update()
        await asyncio.sleep(1.5)
        
        # 6. LOAD MAIN APP
        page.clean()
        
        # Navigation Logic
        body_container = ft.Container(expand=True) # Holds current tab content

        def on_nav_change(e):
            idx = e.control.selected_index
            body_container.content = build_tab_content(idx)
            body_container.update()

        nav_bar = ft.NavigationBar(
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

        app_header = ft.Container(
            content=ft.Row([ft.Icon(ft.icons.SHIELD, color="cyan"), ft.Text("WB NEXUS", size=20, weight="bold")]),
            padding=ft.padding.only(top=40, left=20, bottom=10), bgcolor="#111"
        )

        # Initialize with Tab 0
        body_container.content = build_tab_content(0)
        
        page.add(app_header, body_container, nav_bar)

    # ERROR CATCHER (If app crashes, show why)
    except Exception as e:
        error_msg = traceback.format_exc()
        page.clean()
        page.add(
            ft.Column([
                ft.Icon(ft.icons.ERROR, color="red", size=50),
                ft.Text("CRITICAL ERROR", color="red", size=20),
                ft.Text(str(e), color="white"),
                ft.Text(error_msg, color="grey", size=10)
            ], scroll="auto")
        )

if __name__ == "__main__":
    ft.app(target=main)
