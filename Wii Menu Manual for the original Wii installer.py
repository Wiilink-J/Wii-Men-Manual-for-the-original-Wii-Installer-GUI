import os
import sys
import ssl
import subprocess
import urllib.request
import threading
import customtkinter as ctk

APP_TITLE = "Wii Menu Manual for the original Wii Installer - by Wii-J"

# Dizionario centralizzato con le traduzioni ufficiali (adattato alla nuova GUI a più pagine)
TEXTS = {
    "English": {
        "lang_page_title": "Select your language",
        "continue_btn": "Continue",
        "welcome_title": "Wii Menu Manual Installer",
        "welcome_text": "This program installs a patched version of the Electronic Manual for the Wii Menu, "
                         "for the original Wii console.",
        "start_btn": "Start",
        "installing_title": "Installing",
        "installing_text": "Installing the Wii Menu Manual... Please wait.",
        "success_title": "Success!",
        "success_text": "The channel has been installed successfully.",
        "close_btn": "Close",
        "open_folder_btn": "Open WAD folder",
        "error_dl": "An error occurred during installation. Please check your connection and try again.",
        "retry_btn": "Retry",
    },
    "Français": {
        "lang_page_title": "Sélectionnez votre langue",
        "continue_btn": "Continuer",
        "welcome_title": "Installateur du manuel du menu Wii",
        "welcome_text": "Ce programme installe une version corrigée du manuel électronique du menu Wii, "
                         "pour la console Wii originale.",
        "start_btn": "Démarrer",
        "installing_title": "Installation en cours",
        "installing_text": "Installation du manuel du menu Wii... Veuillez patienter.",
        "success_title": "Succès !",
        "success_text": "La chaîne a été installée avec succès.",
        "close_btn": "Fermer",
        "open_folder_btn": "Ouvrir le dossier WAD",
        "error_dl": "Une erreur s'est produite pendant l'installation. Veuillez vérifier votre connexion et réessayer.",
        "retry_btn": "Réessayer",
    },
    "Español": {
        "lang_page_title": "Selecciona tu idioma",
        "continue_btn": "Continuar",
        "welcome_title": "Instalador del manual del menú de Wii",
        "welcome_text": "Este programa instala una versión parcheada del manual electrónico del menú de Wii, "
                         "para la consola Wii original.",
        "start_btn": "Iniciar",
        "installing_title": "Instalando",
        "installing_text": "Instalando el manual del menú de Wii... Por favor espere.",
        "success_title": "¡Éxito!",
        "success_text": "El canal se ha instalado correctamente.",
        "close_btn": "Cerrar",
        "open_folder_btn": "Abrir carpeta WAD",
        "error_dl": "Se ha producido un error durante la instalación. Comprueba tu conexión e inténtalo de nuevo.",
        "retry_btn": "Reintentar",
    },
    "Nederlands": {
        "lang_page_title": "Selecteer uw taal",
        "continue_btn": "Doorgaan",
        "welcome_title": "Wii-menuhandleiding installatie",
        "welcome_text": "Dit programma installeert een gepatchte versie van de elektronische handleiding voor het "
                         "Wii-menu, voor de originele Wii-console.",
        "start_btn": "Starten",
        "installing_title": "Bezig met installeren",
        "installing_text": "De Wii-menuhandleiding wordt geïnstalleerd... Even geduld.",
        "success_title": "Gelukt!",
        "success_text": "Het kanaal is succesvol geïnstalleerd.",
        "close_btn": "Sluiten",
        "open_folder_btn": "WAD-map openen",
        "error_dl": "Er is een fout opgetreden tijdens de installatie. Controleer uw verbinding en probeer het opnieuw.",
        "retry_btn": "Opnieuw proberen",
    },
    "Italiano": {
        "lang_page_title": "Seleziona la tua lingua",
        "continue_btn": "Continua",
        "welcome_title": "Installer del manuale del menu Wii",
        "welcome_text": "Questo programma installa una versione modificata del manuale elettronico del menu Wii, "
                         "per la console Wii originale.",
        "start_btn": "Inizia",
        "installing_title": "Installazione in corso",
        "installing_text": "Installazione del manuale del menu Wii in corso... Attendere prego.",
        "success_title": "Successo!",
        "success_text": "Il canale è stato installato correttamente.",
        "close_btn": "Chiudi",
        "open_folder_btn": "Apri cartella WAD",
        "error_dl": "Si è verificato un errore durante l'installazione. Controlla la connessione e riprova.",
        "retry_btn": "Riprova",
    },
    "Deutsch": {
        "lang_page_title": "Wählen Sie Ihre Sprache",
        "continue_btn": "Weiter",
        "welcome_title": "Wii-Menü-Handbuch Installer",
        "welcome_text": "Dieses Programm installiert eine gepatchte Version des elektronischen Handbuchs für das "
                         "Wii-Menü, für die originale Wii-Konsole.",
        "start_btn": "Start",
        "installing_title": "Installation läuft",
        "installing_text": "Das Wii-Menü-Handbuch wird installiert... Bitte warten.",
        "success_title": "Erfolg!",
        "success_text": "Der Kanal wurde erfolgreich installiert.",
        "close_btn": "Schließen",
        "open_folder_btn": "WAD-Ordner öffnen",
        "error_dl": "Bei der Installation ist ein Fehler aufgetreten. Bitte überprüfen Sie Ihre Verbindung und versuchen Sie es erneut.",
        "retry_btn": "Erneut versuchen",
    },
    "Português": {
        "lang_page_title": "Selecione o seu idioma",
        "continue_btn": "Continuar",
        "welcome_title": "Instalador do manual do menu Wii",
        "welcome_text": "Este programa instala uma versão modificada do manual eletrônico do menu Wii, "
                         "para o console Wii original.",
        "start_btn": "Iniciar",
        "installing_title": "Instalando",
        "installing_text": "Instalando o manual do menu Wii... Por favor, aguarde.",
        "success_title": "Sucesso!",
        "success_text": "O canal foi instalado com sucesso.",
        "close_btn": "Fechar",
        "open_folder_btn": "Abrir pasta WAD",
        "error_dl": "Ocorreu um erro durante a instalação. Verifique sua conexão e tente novamente.",
        "retry_btn": "Tentar novamente",
    },
}

