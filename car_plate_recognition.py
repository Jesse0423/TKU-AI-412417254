import cv2
import pytesseract

# 設置Tesseract OCR的路徑（如果它不在系統PATH中）
pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

# 讀取本地圖像
image_path = '/Users/jes./Downloads/test.jpeg'
image = cv2.imread(image_path)

# 將圖像轉換為灰度
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 範例圖像預處理代碼
_, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 使用Tesseract OCR進行文本識別
license_plate = pytesseract.image_to_string(binary_image, config='--psm 8')

# 使用正则表达式提取有效的车牌号码（去除非字母和数字的字符）
import re
license_plate_number = re.findall(r'[A-Z0-9]+', license_plate)
result = ''.join(license_plate_number)

# 輸出識別到的車牌號碼
print('車牌號碼:', result)

