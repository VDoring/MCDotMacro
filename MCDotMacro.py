# MCDotMacro by VDoring.
# 프로그램 버전:V0.2  (GitHub Release v0.1.1 - 코드 최적화 버전)
# Command Length 적정길이 : 2000 ~ 4000 예상(테스트필요)


#[0] 사용되는 라이브러리들---
import pyautogui # 키보드 마우스 매크로
import pyperclip # (pyautogui의 하위종속된 라이브러리?)
import tkinter.messagebox as msgbox # 알림창 띄우기
from tkinter import * # GUI 구현
import time # 딜레이 등의 시간조절
import sys # 프로그램 즉시종료 등의 기능이 있음


#[1] GUI 프로그램 창---
sys_now_cmdnum = 0 #프로그램에서 총 몇개의 명령어를 마크에 붙여넣었는지 저장
user_max_cmdnum = 0
is_exit = 0 #유저가 프로그램을 그냥 종료했는지 확인

root = Tk() #(root는 그냥 사용자가 임의로 설정할 수 있는 이름이다)
root.title("MCDotMacro v0.2 (멀티라인 버전)") # 창 제목
root.geometry("400x290+760+400") # 창 크기
root.resizable(False,False) # x,y 값 변경 불가(창 크기 변경불가)

gui_text_print1 = Label(root, text="< Mural Generator 전용 자동입력 프로그램 >",font=("함초롬돋움",14),bg="#C3E7FA") #일반 텍스트 출력
gui_text_print1.pack()
gui_text_print2 = Label(root, text="사용방법: https://github.com/VDoring/MCDotMacro",bg="#C3E7FA")
gui_text_print2.pack()
gui_text_print3 = Label(root, text="\n[팁]", fg="blue")
gui_text_print3.pack()
gui_text_print4 = Label(root, text="마우스를 왼쪽 위 끝까지 올리면 작업을 중지할 수 있습니다.")
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
    if user_max_cmdnum > 31 and user_max_cmdnum < 987:
        msgbox.showinfo("알림","확인버튼을 누르면 3초후 시작됩니다.")
        global is_exit #전역변수 사용
        is_exit = 1
        time.sleep(3)
        root.destroy()
    else:
        msgbox.showinfo("프로그램 실행 불가","값이 너무 작거나 큽니다.\n(동작가능한 값: 32~986)")

#프로그램을 시작할떄 사용하는 버튼
start_button = Button(root, padx=30, pady=5, text="입력", command=saveUserMaxCommandNumber)
start_button.pack()

root.mainloop() # 창이 닫히지 않도록 해준다(GUI 유지)

if is_exit == 0: #유저가 프로그램창을 그냥 종료했다면
    sys.exit() #프로그램 종료

#[1-1] 함수 셋팅---
def BlockSetMinus34_First(): 
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

    global sys_now_cmdnum
    sys_now_cmdnum += 1

def BlockSetMinus34():
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

    global sys_now_cmdnum
    sys_now_cmdnum += 1

def BlockSetMinus35():
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

    global sys_now_cmdnum
    sys_now_cmdnum += 1

def BlockSetMinus33():
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

    global sys_now_cmdnum
    sys_now_cmdnum += 1

def BlockSetMinus35_CanExit():
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

    global sys_now_cmdnum
    sys_now_cmdnum += 1
    if sys_now_cmdnum >= user_max_cmdnum: #유저가 입력한 수만큼 작업했을경우
        msgbox.showinfo("알림","작업이 완료되었습니다.")
        sys.exit() #프로그램 종료

def BlockSetMinus32_CanExit():
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

    global sys_now_cmdnum
    sys_now_cmdnum += 1
    if sys_now_cmdnum >= user_max_cmdnum: #유저가 입력한 수만큼 작업했을경우
        msgbox.showinfo("알림","작업이 완료되었습니다.")
        sys.exit() #프로그램 종료

def BlockSetMinus33_CanExit():
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

    global sys_now_cmdnum
    sys_now_cmdnum += 1
    if sys_now_cmdnum >= user_max_cmdnum: #유저가 입력한 수만큼 작업했을경우
        msgbox.showinfo("알림","작업이 완료되었습니다.")
        sys.exit() #프로그램 종료

def BlockSetMinus31_CanExit():
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

    global sys_now_cmdnum
    sys_now_cmdnum += 1
    if sys_now_cmdnum >= user_max_cmdnum: #유저가 입력한 수만큼 작업했을경우
        msgbox.showinfo("알림","작업이 완료되었습니다.")
        sys.exit() #프로그램 종료


