# 오리지널 Release - 레드스톤 횃불 설치/제거 딜레이 조정 버전
# Command Length 적정길이 : 2000 ~ 4000
# 제대로 작동이 안된다면 길이를 더 줄여야 합니다.

# https://wikidocs.net/85581 - pyautogui 가이드글
# https://www.youtube.com/watch?v=bKPIcoou9N8 - tkinter GUI구현 가이드영상


import pyautogui #키보드 마우스 매크로
import pyperclip #(pyautogui의 하위종속된 친구..?)
import tkinter.messagebox as msgbox #알림창 띄우기
from tkinter import * #GUI 구현
import time #딜레이 등의 시간조절
import sys #프로그램 즉시종료 등의 기능이 있음

#[0]-------------------------------------------------------------------------------------------------------------
# 총 명령어 갯수 유저 입력 및 기타 시스템용 변수 설정
sys_now_cmdnum = 0 #프로그램에서 총 몇개의 명령어를 마크에 붙여넣었는지 저장
user_max_cmdnum = 0
is_exit = 0 #유저가 프로그램을 그냥 종료했는지 확인

root = Tk() #(root는 그냥 사용자가 임의로 설정할 수 있는 이름이다)
root.title("MCDotMacro v0.1.1 (멀티라인 버전)") # 창 제목
root.geometry("400x290+760+400") # 창 크기
root.resizable(False,False) # x,y 값 변경 불가(창 크기 변경불가)

gui_text_print1 = Label(root, text="< Mural Generator 전용 자동입력 프로그램 >",font=("함초롬돋움",14),bg="#C3E7FA") #일반 텍스트 출력
gui_text_print1.pack()
gui_text_print2 = Label(root, text="사용방법: https://github.com/VDoring/MCDotMacro",bg="#C3E7FA")
gui_text_print2.pack()
gui_text_print3 = Label(root, text="\n[팁]", fg="blue")
gui_text_print3.pack()
gui_text_print4 = Label(root, text="마우스를 왼쪽 위 끝까지 옮기면 작업을 중지할 수 있습니다.")
gui_text_print4.pack()
gui_text_print5 = Label(root, text="[주의]", fg="red")
gui_text_print5.pack()
gui_text_print6 = Label(root, text="확인버튼을 누른 이후 끝날떄까지 아무 행동도 하지 말아주세요!\n적정 Command Length수는 2000~4000 입니다.")
gui_text_print6.pack()
gui_text_print_last = Label(root, text="\n\n---------------- 총 명령어 갯수를 입력하세요.(숫자만 입력) ----------------")
gui_text_print_last.pack()

num = Text(root, width=20, height=1) #숫자 입력창
num.pack()

user_max_cmdnum_string = 0 #사용자의 입력값을 받아올 변수(문자열 타입)
def saveUserMaxCommandNumber(): #사용자의 총 명령어칸 수를 저장하는 함수
    user_max_cmdnum_string = num.get("1.0",END) #유저가 입력한 값 저장
    global user_max_cmdnum
    user_max_cmdnum = int(user_max_cmdnum_string) #문자열을 정수로 변환
    #print("사용자의 총 명령어칸 수:",user_max_cmdnum) #(디버그용 출력)
    if user_max_cmdnum > 31:
        msgbox.showinfo("알림","확인버튼을 누르면 3초후 시작됩니다.")
        global is_exit #전역변수 사용
        is_exit = 1
        time.sleep(3)
        root.destroy()
    else:
        msgbox.showinfo("프로그램이 필요없어 보이는데요?","그정도면 Command Length를 최대한 늘여서 직접 입력하는게 훨신 빠를거에요!")

#프로그램을 시작할떄 사용하는 버튼
start_button = Button(root, padx=30, pady=5, text="입력", command=saveUserMaxCommandNumber)
start_button.pack()

root.mainloop() # 창이 닫히지 않도록 해준다(GUI 유지)

if is_exit == 0: #유저가 프로그램창을 그냥 종료했다면
    sys.exit() #프로그램 종료

#[1]-------------------------------------------------------------------------------------------------------------
# 클릭된 상태(남색)인 1번 버튼을 클릭한다. (크롬으로 윈도우 전환)
#original_1_selected = pyautogui.locateOnScreen('1selected.png')
original_1_selected = pyautogui.locateOnScreen('1selectedNXTLine.png')
center_1_selected = pyautogui.center(original_1_selected)
pyautogui.click(center_1_selected)
cmdnum_first_position = pyautogui.position() #1번명령어 버튼의 위치를 저장(다음라인의 명령어버튼 위치를 설정하기 위함)
#sys.exit() #디버그용

# 밑의 명령어칸을 클릭하고 명령어를 복사한다.
original_cmdmsgbox = pyautogui.locateOnScreen('commandBox.png')
center_cmdmsgbox = pyautogui.center(original_cmdmsgbox)
pyautogui.click(center_cmdmsgbox)
time.sleep(0.2)
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.2)
mccmdstr = pyperclip.paste()
time.sleep(0.3)

# 마인크래프트 창을 클릭해 게임 안으로 들어간다.
original_minecraft_esc = pyautogui.locateOnScreen('mcESC.png')
center_minecraft_esc = pyautogui.center(original_minecraft_esc)
pyautogui.click(center_minecraft_esc)

# 명령어를 커맨드블럭에 붙여넣는다.
pyautogui.click(button='right')
original_minecraft_cmd_box = pyautogui.locateOnScreen('mcCMDbox.png')
center_minecraft_cmd_box = pyautogui.center(original_minecraft_cmd_box)
pyautogui.click(center_minecraft_cmd_box)
pyautogui.click(center_minecraft_cmd_box)
time.sleep(0.3)
pyautogui.write(mccmdstr)
time.sleep(0.3)

original_minecraft_cmd_ok = pyautogui.locateOnScreen('mcCMDok.png')
center_minecraft_cmd_ok = pyautogui.center(original_minecraft_cmd_ok)
center_minecraft_cmd_ok_x = center_minecraft_cmd_ok.x
center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y - 30
pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼보다 좀 더 위로 마우스 설정
pyautogui.click(button='left') #클릭하여 윈도우 전환
center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y
pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼으로 위치설정
pyautogui.click(button='left') #완료버튼 눌러 커맨드블럭 창 나가기
#time.sleep(0.2)

# 마인크래프트에서 커맨드블록 주변에 레드스톤 횃불을 설치한다.
pyautogui.moveRel(0, 35, 1)
pyautogui.click(button='right')
pyautogui.moveRel(55, -85, 1)
pyautogui.click(button='right')

# 마인크래프트에서 커맨드블록 주변의 레드스톤 횃불을 제거한다.
time.sleep(1)
pyautogui.click(button='left')
pyautogui.moveRel(-55, 85, 1)
pyautogui.click(button='left')
pyautogui.moveRel(0, -34, 1)

# 마인크래프트에서 커맨드블럭을 제거하고 다시 설치한다.
pyautogui.click(button='left')
pyautogui.scroll(-1) #마크 2번슬롯 이동
pyautogui.click(button='right')
pyautogui.scroll(1) #마크 1번슬롯 이동

# 마인크래프트에서 커맨드블럭 입력창으로 다시 들어간다.(윈도우로 마우스커서전환 하기 위함)
pyautogui.click(button='right')

sys_now_cmdnum += 1


#[2]-------------------------------------------------------------------------------------------------------------
# 다음 명령어를 복사한다.
original_nextnum_selected = pyautogui.locateOnScreen('2NXTLine.png')
center_nextnum_selected = pyautogui.center(original_nextnum_selected)
pyautogui.click(center_nextnum_selected) #2번명령어 클릭
cmdnum_prev_position = pyautogui.position() #2번명령어 마우스 위치값 저장(다음 명령어위치를 지정할때 사용)

original_cmdmsgbox = pyautogui.locateOnScreen('commandBox.png')
center_cmdmsgbox = pyautogui.center(original_cmdmsgbox)
pyautogui.click(center_cmdmsgbox)
time.sleep(0.2)
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.2)
mccmdstr = pyperclip.paste()
time.sleep(0.3) #명령어 복사

# 마인크래프트 커맨드블럭 명령어 입력칸으로 이동
original_minecraft_cmd_box = pyautogui.locateOnScreen('mcCMDbox.png')
center_minecraft_cmd_box = pyautogui.center(original_minecraft_cmd_box)
pyautogui.click(center_minecraft_cmd_box)
pyautogui.click(center_minecraft_cmd_box)

#커맨드블럭 명령어 입력 후 닫기
time.sleep(0.3)
pyautogui.write(mccmdstr) #명령어 붙여넣기
time.sleep(0.3)
original_minecraft_cmd_ok = pyautogui.locateOnScreen('mcCMDok.png')
center_minecraft_cmd_ok = pyautogui.center(original_minecraft_cmd_ok)
center_minecraft_cmd_ok_x = center_minecraft_cmd_ok.x
center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y - 30
pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼보다 좀 더 위로 마우스 설정
pyautogui.click(button='left') #클릭하여 윈도우 전환
center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y
pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼으로 위치설정
pyautogui.click(button='left') #완료버튼 눌러 커맨드블럭 창 나가기
#time.sleep(0.2)

# 마인크래프트에서 커맨드블록 주변에 레드스톤 횃불을 설치한다.
pyautogui.moveRel(0, 35, 1)  #3번째 인자는 소수로도 사용할 수 있음!
pyautogui.click(button='right')
pyautogui.moveRel(55, -85, 1)
pyautogui.click(button='right')

# 마인크래프트에서 커맨드블록 주변의 레드스톤 횃불을 제거한다.
time.sleep(1)
pyautogui.click(button='left')
pyautogui.moveRel(-55, 85, 1)
pyautogui.click(button='left')
pyautogui.moveRel(0, -34, 1)

