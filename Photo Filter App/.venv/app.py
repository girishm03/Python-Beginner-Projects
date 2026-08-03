from tkinter import Tk, filedialog, Label, Button
from PIL import Image, ImageTk, ImageFilter

current_image = None
original_image = None
image_label = None


def load_image():
    global original_image
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")])
    if file_path:
        img = Image.open(file_path)
        original_image = img.copy()
        display_image(img)


def apply_filter(filter_type):
    global current_image
    if current_image is None:
        return

    if filter_type == "grayscale":
        filtered_img = current_image.convert("L")
    elif filter_type == "blur":
        filtered_img = current_image.filter(ImageFilter.BLUR)
    elif filter_type == "sharpen":
        filtered_img = current_image.filter(ImageFilter.SHARPEN)
    else:
        return

    display_image(filtered_img)


def apply_normal_filter():
    global original_image
    if original_image is None:
        return
    display_image(original_image.copy())


def display_image(img):
    global current_image
    current_image = img
    img.thumbnail((800, 600))
    img_tk = ImageTk.PhotoImage(img.resize((400, 400)))
    image_label.config(image=img_tk)
    image_label.image = img_tk


def main():
    global image_label

    window = Tk()
    window.title("Image Filter Application")
    window.geometry("1000x800")

    image_label = Label(window)
    image_label.pack(pady=10)

    load_button = Button(window, text="Load Image", command=load_image)
    load_button.pack(pady=10)

    normal_button = Button(window, text="Normal", command=apply_normal_filter)
    normal_button.pack(pady=10)
    grayscale_button = Button(window, text="Grayscale", command=lambda: apply_filter("grayscale"))
    grayscale_button.pack(pady=10)
    blur_button = Button(window, text="Blur", command=lambda: apply_filter("blur"))
    blur_button.pack(pady=10)
    sharpen_button = Button(window, text="Sharpen", command=lambda: apply_filter("sharpen"))
    sharpen_button.pack(pady=10)

    window.mainloop()


if __name__ == "__main__":
    main()