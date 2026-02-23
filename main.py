import flet as ft

# --- 1. THE FULL DATABASE ---
DATABASE = {
    "books_class_8": [
        {"title": "Class 8 Science (Poribesh O Bigyan)", "link": "https://drive.google.com/file/d/18BUfpM6iwruuXPcOyNTpYpIsifrwypPN/view?usp=sharing"},
        {"title": "Class 8 Mathematics (Ganit Prabha)", "link": ""},
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

def main(page: ft.Page):
    # --- 1. CONFIG ---
    page.title = "WB Nexus"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = "auto"
    
    # --- 2. LINK LAUNCHER ---
    def open_link(e):
        url = e.control.data
        if url:
            page.launch_url(url)

    # --- 3. UI BUILDERS ---
    def create_card(title, link, icon_name, color):
        return ft.Container(
            content=ft.Row([
                ft.Icon(icon_name, color=color),
                ft.Column([
                    ft.Text(title, weight="bold", size=14, width=220, no_wrap=True, overflow=ft.TextOverflow.ELLIPSIS),
                    ft.Text("Tap to Open", size=10, color="grey")
                ]),
                ft.IconButton(ft.icons.OPEN_IN_NEW, icon_color="white", data=link, on_click=open_link)
            ], alignment="spaceBetween"),
            bgcolor="#1f1f1f", padding=10, border_radius=10, margin=ft.margin.only(bottom=5),
            on_click=open_link, data=link
        )

    def create_college_card(item):
        col = "green" if item['seats'] > 0 else "red"
        return ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Text(item['name'], weight="bold", size=16),
                    ft.Container(content=ft.Text(f"{item['seats']} SEATS", color="black", size=10), bgcolor=col, padding=5, border_radius=5)
                ]),
                ft.ElevatedButton("Apply", data=item['link'], on_click=open_link, height=30)
            ]),
            bgcolor="#252525", padding=10, border_radius=10, margin=ft.margin.only(bottom=10)
        )

    # --- 4. TABS ---
    # BOOKS TAB
    books_content = ft.Column(scroll="auto")
    for key in ["books_class_10", "books_class_9", "books_class_8"]:
        books_content.controls.append(ft.Text(key.replace("books_", "CLASS ").upper(), color="orange", weight="bold"))
        for item in DATABASE[key]:
            books_content.controls.append(create_card(item['title'], item['link'], ft.icons.BOOK, "orange"))

    # PAPERS TAB
    papers_content = ft.Column(scroll="auto")
    for key in ["papers_2024", "papers_2023", "papers_2022"]:
        papers_content.controls.append(ft.Text(key.replace("papers_", "YEAR ").upper(), color="cyan", weight="bold"))
        for item in DATABASE[key]:
            papers_content.controls.append(create_card(item['title'], item['link'], ft.icons.DESCRIPTION, "cyan"))

    # COLLEGE & SYLLABUS TABS
    college_content = ft.ListView([create_college_card(x) for x in DATABASE["colleges"]])
    syllabus_content = ft.ListView([create_card(x['title'], x['link'], ft.icons.LIST_ALT, "purple") for x in DATABASE["syllabus_2025"]])

    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(text="Books", icon=ft.icons.BOOK, content=books_content),
            ft.Tab(text="Papers", icon=ft.icons.DESCRIPTION, content=papers_content),
            ft.Tab(text="Colleges", icon=ft.icons.SCHOOL, content=college_content),
            ft.Tab(text="Syllabus", icon=ft.icons.LIST, content=syllabus_content),
        ],
        expand=1
    )

    # --- 5. LAYOUT ---
    page.add(
        ft.Container(
            content=ft.Text("WB NEXUS", size=25, weight="bold", color="cyan"),
            padding=20, alignment=ft.alignment.center
        ),
        tabs
    )
    page.update() # Forces the UI to draw on the phone

if __name__ == "__main__":
    ft.app(target=main)
