# 오리지널 커맨드블럭 부서짐 버그 해결버전    작동OK
# https://wikidocs.net/85581  가이드글1
# https://pynput.readthedocs.io/en/latest/keyboard.html 가이드글2

# Command Length 적정길이 : 4000 ~ 5000
# 잘 작동이 안된다면 길이를 더 줄여야 한다.


import pyautogui
#import pydirectinput
# from pynput.keyboard import Key, Controller
import pyperclip
import time
import sys

#[0]-------------------------------------------------------------------------------------------------------------
# 총 명령어 갯수 유저 입력


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
time.sleep(0.2)

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

#(명령어 붙어넣기 부분)---- 삽질이 많다..
#pyautogui.write('sample')
#pyautogui.keyDown('ctrl')
#pyautogui.keyDown('shift')
#pyautogui.press('left')
#pyautogui.keyUp('shift')
#pyautogui.keyUp('ctrl')

#pyautogui.hotkey('ctrl', 'v')
#time.sleep(0.3)

#pydirectinput.hotkey('ctrl', 'v')

#pyautogui.keyDown('ctrl')
#pyautogui.press('v')
#pyautogui.keyUp('ctrl')

#pydirectinput.keyDown('ctrl')
#pydirectinput.press('v')
#pydirectinput.keyUp('ctrl')

#keyboard = Controller()
#with keyboard.pressed(Key.ctrl):
#    keyboard.press('v')
#    keyboard.release('v')

#keyboard.press(Key.ctrl)
#keyboard.press('v')
#keyboard.release('v')
#keyboard.release(Key.ctrl)

#pyperclip.copy(cmdstr)
#time.sleep(0.2)
#pyautogui.hotkey('ctrl','v')

time.sleep(0.3)
pyautogui.write(mccmdstr)
time.sleep(0.3)

#----

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
time.sleep(0.5)
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
time.sleep(0.2) #명령어 복사

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
time.sleep(0.5)
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
    time.sleep(0.2) #명령어 복사

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
    time.sleep(0.5)
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
    time.sleep(0.2) #명령어 복사

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
    time.sleep(0.5)
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
time.sleep(0.2) #명령어 복사

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
time.sleep(0.5)
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
    time.sleep(0.2) #명령어 복사

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
    time.sleep(0.5)
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
time.sleep(0.2) #명령어 복사

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
time.sleep(0.5)
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
    time.sleep(0.2) #명령어 복사

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
    time.sleep(0.5)
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
time.sleep(0.2) #명령어 복사

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
time.sleep(0.5)
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
    time.sleep(0.2) #명령어 복사

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
    time.sleep(0.5)
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

    #[7]-------------------------------------------------------------------------------------------------------------
# < 100번명령어에서 105번명령어까지 반복 >