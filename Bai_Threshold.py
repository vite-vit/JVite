import cv2

image = cv2.imread("meo.jpg")
cv2.imshow("Anh meo", image)
# Tạo ảnh xám
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Dùng hàm threshold
ret, thresh_binary = cv2.threshold(gray_image, 180, 255, cv2.THRESH_BINARY)
cv2.imshow("Anh meo sau khi threshold", thresh_binary)
# Đọc cạnh
edges = cv2.Canny(gray_image, threshold1=100, threshold2=200)
cv2.imshow(" Anh lay canh", edges)
# Giảm nhiều bằng gauss
new_image = cv2.GaussianBlur(image, ksize=(50, 50), sigmaX=0)
cv2.imshow(" Anh blur", new_image)
cv2.waitKey()
cv2.destroyAllWindows()