# 마인크래프트에서 커맨드블럭을 제거하고 다시 설치한다.
pyautogui.click(button='left')
pyautogui.scroll(-1) #마크 2번슬롯 이동
pyautogui.click(button='right')
pyautogui.scroll(1) #마크 1번슬롯 이동

# 마인크래프트에서 커맨드블럭 입력창으로 다시 들어간다.(윈도우로 마우스커서전환 하기 위함)
pyautogui.click(button='right')

sys_now_cmdnum += 1


#[3]-------------------------------------------------------------------------------------------------------------
# < 3번명령어에서 9번명령어까지 반복 >
for i in range(3,10):
    cmdnum_next_position_x = cmdnum_prev_position.x + 29
    cmdnum_next_position_y = cmdnum_prev_position.y
    pyautogui.moveTo(cmdnum_next_position_x, cmdnum_next_position_y)
    pyautogui.click(button='left')
    cmdnum_prev_position = pyautogui.position() #이전명령어 마우스 위치값 저장(다음 명령어위치를 지정할때 사용)

    original_cmdmsgbox = pyautogui.locateOnScreen('commandBox.png')
    center_cmdmsgbox = pyautogui.center(original_cmdmsgbox)
    pyautogui.click(center_cmdmsgbox)
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.2)
    mccmdstr = pyperclip.paste()
    time.sleep(0.3) #명령어 복사

    # 마인크래프트 커맨드블럭 명령어 입력칸으로 이동
    original_minecraft_cmd_box = pyautogui.locateOnScreen('mcCMDbox.png')
    center_minecraft_cmd_box = pyautogui.center(original_minecraft_cmd_box)
    pyautogui.click(center_minecraft_cmd_box)
    pyautogui.click(center_minecraft_cmd_box)

    #커맨드블럭 명령어 입력 후 닫기
    time.sleep(0.3)
    pyautogui.write(mccmdstr) #명령어 붙여넣기
    time.sleep(0.3)
    original_minecraft_cmd_ok = pyautogui.locateOnScreen('mcCMDok.png')
    center_minecraft_cmd_ok = pyautogui.center(original_minecraft_cmd_ok)
    center_minecraft_cmd_ok_x = center_minecraft_cmd_ok.x
    center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y - 30
    pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼보다 좀 더 위로 마우스 설정
    pyautogui.click(button='left') #클릭하여 윈도우 전환
    center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y
    pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼으로 위치설정
    pyautogui.click(button='left') #완료버튼 눌러 커맨드블럭 창 나가기
    #time.sleep(0.2)

    # 마인크래프트에서 커맨드블록 주변에 레드스톤 횃불을 설치한다.
    pyautogui.moveRel(0, 35, 1)  #3번째 인자는 소수로도 사용할 수 있음!
    pyautogui.click(button='right')
    pyautogui.moveRel(55, -85, 1)
    pyautogui.click(button='right')

    # 마인크래프트에서 커맨드블록 주변의 레드스톤 횃불을 제거한다.
    time.sleep(1)
    pyautogui.click(button='left')
    pyautogui.moveRel(-55, 85, 1)
    pyautogui.click(button='left')
    pyautogui.moveRel(0, -35, 1)

    # 마인크래프트에서 커맨드블럭을 제거하고 다시 설치한다.
    pyautogui.click(button='left')
    pyautogui.scroll(-1) #마크 2번슬롯 이동
    pyautogui.click(button='right')
    pyautogui.scroll(1) #마크 1번슬롯 이동

    # 마인크래프트에서 커맨드블럭 입력창으로 다시 들어간다.(윈도우로 마우스커서전환 하기 위함)
    pyautogui.click(button='right')

    sys_now_cmdnum += 1


#[4]-------------------------------------------------------------------------------------------------------------
# < 10번명령어에서 25번명령어까지 반복 >
#print(cmdnum_next_position_x)
#print(cmdnum_next_position_y)

for i in range(10,26):
    cmdnum_next_position_x += 36.5
    pyautogui.moveTo(cmdnum_next_position_x, cmdnum_next_position_y)
    pyautogui.click(button='left')

    original_cmdmsgbox = pyautogui.locateOnScreen('commandBox.png')
    center_cmdmsgbox = pyautogui.center(original_cmdmsgbox)
    pyautogui.click(center_cmdmsgbox)
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.2)
    mccmdstr = pyperclip.paste()
    time.sleep(0.3) #명령어 복사

    # 마인크래프트 커맨드블럭 명령어 입력칸으로 이동
    original_minecraft_cmd_box = pyautogui.locateOnScreen('mcCMDbox.png')
    center_minecraft_cmd_box = pyautogui.center(original_minecraft_cmd_box)
    pyautogui.click(center_minecraft_cmd_box)
    pyautogui.click(center_minecraft_cmd_box)

    #커맨드블럭 명령어 입력 후 닫기
    time.sleep(0.3)
    pyautogui.write(mccmdstr) #명령어 붙여넣기
    time.sleep(0.3)
    original_minecraft_cmd_ok = pyautogui.locateOnScreen('mcCMDok.png')
    center_minecraft_cmd_ok = pyautogui.center(original_minecraft_cmd_ok)
    center_minecraft_cmd_ok_x = center_minecraft_cmd_ok.x
    center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y - 30
    pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼보다 좀 더 위로 마우스 설정
    pyautogui.click(button='left') #클릭하여 윈도우 전환
    center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y
    pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼으로 위치설정
    pyautogui.click(button='left') #완료버튼 눌러 커맨드블럭 창 나가기
    #time.sleep(0.2)

    # 마인크래프트에서 커맨드블록 주변에 레드스톤 횃불을 설치한다.
    pyautogui.moveRel(0, 35, 1)  #3번째 인자는 소수로도 사용할 수 있음!
    pyautogui.click(button='right')
    pyautogui.moveRel(55, -85, 1)
    pyautogui.click(button='right')

    # 마인크래프트에서 커맨드블록 주변의 레드스톤 횃불을 제거한다.
    time.sleep(1)
    pyautogui.click(button='left')
    pyautogui.moveRel(-55, 85, 1)
    pyautogui.click(button='left')
    pyautogui.moveRel(0, -35, 1)

    # 마인크래프트에서 커맨드블럭을 제거하고 다시 설치한다.
    pyautogui.click(button='left')
    pyautogui.scroll(-1) #마크 2번슬롯 이동
    pyautogui.click(button='right')
    pyautogui.scroll(1) #마크 1번슬롯 이동

    # 마인크래프트에서 커맨드블럭 입력창으로 다시 들어간다.(윈도우로 마우스커서전환 하기 위함)
    pyautogui.click(button='right')

    sys_now_cmdnum += 1

#[5]-------------------------------------------------------------------------------------------------------------
# < 26번명령어에서 52번명령어까지 반복 >

# 26번명령어칸 위치로 "최초한정" 셋팅(이때 1번명령어칸을 기준으로 계산)
cmdnum_next_position_x = cmdnum_first_position.x - (36.5*4)
cmdnum_next_position_y += 15
pyautogui.moveTo(cmdnum_next_position_x, cmdnum_next_position_y)
pyautogui.click(button='left')

original_cmdmsgbox = pyautogui.locateOnScreen('commandBox.png')
center_cmdmsgbox = pyautogui.center(original_cmdmsgbox)
pyautogui.click(center_cmdmsgbox)
time.sleep(0.2)
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.2)
mccmdstr = pyperclip.paste()
time.sleep(0.3) #명령어 복사

# 마인크래프트 커맨드블럭 명령어 입력칸으로 이동
original_minecraft_cmd_box = pyautogui.locateOnScreen('mcCMDbox.png')
center_minecraft_cmd_box = pyautogui.center(original_minecraft_cmd_box)
pyautogui.click(center_minecraft_cmd_box)
pyautogui.click(center_minecraft_cmd_box)

#커맨드블럭 명령어 입력 후 닫기
time.sleep(0.3)
pyautogui.write(mccmdstr) #명령어 붙여넣기
time.sleep(0.3)
original_minecraft_cmd_ok = pyautogui.locateOnScreen('mcCMDok.png')
center_minecraft_cmd_ok = pyautogui.center(original_minecraft_cmd_ok)
center_minecraft_cmd_ok_x = center_minecraft_cmd_ok.x
center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y - 30
pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼보다 좀 더 위로 마우스 설정
pyautogui.click(button='left') #클릭하여 윈도우 전환
center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y
pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼으로 위치설정
pyautogui.click(button='left') #완료버튼 눌러 커맨드블럭 창 나가기
#time.sleep(0.2)

# 마인크래프트에서 커맨드블록 주변에 레드스톤 횃불을 설치한다.
pyautogui.moveRel(0, 35, 1)  #3번째 인자는 소수로도 사용할 수 있음!
pyautogui.click(button='right')
pyautogui.moveRel(55, -85, 1)
pyautogui.click(button='right')

# 마인크래프트에서 커맨드블록 주변의 레드스톤 횃불을 제거한다.
time.sleep(1)
pyautogui.click(button='left')
pyautogui.moveRel(-55, 85, 1)
pyautogui.click(button='left')
pyautogui.moveRel(0, -33, 1)

# 마인크래프트에서 커맨드블럭을 제거하고 다시 설치한다.
pyautogui.click(button='left')
pyautogui.scroll(-1) #마크 2번슬롯 이동
pyautogui.click(button='right')
pyautogui.scroll(1) #마크 1번슬롯 이동

# 마인크래프트에서 커맨드블럭 입력창으로 다시 들어간다.(윈도우로 마우스커서전환 하기 위함)
pyautogui.click(button='right')

sys_now_cmdnum += 1

