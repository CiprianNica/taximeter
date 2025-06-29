
import tkinter as tk
from log_config import config
from gui import TaximetroApp

config()

if __name__ == "__main__":
    root = tk.Tk()
    app = TaximetroApp(root)
    root.mainloop()
