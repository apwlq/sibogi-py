import time
from playsound import playsound
import os

# txt 파일 경로
txt_file_path = "시보기.txt"

# 지난 체크 시간 초기화
last_check_time = 0

# 오늘 날짜 초기화
today_date = ""

# 울린 알람 시간과 날짜를 기록할 집합(set) 초기화
triggered_alarms = set()

while True:
    try:
        # txt 파일이 없으면 새로 생성
        if not os.path.exists(txt_file_path):
            with open(txt_file_path, "w") as new_file:
                new_file.write("")

        # 현재 날짜 가져오기
        current_date = time.strftime("%Y-%m-%d")

        # 날짜가 변경되면 오늘의 날짜를 업데이트하고 triggered_alarms 초기화
        if current_date != today_date:
            today_date = current_date
            triggered_alarms.clear()

        # txt 파일을 열어 수정 시간을 확인
        file_mod_time = os.path.getmtime(txt_file_path)

        # 파일 수정 시간이 지난 체크 시간보다 큰 경우
        if file_mod_time > last_check_time:
            last_check_time = file_mod_time
            print("파일 수정 시간이 변경되었습니다.")

            # txt 파일을 읽어서 시간과 음악 파일 경로를 가져옴
            with open(txt_file_path, "r") as file:
                lines = file.readlines()

        for line in lines:
            line = line.strip()
            parts = line.split()
            if len(parts) == 2:
                alarm_time_str, music_file_path = parts
                current_time_str = time.strftime("%H:%M")

                # 현재 날짜와 알람 시간이 일치하고 이미 울린 알람이 아니면 음악 재생
                if alarm_time_str == current_time_str and alarm_time_str not in triggered_alarms:
                    playsound(music_file_path)
                    triggered_alarms.add(alarm_time_str)

        time.sleep(1)  # 1초마다 체크
    except Exception as e:
        print(f"에러 발생: {e}")