# 27번명령어칸 부터 52번명령어칸까지 반복 시작 >>
for i in range(27,53):
    cmdnum_next_position_x += 36.5
    pyautogui.moveTo(cmdnum_next_position_x, cmdnum_next_position_y)
    pyautogui.click(button='left')

    original_cmdmsgbox = pyautogui.locateOnScreen('commandBox.png')
    center_cmdmsgbox = pyautogui.center(original_cmdmsgbox)
    pyautogui.click(center_cmdmsgbox)
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.2)
    mccmdstr = pyperclip.paste()
    time.sleep(0.3) #명령어 복사

    # 마인크래프트 커맨드블럭 명령어 입력칸으로 이동
    original_minecraft_cmd_box = pyautogui.locateOnScreen('mcCMDbox.png')
    center_minecraft_cmd_box = pyautogui.center(original_minecraft_cmd_box)
    pyautogui.click(center_minecraft_cmd_box)
    pyautogui.click(center_minecraft_cmd_box)

    #커맨드블럭 명령어 입력 후 닫기
    time.sleep(0.3)
    pyautogui.write(mccmdstr) #명령어 붙여넣기
    time.sleep(0.3)
    original_minecraft_cmd_ok = pyautogui.locateOnScreen('mcCMDok.png')
    center_minecraft_cmd_ok = pyautogui.center(original_minecraft_cmd_ok)
    center_minecraft_cmd_ok_x = center_minecraft_cmd_ok.x
    center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y - 30
    pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼보다 좀 더 위로 마우스 설정
    pyautogui.click(button='left') #클릭하여 윈도우 전환
    center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y
    pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼으로 위치설정
    pyautogui.click(button='left') #완료버튼 눌러 커맨드블럭 창 나가기
    #time.sleep(0.2)

    # 마인크래프트에서 커맨드블록 주변에 레드스톤 횃불을 설치한다.
    pyautogui.moveRel(0, 35, 1)  #3번째 인자는 소수로도 사용할 수 있음!
    pyautogui.click(button='right')
    pyautogui.moveRel(55, -85, 1)
    pyautogui.click(button='right')

    # 마인크래프트에서 커맨드블록 주변의 레드스톤 횃불을 제거한다.
    time.sleep(1)
    pyautogui.click(button='left')
    pyautogui.moveRel(-55, 85, 1)
    pyautogui.click(button='left')
    pyautogui.moveRel(0, -35, 1)

    # 마인크래프트에서 커맨드블럭을 제거하고 다시 설치한다.
    pyautogui.click(button='left')
    pyautogui.scroll(-1) #마크 2번슬롯 이동
    pyautogui.click(button='right')
    pyautogui.scroll(1) #마크 1번슬롯 이동

    # 마인크래프트에서 커맨드블럭 입력창으로 다시 들어간다.(윈도우로 마우스커서전환 하기 위함)
    pyautogui.click(button='right')

    sys_now_cmdnum += 1
    if sys_now_cmdnum >= user_max_cmdnum: #유저가 입력한 수만큼 작업했을경우
        msgbox.showinfo("알림","작업이 완료되었습니다.")
        sys.exit() #프로그램 종료


#[6]-------------------------------------------------------------------------------------------------------------
# < 53번명령어에서 79번명령어까지 반복 >

# 53번명령어칸 위치로 "최초한정" 셋팅(이때 1번명령어칸을 기준으로 계산)
cmdnum_next_position_x = cmdnum_first_position.x - (36.5*4)
cmdnum_next_position_y += 15
pyautogui.moveTo(cmdnum_next_position_x, cmdnum_next_position_y)
pyautogui.click(button='left')

original_cmdmsgbox = pyautogui.locateOnScreen('commandBox.png')
center_cmdmsgbox = pyautogui.center(original_cmdmsgbox)
pyautogui.click(center_cmdmsgbox)
time.sleep(0.2)
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.2)
mccmdstr = pyperclip.paste()
time.sleep(0.3) #명령어 복사

# 마인크래프트 커맨드블럭 명령어 입력칸으로 이동
original_minecraft_cmd_box = pyautogui.locateOnScreen('mcCMDbox.png')
center_minecraft_cmd_box = pyautogui.center(original_minecraft_cmd_box)
pyautogui.click(center_minecraft_cmd_box)
pyautogui.click(center_minecraft_cmd_box)

#커맨드블럭 명령어 입력 후 닫기
time.sleep(0.3)
pyautogui.write(mccmdstr) #명령어 붙여넣기
time.sleep(0.3)
original_minecraft_cmd_ok = pyautogui.locateOnScreen('mcCMDok.png')
center_minecraft_cmd_ok = pyautogui.center(original_minecraft_cmd_ok)
center_minecraft_cmd_ok_x = center_minecraft_cmd_ok.x
center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y - 30
pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼보다 좀 더 위로 마우스 설정
pyautogui.click(button='left') #클릭하여 윈도우 전환
center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y
pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼으로 위치설정
pyautogui.click(button='left') #완료버튼 눌러 커맨드블럭 창 나가기
#time.sleep(0.2)

# 마인크래프트에서 커맨드블록 주변에 레드스톤 횃불을 설치한다.
pyautogui.moveRel(0, 35, 1)  #3번째 인자는 소수로도 사용할 수 있음!
pyautogui.click(button='right')
pyautogui.moveRel(55, -85, 1)
pyautogui.click(button='right')

# 마인크래프트에서 커맨드블록 주변의 레드스톤 횃불을 제거한다.
time.sleep(1)
pyautogui.click(button='left')
pyautogui.moveRel(-55, 85, 1)
pyautogui.click(button='left')
pyautogui.moveRel(0, -32, 1)

# 마인크래프트에서 커맨드블럭을 제거하고 다시 설치한다.
pyautogui.click(button='left')
pyautogui.scroll(-1) #마크 2번슬롯 이동
pyautogui.click(button='right')
pyautogui.scroll(1) #마크 1번슬롯 이동

# 마인크래프트에서 커맨드블럭 입력창으로 다시 들어간다.(윈도우로 마우스커서전환 하기 위함)
pyautogui.click(button='right')

sys_now_cmdnum += 1
if sys_now_cmdnum >= user_max_cmdnum: #유저가 입력한 수만큼 작업했을경우
    msgbox.showinfo("알림","작업이 완료되었습니다.")
    sys.exit() #프로그램 종료

#54번명령어칸 부터 79번명령어칸까지 반복 시작 >>
for i in range(54,80):
    cmdnum_next_position_x += 36.5
    pyautogui.moveTo(cmdnum_next_position_x, cmdnum_next_position_y)
    pyautogui.click(button='left')

    original_cmdmsgbox = pyautogui.locateOnScreen('commandBox.png')
    center_cmdmsgbox = pyautogui.center(original_cmdmsgbox)
    pyautogui.click(center_cmdmsgbox)
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.2)
    mccmdstr = pyperclip.paste()
    time.sleep(0.3) #명령어 복사

    # 마인크래프트 커맨드블럭 명령어 입력칸으로 이동
    original_minecraft_cmd_box = pyautogui.locateOnScreen('mcCMDbox.png')
    center_minecraft_cmd_box = pyautogui.center(original_minecraft_cmd_box)
    pyautogui.click(center_minecraft_cmd_box)
    pyautogui.click(center_minecraft_cmd_box)

    #커맨드블럭 명령어 입력 후 닫기
    time.sleep(0.3)
    pyautogui.write(mccmdstr) #명령어 붙여넣기
    time.sleep(0.3)
    original_minecraft_cmd_ok = pyautogui.locateOnScreen('mcCMDok.png')
    center_minecraft_cmd_ok = pyautogui.center(original_minecraft_cmd_ok)
    center_minecraft_cmd_ok_x = center_minecraft_cmd_ok.x
    center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y - 30
    pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼보다 좀 더 위로 마우스 설정
    pyautogui.click(button='left') #클릭하여 윈도우 전환
    center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y
    pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼으로 위치설정
    pyautogui.click(button='left') #완료버튼 눌러 커맨드블럭 창 나가기
    #time.sleep(0.2)

    # 마인크래프트에서 커맨드블록 주변에 레드스톤 횃불을 설치한다.
    pyautogui.moveRel(0, 35, 1)  #3번째 인자는 소수로도 사용할 수 있음!
    pyautogui.click(button='right')
    pyautogui.moveRel(55, -85, 1)
    pyautogui.click(button='right')

    # 마인크래프트에서 커맨드블록 주변의 레드스톤 횃불을 제거한다.
    time.sleep(1)
    pyautogui.click(button='left')
    pyautogui.moveRel(-55, 85, 1)
    pyautogui.click(button='left')
    pyautogui.moveRel(0, -35, 1)

    # 마인크래프트에서 커맨드블럭을 제거하고 다시 설치한다.
    pyautogui.click(button='left')
    pyautogui.scroll(-1) #마크 2번슬롯 이동
    pyautogui.click(button='right')
    pyautogui.scroll(1) #마크 1번슬롯 이동

    # 마인크래프트에서 커맨드블럭 입력창으로 다시 들어간다.(윈도우로 마우스커서전환 하기 위함)
    pyautogui.click(button='right')

    sys_now_cmdnum += 1
    if sys_now_cmdnum >= user_max_cmdnum: #유저가 입력한 수만큼 작업했을경우
        msgbox.showinfo("알림","작업이 완료되었습니다.")
        sys.exit() #프로그램 종료

#[7]-------------------------------------------------------------------------------------------------------------
# < 80번명령어에서 99번명령어까지 반복 >

# 80번명령어칸 위치로 "최초한정" 셋팅(이때 1번명령어칸을 기준으로 계산)
cmdnum_next_position_x = cmdnum_first_position.x - (36.5*4)
cmdnum_next_position_y += 15
pyautogui.moveTo(cmdnum_next_position_x, cmdnum_next_position_y)
pyautogui.click(button='left')

original_cmdmsgbox = pyautogui.locateOnScreen('commandBox.png')
center_cmdmsgbox = pyautogui.center(original_cmdmsgbox)
pyautogui.click(center_cmdmsgbox)
time.sleep(0.2)
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.2)
mccmdstr = pyperclip.paste()
time.sleep(0.3) #명령어 복사