def RecursiveBlockSetMinus31(start,end):
    cmdnum_next_position_x = cmdnum_first_position.x - (34*4)
    cmdnum_next_position_y += 15
    pyautogui.moveTo(cmdnum_next_position_x, cmdnum_next_position_y)
    pyautogui.click(button='left')
    BlockSetMinus31_CanExit()
    for i in range(start+1,end+1):
        cmdnum_next_position_x += 43.8
        pyautogui.moveTo(cmdnum_next_position_x, cmdnum_next_position_y)
        pyautogui.click(button='left')
        BlockSetMinus35_CanExit()

def RecursiveBlockSetMinus32(start,end):
    cmdnum_next_position_x = cmdnum_first_position.x - (34*4)
    cmdnum_next_position_y += 15
    pyautogui.moveTo(cmdnum_next_position_x, cmdnum_next_position_y)
    pyautogui.click(button='left')
    BlockSetMinus32_CanExit()
    for i in range(start+1,end+1):
        cmdnum_next_position_x += 43.8
        pyautogui.moveTo(cmdnum_next_position_x, cmdnum_next_position_y)
        pyautogui.click(button='left')
        BlockSetMinus35_CanExit()

def RecursiveBlockSetMinus33(start,end):
    cmdnum_next_position_x = cmdnum_first_position.x - (34*4)
    cmdnum_next_position_y += 15
    pyautogui.moveTo(cmdnum_next_position_x, cmdnum_next_position_y)
    pyautogui.click(button='left')
    BlockSetMinus33_CanExit()
    for i in range(start+1,end+1):
        cmdnum_next_position_x += 43.8
        pyautogui.moveTo(cmdnum_next_position_x, cmdnum_next_position_y)
        pyautogui.click(button='left')
        BlockSetMinus35_CanExit()

#[2] 1번쨰(최초) 동작---
original_1_selected = pyautogui.locateOnScreen('1selectedNXTLine.png')
if original_1_selected == None: #1번명령어칸 이미지가 다를떄 다른 이미지타입을 검사
    original_1_selected = pyautogui.locateOnScreen('1AnoselectedNXTLine.png')
center_1_selected = pyautogui.center(original_1_selected)
pyautogui.click(center_1_selected)
cmdnum_first_position = pyautogui.position() #1번명령어 버튼의 위치를 저장(다음라인의 명령어버튼 위치를 설정하기 위함)
BlockSetMinus34_First()

#[3] 2번쨰 동작---
original_nextnum_selected = pyautogui.locateOnScreen('2NXTLine.png')
if original_1_selected == None: #2번명령어칸 이미지가 다를떄 다른 이미지타입을 검사
    original_nextnum_selected = pyautogui.locateOnScreen('2AnoNXTLine.png')
center_nextnum_selected = pyautogui.center(original_nextnum_selected)
pyautogui.click(center_nextnum_selected) #2번명령어 클릭
cmdnum_prev_position = pyautogui.position() #2번명령어 마우스 위치값 저장(다음 명령어위치를 지정할때 사용)
BlockSetMinus34()

#[4] 3번쨰~9번째 동작---
for i in range(3,10):
    cmdnum_next_position_x = cmdnum_prev_position.x + 29
    cmdnum_next_position_y = cmdnum_prev_position.y
    pyautogui.moveTo(cmdnum_next_position_x, cmdnum_next_position_y)
    pyautogui.click(button='left')
    cmdnum_prev_position = pyautogui.position() #이전명령어 마우스 위치값 저장(다음 명령어위치를 지정할때 사용)
    BlockSetMinus35()

#[5] 10번쨰~25번쨰 동작---
for i in range(10,26):
    cmdnum_next_position_x += 36.5
    pyautogui.moveTo(cmdnum_next_position_x, cmdnum_next_position_y)
    pyautogui.click(button='left')
    BlockSetMinus35()
    
#[6] 26번쨰~52번쨰 동작---
cmdnum_next_position_x = cmdnum_first_position.x - (36.5*4)
cmdnum_next_position_y += 15
pyautogui.moveTo(cmdnum_next_position_x, cmdnum_next_position_y)
pyautogui.click(button='left')
BlockSetMinus33()
for i in range(27,53):
    cmdnum_next_position_x += 36.5
    pyautogui.moveTo(cmdnum_next_position_x, cmdnum_next_position_y)
    pyautogui.click(button='left')
    BlockSetMinus35_CanExit()

