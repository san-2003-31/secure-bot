import tkinter as tk
from tkinter import messagebox, scrolledtext
import re
import random
import string

# ---------------- PROJECT DATA ----------------
PROJECT_TITLE = "SECURE-BOT: BCA EDITION"
PROJECT_VERSION = "v3.1.0"
UNIQUE_ID = "SEC-BCA-2024-X7"

# UI COLORS
BG_DARK = "#1e1e2e"
BG_LIGHT = "#2a2a3d"
ACCENT = "#00ff41"
TEXT_COLOR = "#ffffff"
BOT_MSG_COLOR = "#a6adbb"

# ---------------- LOGIC ----------------

def analyze_strength(password):
    score = 0
    remarks = []

    if len(password) >= 12:
        score += 1
    else:
        remarks.append("Too short")

    if re.search(r"\d", password):
        score += 1
    else:
        remarks.append("Needs numbers")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        remarks.append("Needs uppercase")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        remarks.append("Needs symbols")

    results = ["DANGER 🛑", "WEAK ⚠️", "MODERATE 🆗", "STRONG ✅", "SECURE 💎"]
    return results[score], remarks


def show_bot_menu():
    return (
        "Welcome User 👋\n"
        "I am SecureBot – an AI-based Password Security Assistant.\n\n"
        "AVAILABLE COMMANDS:\n"
        "• check <password>\n"
        "• generate\n"
        "• advantages\n"
        "• difference\n"
        "• why strength\n"
        "• help\n"
        "• about"
    )


def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    if any(word in user_input for word in ["hi", "hello", "start"]):
        return show_bot_menu()

    if "help" in user_input:
        return (
            "HELP MENU:\n"
            "1. check <password> – Analyze password strength\n"
            "2. generate – Generate secure password\n"
            "3. advantages – Project benefits\n"
            "4. difference – Compare with normal checkers\n"
            "5. why strength – Why password security matters\n"
            "6. about – Project details"
        )

    if "about" in user_input:
        return (
            "PROJECT OVERVIEW:\n"
            "Secure-Bot is a chatbot-based cybersecurity project\n"
            "that analyzes and generates strong passwords.\n\n"
            "Technologies Used:\n"
            "• Python\n"
            "• Tkinter GUI\n"
            "• Cybersecurity rules"
        )

    if "advantages" in user_input:
        return (
            "ADVANTAGES:\n"
            "✔ Chatbot interaction\n"
            "✔ Real-time password checking\n"
            "✔ Secure password generation\n"
            "✔ User-friendly UI\n"
            "✔ Cybersecurity focused"
        )

    if "difference" in user_input:
        return (
            "DIFFERENCE:\n\n"
            "NORMAL CHECKER:\n"
            "• Checks only length\n"
            "• No interaction\n\n"
            "SECURE-BOT:\n"
            "• Chatbot-based\n"
            "• Explains weaknesses\n"
            "• Generates strong passwords"
        )

    if "why strength" in user_input:
        return (
            "WHY PASSWORD STRENGTH IS IMPORTANT:\n"
            "• Prevents hacking\n"
            "• Stops brute-force attacks\n"
            "• Protects user data\n"
            "• Ensures online safety"
        )

    if user_input.startswith("check "):
        pwd = user_input.replace("check ", "").strip()
        result, notes = analyze_strength(pwd)
        suggestion = "Suggestions: " + ", ".join(notes) if notes else "Perfect password security!"
        return f"ANALYSIS RESULT:\nRating: {result}\n{suggestion}"

    if "generate" in user_input:
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        pwd = ''.join(random.SystemRandom().choice(chars) for _ in range(16))
        return f"SECURE PASSWORD GENERATED:\n{pwd}"

    return "Command not recognized. Press ENTER for menu or type 'help'."

# ---------------- UI FUNCTIONS ----------------