# 마인크래프트 커맨드블럭 명령어 입력칸으로 이동
original_minecraft_cmd_box = pyautogui.locateOnScreen('mcCMDbox.png')
center_minecraft_cmd_box = pyautogui.center(original_minecraft_cmd_box)
pyautogui.click(center_minecraft_cmd_box)
pyautogui.click(center_minecraft_cmd_box)

#커맨드블럭 명령어 입력 후 닫기
time.sleep(0.3)
pyautogui.write(mccmdstr) #명령어 붙여넣기
time.sleep(0.3)
original_minecraft_cmd_ok = pyautogui.locateOnScreen('mcCMDok.png')
center_minecraft_cmd_ok = pyautogui.center(original_minecraft_cmd_ok)
center_minecraft_cmd_ok_x = center_minecraft_cmd_ok.x
center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y - 30
pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼보다 좀 더 위로 마우스 설정
pyautogui.click(button='left') #클릭하여 윈도우 전환
center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y
pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼으로 위치설정
pyautogui.click(button='left') #완료버튼 눌러 커맨드블럭 창 나가기
#time.sleep(0.2)

# 마인크래프트에서 커맨드블록 주변에 레드스톤 횃불을 설치한다.
pyautogui.moveRel(0, 35, 1)  #3번째 인자는 소수로도 사용할 수 있음!
pyautogui.click(button='right')
pyautogui.moveRel(55, -85, 1)
pyautogui.click(button='right')

# 마인크래프트에서 커맨드블록 주변의 레드스톤 횃불을 제거한다.
time.sleep(1)
pyautogui.click(button='left')
pyautogui.moveRel(-55, 85, 1)
pyautogui.click(button='left')
pyautogui.moveRel(0, -32, 1)

# 마인크래프트에서 커맨드블럭을 제거하고 다시 설치한다.
pyautogui.click(button='left')
pyautogui.scroll(-1) #마크 2번슬롯 이동
pyautogui.click(button='right')
pyautogui.scroll(1) #마크 1번슬롯 이동

# 마인크래프트에서 커맨드블럭 입력창으로 다시 들어간다.(윈도우로 마우스커서전환 하기 위함)
pyautogui.click(button='right')

sys_now_cmdnum += 1
if sys_now_cmdnum >= user_max_cmdnum: #유저가 입력한 수만큼 작업했을경우
    msgbox.showinfo("알림","작업이 완료되었습니다.")
    sys.exit() #프로그램 종료

# 81번명령어칸 부터 99번명령어칸까지 반복 시작 >>
for i in range(81,100):
    cmdnum_next_position_x += 36.5
    pyautogui.moveTo(cmdnum_next_position_x, cmdnum_next_position_y)
    pyautogui.click(button='left')

    original_cmdmsgbox = pyautogui.locateOnScreen('commandBox.png')
    center_cmdmsgbox = pyautogui.center(original_cmdmsgbox)
    pyautogui.click(center_cmdmsgbox)
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.2)
    mccmdstr = pyperclip.paste()
    time.sleep(0.3) #명령어 복사

    # 마인크래프트 커맨드블럭 명령어 입력칸으로 이동
    original_minecraft_cmd_box = pyautogui.locateOnScreen('mcCMDbox.png')
    center_minecraft_cmd_box = pyautogui.center(original_minecraft_cmd_box)
    pyautogui.click(center_minecraft_cmd_box)
    pyautogui.click(center_minecraft_cmd_box)

    #커맨드블럭 명령어 입력 후 닫기
    time.sleep(0.3)
    pyautogui.write(mccmdstr) #명령어 붙여넣기
    time.sleep(0.3)
    original_minecraft_cmd_ok = pyautogui.locateOnScreen('mcCMDok.png')
    center_minecraft_cmd_ok = pyautogui.center(original_minecraft_cmd_ok)
    center_minecraft_cmd_ok_x = center_minecraft_cmd_ok.x
    center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y - 30
    pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼보다 좀 더 위로 마우스 설정
    pyautogui.click(button='left') #클릭하여 윈도우 전환
    center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y
    pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼으로 위치설정
    pyautogui.click(button='left') #완료버튼 눌러 커맨드블럭 창 나가기
    #time.sleep(0.2)

    # 마인크래프트에서 커맨드블록 주변에 레드스톤 횃불을 설치한다.
    pyautogui.moveRel(0, 35, 1)  #3번째 인자는 소수로도 사용할 수 있음!
    pyautogui.click(button='right')
    pyautogui.moveRel(55, -85, 1)
    pyautogui.click(button='right')

    # 마인크래프트에서 커맨드블록 주변의 레드스톤 횃불을 제거한다.
    time.sleep(1)
    pyautogui.click(button='left')
    pyautogui.moveRel(-55, 85, 1)
    pyautogui.click(button='left')
    pyautogui.moveRel(0, -35, 1)

    # 마인크래프트에서 커맨드블럭을 제거하고 다시 설치한다.
    pyautogui.click(button='left')
    pyautogui.scroll(-1) #마크 2번슬롯 이동
    pyautogui.click(button='right')
    pyautogui.scroll(1) #마크 1번슬롯 이동

    # 마인크래프트에서 커맨드블럭 입력창으로 다시 들어간다.(윈도우로 마우스커서전환 하기 위함)
    pyautogui.click(button='right')

    sys_now_cmdnum += 1
    if sys_now_cmdnum >= user_max_cmdnum: #유저가 입력한 수만큼 작업했을경우
        msgbox.showinfo("알림","작업이 완료되었습니다.")
        sys.exit() #프로그램 종료

#[7]-------------------------------------------------------------------------------------------------------------
# < 100번명령어에서 105번명령어까지 반복 >
# 99번 명령어에서 100번으로 넘어간다. (2칸짜리 명령어칸에서 3칸짜리 명령어칸으로 이동할때 최초의 x값 계산)
cmdnum_next_position_x += 37
pyautogui.moveTo(cmdnum_next_position_x, cmdnum_next_position_y)
pyautogui.click(button='left')

original_cmdmsgbox = pyautogui.locateOnScreen('commandBox.png')
center_cmdmsgbox = pyautogui.center(original_cmdmsgbox)
pyautogui.click(center_cmdmsgbox)
time.sleep(0.2)
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.2)
mccmdstr = pyperclip.paste()
time.sleep(0.3) #명령어 복사

# 마인크래프트 커맨드블럭 명령어 입력칸으로 이동
original_minecraft_cmd_box = pyautogui.locateOnScreen('mcCMDbox.png')
center_minecraft_cmd_box = pyautogui.center(original_minecraft_cmd_box)
pyautogui.click(center_minecraft_cmd_box)
pyautogui.click(center_minecraft_cmd_box)

#커맨드블럭 명령어 입력 후 닫기
time.sleep(0.3)
pyautogui.write(mccmdstr) #명령어 붙여넣기
time.sleep(0.3)
original_minecraft_cmd_ok = pyautogui.locateOnScreen('mcCMDok.png')
center_minecraft_cmd_ok = pyautogui.center(original_minecraft_cmd_ok)
center_minecraft_cmd_ok_x = center_minecraft_cmd_ok.x
center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y - 30
pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼보다 좀 더 위로 마우스 설정
pyautogui.click(button='left') #클릭하여 윈도우 전환
center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y
pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼으로 위치설정
pyautogui.click(button='left') #완료버튼 눌러 커맨드블럭 창 나가기
#time.sleep(0.2)

# 마인크래프트에서 커맨드블록 주변에 레드스톤 횃불을 설치한다.
pyautogui.moveRel(0, 35, 1)  #3번째 인자는 소수로도 사용할 수 있음!
pyautogui.click(button='right')
pyautogui.moveRel(55, -85, 1)
pyautogui.click(button='right')

# 마인크래프트에서 커맨드블록 주변의 레드스톤 횃불을 제거한다.
time.sleep(1)
pyautogui.click(button='left')
pyautogui.moveRel(-55, 85, 1)
pyautogui.click(button='left')
pyautogui.moveRel(0, -33, 1)

# 마인크래프트에서 커맨드블럭을 제거하고 다시 설치한다.
pyautogui.click(button='left')
pyautogui.scroll(-1) #마크 2번슬롯 이동
pyautogui.click(button='right')
pyautogui.scroll(1) #마크 1번슬롯 이동

# 마인크래프트에서 커맨드블럭 입력창으로 다시 들어간다.(윈도우로 마우스커서전환 하기 위함)
pyautogui.click(button='right')

sys_now_cmdnum += 1
if sys_now_cmdnum >= user_max_cmdnum: #유저가 입력한 수만큼 작업했을경우
    msgbox.showinfo("알림","작업이 완료되었습니다.")
    sys.exit() #프로그램 종료

