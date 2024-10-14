## Project     : 별다방조선
## Writer      : 굴히온앤온
## Company     : 조선대학교
## Reg_Date    : 2024.10.14
## Update_data : 2024.10.14
## License     :
## Contents    : 콘솔 프로그래밍을 활용한 커피 전문점에서 사용하는 키오스크 개발


# Kiosk

# 1. 메인 메뉴 출력 : 커피, 스무디, 베이커리
# 2. 메인 메뉴 선택 : 사용자
# 3. 서브 메뉴 출력 : 커피, 스무디, 베이커리
# 4. 서브 메뉴 선택 : 사용자
# 5. 고객 주문 메뉴 목록에 저장 : 선택한 서브 메뉴 #오늘끗
# 6. 추가 주문 여부? : yes or no # 숙제(않되..!)
# 7-1. yes : 1번으로 보내기
# 7-2. no : 최종주문 내역으로 보내기
# 8. 최종주문 내역 출력



from service_kiosk import print_menu, select_menu


################
## 메뉴 만들기 ##
################

main_menu = {
    1 : "coffee",
    2 : "smoothie",
    3 : "bakery"
}

coffee_menu = {
    1 : "americano",
    2 : "espresso"
}

coffee_price = {
    1 : 3500,
    2 : 4000
}

smoothie_menu = {
    1 : "Kiwi smoothie",
    2 : "Banana smoothie",
    3 : "Blueberry smoothie",
    4 : "Strawberry smoothie"
}

smoothie_price = {
    1 : 6000,
    2 : 6000,
    3 : 6000,
    4 : 6000
}

bakery_menu = {
    1 : "cloud bread",
    2 : "crepe cake",
    3 : "tiramisu"
}

bakery_price = {
    1 : 3500,
    2 : 4500,
    3 : 6500,
}


order_list = []     # 고객 주문 기록

while True:
## 1. 메인메뉴 출력
    print("*"*50)
    print("** 별다방조선")
    print_menu(main_menu, 3)


    ## 2. 메인메뉴 선택
    order = select_menu(3)
    
    ## 3. 서브메뉴 출력
    if order == 1:  #coffee
        print_menu(coffee_menu, 2) 
        sub_order = select_menu(2) 
        # [[menu, price], [menu, price]]
        order_list.append([coffee_menu[sub_order], coffee_price[sub_order]])
    elif order == 2:  #smoothie
        print_menu(smoothie_menu, 4) 
        sub_order = select_menu(4)         
        order_list.append([smoothie_menu[sub_order], smoothie_price[sub_order]])
    elif order == 3:  #bakery
        print_menu(bakery_menu, 3) 
        sub_order = select_menu(3)         
        order_list.append([bakery_menu[sub_order], bakery_price[sub_order]])

# 6번 추가 주문하시겠습니까? -> input()
# 결과 y/n
# y : 1번으로 이동
# n : 출력("주문 페이지로 이동합니다.")

    plus = input("추가 주문하시겠습니까?\n")
    if plus == 'y':
        print_menu(main_menu, 3)
    if plus == 'n':
        print("주문 페이지로 이동합니다..")
    

    for item in order_list:
        print(f"주문기록: {item}")


