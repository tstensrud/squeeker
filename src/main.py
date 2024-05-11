import customtkinter as ctk
import tkinter as tk
import users
import posts

class Main:
    def __init__(self):
        self.window_size = "600x400"
        self.root = tk.Tk()
        self.root.title("Squeek")
        self.root.geometry(self.window_size)
        self.root.config(bg="black")

        self.mainframe = ctk.CTkFrame(self.root)
        self.mainframe.pack(fill="both", expand=True)
        
        self.post_entry = ctk.CTkEntry(self.mainframe, width=500)
        self.post_entry.pack(padx=2, pady=10)
        self.post_btn = ctk.CTkButton(self.mainframe, text="Post", command=self.post)
        self.post_btn.pack(padx=2, pady=10)

        self.name_entry = ctk.CTkEntry(self.mainframe, width=300, placeholder_text="Name")
        self.email_entry = ctk.CTkEntry(self.mainframe, width=300, placeholder_text="E-mail")
        self.name_entry.pack(padx=2, pady=10)
        self.email_entry.pack(padx=2, pady=10)
        self.newusr_btn = ctk.CTkButton(self.mainframe, text="New User", command=self.new_user)
        self.newusr_btn.pack(padx=2, pady=10)
        
        self.menu_bar = tk.Menu(self.root)
        self.options_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.options_menu.add_command(label="List users", command=self.list_users)
        self.options_menu.add_command(label="Empty user-table", command=self.clear_users)
        self.menu_bar.add_cascade(label="Options", menu=self.options_menu)        
        
        self.root.config(menu=self.menu_bar)
        self.root.mainloop()

    def post(self):
        pass
    
    def new_user(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        if users.new_user(email, name):
            self.email_entry.delete(0, tk.END)
            self.name_entry.delete(0, tk.END)

    def list_users(self):
        users.fetch_users()
    
    def clear_users(self):
        users.clear_user_table()

def main():
    app = Main()

if __name__ == "__main__":
    main()