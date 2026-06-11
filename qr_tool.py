import tkinter as tk
import qrcode
from tkinter import filedialog, messagebox
from PIL import ImageTk
import ctypes
import cv2

ctypes.windll.shcore.SetProcessDpiAwareness(1)


def scan_qr():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        messagebox.showerror("Error", "Could not access the camera.")
        return

    root.withdraw()
    detector = cv2.QRCodeDetector()
    scanned_dat = None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        data, _, _ = detector.detectAndDecode(frame)
        if data:
            scanned_dat = data
            break

        cv2.imshow("Scanning QR Code... (Press 'q' to Cancel)", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    if scanned_dat:
        display_data(scanned_dat)
    else:
        root.deiconify()


def display_data(data):
    res_win = tk.Toplevel(root)
    res_win.title("Scan Result")    
    res_win.geometry("500x250")
    res_win.configure(bg="#ffffff")
    
    root.withdraw()
    res_win.protocol("WM_DELETE_WINDOW", lambda: [res_win.destroy(), root.deiconify()])
    
    tk.Label(res_win, text="Scanned QR Data:", font=("Fira Code", 10, "bold"), bg="#ffffff").pack(pady=(15, 5))
    
    result_text = tk.Text(res_win, font=("Fira Code", 10), width=45, height=5, wrap="word", bg="#f5f5f5")
    result_text.pack(pady=5, padx=20)

    def copy():
        root.clipboard_clear()
        root.clipboard_append(data.strip())
        messagebox.showinfo("Done", "Data copied to clipboard")

    if data:
        result_text.insert(tk.END, data)
        result_text.config(state="disabled")
        tk.Button(res_win, text="Copy to Clipboard", font=("Fira Code", 10), width=20, command=copy).pack(pady=(15, 5))
    else:
        res_win.destroy()
        messagebox.showerror("Error", "No QR code could be detected in this image.")
        root.deiconify()


def upload_qr():
    img_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.webp")])
    if not img_path:
        return

    img = cv2.imread(img_path)
    detector = cv2.QRCodeDetector()
    data, _, _ = detector.detectAndDecode(img)
    display_data(data)


def save_qr(img):
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if file_path:
        img.save(file_path)


def display_qr(img):
    dis_img = tk.Toplevel()
    dis_img.title("Your QR Code")
    dis_img.configure(bg="#ffffff")
    dis_img.protocol("WM_DELETE_WINDOW", lambda: [dis_img.destroy(), root.deiconify()])

    tk_img = ImageTk.PhotoImage(image=img)
    qr_lab = tk.Label(dis_img, image=tk_img, bg="#ffffff")
    qr_lab.image = tk_img
    qr_lab.pack(padx=20, pady=20)

    save_btn = tk.Button(dis_img, text="Save QR", font=("Fira Code", 10), width=12, command=lambda: save_qr(img))
    save_btn.pack(pady=(0, 20))


def generate_qr():
    root.withdraw()

    txt_win = tk.Toplevel(root)
    txt_win.title("Generate QR Code")
    txt_win.geometry("600x120")
    txt_win.rowconfigure((0, 1), weight=1)
    txt_win.columnconfigure((0, 1), weight=1)
    txt_win.protocol("WM_DELETE_WINDOW", lambda: [txt_win.destroy(), root.deiconify()])

    tk.Label(txt_win, text="Enter Data or Link:", font=("Fira Code", 10, "bold")).grid(row=0, column=0, padx=(20, 5), sticky="e")
    txt_ent = tk.Entry(txt_win, font=("Fira Code", 10), width=35)
    txt_ent.grid(row=0, column=1, padx=(5, 20), sticky="w")

    def on_gen():
        data = txt_ent.get()
        if not data.strip():
            return 
        img = qrcode.make(data)
        txt_win.destroy()
        display_qr(img)

    gen_btn = tk.Button(txt_win, text="Generate", font=("Fira Code", 10, "bold"), width=12, command=on_gen)
    gen_btn.grid(row=1, column=0, columnspan=2, pady=10)


root = tk.Tk()
root.title("QR Tool")
root.geometry("400x300")

opts = {"font": ("Fira Code", 10), "width": 20, "pady": 5}

tk.Label(root, text="QR Code Scanner & Generator", font=("Fira Code", 12, "bold")).pack(pady=20)

scan = tk.Button(root, text="Scan QR Code", **opts, command=scan_qr)
scan.pack(pady=5)

upl = tk.Button(root, text="Upload QR Code", **opts, command=upload_qr)
upl.pack(pady=5)

generate = tk.Button(root, text="Generate QR Code", **opts, command=generate_qr)
generate.pack(pady=5)

root.mainloop()