# 101번명령어칸 부터 105번명령어칸까지 반복 시작 >>
for i in range(101,106):
    cmdnum_next_position_x += 45
    pyautogui.moveTo(cmdnum_next_position_x, cmdnum_next_position_y)
    pyautogui.click(button='left')

    original_cmdmsgbox = pyautogui.locateOnScreen('commandBox.png')
    center_cmdmsgbox = pyautogui.center(original_cmdmsgbox)
    pyautogui.click(center_cmdmsgbox)
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.2)
    mccmdstr = pyperclip.paste()
    time.sleep(0.3) #명령어 복사

    # 마인크래프트 커맨드블럭 명령어 입력칸으로 이동
    original_minecraft_cmd_box = pyautogui.locateOnScreen('mcCMDbox.png')
    center_minecraft_cmd_box = pyautogui.center(original_minecraft_cmd_box)
    pyautogui.click(center_minecraft_cmd_box)
    pyautogui.click(center_minecraft_cmd_box)

    #커맨드블럭 명령어 입력 후 닫기
    time.sleep(0.3)
    pyautogui.write(mccmdstr) #명령어 붙여넣기
    time.sleep(0.3)
    original_minecraft_cmd_ok = pyautogui.locateOnScreen('mcCMDok.png')
    center_minecraft_cmd_ok = pyautogui.center(original_minecraft_cmd_ok)
    center_minecraft_cmd_ok_x = center_minecraft_cmd_ok.x
    center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y - 30
    pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼보다 좀 더 위로 마우스 설정
    pyautogui.click(button='left') #클릭하여 윈도우 전환
    center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y
    pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼으로 위치설정
    pyautogui.click(button='left') #완료버튼 눌러 커맨드블럭 창 나가기
    #time.sleep(0.2)

    # 마인크래프트에서 커맨드블록 주변에 레드스톤 횃불을 설치한다.
    pyautogui.moveRel(0, 35, 1)  #3번째 인자는 소수로도 사용할 수 있음!
    pyautogui.click(button='right')
    pyautogui.moveRel(55, -85, 1)
    pyautogui.click(button='right')

    # 마인크래프트에서 커맨드블록 주변의 레드스톤 횃불을 제거한다.
    time.sleep(1)
    pyautogui.click(button='left')
    pyautogui.moveRel(-55, 85, 1)
    pyautogui.click(button='left')
    pyautogui.moveRel(0, -35, 1)

    # 마인크래프트에서 커맨드블럭을 제거하고 다시 설치한다.
    pyautogui.click(button='left')
    pyautogui.scroll(-1) #마크 2번슬롯 이동
    pyautogui.click(button='right')
    pyautogui.scroll(1) #마크 1번슬롯 이동

    # 마인크래프트에서 커맨드블럭 입력창으로 다시 들어간다.(윈도우로 마우스커서전환 하기 위함)
    pyautogui.click(button='right')

    sys_now_cmdnum += 1
    if sys_now_cmdnum >= user_max_cmdnum: #유저가 입력한 수만큼 작업했을경우
        msgbox.showinfo("알림","작업이 완료되었습니다.")
        sys.exit() #프로그램 종료

#[8]-------------------------------------------------------------------------------------------------------------
# < 106번명령어에서 128번명령어까지 반복 >
cmdnum_next_position_x = cmdnum_first_position.x - (34*4)
cmdnum_next_position_y += 15
pyautogui.moveTo(cmdnum_next_position_x, cmdnum_next_position_y)
pyautogui.click(button='left')

original_cmdmsgbox = pyautogui.locateOnScreen('commandBox.png')
center_cmdmsgbox = pyautogui.center(original_cmdmsgbox)
pyautogui.click(center_cmdmsgbox)
time.sleep(0.2)
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.2)
mccmdstr = pyperclip.paste()
time.sleep(0.3) #명령어 복사

# 마인크래프트 커맨드블럭 명령어 입력칸으로 이동
original_minecraft_cmd_box = pyautogui.locateOnScreen('mcCMDbox.png')
center_minecraft_cmd_box = pyautogui.center(original_minecraft_cmd_box)
pyautogui.click(center_minecraft_cmd_box)
pyautogui.click(center_minecraft_cmd_box)

#커맨드블럭 명령어 입력 후 닫기
time.sleep(0.3)
pyautogui.write(mccmdstr) #명령어 붙여넣기
time.sleep(0.3)
original_minecraft_cmd_ok = pyautogui.locateOnScreen('mcCMDok.png')
center_minecraft_cmd_ok = pyautogui.center(original_minecraft_cmd_ok)
center_minecraft_cmd_ok_x = center_minecraft_cmd_ok.x
center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y - 30
pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼보다 좀 더 위로 마우스 설정
pyautogui.click(button='left') #클릭하여 윈도우 전환
center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y
pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼으로 위치설정
pyautogui.click(button='left') #완료버튼 눌러 커맨드블럭 창 나가기
#time.sleep(0.2)

# 마인크래프트에서 커맨드블록 주변에 레드스톤 횃불을 설치한다.
pyautogui.moveRel(0, 35, 1)  #3번째 인자는 소수로도 사용할 수 있음!
pyautogui.click(button='right')
pyautogui.moveRel(55, -85, 1)
pyautogui.click(button='right')

# 마인크래프트에서 커맨드블록 주변의 레드스톤 횃불을 제거한다.
time.sleep(1)
pyautogui.click(button='left')
pyautogui.moveRel(-55, 85, 1)
pyautogui.click(button='left')
pyautogui.moveRel(0, -31, 1)

# 마인크래프트에서 커맨드블럭을 제거하고 다시 설치한다.
pyautogui.click(button='left')
pyautogui.scroll(-1) #마크 2번슬롯 이동
pyautogui.click(button='right')
pyautogui.scroll(1) #마크 1번슬롯 이동

# 마인크래프트에서 커맨드블럭 입력창으로 다시 들어간다.(윈도우로 마우스커서전환 하기 위함)
pyautogui.click(button='right')

sys_now_cmdnum += 1
if sys_now_cmdnum >= user_max_cmdnum: #유저가 입력한 수만큼 작업했을경우
    msgbox.showinfo("알림","작업이 완료되었습니다.")
    sys.exit() #프로그램 종료

# 107번명령어칸 부터 128번명령어칸까지 반복 시작 >>
for i in range(107,129):
    cmdnum_next_position_x += 43.8
    pyautogui.moveTo(cmdnum_next_position_x, cmdnum_next_position_y)
    pyautogui.click(button='left')

    original_cmdmsgbox = pyautogui.locateOnScreen('commandBox.png')
    center_cmdmsgbox = pyautogui.center(original_cmdmsgbox)
    pyautogui.click(center_cmdmsgbox)
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.2)
    mccmdstr = pyperclip.paste()
    time.sleep(0.3) #명령어 복사

    # 마인크래프트 커맨드블럭 명령어 입력칸으로 이동
    original_minecraft_cmd_box = pyautogui.locateOnScreen('mcCMDbox.png')
    center_minecraft_cmd_box = pyautogui.center(original_minecraft_cmd_box)
    pyautogui.click(center_minecraft_cmd_box)
    pyautogui.click(center_minecraft_cmd_box)

    #커맨드블럭 명령어 입력 후 닫기
    time.sleep(0.3)
    pyautogui.write(mccmdstr) #명령어 붙여넣기
    time.sleep(0.3)
    original_minecraft_cmd_ok = pyautogui.locateOnScreen('mcCMDok.png')
    center_minecraft_cmd_ok = pyautogui.center(original_minecraft_cmd_ok)
    center_minecraft_cmd_ok_x = center_minecraft_cmd_ok.x
    center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y - 30
    pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼보다 좀 더 위로 마우스 설정
    pyautogui.click(button='left') #클릭하여 윈도우 전환
    center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y
    pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼으로 위치설정
    pyautogui.click(button='left') #완료버튼 눌러 커맨드블럭 창 나가기
    #time.sleep(0.2)

    # 마인크래프트에서 커맨드블록 주변에 레드스톤 횃불을 설치한다.
    pyautogui.moveRel(0, 35, 1)  #3번째 인자는 소수로도 사용할 수 있음!
    pyautogui.click(button='right')
    pyautogui.moveRel(55, -85, 1)
    pyautogui.click(button='right')

    # 마인크래프트에서 커맨드블록 주변의 레드스톤 횃불을 제거한다.
    time.sleep(1)
    pyautogui.click(button='left')
    pyautogui.moveRel(-55, 85, 1)
    pyautogui.click(button='left')
    pyautogui.moveRel(0, -35, 1)

    # 마인크래프트에서 커맨드블럭을 제거하고 다시 설치한다.
    pyautogui.click(button='left')
    pyautogui.scroll(-1) #마크 2번슬롯 이동
    pyautogui.click(button='right')
    pyautogui.scroll(1) #마크 1번슬롯 이동

    # 마인크래프트에서 커맨드블럭 입력창으로 다시 들어간다.(윈도우로 마우스커서전환 하기 위함)
    pyautogui.click(button='right')

    sys_now_cmdnum += 1
    if sys_now_cmdnum >= user_max_cmdnum: #유저가 입력한 수만큼 작업했을경우
        msgbox.showinfo("알림","작업이 완료되었습니다.")
        sys.exit() #프로그램 종료

#[9]-------------------------------------------------------------------------------------------------------------
# < 129번명령어에서 150번명령어까지 반복 > < 여기서부터는 코드가 모두 똑같습니다. >
cmdnum_next_position_x = cmdnum_first_position.x - (34*4)
cmdnum_next_position_y += 15
pyautogui.moveTo(cmdnum_next_position_x, cmdnum_next_position_y)
pyautogui.click(button='left')

original_cmdmsgbox = pyautogui.locateOnScreen('commandBox.png')
center_cmdmsgbox = pyautogui.center(original_cmdmsgbox)
pyautogui.click(center_cmdmsgbox)
time.sleep(0.2)
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.2)
mccmdstr = pyperclip.paste()
time.sleep(0.3) #명령어 복사

# 마인크래프트 커맨드블럭 명령어 입력칸으로 이동
original_minecraft_cmd_box = pyautogui.locateOnScreen('mcCMDbox.png')
center_minecraft_cmd_box = pyautogui.center(original_minecraft_cmd_box)
pyautogui.click(center_minecraft_cmd_box)
pyautogui.click(center_minecraft_cmd_box)

#커맨드블럭 명령어 입력 후 닫기
time.sleep(0.3)
pyautogui.write(mccmdstr) #명령어 붙여넣기
time.sleep(0.3)
original_minecraft_cmd_ok = pyautogui.locateOnScreen('mcCMDok.png')
center_minecraft_cmd_ok = pyautogui.center(original_minecraft_cmd_ok)
center_minecraft_cmd_ok_x = center_minecraft_cmd_ok.x
center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y - 30
pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼보다 좀 더 위로 마우스 설정
pyautogui.click(button='left') #클릭하여 윈도우 전환
center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y
pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼으로 위치설정
pyautogui.click(button='left') #완료버튼 눌러 커맨드블럭 창 나가기
#time.sleep(0.2)