LANGUAGES = list(TEXTS.keys())

WAD_FOLDER_NAME = "WAD"
WAD_FILENAME = "Wii Menu Manual - HCAA.wad"
DOWNLOAD_URL = "https://archive.org/download/lv_0_20251206123726/Wii%20Menu%20Manual%20-%20HCAA.wad"


class WiiInstallerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Wii Menu Manual Installer")
        self.geometry("550x420")
        self.resizable(False, False)

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.current_lang = "English"

        # Contenitore che ospita tutte le pagine, sovrapposte tramite grid + tkraise
        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.pack(fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for PageClass in (LanguagePage, WelcomePage, InstallingPage, SuccessPage):
            frame = PageClass(self.container, self)
            self.frames[PageClass] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_page(LanguagePage)

    def show_page(self, page_class):
        frame = self.frames[page_class]
        if hasattr(frame, "refresh_texts"):
            frame.refresh_texts()
        frame.tkraise()

    def t(self, key):
        return TEXTS[self.current_lang][key]


class LanguagePage(ctk.CTkFrame):
    def __init__(self, parent, app: WiiInstallerApp):
        super().__init__(parent, fg_color="transparent")
        self.app = app

        self.title_label = ctk.CTkLabel(self, text=APP_TITLE, font=ctk.CTkFont(size=13, weight="bold"),
                                         wraplength=480, justify="center")
        self.title_label.pack(pady=(40, 20))

        self.lang_title_label = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=15, weight="bold"))
        self.lang_title_label.pack(pady=10)

        self.lang_menu = ctk.CTkOptionMenu(self, values=LANGUAGES, command=self.on_language_selected)
        self.lang_menu.set(self.app.current_lang)
        self.lang_menu.pack(pady=15)

        self.continue_btn = ctk.CTkButton(self, text="", command=self.go_next,
                                           font=ctk.CTkFont(size=13, weight="bold"))
        self.continue_btn.pack(pady=30)

    def on_language_selected(self, choice):
        self.app.current_lang = choice
        self.refresh_texts()

    def go_next(self):
        self.app.show_page(WelcomePage)

    def refresh_texts(self):
        self.lang_title_label.configure(text=self.app.t("lang_page_title"))
        self.continue_btn.configure(text=self.app.t("continue_btn"))


class WelcomePage(ctk.CTkFrame):
    def __init__(self, parent, app: WiiInstallerApp):
        super().__init__(parent, fg_color="transparent")
        self.app = app

        self.title_label = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=17, weight="bold"),
                                         wraplength=480, justify="center")
        self.title_label.pack(pady=(50, 20))

        self.welcome_label = ctk.CTkLabel(self, text="", wraplength=460, font=ctk.CTkFont(size=13),
                                           justify="center")
        self.welcome_label.pack(pady=20)

        self.start_btn = ctk.CTkButton(self, text="", command=self.go_next,
                                        font=ctk.CTkFont(size=14, weight="bold"), width=180, height=40)
        self.start_btn.pack(pady=40)

    def go_next(self):
        self.app.show_page(InstallingPage)

    def refresh_texts(self):
        self.title_label.configure(text=self.app.t("welcome_title"))
        self.welcome_label.configure(text=self.app.t("welcome_text"))
        self.start_btn.configure(text=self.app.t("start_btn"))


