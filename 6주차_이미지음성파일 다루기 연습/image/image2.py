from PIL import Image

img = Image.open('C:\\Github\\ai-programming\\6주차_이미지음성파일 다루기 연습\\h.jpeg')

# 이미지 사이즈 변경
img_resized = img.resize((400,300))

# 변경한 이미지 출력
img_resized.show()

# 비교를 위해 원본 이미지 출력
img.show()
