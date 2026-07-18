# Wii Menu Manual for Original Wii Installer

This software lets you install a patched, custom version of the Wii Menu Manual made specifically for the original Wii. Since manuals already existed for the Wii mini and vWii, this project reimagines how a manual for the original Wii would look.

### 🌍 Language Support
* **Program (.exe):** Available in 7 languages (English, Spanish, French, German, Dutch, Italian, and Portuguese). More languages will be added as compatibility extends.
* **Manual:** Fully tailored in 7 languages (English, Spanish, French, German, Dutch, Italian, and Portuguese). Other languages currently retain the vWii interface (which includes bugs) and will be updated in future releases.

### 🎮 Features & Compatibility
* **Universal:** Works on all types of Wii consoles and the Dolphin emulator.
* **Safe Installation:** Features a unique Channel ID (`HCAA`). It will **not** overwrite or conflict with vWii, Wii mini, or other existing manual versions on your console.
* **Size:** Requires 297 blocks.
* **Removable:** Can be easily deleted anytime via Wii Options > Channels.

---

## 📖 How to Use the Installer

1. Open the `.exe` file (or run the `.py` script if on non-x64 Windows/Mac/Linux).
2. Follow the on-screen instructions provided by the program.
3. Find your patched `.wad` file inside the generated `WAD` folder.

---

## 🛠️ Installation & Requirements

> [!IMPORTANT]
> **Windows x64 Users (Windows 10/11):** You can directly run the GUI `.exe` file.
> **Other Operating Systems:** If you use 32-bit Windows, macOS, or Linux, download the `.py` version and follow the terminal setup below.

---

### 🪟 Windows (32-bit / x32)

1. Download and install Python from the official website.
   *(Make sure to check the box **"Add python.exe to PATH"** during installation).*
2. Open the **Command Prompt** (search for `cmd` in the Windows start menu).
3. Install the required library:
   ```bash
   pip install customtkinter
   ```
4. Run the app by double-clicking `Wii_Menu_Manual_for_the_original_Wii_installer.py` or typing:
   ```bash
   python "Wii_Menu_Manual_for_the_original_Wii_installer.py"
   ```

---

### 🍎 macOS (Mac)

1. Open the **Terminal** (press `Cmd + Space`, type `Terminal`, and press `Enter`).
2. Install the required library:
   ```bash
   pip3 install customtkinter
   ```
   *(Note: If `pip3` or `python3` is missing, install Python from the official website first).*
3. Run the app by typing:
   ```bash
   python3 "Wii_Menu_Manual_for_the_original_Wii_installer.py"
   ```

---

### 🐧 Linux (Ubuntu, Debian, Mint, etc.)

Linux systems usually have Python pre-installed but lack `pip` and `tkinter` graphical support by default.

1. Open the **Terminal** (`Ctrl + Alt + T`).
2. Install the required system components:
   ```bash
   sudo apt update && sudo apt install python3-pip python3-tk -y
   ```
3. Install the required library:
   ```bash
   pip3 install customtkinter
   ```
4. Run the app by typing:
   ```bash
   python3 "Wii_Menu_Manual_for_the_original_Wii_installer.py"
   ```

---

## 🕊️ A Personal Note

Even though I surely did a good job with this, I want to say to others that life isn't just this. Being creative is fine, but it doesn't have to become an addiction. The only one who can give us real peace and joy is God, and He loved so much the world that He gave His only Son Jesus. Real life is more than these consoles. That's why I rarely use all of this, because I know there's a world to discover and to live as a gift of God. This message is an expression of faith, not to convince others. 

### 📖 John 3:16-17
> ¹⁶ *For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life.*  
> ¹⁷ *For God did not send his Son into the world to condemn the world, but to save the world through him.*
