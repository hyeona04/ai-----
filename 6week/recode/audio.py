# 필요한 라이브러리 임포트
import soundfile as sf
from pydub.playback import play

# 음성 파일 경로 지정
file_path = "ISEGYE IDOL-SuperHero.mp3"

# 음성 파일 읽기
data, sample_rate = sf.read(file_path)

# 음성 파일의 메타 정보 출력
print("Sample Rate:", sample_rate)
print("Duration:", len(data) / sample_rate, "seconds")

# 음성 파일의 일부를 재생
audio = pydub.AudioSegment.from_file(file_path, format="mp3")
play(audio)