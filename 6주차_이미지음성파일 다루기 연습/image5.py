from PIL import Image

img = Image.open('C:\\Github\\ai-programming\\6주차_이미지음성파일 다루기 연습\\h.jpeg')

# 좌우대칭
img_flipped_LR = img.transpose(Image.FLIP_LEFT_RIGHT)
img_flipped_LR.show()

# 상하대칭
img_flipped_TB = img.transpose(Image.FLIP_TOP_BOTTOM)
img_flipped_TB.show()

# 상하반전한 이미지 저장
img_flipped_TB.save('cat_flip.jpg')
