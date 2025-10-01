# main.py
# Gerekli kütüphaneleri içe aktar
import cv2
import matplotlib.pyplot as plt

# 1️⃣ Görseli yükle
# images klasöründeki görselin adını buraya yaz
image = cv2.imread("images/ornek.png")  # Eğer jpg ise "ornek.jpg"

# 2️⃣ Görseli siyah-beyaz (grayscale) hale getir
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 3️⃣ Yeni görseli kaydet
cv2.imwrite("images/ornek_gray.png", gray_image)  # PNG veya JPG olabilir

# 4️⃣ Orijinal ve siyah-beyaz görselleri yan yana göster
plt.figure(figsize=(10, 5))

# Orijinal görsel
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # OpenCV BGR kullandığı için RGB'ye çevirdik
plt.title("Orijinal Görsel")
plt.axis("off")

# Siyah-beyaz görsel
plt.subplot(1, 2, 2)
plt.imshow(gray_image, cmap="gray")
plt.title("Siyah-Beyaz Görsel")
plt.axis("off")

# Görselleri göster
plt.show()
