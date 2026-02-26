import flet as ft

# --- 1. THE CLEANED DATABASE ---
DATABASE = {
  # --- BOOKS CLASS 10 ---
  "books_class_10": [
    {"title": "Sahitya Sanchayan (Bengali)", "link": "https://drive.google.com/file/d/1iQAADSemG8pJCG2phDGwGEdrpNGG1_9m/view"},
    {"title": "Bliss (English)", "link": "https://drive.google.com/file/d/1J8ACc0y2ftQ_wSjEqx-C0sA_d8ZjImkx/view"},
    {"title": "Ganit Prakash (Math)", "link": "https://drive.google.com/file/d/11TITkwOSGAFYSz015YStiaxUOUExTkfa/view"},
    {"title": "Koni (Rapid Reader)", "link": "https://drive.google.com/file/d/1jJ-YJIkSyYFG7bSt9Ui9RLfZDWApLKDp/view"}
  ],
  # --- BOOKS CLASS 9 ---
  "books_class_9": [
    {"title": "Sahitya Sanchayan (Class 9)", "link": "https://drive.google.com/file/d/1W1iXt6ba7cKGXK06wU0PdDAP9yq_BNdI/view"},
    {"title": "Bliss (Class 9 English)", "link": "https://drive.google.com/file/d/1MJfjJt_9UrG04iMAanWz2izBx_RaBsgc/view"},
    {"title": "Ganit Prakash (Class 9)", "link": "https://drive.google.com/file/d/1bLVwDsYfENQPta5O6w6DQMOvFURorsJj/view"},
    {"title": "Aam Aatir Bhepu (Rapid)", "link": "https://drive.google.com/file/d/1LdJle7dtqQnfdds_0ENfj3a6KmWACqu-/view"}
  ],
  # --- BOOKS CLASS 8 (Kept Full as requested initially) ---
  "books_class_8": [
    {"title": "Poribesh O Bigyan", "link": "https://drive.google.com/file/d/18BUfpM6iwruuXPcOyNTpYpIsifrwypPN/view"},
    {"title": "Blossoms", "link": "https://drive.google.com/file/d/1ETK2c1uJ802-hOiy0AsYHcmt8imEv_Fw/view"},
    {"title": "Sahitya Mela", "link": "https://drive.google.com/file/d/197KM-v4IG5Zq7SwebNJ1kXv4OuSCwVDF/view"},
    {"title": "Bhasha Charcha", "link": "https://drive.google.com/file/d/1oVPMJrl6iYGF_tYeIzCYpwRBpxd9vLg3/view"},
    {"title": "Pather Panchali", "link": "https://drive.google.com/file/d/1q_cJl8L5XLc96NZA2Cm5x9P_D52jIwNj/view"},
    {"title": "Atit O Aitihya", "link": "https://drive.google.com/file/d/1z9yFpVeblEDkqlOueifS5bOoL-It_y6t/view"},
    {"title": "Amader Prithibi", "link": "https://drive.google.com/file/d/117Pahy31xCyuCGBa_7y_G7OKIE01N4Ch/view"}
  ],
  
  # --- PAPERS ---
  "papers_2024": [
    {"title": "2024 Bengali Paper", "link": "https://drive.google.com/file/d/1cIMbMTMDD0uam_Dpgbw_Pwq3wxaMNoOI/view"},
    {"title": "2024 English Paper", "link": "https://drive.google.com/file/d/1Jy1Mje6v1VExMIs828UMIekf8m7NyXRu/view"},
    {"title": "2024 Math Paper", "link": "https://drive.google.com/file/d/1K21V1xGZEAFGXsGjojFzTo74KqpDFmC-/view"},
    {"title": "2024 Phy Sci", "link": "https://drive.google.com/file/d/1isrdJmWektP7UNi4heeYF52jcuzHHFqF/view"},
    {"title": "2024 Life Sci", "link": "https://drive.google.com/file/d/10uMrtr3cOujv_e07XkaliaEx16Gv9XGf/view"},
    {"title": "2024 History", "link": "https://drive.google.com/file/d/1i1C-plnjdPTpHN551J3xHlcxFzkHRQNE/view"},
    {"title": "2024 Geography", "link": "https://drive.google.com/file/d/1M3oyhEVcA_XW6_-X5L4l1eAhEJTPDh41/view"}
  ],
  "papers_2023": [
    {"title": "2023 Bengali Paper", "link": "https://drive.google.com/file/d/1Eijq8S0kYZG6pZK3cwoO5pcNcIxslH_W/view"},
    {"title": "2023 English Paper", "link": "https://drive.google.com/file/d/1XnGDf2ekn4ljc5LP4_kpRPFXkXrhDuHs/view"},
    {"title": "2023 Math Paper", "link": "https://drive.google.com/file/d/1q8ev-LLr6Ry7jwIWY3M3n3oO3V2rehx-/view"},
    {"title": "2023 Phy Sci", "link": "https://drive.google.com/file/d/1GvH9M-sEWNIX9vDM2GOKmFx1OZyCHHlO/view"},
    {"title": "2023 Life Sci", "link": "https://drive.google.com/file/d/1LywHj2UH2mc2qrJD4KPPKvYbsfwAOTYx/view"},
    {"title": "2023 History", "link": "https://drive.google.com/file/d/1LSiZV1yY4QtUPq8Xu8HWFxCDOpScnO7y/view"},
    {"title": "2023 Geography", "link": "https://drive.google.com/file/d/1shP3OooAaWdeoM2oAnxWR92TEw5uU3QF/view"}
  ],
  "papers_2022": [
    {"title": "2022 Bengali Paper", "link": "https://drive.google.com/file/d/1qiNdm9CJYefLZ-wF-qDLCQnMZNbR7ebU/view"},
    {"title": "2022 English Paper", "link": "https://drive.google.com/file/d/1vuK6W9evHONNvHmk2nUOxvIYw6BdCCtr/view"},
    {"title": "2022 Math Paper", "link": "https://drive.google.com/file/d/1XDwjyeTHDkRnXjJatqMjG-ZtFNEb3hBW/view"},
    {"title": "2022 Phy Sci", "link": "https://drive.google.com/file/d/1sYrcwl5gLVCNEFEcrR4QypBsBe78IQ9g/view"},
    {"title": "2022 Life Sci", "link": "https://drive.google.com/file/d/1zNaUAAEklNCKYdv_dRny_gyfotg5eGOM/view"},
    {"title": "2022 History", "link": "https://drive.google.com/file/d/1ZW4c3u6-G9gPXbMxAO1MQk6-_kh9r05g/view"},
    {"title": "2022 Geography", "link": "https://drive.google.com/file/d/19QWjSKary4IXrv9Bwa0oyADDTXmc3dPA/view"}
  ],
  "colleges": [
    {"name": "Jadavpur Univ", "dept": "Science (B.Sc)", "seats": 15, "cutoff": "98%", "link": "https://jadavpuruniversity.in/"},
    {"name": "Jadavpur Univ", "dept": "Engineering (CSE)", "seats": 12, "cutoff": "WBJEE < 100", "link": "https://jadavpuruniversity.in/"},
    {"name": "Calcutta Univ", "dept": "B.Tech", "seats": 25, "cutoff": "90%", "link": "https://www.caluniv.ac.in/"},
    {"name": "Presidency Univ", "dept": "Arts (BA)", "seats": 0, "cutoff": "CLOSED", "link": "https://presiuniv.ac.in/"},
    {"name": "St. Xavier's", "dept": "Microbiology", "seats": 5, "cutoff": "95%", "link": "https://www.sxccal.edu/"},
    {"name": "St. Xavier's", "dept": "B.Com", "seats": 0, "cutoff": "CLOSED", "link": "https://www.sxccal.edu/"},
    {"name": "Scottish Church", "dept": "Chemistry", "seats": 15, "cutoff": "88%", "link": "https://www.scottishchurch.ac.in/"},
    {"name": "Heritage Inst", "dept": "B.Tech", "seats": 40, "cutoff": "WBJEE", "link": "https://www.heritageit.edu/"},
    {"name": "Techno India", "dept": "ECE", "seats": 60, "cutoff": "Direct", "link": "https://www.technoindiauniversity.ac.in/"}
  ],
  "syllabus_2025": [
    {"title": "Madhyamik 2025 Syllabus", "link": "https://wbbse.wb.gov.in"},
    {"title": "HS 2025 Science Syllabus", "link": "https://wbchse.nic.in"},
    {"title": "HS 2025 Arts Syllabus", "link": "https://wbchse.nic.in"}
  ]
}

