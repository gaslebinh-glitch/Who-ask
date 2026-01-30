diction_list_of_Fruits_we_have = {
    "Apple": 50000,
    "Banana": 50000,
    "Orange": 42000,
    "Mango": 30000,
    "Grapes": 25000,
    "Pineapple": 20000,
    "Strawberry": 15000,
    "Watermelon": 60000,
}

def show_Fruits():
    print("Danh sách trái cây có sẵn:")
    for fruit, price in diction_list_of_Fruits_we_have.items():
        print(f"{fruit}: {price} VND")

def thanh_toán():
    total = 0
    while True:
        fruit = input("Nhập tên trái cây bạn muốn mua (hoặc 'xong' để kết thúc): ")
        if fruit.lower() == 'xong':
            break
        if fruit not in diction_list_of_Fruits_we_have:
            print("Không có loại trái cây này!")
            continue
        try:
            số_lượng = int(input(f"Bạn muốn mua bao nhiêu {fruit}?: "))
            if số_lượng < 0:
                print("Số lượng phải lớn hơn 0!")
                continue
        except ValueError:
            print("Vui lòng nhập số nguyên!")
            continue
        price = diction_list_of_Fruits_we_have[fruit]
        total = price * số_lượng
    print(f"Tổng số tiền bạn cần thanh toán là: {total} VND")
    ban_co = int(input("Nhập số tiền bạn có: "))
    tienthua = ban_co - total
while True:
    show_Fruits()
    choice = input("Bạn có muốn thanh toán không? (có/không): ")
    if choice.lower() == 'có':
        thanh_toán()
        print(f"Cảm ơn bạn đã mua hàng! Đây là tiền thừa của bạn: {tien_hua} VND")
    elif choice.lower() == 'không': 
        print("Cảm ơn bạn đã ghé thăm!")
        break 
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại.")
    print(f"Cảm ơn bạn đã mua hàng! Đây là tiền thừa của bạn: {tienthua} VND")
