import flet as ft
import requests
import threading

# --- 1. THE MASTER DATABASE ---
DATABASE = {
  # --- BOOKS ---
  "books_class_10": [
    {"title": "Sahitya Sanchayan (Bengali)", "link": "https://drive.google.com/file/d/1iQAADSemG8pJCG2phDGwGEdrpNGG1_9m/view"},
    {"title": "Bliss (English)", "link": "https://drive.google.com/file/d/1J8ACc0y2ftQ_wSjEqx-C0sA_d8ZjImkx/view"},
    {"title": "Ganit Prakash (Math)", "link": "https://drive.google.com/file/d/11TITkwOSGAFYSz015YStiaxUOUExTkfa/view"},
    {"title": "Koni (Rapid Reader)", "link": "https://drive.google.com/file/d/1jJ-YJIkSyYFG7bSt9Ui9RLfZDWApLKDp/view"}
  ],
  "books_class_9": [
    {"title": "Sahitya Sanchayan (Class 9)", "link": "https://drive.google.com/file/d/1W1iXt6ba7cKGXK06wU0PdDAP9yq_BNdI/view"},
    {"title": "Bliss (Class 9 English)", "link": "https://drive.google.com/file/d/1MJfjJt_9UrG04iMAanWz2izBx_RaBsgc/view"},
    {"title": "Ganit Prakash (Class 9)", "link": "https://drive.google.com/file/d/1bLVwDsYfENQPta5O6w6DQMOvFURorsJj/view"},
    {"title": "Aam Aatir Bhepu", "link": "https://drive.google.com/file/d/1LdJle7dtqQnfdds_0ENfj3a6KmWACqu-/view"}
  ],
  "books_class_8": [
    {"title": "Poribesh O Bigyan", "link": "https://drive.google.com/file/d/18BUfpM6iwruuXPcOyNTpYpIsifrwypPN/view"},
    {"title": "Blossoms", "link": "https://drive.google.com/file/d/1ETK2c1uJ802-hOiy0AsYHcmt8imEv_Fw/view"},
    {"title": "Sahitya Mela", "link": "https://drive.google.com/file/d/197KM-v4IG5Zq7SwebNJ1kXv4OuSCwVDF/view"},
    {"title": "Bhasha Charcha", "link": "https://drive.google.com/file/d/1oVPMJrl6iYGF_tYeIzCYpwRBpxd9vLg3/view"},
    {"title": "Pather Panchali", "link": "https://drive.google.com/file/d/1q_cJl8L5XLc96NZA2Cm5x9P_D52jIwNj/view"},
    {"title": "Atit O Aitihya", "link": "https://drive.google.com/file/d/1z9yFpVeblEDkqlOueifS5bOoL-It_y6t/view"},
    {"title": "Amader Prithibi", "link": "https://drive.google.com/file/d/117Pahy31xCyuCGBa_7y_G7OKIE01N4Ch/view"}
  ],
  "books_hs": [
    {"title": "A Text Book of English (B) - Class 12", "link": "https://drive.google.com/file/d/1n7oZPsG83TpHLO4Riz47t1CDqkWaEt--/view?usp=sharing"},
    {"title": "Sahitya Chorcha (Bengali) - Class 12", "link": "https://drive.google.com/file/d/10yohNVzqZ_ITnOEzT4AhK5GNlJUwYm8v/view?usp=drive_link"},
    {"title": "Sahitya Chorcha (Bengali) - Class 11", "link": "https://drive.google.com/file/d/1sLUQVNCDE0xF5Myw4it94O8EmoLmfjmc/view?usp=drive_link"},
    {"title": "Bangalir Bhasha O Sanaskriti - Class 11", "link": "https://drive.google.com/file/d/1dUgC4Mck79Wo9a8gXnOJfL_E9LXrP22e/view?usp=drive_link"},
    {"title": "Rhapsody English (A) - Class 11 & 12", "link": "https://drive.google.com/file/d/1qvb5CVobsd3RMHJCqt5HiMoqOYB1fP-t/view?usp=drive_link"},
    {"title": "Sahitya Katha - Class 11 & 12", "link": "https://drive.google.com/file/d/13oE6xt5pOoIh7rmj9Zdmmj4hWzwnC-Ka/view?usp=drive_link"},
    {"title": "Mediscape (Medical Prep)", "link": "https://drive.google.com/file/d/1Dpo7rvUbMl2OPk6_4Mwg1tI6FVXkYu36/view?usp=drive_link"}
  ],
  
  # --- PAPERS ---
  "papers_2024": [
    {"title": "2024 Bengali", "link": "https://drive.google.com/file/d/1cIMbMTMDD0uam_Dpgbw_Pwq3wxaMNoOI/view"},
    {"title": "2024 English", "link": "https://drive.google.com/file/d/1Jy1Mje6v1VExMIs828UMIekf8m7NyXRu/view"},
    {"title": "2024 Math", "link": "https://drive.google.com/file/d/1K21V1xGZEAFGXsGjojFzTo74KqpDFmC-/view"},
    {"title": "2024 Phy Sci", "link": "https://drive.google.com/file/d/1isrdJmWektP7UNi4heeYF52jcuzHHFqF/view"},
    {"title": "2024 Life Sci", "link": "https://drive.google.com/file/d/10uMrtr3cOujv_e07XkaliaEx16Gv9XGf/view"},
    {"title": "2024 History", "link": "https://drive.google.com/file/d/1i1C-plnjdPTpHN551J3xHlcxFzkHRQNE/view"},
    {"title": "2024 Geography", "link": "https://drive.google.com/file/d/1M3oyhEVcA_XW6_-X5L4l1eAhEJTPDh41/view"}
  ],
  "papers_2023": [
    {"title": "2023 Bengali", "link": "https://drive.google.com/file/d/1Eijq8S0kYZG6pZK3cwoO5pcNcIxslH_W/view"},
    {"title": "2023 English", "link": "https://drive.google.com/file/d/1XnGDf2ekn4ljc5LP4_kpRPFXkXrhDuHs/view"},
    {"title": "2023 Math", "link": "https://drive.google.com/file/d/1q8ev-LLr6Ry7jwIWY3M3n3oO3V2rehx-/view"},
    {"title": "2023 Phy Sci", "link": "https://drive.google.com/file/d/1GvH9M-sEWNIX9vDM2GOKmFx1OZyCHHlO/view"},
    {"title": "2023 Life Sci", "link": "https://drive.google.com/file/d/1LywHj2UH2mc2qrJD4KPPKvYbsfwAOTYx/view"},
    {"title": "2023 History", "link": "https://drive.google.com/file/d/1LSiZV1yY4QtUPq8Xu8HWFxCDOpScnO7y/view"},
    {"title": "2023 Geography", "link": "https://drive.google.com/file/d/1shP3OooAaWdeoM2oAnxWR92TEw5uU3QF/view"}
  ],
  "papers_2022": [
    {"title": "2022 Bengali", "link": "https://drive.google.com/file/d/1qiNdm9CJYefLZ-wF-qDLCQnMZNbR7ebU/view"},
    {"title": "2022 English", "link": "https://drive.google.com/file/d/1vuK6W9evHONNvHmk2nUOxvIYw6BdCCtr/view"},
    {"title": "2022 Math", "link": "https://drive.google.com/file/d/1XDwjyeTHDkRnXjJatqMjG-ZtFNEb3hBW/view"},
    {"title": "2022 Phy Sci", "link": "https://drive.google.com/file/d/1sYrcwl5gLVCNEFEcrR4QypBsBe78IQ9g/view"},
    {"title": "2022 Life Sci", "link": "https://drive.google.com/file/d/1zNaUAAEklNCKYdv_dRny_gyfotg5eGOM/view"},
    {"title": "2022 History", "link": "https://drive.google.com/file/d/1ZW4c3u6-G9gPXbMxAO1MQk6-_kh9r05g/view"},
    {"title": "2022 Geography", "link": "https://drive.google.com/file/d/19QWjSKary4IXrv9Bwa0oyADDTXmc3dPA/view"}
  ],
  "colleges": [
    {"name": "Jadavpur Univ", "dept": "Science", "seats": 15, "cutoff": "98%", "link": "https://jadavpuruniversity.in/"},
    {"name": "Jadavpur Univ", "dept": "Engineering", "seats": 12, "cutoff": "WBJEE < 100", "link": "https://jadavpuruniversity.in/"},
    {"name": "Calcutta Univ", "dept": "B.Tech", "seats": 25, "cutoff": "90%", "link": "https://www.caluniv.ac.in/"},
    {"name": "Presidency Univ", "dept": "Arts", "seats": 0, "cutoff": "CLOSED", "link": "https://presiuniv.ac.in/"},
    {"name": "St. Xavier's", "dept": "Microbio", "seats": 5, "cutoff": "95%", "link": "https://www.sxccal.edu/"},
    {"name": "St. Xavier's", "dept": "B.Com", "seats": 0, "cutoff": "CLOSED", "link": "https://www.sxccal.edu/"},
    {"name": "Scottish Church", "dept": "Chemistry", "seats": 15, "cutoff": "88%", "link": "https://www.scottishchurch.ac.in/"},
    {"name": "Heritage Inst", "dept": "B.Tech", "seats": 40, "cutoff": "WBJEE", "link": "https://www.heritageit.edu/"},
    {"name": "Techno India", "dept": "ECE", "seats": 60, "cutoff": "Direct", "link": "https://www.technoindiauniversity.ac.in/"},
    {"name": "IEM Kolkata", "dept": "BCA", "seats": 20, "cutoff": "Exam", "link": "https://iem.edu.in/"},
    {"name": "Bethune College", "dept": "English", "seats": 10, "cutoff": "91%", "link": "http://www.bethunecollege.ac.in/"},
    {"name": "Asutosh College", "dept": "Zoology", "seats": 18, "cutoff": "87%", "link": "https://asutoshcollege.in/"},
    {"name": "Surendranath", "dept": "General Sci", "seats": 100, "cutoff": "70%", "link": "http://www.surendranathcollege.org/"},
    {"name": "City College", "dept": "Commerce", "seats": 50, "cutoff": "75%", "link": "http://www.citycollegekolkata.org/"},
    {"name": "Bangabasi College", "dept": "Arts", "seats": 80, "cutoff": "65%", "link": "https://bangabasi.ac.in/"}
  ],
  "syllabus_2025": [
    {"title": "Madhyamik 2025 Syllabus", "link": "https://wbbse.wb.gov.in"},
    {"title": "HS 2025 Science Syllabus", "link": "https://wbchse.nic.in"},
    {"title": "HS 2025 Arts Syllabus", "link": "https://wbchse.nic.in"},
    {"title": "HS 2025 Commerce Syllabus", "link": "https://wbchse.nic.in"}
  ]
}

