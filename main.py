import flet as ft

# --- FULL INTEGRATED DATABASE ---
DATABASE = {
    "books_class_8": [
        {"title": "Class 8 Science (Poribesh O Bigyan)", "link": "https://drive.google.com/file/d/18BUfpM6iwruuXPcOyNTpYpIsifrwypPN/view?usp=sharing"},
        {"title": "Class 8 Mathematics (Ganit Prabha)", "link": "https://wbbse.wb.gov.in"},
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
        {"title": "Madhyamik 2024 - Bengali", "link": "https://drive.google.com/file/d/1cIMbMTMDD0uam_Dpgbw_Pwq3wxaMNoOI/view?usp=sharing"},
        {"title": "Madhyamik 2024 - English", "link": "https://drive.google.com/file/d/1Jy1Mje6v1VExMIs828UMIekf8m7NyXRu/view?usp=sharing"},
        {"title": "Madhyamik 2024 - Math", "link": "https://drive.google.com/file/d/1K21V1xGZEAFGXsGjojFzTo74KqpDFmC-/view?usp=sharing"}
    ],
    "colleges": [
        {"title": "Jadavpur University", "link": "https://jadavpuruniversity.in/"},
        {"title": "Presidency University", "link": "https://presiuniv.ac.in/"}
    ],
    "syllabus_2025": [
        {"title": "Madhyamik 2025 Syllabus", "link": "https://wbbse.wb.gov.in"}
    ]
}

def main(page: ft.Page):
    page.title = "WB-NEXUS"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.padding = 20

    def open_link(e):
        if e.control.data:
            page.launch_url(e.control.data)

    # UI Header
    container = ft.Column(spacing=20, expand=True)
    container.controls.append(
        ft.Text("WB-NEXUS", size=32, weight="bold", color="orange")
    )

    # Build List from Database
    for section_key, items in DATABASE.items():
        display_name = section_key.replace("_", " ").upper()
        container.controls.append(ft.Text(display_name, size=18, weight="bold", color="blue"))
        
        for item in items:
            container.controls.append(
                ft.Container(
                    content=ft.ListTile(
                        leading=ft.Icon(ft.icons.CHEVRON_RIGHT, color="orange"),
                        title=ft.Text(item["title"], size=14),
                        subtitle=ft.Text("View Document", size=12, color="grey"),
                        on_click=open_link,
                        data=item["link"],
                    ),
                    bgcolor="#1e1e1e",
                    border_radius=12,
                )
            )

    page.add(container)

if __name__ == "__main__":
    ft.app(target=main)