class InstallingPage(ctk.CTkFrame):
    def __init__(self, parent, app: WiiInstallerApp):
        super().__init__(parent, fg_color="transparent")
        self.app = app
        self._started = False

        self.title_label = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=17, weight="bold"))
        self.title_label.pack(pady=(60, 20))

        self.status_label = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=12), wraplength=460,
                                          justify="center")
        self.status_label.pack(pady=15)

        self.progress_bar = ctk.CTkProgressBar(self, width=350)
        self.progress_bar.pack(pady=15)
        self.progress_bar.set(0)

        self.retry_btn = ctk.CTkButton(self, text="", command=self.start_install,
                                        font=ctk.CTkFont(size=13, weight="bold"))
        # Il pulsante di retry viene mostrato solo in caso di errore

    def refresh_texts(self):
        self.title_label.configure(text=self.app.t("installing_title"))
        self.retry_btn.configure(text=self.app.t("retry_btn"))
        if not self._started:
            self.status_label.configure(text=self.app.t("installing_text"), text_color="#3B8ED0")
            self.progress_bar.set(0)
            self.retry_btn.pack_forget()
            self.start_install()

    def start_install(self):
        self._started = True
        self.retry_btn.pack_forget()
        self.status_label.configure(text=self.app.t("installing_text"), text_color="#3B8ED0")
        self.progress_bar.set(0)
        self.progress_bar.start()
        threading.Thread(target=self.execute_download, daemon=True).start()

    def execute_download(self):
        try:
            wad_dir = os.path.join(os.getcwd(), WAD_FOLDER_NAME)
            os.makedirs(wad_dir, exist_ok=True)
            destination_path = os.path.join(wad_dir, WAD_FILENAME)

            ssl_context = ssl._create_unverified_context()
            opener = urllib.request.build_opener(urllib.request.HTTPSHandler(context=ssl_context))
            opener.addheaders = [
                ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                               '(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'),
                ('Accept', '*/*'),
                ('Connection', 'keep-alive')
            ]
            urllib.request.install_opener(opener)

            # Scarica direttamente nella cartella WAD
            urllib.request.urlretrieve(DOWNLOAD_URL, destination_path)

            if os.path.exists(destination_path):
                self.after(0, self.on_success)
            else:
                raise Exception("File not found after download.")

        except Exception as e:
            self.after(0, lambda: self.on_error(str(e)))

    def on_success(self):
        self.progress_bar.stop()
        self.progress_bar.set(1)
        self._started = False
        self.app.show_page(SuccessPage)

    def on_error(self, error_details):
        self.progress_bar.stop()
        self.progress_bar.set(0)
        self._started = False
        msg = f"{self.app.t('error_dl')}\n\n{error_details}"
        self.status_label.configure(text=msg, text_color="red")
        self.retry_btn.pack(pady=15)


class SuccessPage(ctk.CTkFrame):
    def __init__(self, parent, app: WiiInstallerApp):
        super().__init__(parent, fg_color="transparent")
        self.app = app

        self.title_label = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=20, weight="bold"),
                                         text_color="green")
        self.title_label.pack(pady=(60, 20))

        self.text_label = ctk.CTkLabel(self, text="", wraplength=460, font=ctk.CTkFont(size=13),
                                        justify="center")
        self.text_label.pack(pady=15)

        self.buttons_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.buttons_frame.pack(pady=40)

        self.open_folder_btn = ctk.CTkButton(self.buttons_frame, text="", command=self.open_folder_and_close,
                                              font=ctk.CTkFont(size=13, weight="bold"), width=180)
        self.open_folder_btn.grid(row=0, column=0, padx=10)

        self.close_btn = ctk.CTkButton(self.buttons_frame, text="", command=self.app.destroy,
                                        font=ctk.CTkFont(size=13, weight="bold"), width=180,
                                        fg_color="gray40", hover_color="gray30")
        self.close_btn.grid(row=0, column=1, padx=10)

    def refresh_texts(self):
        self.title_label.configure(text=self.app.t("success_title"))
        self.text_label.configure(text=self.app.t("success_text"))
        self.open_folder_btn.configure(text=self.app.t("open_folder_btn"))
        self.close_btn.configure(text=self.app.t("close_btn"))

    def open_folder_and_close(self):
        wad_dir = os.path.join(os.getcwd(), WAD_FOLDER_NAME)
        try:
            if sys.platform.startswith("win"):
                os.startfile(wad_dir)
            elif sys.platform == "darwin":
                subprocess.Popen(["open", wad_dir])
            else:
                subprocess.Popen(["xdg-open", wad_dir])
        except Exception:
            pass
        self.app.destroy()


if __name__ == "__main__":
    app = WiiInstallerApp()
    app.mainloop()
