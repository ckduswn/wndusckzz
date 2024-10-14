# 메뉴 출력 가능
def print_menu(menu:dict, menu_cnt:int):  # dict:menu, int:count
     for i in range(1, menu_cnt+1):       # 1, 2, 3
         print(f"** {i}.{menu[i]}")
 
 # 메뉴 선택 기능
def select_menu(menu_cnt:int) -> int:
    while True:
        order = int(input(">> 메뉴: ")) 
        if order > menu_cnt or order < 1: 
            print(">> WARNING : 올바른 번호를 입력해 주세요.")
        else:
            break
    return order