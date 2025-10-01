## Adım Adım Uygulama

1. Görseli yükleyin:
```python
import cv2
image = cv2.imread("images1.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("images1.png", gray)
import matplotlib.pyplot as plt

plt.subplot(1,2,1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Orijinal")

plt.subplot(1,2,2)
plt.imshow(gray, cmap="gray")
plt.title("Siyah-Beyaz")

plt.show()

## Sonuç

Aşağıda orijinal ve siyah-beyaz hale getirilmiş görsel karşılaştırması yer almaktadır:

![Orijinal Görsel](images1.png)
![Siyah-Beyaz Görsel](images1_gray.png)

