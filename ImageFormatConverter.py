import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image
from ttkthemes import ThemedStyle


def open_file_dialog():
    global file_path

  
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])

    if file_path:
        
        image = Image.open(file_path)

      
        image_info = f"اسم الصورة: {image.filename}\n"
        image_info += f"الحجم: {image.size}\n"
        image_info += f"النوع: {image.format}\n"
        image_info += f"تاريخ الإنشاء: {image.info.get('DateTime', 'غير معروف')}"

     
        label.config(text=image_info)

        entry_source_format.config(state=tk.NORMAL)
        entry_source_format.delete(0, tk.END)
        entry_source_format.insert(0, image.format.lower())
        entry_source_format.config(state=tk.DISABLED)

      
        radio_button_png.config(state=tk.NORMAL)
        radio_button_jpeg.config(state=tk.NORMAL)
        convert_button.config(state=tk.NORMAL)


def convert_image():
 
    source_format = entry_source_format.get()

  
    if radio_variable.get() == 1:
        target_format = "png"
    else:
        target_format = "jpeg"

    try:
     
        image = Image.open(file_path)
        output_file = file_path.replace(source_format, target_format)

       
        if image.mode != "RGB":
            image = image.convert("RGB")

        image.save(output_file, target_format.upper())
        messagebox.showinfo("تم!", f"تم تحويل الصورة إلى صيغة {target_format} بنجاح.")
    except Exception as e:
        messagebox.showerror("خطأ!", f"حدث خطأ أثناء تحويل الصورة: {str(e)}")


def exit_application():
    root.destroy()



root = tk.Tk()
root.title("تحويل الصور")
root.attributes("-fullscreen", True)


main_frame = ttk.Frame(root)
main_frame.pack(padx=20, pady=20)

style = ThemedStyle(root)
style.set_theme("arc")


title_label = ttk.Label(main_frame, text="تحويل الصور", font=("Helvetica", 24))
title_label.grid(row=0, column=0, columnspan=2, pady=10)


entry_source_format = ttk.Entry(main_frame, state=tk.DISABLED, width=20, font=("Helvetica", 14))
entry_source_format.grid(row=1, column=0, columnspan=2, padx=20, pady=5)
entry_source_format.insert(0, "الصيغة الحالية")


radio_variable = tk.IntVar()
radio_button_png = ttk.Radiobutton(main_frame, text="PNG", variable=radio_variable, value=1, state=tk.DISABLED)
radio_button_png.grid(row=2, column=0, padx=20, pady=5)

radio_button_jpeg = ttk.Radiobutton(main_frame, text="JPEG", variable=radio_variable, value=2, state=tk.DISABLED)
radio_button_jpeg.grid(row=2, column=1, padx=20, pady=5)


radio_variable.set(1)


convert_button = ttk.Button(main_frame, text="تحويل الصورة", command=convert_image, state=tk.DISABLED)
convert_button.grid(row=3, column=0, columnspan=2, padx=20, pady=10)


button = ttk.Button(main_frame, text="اختيار الصورة", command=open_file_dialog)
button.grid(row=4, column=0, columnspan=2, padx=20, pady=10)


exit_button = ttk.Button(main_frame, text="خروج", command=exit_application)
exit_button.grid(row=5, column=0, columnspan=2, padx=20, pady=10)


label = ttk.Label(root, text="اختر الصورة", font=("Helvetica", 14))
label.pack(padx=20, pady=20)


root.mainloop()
