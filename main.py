import time
from playsound import playsound
import os

# txt 파일 경로
txt_file_path = "시보기.txt"

# 지난 체크 시간 초기화
last_check_time = 0

while True:
    try:
        # txt 파일을 열어 수정 시간을 확인
        file_mod_time = os.path.getmtime(txt_file_path)
        
        # 파일 수정 시간이 지난 체크 시간보다 큰 경우
        if file_mod_time > last_check_time:
            last_check_time = file_mod_time
            
            # txt 파일을 읽어서 시간과 음악 파일 경로를 가져옴
            with open(txt_file_path, "r") as file:
                lines = file.readlines()
                for line in lines:
                    line = line.strip()
                    parts = line.split()
                    if len(parts) == 2:
                        alarm_time_str, music_file_path = parts
                        current_time_str = time.strftime("%H:%M:%S")
                        
                        if alarm_time_str == current_time_str:
                            # 알람 시간과 현재 시간이 일치하면 음악 재생
                            playsound(music_file_path)
        time.sleep(1)  # 1초마다 체크
    except Exception as e:
        print(f"에러 발생: {e}")