def insert_to_chat(sender, message, color):
    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, f"{sender}: ", "sender")
    chat_display.insert(tk.END, f"{message}\n\n", "msg")
    chat_display.tag_config("sender", foreground=ACCENT, font=("Courier", 10, "bold"))
    chat_display.tag_config("msg", foreground=color, font=("Courier", 10))
    chat_display.config(state=tk.DISABLED)
    chat_display.see(tk.END)


def on_send(event=None):
    msg = user_entry.get().strip()

    # ENTER pressed without typing anything → show menu
    if not msg:
        insert_to_chat("BOT", show_bot_menu(), BOT_MSG_COLOR)
        user_entry.delete(0, tk.END)
        return

    insert_to_chat("USER", msg, TEXT_COLOR)
    reply = chatbot_response(msg)
    insert_to_chat("BOT", reply, BOT_MSG_COLOR)
    user_entry.delete(0, tk.END)


def quick_generate():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    pwd = ''.join(random.SystemRandom().choice(chars) for _ in range(16))
    insert_to_chat("SYSTEM", f"NEW SECURE KEY:\n{pwd}", ACCENT)


def show_info():
    messagebox.showinfo(
        "Project Info",
        f"{PROJECT_TITLE}\nVersion: {PROJECT_VERSION}\nID: {UNIQUE_ID}\n\nFinal Year BCA Cybersecurity Project"
    )

# ---------------- GUI ----------------

root = tk.Tk()
root.title(PROJECT_TITLE)
root.geometry("550x750")
root.configure(bg=BG_DARK)

header = tk.Frame(root, bg=BG_LIGHT, pady=15)
header.pack(fill="x")

tk.Label(
    header, text="🛡️ SECURITY COMMAND CENTER",
    fg=ACCENT, bg=BG_LIGHT,
    font=("Courier", 16, "bold")
).pack()

tk.Label(
    header, text=f"Build: {UNIQUE_ID}",
    fg="gray", bg=BG_LIGHT,
    font=("Courier", 8)
).pack()

chat_frame = tk.Frame(root, bg=BG_DARK, padx=20, pady=10)
chat_frame.pack(fill="both", expand=True)

chat_display = scrolledtext.ScrolledText(
    chat_frame, bg=BG_LIGHT, fg=TEXT_COLOR,
    insertbackground=TEXT_COLOR,
    font=("Courier", 10),
    borderwidth=0, padx=10, pady=10
)
chat_display.pack(fill="both", expand=True)
chat_display.config(state=tk.DISABLED)

input_frame = tk.Frame(root, bg=BG_DARK, padx=20, pady=20)
input_frame.pack(fill="x")

user_entry = tk.Entry(
    input_frame, bg=BG_LIGHT, fg=ACCENT,
    insertbackground=ACCENT,
    font=("Courier", 12),
    borderwidth=1, relief="flat"
)
user_entry.pack(side="left", fill="x", expand=True, ipady=8, padx=(0, 10))
user_entry.bind("<Return>", on_send)

tk.Button(
    input_frame, text="EXECUTE",
    command=on_send,
    bg=ACCENT, fg=BG_DARK,
    font=("Courier", 10, "bold"),
    relief="flat", padx=15
).pack(side="right")

tool_bar = tk.Frame(root, bg=BG_LIGHT, pady=10)
tool_bar.pack(fill="x")

tk.Button(
    tool_bar, text="[ GENERATE SECURE KEY ]",
    command=quick_generate,
    bg=BG_LIGHT, fg=ACCENT,
    font=("Courier", 10),
    borderwidth=0
).pack(side="left", padx=20)

tk.Button(
    tool_bar, text="[ PROJECT INFO ]",
    command=show_info,
    bg=BG_LIGHT, fg=ACCENT,
    font=("Courier", 10),
    borderwidth=0
).pack(side="right", padx=20)

# Default message
insert_to_chat(
    "BOT",
    "SecureBot Initialized ✅\nPress ENTER to view menu or type 'help'.",
    BOT_MSG_COLOR
)

root.mainloop()
