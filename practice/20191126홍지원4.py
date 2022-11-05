print("기차를 차고 이동하려고 한다.")
print("해당 도시를 입력하시오")
print("지역A. 대전, 대구, 전주 : 10,000원")
print("지역B. 창원, 광주 : 20,000원")
print("지역C. 여수, 목포, 부산 : 30,000원")
print("지역D. 기타지역 : 5,000원")

def train_ticket(d):
    if d == "대전" or d=="대구" or d=="전주":
        p="10,000원"
    elif d== "창원" or d=="광주":
        p="20,000원"
    elif d== "여수" or d=="목포" or d=="부산":
        p="30,000원"
    else:
        p="5,000원"
    print("도착지",d,"가격:",p)

ticket=str(input("목적지가 어디입니까?"))
train_ticket(ticket)

           