def main(page: ft.Page):
    # --- 1. CONFIG ---
    page.title = "WB-NEXUS"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.spacing = 0
    page.theme = ft.Theme(color_scheme_seed="cyan", use_material3=True)

    # --- 2. LINK OPENER ---
    def open_link(e):
        if e.control.data: page.launch_url(e.control.data)

    # --- 3. UI GENERATORS ---
    # These create the cards but DO NOT add them to the page yet.
    
    def create_book_card(item):
        return ft.Container(
            content=ft.Row([
                ft.Icon(ft.icons.BOOK, color="orange"),
                ft.Column([
                    ft.Text(item['title'], weight="bold", size=14, width=160, no_wrap=True, overflow=ft.TextOverflow.ELLIPSIS),
                    ft.Text("Official PDF", size=10, color="grey")
                ], expand=True, spacing=2),
                ft.IconButton(ft.icons.VISIBILITY, icon_color="white", data=item['link'], on_click=open_link),
                ft.IconButton(ft.icons.DOWNLOAD, icon_color="orange", data=item['link'], on_click=open_link)
            ], alignment="spaceBetween"),
            bgcolor="#1f1f1f", padding=10, border_radius=12, margin=ft.margin.only(bottom=5)
        )

    def create_paper_card(item):
        return ft.Container(
            content=ft.Row([
                ft.Icon(ft.icons.DESCRIPTION, color="cyan"),
                ft.Column([
                    ft.Text(item['title'], weight="bold", size=14, width=160, no_wrap=True, overflow=ft.TextOverflow.ELLIPSIS),
                    ft.Text("Previous Year", size=10, color="grey")
                ], expand=True, spacing=2),
                ft.IconButton(ft.icons.DOWNLOAD, icon_color="cyan", data=item['link'], on_click=open_link)
            ], alignment="spaceBetween"),
            bgcolor="#1f1f1f", padding=10, border_radius=12, margin=ft.margin.only(bottom=5)
        )

    def create_college_card(item):
        seats = item.get('seats', 0)
        col = "green" if seats > 0 else "red"
        status = f"{seats} LEFT" if seats > 0 else "FULL"
        return ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Column([ft.Text(item['name'], weight="bold", size=14), ft.Text(item.get('dept', ''), size=11, color="cyan")]),
                    ft.Container(content=ft.Text(status, size=10, color="black"), bgcolor=col, padding=5, border_radius=5)
                ], alignment="spaceBetween"),
                ft.Divider(height=5, color="#333"),
                ft.ElevatedButton("Check", height=30, style=ft.ButtonStyle(bgcolor="blue", color="white"), data=item['link'], on_click=open_link)
            ]),
            padding=10, margin=ft.margin.only(bottom=5), bgcolor="#1a1a1a", border_radius=12, border=ft.border.all(1, "#333")
        )

    def create_syllabus_card(item):
        return ft.Container(
            content=ft.Row([
                ft.Icon(ft.icons.LIST_ALT, color="purple"),
                ft.Text(item['title'], weight="bold", size=14, expand=True),
                ft.IconButton(ft.icons.DOWNLOAD, icon_color="purple", data=item['link'], on_click=open_link)
            ]),
            bgcolor="#1f1f1f", padding=10, border_radius=12, margin=ft.margin.only(bottom=5)
        )

    # --- 4. DYNAMIC PAGE LOADER (THE FIX) ---
    # We do NOT build everything at once. We build only what is requested.
    
    body = ft.Container(expand=True) # Empty container to start

    def change_tab(e):
        idx = e.control.selected_index
        
        # Load Books (Default)
        if idx == 0:
            content = ft.ListView(expand=True, padding=10, spacing=5)
            for k in ["books_class_10", "books_class_9", "books_class_8"]:
                if k in DATABASE:
                    content.controls.append(ft.Text(k.replace("books_", "CLASS ").upper(), color="orange", weight="bold"))
                    for x in DATABASE[k]: content.controls.append(create_book_card(x))
            body.content = content

        # Load Papers
        elif idx == 1:
            content = ft.ListView(expand=True, padding=10, spacing=5)
            for k in ["papers_2024", "papers_2023", "papers_2022"]:
                if k in DATABASE:
                    content.controls.append(ft.Text(k.replace("papers_", "YEAR ").upper(), color="cyan", weight="bold"))
                    for x in DATABASE[k]: content.controls.append(create_paper_card(x))
            body.content = content

        # Load Syllabus
        elif idx == 2:
            content = ft.ListView(expand=True, padding=10, spacing=5)
            content.controls.append(ft.Text("OFFICIAL SYLLABUS", color="purple", weight="bold"))
            for x in DATABASE.get("syllabus_2025", []): content.controls.append(create_syllabus_card(x))
            body.content = content
        
        # Load Colleges
        elif idx == 3:
            content = ft.ListView(expand=True, padding=10, spacing=5)
            content.controls.append(ft.Text("ADMISSION TRACKER", color="green", weight="bold"))
            for x in DATABASE.get("colleges", []): content.controls.append(create_college_card(x))
            body.content = content

        page.update()

    # --- 5. LAUNCHER LOGIC ---
    def launch_app(e):
        page.clean()
        
        # Header
        header = ft.Container(
            content=ft.Row([ft.Icon(ft.icons.SHIELD_MOON, color="cyan"), ft.Text("WB-NEXUS", size=20, weight="bold")]),
            padding=ft.padding.only(top=40, left=20, bottom=10), bgcolor="#0a0a0a",
            border=ft.border.only(bottom=ft.border.BorderSide(1, "#222"))
        )

        # Nav
        nav = ft.NavigationBar(
            selected_index=0,
            on_change=change_tab,
            bgcolor="#0a0a0a",
            destinations=[
                ft.NavigationDestination(icon=ft.icons.BOOK, label="Books"),
                ft.NavigationDestination(icon=ft.icons.DESCRIPTION, label="Papers"),
                ft.NavigationDestination(icon=ft.icons.LIST, label="Syllabus"),
                ft.NavigationDestination(icon=ft.icons.SCHOOL, label="Colleges"),
            ]
        )

        # Initial Load (Books)
        # We manually trigger the logic for Tab 0
        content = ft.ListView(expand=True, padding=10, spacing=5)
        for k in ["books_class_10", "books_class_9", "books_class_8"]:
            if k in DATABASE:
                content.controls.append(ft.Text(k.replace("books_", "CLASS ").upper(), color="orange", weight="bold"))
                for x in DATABASE[k]: content.controls.append(create_book_card(x))
        body.content = content

        page.add(ft.Column([header, body], expand=True, spacing=0), nav)

    # --- 6. START SCREEN ---
    start_btn = ft.Container(
        content=ft.Column([
            ft.Icon(name=ft.icons.SHIELD_MOON, size=100, color="cyan"),
            ft.Text("WB-NEXUS", size=35, weight="bold", color="white"),
            ft.Text("Student Portal", size=14, color="grey"),
            ft.Container(height=40),
            ft.ElevatedButton("ENTER APP", on_click=launch_app, height=50, width=200, 
                              style=ft.ButtonStyle(bgcolor="cyan", color="black"))
        ], alignment="center", horizontal_alignment="center"),
        alignment=ft.alignment.center, expand=True, bgcolor="#0a0a0a"
    )

    page.add(start_btn)

if __name__ == "__main__":
    ft.app(target=main)
