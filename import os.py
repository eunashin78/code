import os
import pyautogui
import time


def capture_after_click(x, y, filename, save_path):



    # 화면 캡처
    screenshot = pyautogui.screenshot()
    # 마우스 클릭
    pyautogui.click()
    time.sleep(1)

    # 파일로 저장
    file_path = os.path.join(save_path, filename)
    screenshot.save(file_path)
    print(f'Screenshot saved as {file_path}')

# 반복 횟수
num_iterations = 34

# 마우스 현재 위치
x_pos, y_pos = map(int, pyautogui.position())

#저장할 경로
save_path = r'C:\Users\LG\Desktop\영문학입문\사진들'


for i in range(5, 0, -1):
    print(i)
    time.sleep(1)
print("시작!")

# 지정된 횟수만큼 반복
for i in range(num_iterations):
    # 파일 이름 설정
    filename = f'screenshot_{i+1}.png'

    # 클릭 및 화면 캡처 수행
    capture_after_click(x_pos, y_pos, filename, save_path)