def main(page: ft.Page):
    # 1. CONFIG
    page.title = "WB-NEXUS"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.spacing = 0
    page.theme = ft.Theme(color_scheme_seed="cyan", use_material3=True)

    # --- 2. CLICK-TO-START LOGIC ---
    def launch_app(e):
        page.clean()
        
        # UTILS
        def handle_link(e):
            if e.control.data: page.launch_url(e.control.data)

        # UI: Resource Card
        def create_card(title, link, icon, color):
            return ft.Container(
                content=ft.Row([
                    ft.Container(
                        content=ft.Icon(icon, color=color, size=24),
                        padding=10, 
                        bgcolor=ft.colors.with_opacity(0.1, color), 
                        border_radius=10
                    ),
                    ft.Column([
                        ft.Text(title, weight="bold", size=14, color="white", width=140, no_wrap=True, overflow=ft.TextOverflow.ELLIPSIS),
                        ft.Text("WB Official", size=10, color="grey"),
                    ], expand=True, spacing=2),
                    
                    # VIEW ICON (Eye)
                    ft.IconButton(ft.icons.VISIBILITY, icon_color="grey", tooltip="View", data=link, on_click=handle_link),
                    # DOWNLOAD ICON (Arrow)
                    ft.IconButton(ft.icons.DOWNLOAD_ROUNDED, icon_color=color, tooltip="Download", data=link, on_click=handle_link)
                ], alignment="spaceBetween"),
                bgcolor="#1f1f1f", padding=10, border_radius=12, margin=ft.margin.only(bottom=8)
            )

        # UI: College Card
        def create_college_card(item):
            col = "green" if item.get('seats', 0) > 0 else "red"
            status = f"{item.get('seats', 0)} SEATS" if item.get('seats', 0) > 0 else "FULL"
            return ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Column([
                            ft.Text(item['name'], weight="bold", size=15),
                            ft.Text(item.get('dept', ''), size=11, color="cyan")
                        ], expand=True),
                        ft.Container(content=ft.Text(status, size=10, weight="bold", color="black"), 
                                     bgcolor=col, padding=5, border_radius=5)
                    ]),
                    ft.Divider(height=5, color="#333"),
                    ft.Row([
                        ft.Text(f"Cutoff: {item.get('cutoff', 'N/A')}", size=11, color="grey"),
                        ft.ElevatedButton("Apply", height=25, style=ft.ButtonStyle(bgcolor="blue", color="white"), 
                                          data=item['link'], on_click=handle_link)
                    ], alignment="spaceBetween")
                ]),
                padding=15, margin=ft.margin.only(bottom=10), bgcolor="#1a1a1a", border_radius=15, border=ft.border.all(1, "#333")
            )

        # --- AI LOGIC (LIGHTWEIGHT) ---
        def generate_ai_response(prompt):
            try:
                full_prompt = (
                    "You are a strict AI Tutor for West Bengal Board students (WBBSE/WBCHSE). "
                    "Your ONLY purpose is to answer educational questions. "
                    "If the user asks about ANYTHING else (movies, dating, politics, violence), "
                    "refuse by saying: 'I am an educational AI. I only discuss studies.' "
                    f"User Question: {prompt}"
                )
                
                url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
                params = {"key": "AIzaSyBt0LXmELJ47vxrGQGz3q3VWAd2XC8TZ1g"} # API KEY
                headers = {"Content-Type": "application/json"}
                data = {"contents": [{"parts": [{"text": full_prompt}]}]}
                
                response = requests.post(url, headers=headers, params=params, json=data)
                
                if response.status_code == 200:
                    return response.json()['candidates'][0]['content']['parts'][0]['text']
                else:
                    return "Error: AI Service Unavailable."
            except Exception as e:
                return f"Error: Check Internet Connection."

        chat_history = ft.Column(scroll="auto", expand=True, spacing=15)
        
        def send_ai(e):
            q = ai_input.value
            if not q: return
            ai_input.value = ""
            
            # User Bubble (Right)
            chat_history.controls.append(
                ft.Container(
                    content=ft.Text(q, color="white"),
                    bgcolor="#333", padding=12, border_radius=ft.border_radius.only(12,12,0,12),
                    alignment=ft.alignment.center_right, margin=ft.margin.only(left=50)
                )
            )
            
            loading = ft.Text("Thinking...", color="cyan", italic=True)
            chat_history.controls.append(loading)
            page.update()

            def process():
                res = generate_ai_response(q)
                chat_history.controls.remove(loading)
                # AI Bubble (Left)
                chat_history.controls.append(
                    ft.Container(
                        content=ft.Markdown(res, selectable=True),
                        bgcolor="#004d40", border=ft.border.all(1, "cyan"),
                        padding=12, border_radius=ft.border_radius.only(12,12,12,0),
                        margin=ft.margin.only(right=20)
                    )
                )
                page.update()

            threading.Thread(target=process).start()

        ai_input = ft.TextField(hint_text="Ask your AI Tutor...", expand=True, border_radius=20, 
                                bgcolor="#222", border_width=0, on_submit=send_ai)

        ai_view = ft.Column([
            ft.Container(content=chat_history, expand=True, padding=10),
            ft.Container(
                content=ft.Row([ai_input, ft.IconButton(ft.icons.SEND_ROUNDED, icon_color="cyan", on_click=send_ai)]),
                padding=10, bgcolor="#111"
            )
        ], expand=True)


        # --- MAIN BODY CONTAINER ---
        body = ft.Container(expand=True)

        # --- DYNAMIC CONTENT LOADER ---
        def load_tab_content(idx):
            # We build the list ONLY when the tab is clicked to prevent memory overload
            content_list = ft.ListView(expand=True, padding=15, spacing=5)

            if idx == 0: # Books
                if "books_hs" in DATABASE:
                    content_list.controls.append(ft.Text("CLASS 11-12 (HS)", color="cyan", weight="bold"))
                    for x in DATABASE["books_hs"]: content_list.controls.append(create_card(x['title'], x['link'], ft.icons.BOOK, "cyan"))
                for k in ["books_class_10", "books_class_9", "books_class_8"]:
                    if k in DATABASE:
                        content_list.controls.append(ft.Text(k.replace("books_", "CLASS ").upper(), color="orange", weight="bold"))
                        for x in DATABASE[k]: content_list.controls.append(create_card(x['title'], x['link'], ft.icons.BOOK, "orange"))
            
            elif idx == 1: # Papers
                for k in ["papers_2024", "papers_2023", "papers_2022"]:
                    if k in DATABASE:
                        content_list.controls.append(ft.Text(k.replace("papers_", "YEAR ").upper(), color="cyan", weight="bold"))
                        for x in DATABASE[k]: content_list.controls.append(create_card(x['title'], x['link'], ft.icons.DESCRIPTION, "cyan"))

            elif idx == 2: # Syllabus
                content_list.controls.append(ft.Text("LATEST SYLLABUS", color="purple", weight="bold"))
                for x in DATABASE.get("syllabus_2025", []): content_list.controls.append(create_card(x['title'], x['link'], ft.icons.LIST_ALT, "purple"))

            elif idx == 3: # Colleges
                content_list.controls.append(ft.Text("ADMISSION TRACKER", color="green", weight="bold"))
                for x in DATABASE.get("colleges", []): content_list.controls.append(create_college_card(x))
            
            return content_list

        def on_nav(e):
            idx = e.control.selected_index
            if idx == 4: # AI Tab
                body.content = ai_view
            else:
                body.content = load_tab_content(idx)
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
                ft.NavigationDestination(icon=ft.icons.AUTO_AWESOME, label="AI Tutor"),
            ]
        )

        header = ft.Container(
            content=ft.Row([ft.Icon(ft.icons.SHIELD_MOON, color="cyan", size=28), ft.Text("WB-NEXUS", size=22, weight="bold")], alignment="center"),
            padding=ft.padding.only(top=40, bottom=15), bgcolor="#0a0a0a",
            border=ft.border.only(bottom=ft.border.BorderSide(1, "#222"))
        )

        # Initial Load (Books)
        body.content = load_tab_content(0)

        page.add(ft.Column([header, body], expand=True, spacing=0), nav_bar)
        page.update()

    # --- 3. STARTUP SCREEN (SAFE) ---
    start_btn = ft.Container(
        content=ft.Column([
            ft.Icon(name=ft.icons.SHIELD_MOON, size=100, color="cyan"),
            ft.Text("WB-NEXUS", size=35, weight="bold", color="white"),
            ft.Text("Student Portal", size=14, color="grey"),
            ft.Container(height=40),
            ft.ElevatedButton("ENTER APP", on_click=launch_app, height=50, width=200, 
                              style=ft.ButtonStyle(bgcolor="cyan", color="black"))
        ], alignment="center", horizontal_alignment="center"),
        alignment=ft.alignment.center,
        expand=True,
        bgcolor="#0a0a0a"
    )

    page.add(start_btn)

if __name__ == "__main__":
    ft.app(target=main)
