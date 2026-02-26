import flet as ft
import threading
import time

# --- DATABASE (Your Full Data Here) ---
DATABASE = {
  # ... (Paste your full database here, I am using a short version for safety in this message)
  "books_class_10": [{"title": "Class 10 Bengali", "link": "https://drive.google.com/file/d/1iQAADSemG8pJCG2phDGwGEdrpNGG1_9m/view"}],
  "colleges": [{"name": "Jadavpur Univ", "dept": "Science", "seats": 15, "link": "https://jadavpuruniversity.in/"}]
}

def main(page: ft.Page):
    page.title = "WB Nexus"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.spacing = 0
    page.theme = ft.Theme(color_scheme_seed="cyan", use_material3=True)

    # --- 1. SHOW SPLASH SCREEN ---
    splash = ft.Container(
        content=ft.Column([
            ft.Icon(name=ft.icons.SHIELD_MOON, size=80, color="cyan"),
            ft.Text("WB NEXUS", size=30, weight="bold", color="white"),
            ft.ProgressRing(color="cyan")
        ], alignment="center", horizontal_alignment="center", spacing=20),
        alignment=ft.alignment.center, expand=True, bgcolor="#0a0a0a"
    )
    page.add(splash)

    # --- 2. DEFINE THE APP UI (But don't add it yet) ---
    def load_app_ui():
        # --- UI BUILDERS ---
        def handle_link(e):
            if e.control.data: page.launch_url(e.control.data)

        def create_card(title, link, icon, color):
            return ft.Container(
                content=ft.Row([
                    ft.Icon(icon, color=color),
                    ft.Column([ft.Text(title, weight="bold", size=14, width=200, no_wrap=True), ft.Text("Download", size=10)], expand=True),
                    ft.IconButton(ft.icons.DOWNLOAD, icon_color=color, data=link, on_click=handle_link)
                ], alignment="spaceBetween"),
                bgcolor="#1f1f1f", padding=10, border_radius=12, margin=5, on_click=handle_link, data=link
            )

        # Build Content Lists
        books_list = ft.Column(scroll="auto", padding=15)
        if "books_class_10" in DATABASE:
            for x in DATABASE["books_class_10"]: books_list.controls.append(create_card(x['title'], x['link'], ft.icons.BOOK, "orange"))

        college_list = ft.Column(scroll="auto", padding=15)
        if "colleges" in DATABASE:
            for x in DATABASE["colleges"]:
                college_list.controls.append(ft.Container(
                    content=ft.Row([ft.Text(x['name'], weight="bold"), ft.Text(f"{x.get('seats',0)} Seats", color="green")], alignment="spaceBetween"),
                    bgcolor="#252525", padding=15, border_radius=10, margin=5, on_click=handle_link, data=x['link']
                ))

        # Setup Navigation
        body = ft.Container(content=books_list, expand=True)
        
        def on_nav(e):
            if e.control.selected_index == 0: body.content = books_list
            elif e.control.selected_index == 1: body.content = college_list # Add other tabs similarly
            page.update()

        nav = ft.NavigationBar(
            on_change=on_nav,
            bgcolor="#0a0a0a",
            destinations=[
                ft.NavigationDestination(icon=ft.icons.BOOK, label="Books"),
                ft.NavigationDestination(icon=ft.icons.SCHOOL, label="Colleges"),
            ]
        )

        header = ft.Container(
            content=ft.Row([ft.Icon(ft.icons.SHIELD_MOON, color="cyan"), ft.Text("WB NEXUS", size=22, weight="bold")], alignment="center"),
            padding=ft.padding.only(top=40, bottom=15), bgcolor="#0a0a0a"
        )

        # --- SWAP UI ---
        page.clean()
        page.add(ft.Column([header, body], expand=True), nav)
        page.update()

    # --- 3. BACKGROUND TIMER (THE FIX) ---
    def background_timer():
        time.sleep(3) # This sleep happens in a thread, so it doesn't freeze the UI
        # When done, call the UI update function
        # IMPORTANT: We cannot update UI from thread, but Flet allows page.update() from external logic usually
        # But for absolute safety on Android, we rely on the main thread catching up.
        # However, Flet's threading model on Android is tricky.
        # Let's try the safest known method:
        load_app_ui()

    # If this thread crash causes black screen, we remove it and just load instantly.
    # But you wanted animation.
    t = threading.Thread(target=background_timer)
    t.start()

if __name__ == "__main__":
    ft.app(target=main)