# 마인크래프트에서 커맨드블록 주변에 레드스톤 횃불을 설치한다.
pyautogui.moveRel(0, 35, 1)  #3번째 인자는 소수로도 사용할 수 있음!
pyautogui.click(button='right')
pyautogui.moveRel(55, -85, 1)
pyautogui.click(button='right')

# 마인크래프트에서 커맨드블록 주변의 레드스톤 횃불을 제거한다.
time.sleep(1)
pyautogui.click(button='left')
pyautogui.moveRel(-55, 85, 1)
pyautogui.click(button='left')
pyautogui.moveRel(0, -32, 1)

# 마인크래프트에서 커맨드블럭을 제거하고 다시 설치한다.
pyautogui.click(button='left')
pyautogui.scroll(-1) #마크 2번슬롯 이동
pyautogui.click(button='right')
pyautogui.scroll(1) #마크 1번슬롯 이동

# 마인크래프트에서 커맨드블럭 입력창으로 다시 들어간다.(윈도우로 마우스커서전환 하기 위함)
pyautogui.click(button='right')

sys_now_cmdnum += 1
if sys_now_cmdnum >= user_max_cmdnum: #유저가 입력한 수만큼 작업했을경우
    msgbox.showinfo("알림","작업이 완료되었습니다.")
    sys.exit() #프로그램 종료

# 130번명령어칸 부터 150번명령어칸까지 반복 시작 >>
for i in range(130,151):
    cmdnum_next_position_x += 43.8
    pyautogui.moveTo(cmdnum_next_position_x, cmdnum_next_position_y)
    pyautogui.click(button='left')

    original_cmdmsgbox = pyautogui.locateOnScreen('commandBox.png')
    center_cmdmsgbox = pyautogui.center(original_cmdmsgbox)
    pyautogui.click(center_cmdmsgbox)
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.2)
    mccmdstr = pyperclip.paste()
    time.sleep(0.3) #명령어 복사

    # 마인크래프트 커맨드블럭 명령어 입력칸으로 이동
    original_minecraft_cmd_box = pyautogui.locateOnScreen('mcCMDbox.png')
    center_minecraft_cmd_box = pyautogui.center(original_minecraft_cmd_box)
    pyautogui.click(center_minecraft_cmd_box)
    pyautogui.click(center_minecraft_cmd_box)

    #커맨드블럭 명령어 입력 후 닫기
    time.sleep(0.3)
    pyautogui.write(mccmdstr) #명령어 붙여넣기
    time.sleep(0.3)
    original_minecraft_cmd_ok = pyautogui.locateOnScreen('mcCMDok.png')
    center_minecraft_cmd_ok = pyautogui.center(original_minecraft_cmd_ok)
    center_minecraft_cmd_ok_x = center_minecraft_cmd_ok.x
    center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y - 30
    pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼보다 좀 더 위로 마우스 설정
    pyautogui.click(button='left') #클릭하여 윈도우 전환
    center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y
    pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼으로 위치설정
    pyautogui.click(button='left') #완료버튼 눌러 커맨드블럭 창 나가기
    #time.sleep(0.2)

    # 마인크래프트에서 커맨드블록 주변에 레드스톤 횃불을 설치한다.
    pyautogui.moveRel(0, 35, 1)  #3번째 인자는 소수로도 사용할 수 있음!
    pyautogui.click(button='right')
    pyautogui.moveRel(55, -85, 1)
    pyautogui.click(button='right')

    # 마인크래프트에서 커맨드블록 주변의 레드스톤 횃불을 제거한다.
    time.sleep(1)
    pyautogui.click(button='left')
    pyautogui.moveRel(-55, 85, 1)
    pyautogui.click(button='left')
    pyautogui.moveRel(0, -35, 1)

    # 마인크래프트에서 커맨드블럭을 제거하고 다시 설치한다.
    pyautogui.click(button='left')
    pyautogui.scroll(-1) #마크 2번슬롯 이동
    pyautogui.click(button='right')
    pyautogui.scroll(1) #마크 1번슬롯 이동

    # 마인크래프트에서 커맨드블럭 입력창으로 다시 들어간다.(윈도우로 마우스커서전환 하기 위함)
    pyautogui.click(button='right')

    sys_now_cmdnum += 1
    if sys_now_cmdnum >= user_max_cmdnum: #유저가 입력한 수만큼 작업했을경우
        msgbox.showinfo("알림","작업이 완료되었습니다.")
        sys.exit() #프로그램 종료

#[10]-------------------------------------------------------------------------------------------------------------
# < 151번명령어에서 172번명령어까지 반복 >
cmdnum_next_position_x = cmdnum_first_position.x - (34*4)
cmdnum_next_position_y += 15
pyautogui.moveTo(cmdnum_next_position_x, cmdnum_next_position_y)
pyautogui.click(button='left')

original_cmdmsgbox = pyautogui.locateOnScreen('commandBox.png')
center_cmdmsgbox = pyautogui.center(original_cmdmsgbox)
pyautogui.click(center_cmdmsgbox)
time.sleep(0.2)
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.2)
mccmdstr = pyperclip.paste()
time.sleep(0.3) #명령어 복사

# 마인크래프트 커맨드블럭 명령어 입력칸으로 이동
original_minecraft_cmd_box = pyautogui.locateOnScreen('mcCMDbox.png')
center_minecraft_cmd_box = pyautogui.center(original_minecraft_cmd_box)
pyautogui.click(center_minecraft_cmd_box)
pyautogui.click(center_minecraft_cmd_box)

#커맨드블럭 명령어 입력 후 닫기
time.sleep(0.3)
pyautogui.write(mccmdstr) #명령어 붙여넣기
time.sleep(0.3)
original_minecraft_cmd_ok = pyautogui.locateOnScreen('mcCMDok.png')
center_minecraft_cmd_ok = pyautogui.center(original_minecraft_cmd_ok)
center_minecraft_cmd_ok_x = center_minecraft_cmd_ok.x
center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y - 30
pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼보다 좀 더 위로 마우스 설정
pyautogui.click(button='left') #클릭하여 윈도우 전환
center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y
pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼으로 위치설정
pyautogui.click(button='left') #완료버튼 눌러 커맨드블럭 창 나가기
#time.sleep(0.2)

# 마인크래프트에서 커맨드블록 주변에 레드스톤 횃불을 설치한다.
pyautogui.moveRel(0, 35, 1)  #3번째 인자는 소수로도 사용할 수 있음!
pyautogui.click(button='right')
pyautogui.moveRel(55, -85, 1)
pyautogui.click(button='right')

# 마인크래프트에서 커맨드블록 주변의 레드스톤 횃불을 제거한다.
time.sleep(1)
pyautogui.click(button='left')
pyautogui.moveRel(-55, 85, 1)
pyautogui.click(button='left')
pyautogui.moveRel(0, -33, 1)

# 마인크래프트에서 커맨드블럭을 제거하고 다시 설치한다.
pyautogui.click(button='left')
pyautogui.scroll(-1) #마크 2번슬롯 이동
pyautogui.click(button='right')
pyautogui.scroll(1) #마크 1번슬롯 이동

# 마인크래프트에서 커맨드블럭 입력창으로 다시 들어간다.(윈도우로 마우스커서전환 하기 위함)
pyautogui.click(button='right')

sys_now_cmdnum += 1
if sys_now_cmdnum >= user_max_cmdnum: #유저가 입력한 수만큼 작업했을경우
    msgbox.showinfo("알림","작업이 완료되었습니다.")
    sys.exit() #프로그램 종료

# 152번명령어칸 부터 172번명령어칸까지 반복 시작 >>
for i in range(152,173):
    cmdnum_next_position_x += 43.8
    pyautogui.moveTo(cmdnum_next_position_x, cmdnum_next_position_y)
    pyautogui.click(button='left')

    original_cmdmsgbox = pyautogui.locateOnScreen('commandBox.png')
    center_cmdmsgbox = pyautogui.center(original_cmdmsgbox)
    pyautogui.click(center_cmdmsgbox)
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.2)
    mccmdstr = pyperclip.paste()
    time.sleep(0.3) #명령어 복사

    # 마인크래프트 커맨드블럭 명령어 입력칸으로 이동
    original_minecraft_cmd_box = pyautogui.locateOnScreen('mcCMDbox.png')
    center_minecraft_cmd_box = pyautogui.center(original_minecraft_cmd_box)
    pyautogui.click(center_minecraft_cmd_box)
    pyautogui.click(center_minecraft_cmd_box)

    #커맨드블럭 명령어 입력 후 닫기
    time.sleep(0.3)
    pyautogui.write(mccmdstr) #명령어 붙여넣기
    time.sleep(0.3)
    original_minecraft_cmd_ok = pyautogui.locateOnScreen('mcCMDok.png')
    center_minecraft_cmd_ok = pyautogui.center(original_minecraft_cmd_ok)
    center_minecraft_cmd_ok_x = center_minecraft_cmd_ok.x
    center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y - 30
    pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼보다 좀 더 위로 마우스 설정
    pyautogui.click(button='left') #클릭하여 윈도우 전환
    center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y
    pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼으로 위치설정
    pyautogui.click(button='left') #완료버튼 눌러 커맨드블럭 창 나가기
    #time.sleep(0.2)

    # 마인크래프트에서 커맨드블록 주변에 레드스톤 횃불을 설치한다.
    pyautogui.moveRel(0, 35, 1)  #3번째 인자는 소수로도 사용할 수 있음!
    pyautogui.click(button='right')
    pyautogui.moveRel(55, -85, 1)
    pyautogui.click(button='right')

    # 마인크래프트에서 커맨드블록 주변의 레드스톤 횃불을 제거한다.
    time.sleep(1)
    pyautogui.click(button='left')
    pyautogui.moveRel(-55, 85, 1)
    pyautogui.click(button='left')
    pyautogui.moveRel(0, -35, 1)

    # 마인크래프트에서 커맨드블럭을 제거하고 다시 설치한다.
    pyautogui.click(button='left')
    pyautogui.scroll(-1) #마크 2번슬롯 이동
    pyautogui.click(button='right')
    pyautogui.scroll(1) #마크 1번슬롯 이동

    # 마인크래프트에서 커맨드블럭 입력창으로 다시 들어간다.(윈도우로 마우스커서전환 하기 위함)
    pyautogui.click(button='right')

    sys_now_cmdnum += 1
    if sys_now_cmdnum >= user_max_cmdnum: #유저가 입력한 수만큼 작업했을경우
        msgbox.showinfo("알림","작업이 완료되었습니다.")
        sys.exit() #프로그램 종료

