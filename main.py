from PIL import Image
import sys

def image_to_ascii(image_path, output_width=100):
    try:
        img = Image.open(image_path)
    except Exception as e:
        print(f"Ошибка загрузки изображения: {e}")
        return

    # Конвертируем в оттенки серого
    img = img.convert("L")

    # Ресайзим изображение (сохраняем пропорции)
    width, height = img.size
    aspect_ratio = height / width
    new_height = int(output_width * aspect_ratio * 0.55)  # 0.55 чтобы учесть пропорции символов
    img = img.resize((output_width, new_height))

    # Пиксели -> ASCII
    pixels = img.getdata()
    ascii_chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
    ascii_str = ""

    for pixel in pixels:
        # Масштабируем значение пикселя (0-255) к индексу ascii_chars
        ascii_str += ascii_chars[pixel // 25]  # 25 = 255 / 10 символов
    ascii_str_len = len(ascii_str)
    ascii_img = ""

    # Разбиваем строку на линии
    for i in range(0, ascii_str_len, output_width):
        ascii_img += ascii_str[i:i+output_width] + "\n"

    print(ascii_img)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python image_to_ascii.py <путь_к_изображению> [ширина]")
        sys.exit(1)

    image_path = sys.argv[1]
    width = int(sys.argv[2]) if len(sys.argv) > 2 else 100
    image_to_ascii(image_path, width)