#[7] 53번째~79번째 동작---
cmdnum_next_position_x = cmdnum_first_position.x - (36.5*4)
cmdnum_next_position_y += 15
pyautogui.moveTo(cmdnum_next_position_x, cmdnum_next_position_y)
pyautogui.click(button='left')
BlockSetMinus32_CanExit()
for i in range(54,80):
    cmdnum_next_position_x += 36.5
    pyautogui.moveTo(cmdnum_next_position_x, cmdnum_next_position_y)
    pyautogui.click(button='left')
    BlockSetMinus35_CanExit()

#[8] 80번째~99번쨰 동작---
cmdnum_next_position_x = cmdnum_first_position.x - (36.5*4)
cmdnum_next_position_y += 15
pyautogui.moveTo(cmdnum_next_position_x, cmdnum_next_position_y)
pyautogui.click(button='left')
BlockSetMinus32_CanExit()
for i in range(81,100):
    cmdnum_next_position_x += 36.5
    pyautogui.moveTo(cmdnum_next_position_x, cmdnum_next_position_y)
    pyautogui.click(button='left')
    BlockSetMinus35_CanExit()

#[9] 100번쨰~105번쨰 동작---
cmdnum_next_position_x += 37
pyautogui.moveTo(cmdnum_next_position_x, cmdnum_next_position_y)
pyautogui.click(button='left')
BlockSetMinus33_CanExit()
for i in range(101,106):
    cmdnum_next_position_x += 45
    pyautogui.moveTo(cmdnum_next_position_x, cmdnum_next_position_y)
    pyautogui.click(button='left')
    BlockSetMinus35_CanExit()

#[10] 106번쨰~128번쨰 동작 <이후부터는 코드가 비슷하다>---
RecursiveBlockSetMinus31(106,128)

#[11] 129번째~150번째 동작
RecursiveBlockSetMinus32(129,150)

#[12] 151번쨰~172번쨰 동작
RecursiveBlockSetMinus33(151,172)

#[13] 173번째~194번쨰 동작
RecursiveBlockSetMinus32(173,194)

#[14] 195번째~216번째 동작
RecursiveBlockSetMinus32(195,216)

#[15] 217번쨰~238번쨰 동작
RecursiveBlockSetMinus32(217,238)

# 239~260---
RecursiveBlockSetMinus31(239,260)

# 261~282
RecursiveBlockSetMinus32(261,282)

# 283~304
RecursiveBlockSetMinus33(283,304)

# 305~326
RecursiveBlockSetMinus32(305,326)

# 327~348
RecursiveBlockSetMinus32(327,348)

# 349~370
RecursiveBlockSetMinus32(349,370)

# 371~392---
RecursiveBlockSetMinus31(371,392)

# 393~414
RecursiveBlockSetMinus32(393,414)

# 415~436
RecursiveBlockSetMinus33(415,436)

# 437~458
RecursiveBlockSetMinus32(437,458)

# 459~480
RecursiveBlockSetMinus32(459,480)

# 481~502
RecursiveBlockSetMinus32(481,502)

# 503~524---
RecursiveBlockSetMinus31(503,524)

# 525~546
RecursiveBlockSetMinus32(525,546)

# 547~568
RecursiveBlockSetMinus33(547,568)

# 569~590
RecursiveBlockSetMinus32(569,590)

# 591~612
RecursiveBlockSetMinus32(591,612)

# 613~634
RecursiveBlockSetMinus32(613,634)

# 635~656---
RecursiveBlockSetMinus31(635,656)

# 657~678
RecursiveBlockSetMinus32(657,678)

# 679~700
RecursiveBlockSetMinus33(679,700)

# 701~722
RecursiveBlockSetMinus32(701,722)

# 723~744
RecursiveBlockSetMinus32(723,744)

# 745~766
RecursiveBlockSetMinus32(745,766)

# 767~788---
RecursiveBlockSetMinus31(767,788)

# 789~810
RecursiveBlockSetMinus32(789,810)

# 811~832
RecursiveBlockSetMinus33(811,832)

# 833~854
RecursiveBlockSetMinus32(833,854)

# 855~876
RecursiveBlockSetMinus32(855,876)

# 877~898
RecursiveBlockSetMinus32(877,898)

# 899~920---
RecursiveBlockSetMinus31(899,920)

# 921~942
RecursiveBlockSetMinus32(921,942)

# 943~964
RecursiveBlockSetMinus33(943,964)

# 965~986
RecursiveBlockSetMinus32(965,986)

#필요시 추가예정