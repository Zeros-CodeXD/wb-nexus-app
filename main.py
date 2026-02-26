import flet as ft
import threading

# --- 1. THE COMPLETE MASTER DATABASE (EMBEDDED) ---
DATABASE = {
  # --- BOOKS CLASS 10 ---
  "books_class_10": [
    {"title": "Sahitya Sanchayan (Bengali)", "link": "https://drive.google.com/file/d/1iQAADSemG8pJCG2phDGwGEdrpNGG1_9m/view"},
    {"title": "Bliss (English)", "link": "https://drive.google.com/file/d/1J8ACc0y2ftQ_wSjEqx-C0sA_d8ZjImkx/view"},
    {"title": "Ganit Prakash (Math)", "link": "https://drive.google.com/file/d/11TITkwOSGAFYSz015YStiaxUOUExTkfa/view"},
    {"title": "Koni (Rapid Reader)", "link": "https://drive.google.com/file/d/1jJ-YJIkSyYFG7bSt9Ui9RLfZDWApLKDp/view"},
    {"title": "Bhouto Bigyan (Physical Sci)", "link": "https://drive.google.com/file/d/YOUR_LINK"},
    {"title": "Jiban Bigyan (Life Sci)", "link": "https://drive.google.com/file/d/YOUR_LINK"},
    {"title": "Itihas (History)", "link": "https://drive.google.com/file/d/YOUR_LINK"},
    {"title": "Bhugol (Geography)", "link": "https://drive.google.com/file/d/YOUR_LINK"}
  ],
  # --- BOOKS CLASS 9 ---
  "books_class_9": [
    {"title": "Sahitya Sanchayan (Bengali)", "link": "https://drive.google.com/file/d/1W1iXt6ba7cKGXK06wU0PdDAP9yq_BNdI/view"},
    {"title": "Bliss (English)", "link": "https://drive.google.com/file/d/1MJfjJt_9UrG04iMAanWz2izBx_RaBsgc/view"},
    {"title": "Ganit Prakash (Math)", "link": "https://drive.google.com/file/d/1bLVwDsYfENQPta5O6w6DQMOvFURorsJj/view"},
    {"title": "Aam Aatir Bhepu (Rapid)", "link": "https://drive.google.com/file/d/1LdJle7dtqQnfdds_0ENfj3a6KmWACqu-/view"},
    {"title": "Physical Science", "link": "https://drive.google.com/file/d/YOUR_LINK"},
    {"title": "Life Science", "link": "https://drive.google.com/file/d/YOUR_LINK"}
  ],
  # --- BOOKS CLASS 8 ---
  "books_class_8": [
    {"title": "Sahitya Mela (Bengali)", "link": "https://drive.google.com/file/d/197KM-v4IG5Zq7SwebNJ1kXv4OuSCwVDF/view"},
    {"title": "Blossoms (English)", "link": "https://drive.google.com/file/d/1ETK2c1uJ802-hOiy0AsYHcmt8imEv_Fw/view"},
    {"title": "Ganit Prabha (Math)", "link": "https://drive.google.com/file/d/YOUR_LINK"},
    {"title": "Poribesh O Bigyan (Science)", "link": "https://drive.google.com/file/d/18BUfpM6iwruuXPcOyNTpYpIsifrwypPN/view"},
    {"title": "Pather Panchali (Rapid)", "link": "https://drive.google.com/file/d/1q_cJl8L5XLc96NZA2Cm5x9P_D52jIwNj/view"},
    {"title": "Atit O Aitihya (History)", "link": "https://drive.google.com/file/d/1z9yFpVeblEDkqlOueifS5bOoL-It_y6t/view"},
    {"title": "Amader Prithibi (Geo)", "link": "https://drive.google.com/file/d/117Pahy31xCyuCGBa_7y_G7OKIE01N4Ch/view"},
    {"title": "Bhasha Charcha (Grammar)", "link": "https://drive.google.com/file/d/1oVPMJrl6iYGF_tYeIzCYpwRBpxd9vLg3/view"}
  ],
  
  # --- PAPERS 2024 ---
  "papers_2024": [
    {"title": "2024 Bengali Paper", "link": "https://drive.google.com/file/d/1cIMbMTMDD0uam_Dpgbw_Pwq3wxaMNoOI/view"},
    {"title": "2024 English Paper", "link": "https://drive.google.com/file/d/1Jy1Mje6v1VExMIs828UMIekf8m7NyXRu/view"},
    {"title": "2024 Math Paper", "link": "https://drive.google.com/file/d/1K21V1xGZEAFGXsGjojFzTo74KqpDFmC-/view"},
    {"title": "2024 Physical Science", "link": "https://drive.google.com/file/d/1isrdJmWektP7UNi4heeYF52jcuzHHFqF/view"},
    {"title": "2024 Life Science", "link": "https://drive.google.com/file/d/10uMrtr3cOujv_e07XkaliaEx16Gv9XGf/view"},
    {"title": "2024 History Paper", "link": "https://drive.google.com/file/d/1i1C-plnjdPTpHN551J3xHlcxFzkHRQNE/view"},
    {"title": "2024 Geography Paper", "link": "https://drive.google.com/file/d/1M3oyhEVcA_XW6_-X5L4l1eAhEJTPDh41/view"}
  ],
  # --- PAPERS 2023 ---
  "papers_2023": [
    {"title": "2023 Bengali Paper", "link": "https://drive.google.com/file/d/1Eijq8S0kYZG6pZK3cwoO5pcNcIxslH_W/view"},
    {"title": "2023 English Paper", "link": "https://drive.google.com/file/d/1XnGDf2ekn4ljc5LP4_kpRPFXkXrhDuHs/view"},
    {"title": "2023 Math Paper", "link": "https://drive.google.com/file/d/1q8ev-LLr6Ry7jwIWY3M3n3oO3V2rehx-/view"},
    {"title": "2023 Physical Science", "link": "https://drive.google.com/file/d/1GvH9M-sEWNIX9vDM2GOKmFx1OZyCHHlO/view"},
    {"title": "2023 Life Science", "link": "https://drive.google.com/file/d/1LywHj2UH2mc2qrJD4KPPKvYbsfwAOTYx/view"},
    {"title": "2023 History Paper", "link": "https://drive.google.com/file/d/1LSiZV1yY4QtUPq8Xu8HWFxCDOpScnO7y/view"},
    {"title": "2023 Geography Paper", "link": "https://drive.google.com/file/d/1shP3OooAaWdeoM2oAnxWR92TEw5uU3QF/view"}
  ],
  # --- PAPERS 2022 ---
  "papers_2022": [
    {"title": "2022 Bengali Paper", "link": "https://drive.google.com/file/d/1qiNdm9CJYefLZ-wF-qDLCQnMZNbR7ebU/view"},
    {"title": "2022 English Paper", "link": "https://drive.google.com/file/d/1vuK6W9evHONNvHmk2nUOxvIYw6BdCCtr/view"},
    {"title": "2022 Math Paper", "link": "https://drive.google.com/file/d/1XDwjyeTHDkRnXjJatqMjG-ZtFNEb3hBW/view"},
    {"title": "2022 Physical Science", "link": "https://drive.google.com/file/d/1sYrcwl5gLVCNEFEcrR4QypBsBe78IQ9g/view"},
    {"title": "2022 Life Science", "link": "https://drive.google.com/file/d/1zNaUAAEklNCKYdv_dRny_gyfotg5eGOM/view"},
    {"title": "2022 History Paper", "link": "https://drive.google.com/file/d/1ZW4c3u6-G9gPXbMxAO1MQk6-_kh9r05g/view"},
    {"title": "2022 Geography Paper", "link": "https://drive.google.com/file/d/19QWjSKary4IXrv9Bwa0oyADDTXmc3dPA/view"}
  ],

  # --- COLLEGES (FULL LIST) ---
  "colleges": [
    {"name": "Jadavpur University", "dept": "CSE / IT", "seats": 12, "cutoff": "98%", "link": "https://jadavpuruniversity.in/"},
    {"name": "Jadavpur University", "dept": "Physics Hons", "seats": 8, "cutoff": "94%", "link": "https://jadavpuruniversity.in/"},
    {"name": "Calcutta University", "dept": "B.Tech", "seats": 25, "cutoff": "90%", "link": "https://www.caluniv.ac.in/"},
    {"name": "Presidency Univ", "dept": "Economics", "seats": 0, "cutoff": "CLOSED", "link": "https://presiuniv.ac.in/"},
    {"name": "St. Xavier's College", "dept": "B.Com (Morning)", "seats": 0, "cutoff": "CLOSED", "link": "https://www.sxccal.edu/"},
    {"name": "St. Xavier's College", "dept": "Microbiology", "seats": 5, "cutoff": "95%", "link": "https://www.sxccal.edu/"},
    {"name": "Scottish Church", "dept": "Chemistry", "seats": 15, "cutoff": "88%", "link": "https://www.scottishchurch.ac.in/"},
    {"name": "Heritage Institute", "dept": "CSE (B.Tech)", "seats": 40, "cutoff": "WBJEE Rank", "link": "https://www.heritageit.edu/"},
    {"name": "Techno India (Main)", "dept": "ECE", "seats": 60, "cutoff": "Direct/Rank", "link": "https://www.technoindiauniversity.ac.in/"},
    {"name": "IEM Kolkata", "dept": "BCA", "seats": 20, "cutoff": "Exam", "link": "https://iem.edu.in/"},
    {"name": "Bethune College", "dept": "English Hons", "seats": 10, "cutoff": "91%", "link": "http://www.bethunecollege.ac.in/"},
    {"name": "Asutosh College", "dept": "Zoology", "seats": 18, "cutoff": "87%", "link": "https://asutoshcollege.in/"},
    {"name": "Surendranath College", "dept": "General Science", "seats": 100, "cutoff": "70%", "link": "http://www.surendranathcollege.org/"},
    {"name": "City College", "dept": "Commerce", "seats": 50, "cutoff": "75%", "link": "http://www.citycollegekolkata.org/"},
    {"name": "Bangabasi College", "dept": "Arts", "seats": 80, "cutoff": "65%", "link": "https://bangabasi.ac.in/"}
  ],

  # --- SYLLABUS ---
  "syllabus_2025": [
    {"title": "Madhyamik 2025 Full Syllabus", "link": "https://wbbse.wb.gov.in"},
    {"title": "HS 2025 Science Syllabus", "link": "https://wbchse.nic.in"},
    {"title": "HS 2025 Arts Syllabus", "link": "https://wbchse.nic.in"},
    {"title": "HS 2025 Commerce Syllabus", "link": "https://wbchse.nic.in"}
  ]
}

