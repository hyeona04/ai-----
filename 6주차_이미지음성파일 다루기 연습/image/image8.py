  #이미지를 바이트배열로 변환 하기 

def image_to_byte_array(image_path):
    with open(image_path,"rb") as image_file:
        byte_array = bytearray(image_file.read())
    return byte_array

image_path =  "C:\\Github\\ai-programming\\6주차_이미지음성파일 다루기 연습\\h.jpeg"

imapge_byte_array = image_to_byte_array(image_path)

print(len(imapge_byte_array))
