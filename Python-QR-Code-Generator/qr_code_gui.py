import qrcode
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import os

# กำหนดสีและธีม
BACKGROUND_COLOR = "#F0F8FF"  # Alice Blue
ACCENT_COLOR = "#4682B4"  # Steel Blue
BUTTON_COLOR = "#1E90FF"  # Dodger Blue
TEXT_COLOR = "#2F4F4F"  # Dark Slate Gray
PREVIEW_SIZE = 320  # ขนาด QR Code ในส่วน preview

# ตัวแปรระดับโกลบอลสำหรับเก็บภาพ QR Code
current_qr_image = None


def generate_qr_code():
    # รับข้อความจาก Text Box
    text = text_box.get("1.0", tk.END).strip()
    if not text:
        status_label.config(text="⚠️ กรุณากรอกข้อความ", foreground="#FF6347")
        return

    # สร้าง QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color=qr_color.get(), back_color="white")

    # แสดง QR Code ในส่วน preview
    global qr_image_tk, current_qr_image
    current_qr_image = img  # เก็บภาพ QR Code ไว้สำหรับบันทึก
    qr_image = img.resize((PREVIEW_SIZE, PREVIEW_SIZE))
    qr_image_tk = ImageTk.PhotoImage(qr_image)
    qr_label.config(image=qr_image_tk)
    status_label.config(text="✅ สร้าง QR Code สำเร็จ", foreground="#228B22")
    save_button.config(state=tk.NORMAL)


def save_qr_code():
    global current_qr_image

    if current_qr_image is None:
        status_label.config(text="⚠️ กรุณาสร้าง QR Code ก่อน", foreground="#FF6347")
        return

    # เลือกตำแหน่งและชื่อไฟล์ที่จะบันทึก
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")],
        title="บันทึก QR Code"
    )
    if not file_path:
        return

    # บันทึก QR Code
    try:
        current_qr_image.save(file_path)
        status_label.config(text=f"✅ บันทึก QR Code ที่ {os.path.basename(file_path)}", foreground="#228B22")
    except Exception as e:
        status_label.config(text=f"❌ เกิดข้อผิดพลาด: {str(e)}", foreground="#FF6347")


# สร้างหน้าต่างหลักของโปรแกรม
root = tk.Tk()
root.title("QR Code Generator")
root.configure(bg=BACKGROUND_COLOR)
root.geometry("550x750")  # กำหนดขนาดเริ่มต้น

# สร้าง style สำหรับ ttk widgets
style = ttk.Style()
style.theme_use('clam')
style.configure('TFrame', background=BACKGROUND_COLOR)
style.configure('TLabel', background=BACKGROUND_COLOR, foreground=TEXT_COLOR, font=('Helvetica', 10))
style.configure('TButton', background=BUTTON_COLOR, foreground='white', font=('Helvetica', 10, 'bold'))
style.map('TButton', background=[('active', ACCENT_COLOR)])

# สร้าง frame หลัก
main_frame = ttk.Frame(root, padding="20")
main_frame.pack(fill=tk.BOTH, expand=True)

# หัวข้อโปรแกรม
header_label = ttk.Label(main_frame, text="QR Code Generator", font=('Helvetica', 18, 'bold'))
header_label.pack(pady=10)

# สร้าง frame สำหรับข้อความนำเข้า
input_frame = ttk.Frame(main_frame, padding="10")
input_frame.pack(fill=tk.X, pady=5)

# ส่วน Text Box สำหรับกรอกข้อความ
text_box_label = ttk.Label(input_frame, text="กรุณากรอกข้อความหรือ URL:", font=('Helvetica', 11))
text_box_label.pack(anchor="w", pady=5)

text_box = tk.Text(input_frame, height=5, width=50, font=('Helvetica', 11),
                   bg="white", fg=TEXT_COLOR, bd=2, relief=tk.GROOVE)
text_box.pack(fill=tk.X, pady=5)

# สร้าง frame สำหรับตัวเลือก
options_frame = ttk.Frame(main_frame)
options_frame.pack(fill=tk.X, pady=10)

# เลือกสี QR Code
color_label = ttk.Label(options_frame, text="สี QR Code:", font=('Helvetica', 11))
color_label.pack(side=tk.LEFT, padx=5)

qr_color = tk.StringVar(value="black")
color_combo = ttk.Combobox(options_frame, textvariable=qr_color,
                           values=["black", "blue", "red", "green", "purple", "#FF6600"],
                           width=10, state="readonly")
color_combo.pack(side=tk.LEFT, padx=5)

# ปุ่มสำหรับสร้าง QR Code แบบสวยงาม
generate_button = tk.Button(main_frame, text="สร้าง QR Code", font=('Helvetica', 11, 'bold'),
                            bg=BUTTON_COLOR, fg="white", relief=tk.RAISED,
                            height=2, command=generate_qr_code, cursor="hand2")
generate_button.pack(pady=15, padx=30, fill=tk.X)

# สร้าง frame สำหรับตัวอย่าง QR Code
preview_frame = ttk.Frame(main_frame)
preview_frame.pack(pady=10)

preview_label = ttk.Label(preview_frame, text="ตัวอย่าง QR Code", font=('Helvetica', 12, 'bold'))
preview_label.pack(pady=5)

# สร้างกรอบแสดง QR Code
qr_frame = ttk.Frame(preview_frame, borderwidth=2, relief=tk.GROOVE)
qr_frame.pack(pady=10)

# ส่วนแสดงตัวอย่าง QR Code
qr_label = ttk.Label(qr_frame, background="white")
qr_label.pack(padx=10, pady=10)

# เตรียมพื้นที่สำหรับภาพ QR Code ตั้งแต่ต้น
empty_image = Image.new('RGB', (PREVIEW_SIZE, PREVIEW_SIZE), color='white')
empty_image_tk = ImageTk.PhotoImage(empty_image)
qr_label.config(image=empty_image_tk)

# สร้างเส้นคั่น
separator = ttk.Separator(main_frame, orient='horizontal')
separator.pack(fill=tk.X, pady=10)

# ปุ่มสำหรับบันทึก QR Code
save_button = tk.Button(main_frame, text="บันทึก QR Code", font=('Helvetica', 11, 'bold'),
                        bg="#28a745", fg="white", relief=tk.RAISED,
                        height=2, command=save_qr_code, cursor="hand2", state=tk.DISABLED)
save_button.pack(pady=10, padx=30, fill=tk.X)

# สถานะการทำงาน
status_label = ttk.Label(main_frame, text="", font=('Helvetica', 10))
status_label.pack(pady=10)

# ส่วนล่างสุดของหน้าต่าง
footer_label = ttk.Label(main_frame, text="© 2025 QR Code Generator", font=('Helvetica', 8))
footer_label.pack(side=tk.BOTTOM, pady=5)

# เริ่มต้นโปรแกรม
root.mainloop()