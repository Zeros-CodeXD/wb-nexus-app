import flet as ft
import requests
import threading
import json
import time

# --- 1. CONFIGURATION ---
DEFAULT_API_KEY = "AIzaSyBt0LXmELJ47vxrGQGz3q3VWAd2XC8TZ1g" 

# --- 2. THE MASTER DATABASE ---
DATABASE = {
  "books_hs": [
    {"title": "A Text Book of English (B) - Class 12", "link": "https://drive.google.com/file/d/1n7oZPsG83TpHLO4Riz47t1CDqkWaEt--/view?usp=sharing"},
    {"title": "Sahitya Chorcha (Bengali) - Class 12", "link": "https://drive.google.com/file/d/10yohNVzqZ_ITnOEzT4AhK5GNlJUwYm8v/view?usp=drive_link"},
    {"title": "Sahitya Chorcha (Bengali) - Class 11", "link": "https://drive.google.com/file/d/1sLUQVNCDE0xF5Myw4it94O8EmoLmfjmc/view?usp=drive_link"},
    {"title": "Bangalir Bhasha O Sanaskriti - Class 11", "link": "https://drive.google.com/file/d/1dUgC4Mck79Wo9a8gXnOJfL_E9LXrP22e/view?usp=drive_link"},
    {"title": "Rhapsody English (A) - Class 11 & 12", "link": "https://drive.google.com/file/d/1qvb5CVobsd3RMHJCqt5HiMoqOYB1fP-t/view?usp=drive_link"},
    {"title": "Sahitya Katha - Class 11 & 12", "link": "https://drive.google.com/file/d/13oE6xt5pOoIh7rmj9Zdmmj4hWzwnC-Ka/view?usp=drive_link"},
    {"title": "Mediscape (Medical Prep)", "link": "https://drive.google.com/file/d/1Dpo7rvUbMl2OPk6_4Mwg1tI6FVXkYu36/view?usp=drive_link"}
  ],
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
  "papers_2024": [
    {"title": "2024 Bengali Paper", "link": "https://drive.google.com/file/d/1cIMbMTMDD0uam_Dpgbw_Pwq3wxaMNoOI/view"},
    {"title": "2024 English Paper", "link": "https://drive.google.com/file/d/1Jy1Mje6v1VExMIs828UMIekf8m7NyXRu/view"},
    {"title": "2024 Math Paper", "link": "https://drive.google.com/file/d/1K21V1xGZEAFGXsGjojFzTo74KqpDFmC-/view"},
    {"title": "2024 Physical Science", "link": "https://drive.google.com/file/d/1isrdJmWektP7UNi4heeYF52jcuzHHFqF/view"},
    {"title": "2024 Life Science", "link": "https://drive.google.com/file/d/10uMrtr3cOujv_e07XkaliaEx16Gv9XGf/view"},
    {"title": "2024 History", "link": "https://drive.google.com/file/d/1i1C-plnjdPTpHN551J3xHlcxFzkHRQNE/view"},
    {"title": "2024 Geography", "link": "https://drive.google.com/file/d/1M3oyhEVcA_XW6_-X5L4l1eAhEJTPDh41/view"}
  ],
  "papers_2023": [
    {"title": "2023 Bengali Paper", "link": "https://drive.google.com/file/d/1Eijq8S0kYZG6pZK3cwoO5pcNcIxslH_W/view"},
    {"title": "2023 English Paper", "link": "https://drive.google.com/file/d/1XnGDf2ekn4ljc5LP4_kpRPFXkXrhDuHs/view"},
    {"title": "2023 Math Paper", "link": "https://drive.google.com/file/d/1q8ev-LLr6Ry7jwIWY3M3n3oO3V2rehx-/view"},
    {"title": "2023 Physical Science", "link": "https://drive.google.com/file/d/1GvH9M-sEWNIX9vDM2GOKmFx1OZyCHHlO/view"},
    {"title": "2023 Life Science", "link": "https://drive.google.com/file/d/1LywHj2UH2mc2qrJD4KPPKvYbsfwAOTYx/view"},
    {"title": "2023 History", "link": "https://drive.google.com/file/d/1LSiZV1yY4QtUPq8Xu8HWFxCDOpScnO7y/view"},
    {"title": "2023 Geography", "link": "https://drive.google.com/file/d/1shP3OooAaWdeoM2oAnxWR92TEw5uU3QF/view"}
  ],
  "papers_2022": [
    {"title": "2022 Bengali Paper", "link": "https://drive.google.com/file/d/1qiNdm9CJYefLZ-wF-qDLCQnMZNbR7ebU/view"},
    {"title": "2022 English Paper", "link": "https://drive.google.com/file/d/1vuK6W9evHONNvHmk2nUOxvIYw6BdCCtr/view"},
    {"title": "2022 Math Paper", "link": "https://drive.google.com/file/d/1XDwjyeTHDkRnXjJatqMjG-ZtFNEb3hBW/view"},
    {"title": "2022 Phy Sci", "link": "https://drive.google.com/file/d/1sYrcwl5gLVCNEFEcrR4QypBsBe78IQ9g/view"},
    {"title": "2022 Life Science", "link": "https://drive.google.com/file/d/1zNaUAAEklNCKYdv_dRny_gyfotg5eGOM/view"},
    {"title": "2022 History", "link": "https://drive.google.com/file/d/1ZW4c3u6-G9gPXbMxAO1MQk6-_kh9r05g/view"},
    {"title": "2022 Geography", "link": "https://drive.google.com/file/d/19QWjSKary4IXrv9Bwa0oyADDTXmc3dPA/view"}
  ],
  "colleges": [
    {"name": "Jadavpur University", "dept": "CSE / IT", "seats": 12, "cutoff": "98%", "link": "https://jadavpuruniversity.in/"},
    {"name": "Jadavpur University", "dept": "Physics Hons", "seats": 8, "cutoff": "94%", "link": "https://jadavpuruniversity.in/"},
    {"name": "Calcutta University", "dept": "B.Tech", "seats": 25, "cutoff": "90%", "link": "https://www.caluniv.ac.in/"},
    {"name": "Presidency Univ", "dept": "Economics", "seats": 0, "cutoff": "CLOSED", "link": "https://presiuniv.ac.in/"},
    {"name": "St. Xavier's College", "dept": "B.Com", "seats": 0, "cutoff": "CLOSED", "link": "https://www.sxccal.edu/"},
    {"name": "St. Xavier's College", "dept": "Microbiology", "seats": 5, "cutoff": "95%", "link": "https://www.sxccal.edu/"},
    {"name": "Scottish Church", "dept": "Chemistry", "seats": 15, "cutoff": "88%", "link": "https://www.scottishchurch.ac.in/"},
    {"name": "Heritage Institute", "dept": "CSE", "seats": 40, "cutoff": "WBJEE", "link": "https://www.heritageit.edu/"},
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

    # 2. CLICK-TO-START LOGIC
    def launch_app(e):
        try:
            page.clean()
            
            # --- GLOBAL STATE ---
            # Retrieve saved key or use default
            saved_key = page.client_storage.get("api_key")
            current_api_key = [saved_key if saved_key else DEFAULT_API_KEY]
            
            # Retrieve chat history
            saved_chats = page.client_storage.get("saved_chats") or []
            
            # Retrieve temp
            ai_temp = [page.client_storage.get("ai_temp") or 0.5]
            
            current_search = [""]
            current_tab = [0]
            
            # --- UTILS ---
            def handle_link(e):
                if e.control.data: page.launch_url(e.control.data)

            # --- CARD BUILDERS ---
            def create_card(title, link, icon, color):
                return ft.Container(
                    content=ft.Row([
                        ft.Container(content=ft.Icon(icon, color=color, size=24), padding=10, bgcolor=ft.colors.with_opacity(0.1, color), border_radius=10),
                        ft.Column([
                            ft.Text(title, weight="bold", size=14, color="white", width=140, no_wrap=True, overflow=ft.TextOverflow.ELLIPSIS),
                            ft.Text("Official PDF", size=10, color="grey"),
                        ], expand=True, spacing=2),
                        ft.IconButton(ft.icons.VISIBILITY, icon_color="grey", tooltip="View", data=link, on_click=handle_link),
                        ft.IconButton(ft.icons.DOWNLOAD_ROUNDED, icon_color=color, tooltip="Download", data=link, on_click=handle_link)
                    ], alignment="spaceBetween"),
                    bgcolor="#1a1a1a", padding=10, border_radius=15, margin=ft.margin.only(bottom=8),
                    shadow=ft.BoxShadow(spread_radius=0, blur_radius=5, color=ft.colors.with_opacity(0.3, "black")),
                    on_click=handle_link, data=link
                )

            def create_college_card(item):
                col = "green" if item.get('seats', 0) > 0 else "red"
                status = f"{item.get('seats', 0)} LEFT" if item.get('seats', 0) > 0 else "FULL"
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
                        ft.Divider(height=10, color="#333"),
                        ft.Row([
                            ft.Text(f"Cutoff: {item.get('cutoff', 'N/A')}", size=11, color="grey"),
                            ft.ElevatedButton("Apply", height=28, style=ft.ButtonStyle(bgcolor="blue", color="white"), 
                                              data=item['link'], on_click=handle_link)
                        ], alignment="spaceBetween")
                    ]),
                    padding=15, margin=ft.margin.only(bottom=10), bgcolor="#1a1a1a", border_radius=15,
                    shadow=ft.BoxShadow(spread_radius=0, blur_radius=5, color=ft.colors.with_opacity(0.3, "black"))
                )

            # --- AI LOGIC (FIXED 404 & STRUCTURE) ---
            def generate_ai_response(prompt, temp):
                try:
                    full_prompt = (
                        "You are a strict AI Tutor for West Bengal Board students (WBBSE/WBCHSE). "
                        "Your ONLY purpose is to answer educational questions, suggest topics, and help with exams. "
                        "If the user asks about ANYTHING else (movies, dating, politics, violence, jokes), "
                        "refuse by saying: 'I am an educational AI. I only discuss studies.' "
                        f"User Question: {prompt}"
                    )
                    
                    # URL structure for Gemini 1.5 Flash (Corrected)
                    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={current_api_key[0]}"
                    headers = {"Content-Type": "application/json"}
                    data = {
                        "contents": [{"parts": [{"text": full_prompt}]}], 
                        "generationConfig": {"temperature": temp}
                    }
                    
                    response = requests.post(url, headers=headers, json=data, timeout=15)
                    
                    if response.status_code == 200:
                        return response.json()['candidates'][0]['content']['parts'][0]['text']
                    else:
                        return f"API Error: {response.status_code} - {response.text}"
                except Exception as e:
                    return f"Connection Failed: {str(e)}"

            # --- AI UI COMPONENTS ---
            chat_list = ft.ListView(expand=True, spacing=15, padding=10)
            ai_input = ft.TextField(hint_text="Ask your AI Tutor...", expand=True, border_radius=20, 
                                    bgcolor="#222", border_width=0)
            
            def send_ai(e):
                q = ai_input.value
                if not q: return
                ai_input.value = ""
                
                # User Bubble
                chat_list.controls.append(ft.Container(
                    content=ft.Text(q, color="white"),
                    bgcolor="#333", padding=12, border_radius=ft.border_radius.only(12,12,0,12),
                    alignment=ft.alignment.center_right, margin=ft.margin.only(left=50)
                ))
                
                loading = ft.Text("Thinking...", color="cyan", italic=True)
                chat_list.controls.append(loading)
                page.update()

                def process():
                    res = generate_ai_response(q, ai_temp[0])
                    chat_list.controls.remove(loading)
                    chat_list.controls.append(ft.Container(
                        content=ft.Text(res, color="white", selectable=True),
                        bgcolor="#004d40", padding=12, border_radius=ft.border_radius.only(12,12,12,0),
                        margin=ft.margin.only(right=20)
                    ))
                    
                    # Auto-save session snippet
                    saved_chats.insert(0, {"title": q[:30], "content": res[:200]})
                    page.client_storage.set("saved_chats", saved_chats)
                    update_history_drawer() # Refresh drawer
                    page.update()

                threading.Thread(target=process).start()
            
            ai_input.on_submit = send_ai

            # --- DRAWERS ---
            
            # Left Drawer (Settings)
            def update_key(e):
                current_api_key[0] = e.control.value
                page.client_storage.set("api_key", e.control.value)
            
            def update_temp(e):
                ai_temp[0] = float(e.control.value)
                page.client_storage.set("ai_temp", ai_temp[0])

            left_drawer = ft.NavigationDrawer(
                controls=[
                    ft.Container(height=20),
                    ft.Text("Settings", size=20, weight="bold", color="cyan", text_align="center"),
                    ft.Divider(),
                    ft.Container(content=ft.Column([
                        ft.Text("API Key (Optional)", size=14),
                        ft.TextField(value=current_api_key[0], password=True, can_reveal_password=True, on_change=update_key, height=40, text_size=12),
                        ft.Container(height=10),
                        ft.Text("Creativity Level", size=14),
                        ft.Slider(min=0.0, max=1.0, divisions=10, value=ai_temp[0], on_change=update_temp),
                        ft.Text("Low = Strict | High = Creative", size=10, color="grey")
                    ]), padding=20)
                ], bgcolor="#111"
            )

            # Right Drawer (History)
            history_col = ft.Column()

            def delete_chat(idx):
                del saved_chats[idx]
                page.client_storage.set("saved_chats", saved_chats)
                update_history_drawer()
                page.update()

            def update_history_drawer():
                history_col.controls.clear()
                for i, chat in enumerate(saved_chats):
                    history_col.controls.append(
                        ft.Container(
                            content=ft.Row([
                                ft.Column([
                                    ft.Text(chat['title'], weight="bold", size=12, max_lines=1, overflow=ft.TextOverflow.ELLIPSIS),
                                    ft.Text(chat['content'][:40]+"...", size=10, color="grey")
                                ], expand=True),
                                ft.PopupMenuButton(
                                    items=[
                                        ft.PopupMenuItem(text="Delete", on_click=lambda _, x=i: delete_chat(x))
                                    ]
                                )
                            ]),
                            bgcolor="#222", padding=10, border_radius=5, margin=ft.margin.only(bottom=5)
                        )
                    )

            update_history_drawer() # Initial load

            right_drawer = ft.NavigationDrawer(
                controls=[
                    ft.Container(height=20),
                    ft.Text("Saved Chats", size=20, weight="bold", color="orange", text_align="center"),
                    ft.Divider(),
                    ft.Container(content=history_col, padding=10, expand=True)
                ], bgcolor="#111"
            )

            # --- AI VIEW LAYOUT ---
            ai_view = ft.Column([
                ft.Container(
                    content=ft.Row([
                        ft.IconButton(ft.icons.SETTINGS, icon_color="grey", on_click=lambda e: page.open_drawer(left_drawer)),
                        ft.Text("AI TUTOR", weight="bold", size=16, color="cyan"),
                        ft.IconButton(ft.icons.HISTORY, icon_color="grey", on_click=lambda e: page.open_end_drawer(right_drawer))
                    ], alignment="spaceBetween"),
                    padding=10, bgcolor="#111"
                ),
                ft.Container(content=chat_list, expand=True, padding=10),
                ft.Container(
                    content=ft.Row([ai_input, ft.IconButton(ft.icons.SEND_ROUNDED, icon_color="cyan", on_click=send_ai)]),
                    padding=10, bgcolor="#111"
                )
            ], expand=True)

            # --- DYNAMIC CONTENT LOADER ---
            body_content = ft.ListView(expand=True, padding=15, spacing=10)
            
            # Header Components (Search Bar)
            search_bar = ft.TextField(hint_text="Search...", prefix_icon=ft.icons.SEARCH, height=40, text_size=13, 
                                     border_radius=20, bgcolor="#222", border_width=0)
            
            # Top Header (Dynamic)
            header_row = ft.Row([
                ft.Icon(ft.icons.SHIELD_MOON, color="cyan", size=28),
                ft.Text("WB-NEXUS", size=22, weight="bold"),
                ft.IconButton(icon=ft.icons.INFO_OUTLINE, icon_color="grey") # Info dialog placeholder
            ], alignment="spaceBetween")

            header_container = ft.Container(
                content=ft.Column([header_row, search_bar]),
                padding=ft.padding.only(top=40, left=20, right=20, bottom=15),
                gradient=ft.LinearGradient(begin=ft.alignment.top_center, end=ft.alignment.bottom_center, colors=["#111", "#1a1a1a"]),
                border=ft.border.only(bottom=ft.border.BorderSide(1, "#333"))
            )

            def update_view():
                body_content.controls.clear()
                idx = current_tab[0]
                query = search_bar.value.lower() if search_bar.value else ""
                def match(text): return query in text.lower()

                if idx == 0: # Books
                    if "books_hs" in DATABASE:
                        if any(match(x['title']) for x in DATABASE["books_hs"]):
                            body_content.controls.append(ft.Text("HIGHER SECONDARY (11-12)", color="cyan", weight="bold"))
                            for x in DATABASE["books_hs"]: 
                                if match(x['title']): body_content.controls.append(create_card(x['title'], x['link'], ft.icons.BOOK, "cyan"))
                    for k in ["books_class_10", "books_class_9", "books_class_8"]:
                        if k in DATABASE:
                            if any(match(x['title']) for x in DATABASE[k]):
                                body_content.controls.append(ft.Text(k.replace("books_", "CLASS ").upper(), color="orange", weight="bold"))
                                for x in DATABASE[k]: 
                                    if match(x['title']): body_content.controls.append(create_card(x['title'], x['link'], ft.icons.BOOK, "orange"))

                elif idx == 1: # Papers
                    for k in ["papers_2024", "papers_2023", "papers_2022"]:
                        if k in DATABASE:
                            if any(match(x['title']) for x in DATABASE[k]):
                                body_content.controls.append(ft.Text(k.replace("papers_", "YEAR ").upper(), color="cyan", weight="bold"))
                                for x in DATABASE[k]: 
                                    if match(x['title']): body_content.controls.append(create_card(x['title'], x['link'], ft.icons.DESCRIPTION, "cyan"))

                elif idx == 2: # Syllabus
                    body_content.controls.append(ft.Text("LATEST SYLLABUS", color="purple", weight="bold"))
                    for x in DATABASE.get("syllabus_2025", []): 
                        if match(x['title']): body_content.controls.append(create_card(x['title'], x['link'], ft.icons.LIST_ALT, "purple"))

                elif idx == 3: # Colleges
                    body_content.controls.append(ft.Text("ADMISSION TRACKER", color="green", weight="bold"))
                    for x in DATABASE.get("colleges", []):
                        if match(x['name']) or match(x['dept']): body_content.controls.append(create_college_card(x))

                if not body_content.controls:
                    body_content.controls.append(ft.Text("No results found.", color="grey", italic=True))
                
                page.update()

            search_bar.on_change = lambda e: update_view()

            # --- NAVIGATION ---
            def on_nav(e):
                current_tab[0] = e.control.selected_index
                if e.control.selected_index == 4: # AI Tab
                    # HIDE SEARCH BAR for AI Tab
                    main_layout.content = ai_view
                    header_container.content.controls[1].visible = False # Hide search input
                else:
                    main_layout.content = body_content
                    header_container.content.controls[1].visible = True # Show search input
                    update_view()
                page.update()

            nav_bar = ft.NavigationBar(
                selected_index=0,
                on_change=on_nav,
                bgcolor="#111",
                destinations=[
                    ft.NavigationDestination(icon=ft.icons.BOOK, label="Books"),
                    ft.NavigationDestination(icon=ft.icons.DESCRIPTION, label="Papers"),
                    ft.NavigationDestination(icon=ft.icons.LIST, label="Syllabus"),
                    ft.NavigationDestination(icon=ft.icons.SCHOOL, label="Colleges"),
                    ft.NavigationDestination(icon=ft.icons.AUTO_AWESOME, label="AI Tutor"),
                ]
            )

            # Assemble
            main_layout = ft.Container(content=body_content, expand=True)
            update_view() 
            page.add(ft.Column([header_container, main_layout], expand=True, spacing=0), nav_bar)

        except Exception as err:
            page.clean()
            page.add(ft.Column([
                ft.Text("CRASH DETECTED", color="red", size=20, weight="bold"),
                ft.Text(f"Error: {str(err)}", color="white")
            ], alignment="center", horizontal_alignment="center"))

    # --- 3. STARTUP SCREEN ---
    start_btn = ft.Container(
        content=ft.Column([
            ft.Icon(name=ft.icons.SHIELD_MOON, size=100, color="cyan"),
            ft.Text("WB-NEXUS", size=35, weight="bold", color="white"),
            ft.Text("Your Academic Companion", size=14, color="grey"),
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