#[11]-------------------------------------------------------------------------------------------------------------
# < 173번명령어에서 194번명령어까지 반복 >
cmdnum_next_position_x = cmdnum_first_position.x - (34*4)
cmdnum_next_position_y += 15
pyautogui.moveTo(cmdnum_next_position_x, cmdnum_next_position_y)
pyautogui.click(button='left')

original_cmdmsgbox = pyautogui.locateOnScreen('commandBox.png')
center_cmdmsgbox = pyautogui.center(original_cmdmsgbox)
pyautogui.click(center_cmdmsgbox)
time.sleep(0.2)
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.2)
mccmdstr = pyperclip.paste()
time.sleep(0.3) #명령어 복사

# 마인크래프트 커맨드블럭 명령어 입력칸으로 이동
original_minecraft_cmd_box = pyautogui.locateOnScreen('mcCMDbox.png')
center_minecraft_cmd_box = pyautogui.center(original_minecraft_cmd_box)
pyautogui.click(center_minecraft_cmd_box)
pyautogui.click(center_minecraft_cmd_box)

#커맨드블럭 명령어 입력 후 닫기
time.sleep(0.3)
pyautogui.write(mccmdstr) #명령어 붙여넣기
time.sleep(0.3)
original_minecraft_cmd_ok = pyautogui.locateOnScreen('mcCMDok.png')
center_minecraft_cmd_ok = pyautogui.center(original_minecraft_cmd_ok)
center_minecraft_cmd_ok_x = center_minecraft_cmd_ok.x
center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y - 30
pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼보다 좀 더 위로 마우스 설정
pyautogui.click(button='left') #클릭하여 윈도우 전환
center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y
pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼으로 위치설정
pyautogui.click(button='left') #완료버튼 눌러 커맨드블럭 창 나가기
#time.sleep(0.2)

# 마인크래프트에서 커맨드블록 주변에 레드스톤 횃불을 설치한다.
pyautogui.moveRel(0, 35, 1)  #3번째 인자는 소수로도 사용할 수 있음!
pyautogui.click(button='right')
pyautogui.moveRel(55, -85, 1)
pyautogui.click(button='right')

# 마인크래프트에서 커맨드블록 주변의 레드스톤 횃불을 제거한다.
time.sleep(1)
pyautogui.click(button='left')
pyautogui.moveRel(-55, 85, 1)
pyautogui.click(button='left')
pyautogui.moveRel(0, -32, 1)

# 마인크래프트에서 커맨드블럭을 제거하고 다시 설치한다.
pyautogui.click(button='left')
pyautogui.scroll(-1) #마크 2번슬롯 이동
pyautogui.click(button='right')
pyautogui.scroll(1) #마크 1번슬롯 이동

# 마인크래프트에서 커맨드블럭 입력창으로 다시 들어간다.(윈도우로 마우스커서전환 하기 위함)
pyautogui.click(button='right')

sys_now_cmdnum += 1
if sys_now_cmdnum >= user_max_cmdnum: #유저가 입력한 수만큼 작업했을경우
    msgbox.showinfo("알림","작업이 완료되었습니다.")
    sys.exit() #프로그램 종료

# 174번명령어칸 부터 194번명령어칸까지 반복 시작 >>
for i in range(174,195):
    cmdnum_next_position_x += 43.8
    pyautogui.moveTo(cmdnum_next_position_x, cmdnum_next_position_y)
    pyautogui.click(button='left')

    original_cmdmsgbox = pyautogui.locateOnScreen('commandBox.png')
    center_cmdmsgbox = pyautogui.center(original_cmdmsgbox)
    pyautogui.click(center_cmdmsgbox)
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.2)
    mccmdstr = pyperclip.paste()
    time.sleep(0.3) #명령어 복사

    # 마인크래프트 커맨드블럭 명령어 입력칸으로 이동
    original_minecraft_cmd_box = pyautogui.locateOnScreen('mcCMDbox.png')
    center_minecraft_cmd_box = pyautogui.center(original_minecraft_cmd_box)
    pyautogui.click(center_minecraft_cmd_box)
    pyautogui.click(center_minecraft_cmd_box)

    #커맨드블럭 명령어 입력 후 닫기
    time.sleep(0.3)
    pyautogui.write(mccmdstr) #명령어 붙여넣기
    time.sleep(0.3)
    original_minecraft_cmd_ok = pyautogui.locateOnScreen('mcCMDok.png')
    center_minecraft_cmd_ok = pyautogui.center(original_minecraft_cmd_ok)
    center_minecraft_cmd_ok_x = center_minecraft_cmd_ok.x
    center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y - 30
    pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼보다 좀 더 위로 마우스 설정
    pyautogui.click(button='left') #클릭하여 윈도우 전환
    center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y
    pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼으로 위치설정
    pyautogui.click(button='left') #완료버튼 눌러 커맨드블럭 창 나가기
    #time.sleep(0.2)

    # 마인크래프트에서 커맨드블록 주변에 레드스톤 횃불을 설치한다.
    pyautogui.moveRel(0, 35, 1)  #3번째 인자는 소수로도 사용할 수 있음!
    pyautogui.click(button='right')
    pyautogui.moveRel(55, -85, 1)
    pyautogui.click(button='right')

    # 마인크래프트에서 커맨드블록 주변의 레드스톤 횃불을 제거한다.
    time.sleep(1)
    pyautogui.click(button='left')
    pyautogui.moveRel(-55, 85, 1)
    pyautogui.click(button='left')
    pyautogui.moveRel(0, -35, 1)

    # 마인크래프트에서 커맨드블럭을 제거하고 다시 설치한다.
    pyautogui.click(button='left')
    pyautogui.scroll(-1) #마크 2번슬롯 이동
    pyautogui.click(button='right')
    pyautogui.scroll(1) #마크 1번슬롯 이동

    # 마인크래프트에서 커맨드블럭 입력창으로 다시 들어간다.(윈도우로 마우스커서전환 하기 위함)
    pyautogui.click(button='right')

    sys_now_cmdnum += 1
    if sys_now_cmdnum >= user_max_cmdnum: #유저가 입력한 수만큼 작업했을경우
        msgbox.showinfo("알림","작업이 완료되었습니다.")
        sys.exit() #프로그램 종료

#[12]-------------------------------------------------------------------------------------------------------------
# < 195번명령어에서 216번명령어까지 반복 >
cmdnum_next_position_x = cmdnum_first_position.x - (34*4)
cmdnum_next_position_y += 15
pyautogui.moveTo(cmdnum_next_position_x, cmdnum_next_position_y)
pyautogui.click(button='left')

original_cmdmsgbox = pyautogui.locateOnScreen('commandBox.png')
center_cmdmsgbox = pyautogui.center(original_cmdmsgbox)
pyautogui.click(center_cmdmsgbox)
time.sleep(0.2)
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.2)
mccmdstr = pyperclip.paste()
time.sleep(0.3) #명령어 복사

# 마인크래프트 커맨드블럭 명령어 입력칸으로 이동
original_minecraft_cmd_box = pyautogui.locateOnScreen('mcCMDbox.png')
center_minecraft_cmd_box = pyautogui.center(original_minecraft_cmd_box)
pyautogui.click(center_minecraft_cmd_box)
pyautogui.click(center_minecraft_cmd_box)

#커맨드블럭 명령어 입력 후 닫기
time.sleep(0.3)
pyautogui.write(mccmdstr) #명령어 붙여넣기
time.sleep(0.3)
original_minecraft_cmd_ok = pyautogui.locateOnScreen('mcCMDok.png')
center_minecraft_cmd_ok = pyautogui.center(original_minecraft_cmd_ok)
center_minecraft_cmd_ok_x = center_minecraft_cmd_ok.x
center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y - 30
pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼보다 좀 더 위로 마우스 설정
pyautogui.click(button='left') #클릭하여 윈도우 전환
center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y
pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼으로 위치설정
pyautogui.click(button='left') #완료버튼 눌러 커맨드블럭 창 나가기
#time.sleep(0.2)

# 마인크래프트에서 커맨드블록 주변에 레드스톤 횃불을 설치한다.
pyautogui.moveRel(0, 35, 1)  #3번째 인자는 소수로도 사용할 수 있음!
pyautogui.click(button='right')
pyautogui.moveRel(55, -85, 1)
pyautogui.click(button='right')

# 마인크래프트에서 커맨드블록 주변의 레드스톤 횃불을 제거한다.
time.sleep(1)
pyautogui.click(button='left')
pyautogui.moveRel(-55, 85, 1)
pyautogui.click(button='left')
pyautogui.moveRel(0, -32, 1)

# 마인크래프트에서 커맨드블럭을 제거하고 다시 설치한다.
pyautogui.click(button='left')
pyautogui.scroll(-1) #마크 2번슬롯 이동
pyautogui.click(button='right')
pyautogui.scroll(1) #마크 1번슬롯 이동

