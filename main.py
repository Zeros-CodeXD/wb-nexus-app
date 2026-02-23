import flet as ft
import json
import webbrowser
import os
import time
import threading

def main(page: ft.Page):
    # --- 1. APP CONFIGURATION ---
    page.title = "WB Nexus"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.spacing = 0
    page.window_width = 400
    page.window_height = 800
    
    # Modern Material 3 Theme
    page.theme = ft.Theme(color_scheme_seed="cyan", use_material3=True)

    # --- 2. DATABASE (ANDROID COMPATIBLE) ---
    database = {}
    
    # On Android, Flet automatically maps the 'assets' folder to the root
    # So we just ask for 'assets/assets.json'
    json_path = 'assets/assets.json'

    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            database = json.load(f)
    except Exception as e:
        # If that fails (sometimes happens on PC debug), try absolute path
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            abs_path = os.path.join(script_dir, 'assets', 'assets.json')
            with open(abs_path, 'r', encoding='utf-8') as f:
                database = json.load(f)
        except:
            pass

    # --- 3. UTILITY FUNCTIONS ---
    def handle_click(e):
        if e.control.data: webbrowser.open(e.control.data)

    # --- 4. COMPONENT: RESOURCE CARD (Books/Papers/Syllabus) ---
    def create_card(title, link, icon_name, color):
        return ft.Container(
            content=ft.Row([
                ft.Container(
                    content=ft.Icon(icon_name, color=color, size=24),
                    padding=10, bgcolor=ft.colors.with_opacity(0.1, color), border_radius=10
                ),
                ft.Column([
                    ft.Text(title, size=14, weight="bold", max_lines=1, overflow="ellipsis", color="white"),
                    ft.Text("Official PDF", size=11, color="grey"),
                ], expand=True, spacing=2),
                ft.IconButton(ft.icons.VISIBILITY, icon_color="white", data=link, on_click=handle_click),
                ft.IconButton(ft.icons.DOWNLOAD, icon_color=color, data=link, on_click=handle_click)
            ], alignment="spaceBetween"),
            padding=10, margin=ft.margin.only(bottom=5),
            bgcolor="#1f1f1f", border_radius=12
        )

    # --- 5. COMPONENT: COLLEGE CARD ---
    def create_college_card(item):
        status_col = "green" if item['seats'] > 0 else "red"
        status_text = f"{item['seats']} SEATS" if item['seats'] > 0 else "FULL"

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
                    ft.ElevatedButton("Apply", height=30, style=ft.ButtonStyle(color="white", bgcolor="blue"), 
                                      data=item['link'], on_click=handle_click)
                ], alignment="spaceBetween")
            ]),
            padding=15, margin=ft.margin.only(bottom=10), bgcolor="#252525", border_radius=15
        )

    # --- 6. COMPONENT: NOTIFICATION BANNER ---
    def create_notification():
        # You can add a "notification" key to your assets.json later to make this dynamic
        # For now, we hardcode a sample alert
        news_text = "📢 UPDATE: Madhyamik 2025 Routine Released! Check Syllabus."
        news_link = "https://wbbse.wb.gov.in"
        
        return ft.Container(
            content=ft.Row([
                ft.Icon(ft.icons.CAMPAIGN, color="black"),
                ft.Text(news_text, color="black", weight="bold", size=12, expand=True),
                ft.Icon(ft.icons.ARROW_FORWARD, color="black", size=16)
            ]),
            bgcolor="amber",
            padding=10,
            border_radius=8,
            margin=ft.margin.only(bottom=15),
            on_click=lambda e: webbrowser.open(news_link)
        )

    # --- 7. MAIN DASHBOARD LOGIC ---
    def load_dashboard():
        page.clean()
        
        current_tab_index = [0]
        content_area = ft.Column(expand=True, scroll="auto", spacing=10)

        # --- CONTENT BUILDER ---
        def update_list_view(search_query=""):
            content_area.controls.clear()
            
            # 1. ALWAYS ADD NOTIFICATION AT THE TOP
            content_area.controls.append(create_notification())
            
            idx = current_tab_index[0]
            query = search_query.lower()
            def match(text): return query in text.lower()

            # TAB 0: BOOKS
            if idx == 0:
                keys = ["books_class_10", "books_class_9", "books_class_8"]
                for k in keys:
                    if k in database:
                        filtered = [x for x in database[k] if match(x['title'])]
                        if filtered:
                            content_area.controls.append(ft.Text(k.replace("books_", "CLASS ").upper(), size=12, weight="bold", color="orange"))
                            for x in filtered: content_area.controls.append(create_card(x['title'], x['link'], ft.icons.BOOK, "orange"))

            # TAB 1: PAPERS
            elif idx == 1:
                keys = ["papers_2024", "papers_2023", "papers_2022"]
                for k in keys:
                    if k in database:
                        filtered = [x for x in database[k] if match(x['title'])]
                        if filtered:
                            content_area.controls.append(ft.Text(k.replace("papers_", "YEAR ").upper(), size=12, weight="bold", color="cyan"))
                            for x in filtered: content_area.controls.append(create_card(x['title'], x['link'], ft.icons.DESCRIPTION, "cyan"))

            # TAB 2: SYLLABUS
            elif idx == 2:
                if "syllabus_2025" in database:
                    filtered = [x for x in database["syllabus_2025"] if match(x['title'])]
                    if filtered:
                        content_area.controls.append(ft.Text("OFFICIAL SYLLABUS", size=12, weight="bold", color="purple"))
                        for x in filtered: content_area.controls.append(create_card(x['title'], x['link'], ft.icons.LIST_ALT, "purple"))

            # TAB 3: COLLEGES
            elif idx == 3:
                if "colleges" in database:
                    filtered = [x for x in database["colleges"] if match(x['name']) or match(x['stream'])]
                    if filtered:
                        content_area.controls.append(ft.Text("SEARCH RESULTS", size=12, weight="bold", color="green"))
                        for x in filtered: content_area.controls.append(create_college_card(x))

            # Empty State
            if len(content_area.controls) == 1: # Only notification exists
                content_area.controls.append(ft.Text("No results found.", color="grey", italic=True))
            
            page.update()

        # --- EVENTS ---
        def on_search(e): update_list_view(e.control.value)
        
        def on_nav_change(e):
            current_tab_index[0] = e.control.selected_index
            search_field.value = ""
            update_list_view("")

        # --- UI LAYOUT ---
        search_field = ft.TextField(
            prefix_icon=ft.icons.SEARCH,
            hint_text="Search resources...",
            text_size=12,
            height=40,
            border_radius=20,
            bgcolor="#222",
            border_width=0,
            on_change=on_search
        )

        app_bar = ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Icon(ft.icons.SHIELD, color="cyan", size=30),
                    ft.Text("WB NEXUS", size=22, weight="bold")
                ]),
                search_field
            ]),
            padding=ft.padding.only(left=20, right=20, top=40, bottom=10),
            bgcolor="#111"
        )

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

        update_list_view("")
        page.add(app_bar, ft.Container(content=content_area, expand=True, padding=20), nav)

    # --- 8. SPLASH SCREEN ---
    def run_splash_sequence():
        logo_icon = ft.Icon(name=ft.icons.SHIELD_MOON, size=0, color="cyan")
        logo_text = ft.Text("WB NEXUS", size=0, weight="bold", opacity=0)
        sub_text = ft.Text("Your Academic Companion", size=12, color="grey", opacity=0)

        splash = ft.Container(
            content=ft.Column([logo_icon, logo_text, sub_text], 
                            alignment="center", horizontal_alignment="center", spacing=10),
            alignment=ft.alignment.center, expand=True, bgcolor="#0a0a0a"
        )

        page.add(splash)
        page.update()

        time.sleep(0.5)
        logo_icon.size = 80; logo_icon.update()
        time.sleep(0.3)
        logo_text.size = 30; logo_text.opacity = 1; logo_text.update()
        sub_text.opacity = 1; sub_text.update()
        time.sleep(1.5)
        splash.opacity = 0; splash.animate_opacity = 500; splash.update()
        time.sleep(0.5)
        
        load_dashboard()

    run_splash_sequence()

if __name__ == "__main__":

    ft.app(target=main)
