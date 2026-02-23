import flet as ft
import json
import webbrowser
import os
import time

def main(page: ft.Page):
    # --- 1. CONFIG ---
    page.title = "WB Nexus"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.spacing = 0
    page.theme = ft.Theme(color_scheme_seed="cyan", use_material3=True)

    # --- ERROR LOGGING WIDGET (To see why it crashes) ---
    debug_text = ft.Text("Initializing...", color="red", size=12)
    
    # --- 2. DATABASE LOADING (ANDROID FIXED) ---
    database = {}
    
    try:
        # On Android/Flet, assets are usually relative to the root
        # We try two common paths
        possible_paths = ['assets/assets.json', 'assets.json']
        json_loaded = False
        
        for path in possible_paths:
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8') as f:
                    database = json.load(f)
                json_loaded = True
                debug_text.value = f"Loaded from: {path}"
                break
        
        if not json_loaded:
            debug_text.value = "ERROR: assets.json not found in APK bundle."
            
    except Exception as e:
        debug_text.value = f"CRASH: {str(e)}"

    # --- 3. UI COMPONENTS ---
    def handle_click(e):
        if e.control.data: webbrowser.open(e.control.data)

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

    # --- 4. DASHBOARD BUILDER ---
    def load_dashboard():
        # DO NOT use page.clean() immediately, or we lose the debug info if it crashes
        # Instead, we overwrite the content
        
        current_tab_index = [0]
        content_area = ft.Column(expand=True, scroll="auto", spacing=10)

        # Content Builder
        def update_list_view(search_query=""):
            content_area.controls.clear()
            
            # Debug info at top (Temporary)
            # content_area.controls.append(debug_text) 

            idx = current_tab_index[0]
            query = search_query.lower()
            def match(text): return query in text.lower()

            # TAB 0: BOOKS
            if idx == 0:
                keys = ["books_class_10", "books_class_9", "books_class_8"]
                found = False
                for k in keys:
                    if k in database:
                        found = True
                        filtered = [x for x in database[k] if match(x['title'])]
                        if filtered:
                            content_area.controls.append(ft.Text(k.replace("books_", "CLASS ").upper(), size=12, weight="bold", color="orange"))
                            for x in filtered: content_area.controls.append(create_card(x['title'], x['link'], ft.icons.BOOK, "orange"))
                if not found: content_area.controls.append(ft.Text("Database empty or not loaded.", color="red"))

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

            page.update()

        def on_search(e): update_list_view(e.control.value)
        def on_nav_change(e):
            current_tab_index[0] = e.control.selected_index
            update_list_view("")

        search_field = ft.TextField(
            prefix_icon=ft.icons.SEARCH,
            hint_text="Search resources...",
            text_size=12, height=40, border_radius=20, bgcolor="#222", border_width=0,
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

        page.clean()
        page.add(app_bar, ft.Container(content=content_area, expand=True, padding=20), nav)
        update_list_view("")

    # --- 5. SPLASH SCREEN (Simplified) ---
    # We removed the opacity animation because sometimes it causes black screen on low-end phones
    # We just show logo -> wait -> load
    
    logo_icon = ft.Icon(name=ft.icons.SHIELD_MOON, size=80, color="cyan")
    logo_text = ft.Text("WB NEXUS", size=30, weight="bold")
    
    splash = ft.Container(
        content=ft.Column([logo_icon, logo_text, debug_text], 
                        alignment="center", horizontal_alignment="center", spacing=10),
        alignment=ft.alignment.center, expand=True, bgcolor="#0a0a0a"
    )

    page.add(splash)
    
    # Wait a bit then load dashboard if no critical error
    # We use a thread so the UI doesn't freeze
    def transition_to_app():
        time.sleep(2)
        # Only load if database worked (or even if it didn't, show empty UI)
        load_dashboard()

    t = threading.Thread(target=transition_to_app)
    t.start()

if __name__ == "__main__":
    ft.app(target=main)