def main(page: ft.Page):
    # 1. CONFIG
    page.title = "WB Nexus"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.spacing = 0
    page.theme = ft.Theme(color_scheme_seed="cyan", use_material3=True)

    # 2. LINK HANDLER
    def handle_link(e):
        if e.control.data: page.launch_url(e.control.data)

    # 3. BUILDERS
    def create_card(title, link, icon, color):
        return ft.Container(
            content=ft.Row([
                ft.Icon(icon, color=color, size=24),
                ft.Column([
                    ft.Text(title, weight="bold", size=14, color="white", width=200, no_wrap=True, overflow=ft.TextOverflow.ELLIPSIS),
                    ft.Text("Official PDF", size=11, color="grey"),
                ], expand=True, spacing=2),
                ft.IconButton(ft.icons.DOWNLOAD, icon_color=color, data=link, on_click=handle_link)
            ], alignment="spaceBetween"),
            bgcolor="#1f1f1f", padding=10, border_radius=12, margin=ft.margin.only(bottom=8),
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
            padding=15, margin=ft.margin.only(bottom=10), bgcolor="#252525", border_radius=15
        )

    # 4. PRE-BUILD VIEWS (Background)
    # We build these BEFORE showing them so there is no lag when clicking tabs
    views = {}
    
    # Books
    v = ft.Column(scroll="auto", padding=15)
    if "books_class_10" in DATABASE:
        for x in DATABASE["books_class_10"]: v.controls.append(create_card(x['title'], x['link'], ft.icons.BOOK, "orange"))
    views[0] = v

    # Papers (Placeholder if empty)
    views[1] = ft.Column([ft.Text("Papers coming soon...", color="grey")], padding=20)

    # Syllabus
    v = ft.Column(scroll="auto", padding=15)
    if "syllabus_2025" in DATABASE:
        for x in DATABASE["syllabus_2025"]: v.controls.append(create_card(x['title'], x['link'], ft.icons.LIST_ALT, "purple"))
    views[2] = v

    # Colleges
    v = ft.Column(scroll="auto", padding=15)
    if "colleges" in DATABASE:
        for x in DATABASE["colleges"]: v.controls.append(create_college_card(x))
    views[3] = v

    # 5. NAVIGATION LOGIC
    body = ft.Container(content=views[0], expand=True)

    def on_nav(e):
        body.content = views[e.control.selected_index]
        page.update()

    nav_bar = ft.NavigationBar(
        selected_index=0,
        on_change=on_nav,
        bgcolor="#0a0a0a",
        destinations=[
            ft.NavigationDestination(icon=ft.icons.BOOK, label="Books"),
            ft.NavigationDestination(icon=ft.icons.DESCRIPTION, label="Papers"),
            ft.NavigationDestination(icon=ft.icons.LIST, label="Syllabus"),
            ft.NavigationDestination(icon=ft.icons.SCHOOL, label="Colleges"),
        ]
    )

    header = ft.Container(
        content=ft.Row([ft.Icon(ft.icons.SHIELD_MOON, color="cyan"), ft.Text("WB NEXUS", size=22, weight="bold")], alignment="center"),
        padding=ft.padding.only(top=40, bottom=15), bgcolor="#0a0a0a"
    )

    # 6. APP LAUNCHER (THE FIX)
    def start_app():
        # Clear Splash
        page.clean()
        # Add Real App
        page.add(header, body, nav_bar)
        page.update()

    # Show Splash
    page.add(
        ft.Container(
            content=ft.Column([
                ft.ProgressRing(),
                ft.Text("Loading...")
            ], alignment="center", horizontal_alignment="center"),
            alignment=ft.alignment.center, expand=True
        )
    )
    
    # Wait 2 seconds in a SEPARATE THREAD, then run start_app
    # This prevents the UI from freezing
    timer = threading.Timer(2.0, start_app)
    timer.start()

if __name__ == "__main__":
    ft.app(target=main)