# 마인크래프트에서 커맨드블럭 입력창으로 다시 들어간다.(윈도우로 마우스커서전환 하기 위함)
pyautogui.click(button='right')

sys_now_cmdnum += 1
if sys_now_cmdnum >= user_max_cmdnum: #유저가 입력한 수만큼 작업했을경우
    msgbox.showinfo("알림","작업이 완료되었습니다.")
    sys.exit() #프로그램 종료

# 196번명령어칸 부터 216번명령어칸까지 반복 시작 >>
for i in range(196,217):
    cmdnum_next_position_x += 43.8
    pyautogui.moveTo(cmdnum_next_position_x, cmdnum_next_position_y)
    pyautogui.click(button='left')

    original_cmdmsgbox = pyautogui.locateOnScreen('commandBox.png')
    center_cmdmsgbox = pyautogui.center(original_cmdmsgbox)
    pyautogui.click(center_cmdmsgbox)
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.2)
    mccmdstr = pyperclip.paste()
    time.sleep(0.3) #명령어 복사

    # 마인크래프트 커맨드블럭 명령어 입력칸으로 이동
    original_minecraft_cmd_box = pyautogui.locateOnScreen('mcCMDbox.png')
    center_minecraft_cmd_box = pyautogui.center(original_minecraft_cmd_box)
    pyautogui.click(center_minecraft_cmd_box)
    pyautogui.click(center_minecraft_cmd_box)

    #커맨드블럭 명령어 입력 후 닫기
    time.sleep(0.3)
    pyautogui.write(mccmdstr) #명령어 붙여넣기
    time.sleep(0.3)
    original_minecraft_cmd_ok = pyautogui.locateOnScreen('mcCMDok.png')
    center_minecraft_cmd_ok = pyautogui.center(original_minecraft_cmd_ok)
    center_minecraft_cmd_ok_x = center_minecraft_cmd_ok.x
    center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y - 30
    pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼보다 좀 더 위로 마우스 설정
    pyautogui.click(button='left') #클릭하여 윈도우 전환
    center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y
    pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼으로 위치설정
    pyautogui.click(button='left') #완료버튼 눌러 커맨드블럭 창 나가기
    #time.sleep(0.2)

    # 마인크래프트에서 커맨드블록 주변에 레드스톤 횃불을 설치한다.
    pyautogui.moveRel(0, 35, 1)  #3번째 인자는 소수로도 사용할 수 있음!
    pyautogui.click(button='right')
    pyautogui.moveRel(55, -85, 1)
    pyautogui.click(button='right')

    # 마인크래프트에서 커맨드블록 주변의 레드스톤 횃불을 제거한다.
    time.sleep(1)
    pyautogui.click(button='left')
    pyautogui.moveRel(-55, 85, 1)
    pyautogui.click(button='left')
    pyautogui.moveRel(0, -35, 1)

    # 마인크래프트에서 커맨드블럭을 제거하고 다시 설치한다.
    pyautogui.click(button='left')
    pyautogui.scroll(-1) #마크 2번슬롯 이동
    pyautogui.click(button='right')
    pyautogui.scroll(1) #마크 1번슬롯 이동

    # 마인크래프트에서 커맨드블럭 입력창으로 다시 들어간다.(윈도우로 마우스커서전환 하기 위함)
    pyautogui.click(button='right')

    sys_now_cmdnum += 1
    if sys_now_cmdnum >= user_max_cmdnum: #유저가 입력한 수만큼 작업했을경우
        msgbox.showinfo("알림","작업이 완료되었습니다.")
        sys.exit() #프로그램 종료

#[13]-------------------------------------------------------------------------------------------------------------
# < 217번명령어에서 238번명령어까지 반복 >
cmdnum_next_position_x = cmdnum_first_position.x - (34*4)
cmdnum_next_position_y += 15
pyautogui.moveTo(cmdnum_next_position_x, cmdnum_next_position_y)
pyautogui.click(button='left')

original_cmdmsgbox = pyautogui.locateOnScreen('commandBox.png')
center_cmdmsgbox = pyautogui.center(original_cmdmsgbox)
pyautogui.click(center_cmdmsgbox)
time.sleep(0.2)
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.2)
mccmdstr = pyperclip.paste()
time.sleep(0.3) #명령어 복사

# 마인크래프트 커맨드블럭 명령어 입력칸으로 이동
original_minecraft_cmd_box = pyautogui.locateOnScreen('mcCMDbox.png')
center_minecraft_cmd_box = pyautogui.center(original_minecraft_cmd_box)
pyautogui.click(center_minecraft_cmd_box)
pyautogui.click(center_minecraft_cmd_box)

#커맨드블럭 명령어 입력 후 닫기
time.sleep(0.3)
pyautogui.write(mccmdstr) #명령어 붙여넣기
time.sleep(0.3)
original_minecraft_cmd_ok = pyautogui.locateOnScreen('mcCMDok.png')
center_minecraft_cmd_ok = pyautogui.center(original_minecraft_cmd_ok)
center_minecraft_cmd_ok_x = center_minecraft_cmd_ok.x
center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y - 30
pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼보다 좀 더 위로 마우스 설정
pyautogui.click(button='left') #클릭하여 윈도우 전환
center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y
pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼으로 위치설정
pyautogui.click(button='left') #완료버튼 눌러 커맨드블럭 창 나가기
#time.sleep(0.2)

# 마인크래프트에서 커맨드블록 주변에 레드스톤 횃불을 설치한다.
pyautogui.moveRel(0, 35, 1)  #3번째 인자는 소수로도 사용할 수 있음!
pyautogui.click(button='right')
pyautogui.moveRel(55, -85, 1)
pyautogui.click(button='right')

# 마인크래프트에서 커맨드블록 주변의 레드스톤 횃불을 제거한다.
time.sleep(1)
pyautogui.click(button='left')
pyautogui.moveRel(-55, 85, 1)
pyautogui.click(button='left')
pyautogui.moveRel(0, -32, 1)

# 마인크래프트에서 커맨드블럭을 제거하고 다시 설치한다.
pyautogui.click(button='left')
pyautogui.scroll(-1) #마크 2번슬롯 이동
pyautogui.click(button='right')
pyautogui.scroll(1) #마크 1번슬롯 이동

# 마인크래프트에서 커맨드블럭 입력창으로 다시 들어간다.(윈도우로 마우스커서전환 하기 위함)
pyautogui.click(button='right')

sys_now_cmdnum += 1
if sys_now_cmdnum >= user_max_cmdnum: #유저가 입력한 수만큼 작업했을경우
    msgbox.showinfo("알림","작업이 완료되었습니다.")
    sys.exit() #프로그램 종료

# 218번명령어칸 부터 238번명령어칸까지 반복 시작 >>
for i in range(218,239):
    cmdnum_next_position_x += 43.8
    pyautogui.moveTo(cmdnum_next_position_x, cmdnum_next_position_y)
    pyautogui.click(button='left')

    original_cmdmsgbox = pyautogui.locateOnScreen('commandBox.png')
    center_cmdmsgbox = pyautogui.center(original_cmdmsgbox)
    pyautogui.click(center_cmdmsgbox)
    time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.2)
    mccmdstr = pyperclip.paste()
    time.sleep(0.3) #명령어 복사

    # 마인크래프트 커맨드블럭 명령어 입력칸으로 이동
    original_minecraft_cmd_box = pyautogui.locateOnScreen('mcCMDbox.png')
    center_minecraft_cmd_box = pyautogui.center(original_minecraft_cmd_box)
    pyautogui.click(center_minecraft_cmd_box)
    pyautogui.click(center_minecraft_cmd_box)

    #커맨드블럭 명령어 입력 후 닫기
    time.sleep(0.3)
    pyautogui.write(mccmdstr) #명령어 붙여넣기
    time.sleep(0.3)
    original_minecraft_cmd_ok = pyautogui.locateOnScreen('mcCMDok.png')
    center_minecraft_cmd_ok = pyautogui.center(original_minecraft_cmd_ok)
    center_minecraft_cmd_ok_x = center_minecraft_cmd_ok.x
    center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y - 30
    pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼보다 좀 더 위로 마우스 설정
    pyautogui.click(button='left') #클릭하여 윈도우 전환
    center_minecraft_cmd_ok_y = center_minecraft_cmd_ok.y
    pyautogui.moveTo(center_minecraft_cmd_ok_x, center_minecraft_cmd_ok_y) #마크 커맨드블럭 '완료'버튼으로 위치설정
    pyautogui.click(button='left') #완료버튼 눌러 커맨드블럭 창 나가기
    #time.sleep(0.2)

    # 마인크래프트에서 커맨드블록 주변에 레드스톤 횃불을 설치한다.
    pyautogui.moveRel(0, 35, 1)  #3번째 인자는 소수로도 사용할 수 있음!
    pyautogui.click(button='right')
    pyautogui.moveRel(55, -85, 1)
    pyautogui.click(button='right')

    # 마인크래프트에서 커맨드블록 주변의 레드스톤 횃불을 제거한다.
    time.sleep(1)
    pyautogui.click(button='left')
    pyautogui.moveRel(-55, 85, 1)
    pyautogui.click(button='left')
    pyautogui.moveRel(0, -35, 1)

    # 마인크래프트에서 커맨드블럭을 제거하고 다시 설치한다.
    pyautogui.click(button='left')
    pyautogui.scroll(-1) #마크 2번슬롯 이동
    pyautogui.click(button='right')
    pyautogui.scroll(1) #마크 1번슬롯 이동

    # 마인크래프트에서 커맨드블럭 입력창으로 다시 들어간다.(윈도우로 마우스커서전환 하기 위함)
    pyautogui.click(button='right')

    sys_now_cmdnum += 1
    if sys_now_cmdnum >= user_max_cmdnum: #유저가 입력한 수만큼 작업했을경우
        msgbox.showinfo("알림","작업이 완료되었습니다.")
        sys.exit() #프로그램 종료