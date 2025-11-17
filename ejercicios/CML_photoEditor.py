# Python exercises for AI Programming Course: Editor de imágenes
# Exercises solved by Carmen Montalvo Luque, 11/2025

# =====================================================
# Ejercicio 2
#
# Implementa el proyecto de manipulación de imágenes en Python del vídeo.
# (Versión simplificada e independiente, inspirada en pyphotoshop.)
# =====================================================

try:
    from PIL import Image, ImageFilter, ImageEnhance
except:
    print("Pillow not installed. Install it with: pip install pillow")
    Image = None

def adjust_brightness(img, factor):
    enhancer = ImageEnhance.Brightness(img)
    return enhancer.enhance(factor)

def adjust_contrast(img, factor):
    enhancer = ImageEnhance.Contrast(img)
    return enhancer.enhance(factor)

def apply_blur(img, radius=2):
    return img.filter(ImageFilter.GaussianBlur(radius))

def edge_detect(img):
    e = img.convert('L').filter(ImageFilter.FIND_EDGES)
    return e.convert('RGB')

def run_image_tool():
    if Image is None:
        return

    path = input("\nEnter image path (png/jpg): ").strip()
    try:
        img = Image.open(path).convert('RGB')
    except Exception as e:
        print("Error:", e)
        return

    while True:
        print("\nImage tools:")
        print("1) Brightness")
        print("2) Contrast")
        print("3) Blur")
        print("4) Edge detect")
        print("5) Save and exit")
        print("6) Exit without saving")
        opt = input("Choice: ").strip()

        if opt == "1":
            f = float(input("Brightness factor (e.g 1.2): "))
            img = adjust_brightness(img, f)
        elif opt == "2":
            f = float(input("Contrast factor (e.g 1.5): "))
            img = adjust_contrast(img, f)
        elif opt == "3":
            r = float(input("Blur radius: "))
            img = apply_blur(img, r)
        elif opt == "4":
            img = edge_detect(img)
        elif opt == "5":
            out = input("Output filename: ")
            img.save(out)
            print("Saved.")
            return
        elif opt == "6":
            return
        else:
            print("Invalid.")

if __name__ == "__main__":
    run_image_tool()
