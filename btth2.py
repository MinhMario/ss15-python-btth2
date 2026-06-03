atm_vault_balance = 50000000
user_account_balance = 10000000


def display_balances():
    print("--- SỐ DƯ TÀI KHOẢN ---")
    print(f"Tài khoản của bạn: {user_account_balance:,} VND")
    print(f"(Debug) Tiền mặt trong ATM: {atm_vault_balance:,} VND")


def deposit_money(amount):
    global user_account_balance, atm_vault_balance
    user_account_balance += amount
    atm_vault_balance += amount
    return True


def check_withdrawal_rules(amount):
    fee = 1100
    total_deduction = amount + fee
    if total_deduction > user_account_balance:
        return "INSUFFICIENT_FUNDS"
    if amount > atm_vault_balance:
        return "ATM_OUT_OF_CASH"
    return "OK"


def execute_withdrawal(total_deduction, amount_to_dispense):
    global user_account_balance, atm_vault_balance
    user_account_balance -= total_deduction
    atm_vault_balance -= amount_to_dispense


while True:
    print("\n============= SMART ATM =============")
    print("1. Xem số dư")
    print("2. Nạp tiền")
    print("3. Rút tiền")
    print("4. Kết thúc giao dịch")
    print("=====================================")
    choice = input("Vui lòng chọn giao dịch (1-4): ").strip()

    if choice == '1':
        display_balances()

    elif choice == '2':
        print("--- NẠP TIỀN ---")
        amount_input = input("Nhập số tiền muốn nạp: ").strip()
        if not amount_input.isdigit():
            print("Số tiền không hợp lệ")
        else:
            amount = int(amount_input)
            if amount <= 0:
                print("Số tiền không hợp lệ")
            else:
                if deposit_money(amount):
                    print(f"Giao dịch thành công! Số dư tài khoản hiện tại: {user_account_balance:,} VND.")

    elif choice == '3':
        print("--- RÚT TIỀN ---")
        amount_input = input("Nhập số tiền cần rút: ").strip()
        if not amount_input.isdigit():
            print("Số tiền không hợp lệ")
        else:
            amount = int(amount_input)
            if amount <= 0:
                print("Số tiền không hợp lệ")
            elif amount % 50000 != 0:
                print("Số tiền rút phải là bội số của 50,000")
            else:
                status = check_withdrawal_rules(amount)
                if status == "INSUFFICIENT_FUNDS":
                    print("Giao dịch thất bại: Số dư tài khoản không đủ.")
                elif status == "ATM_OUT_OF_CASH":
                    print("Giao dịch thất bại: Máy ATM không đủ tiền mặt để phục vụ.")
                else:
                    fee = 1100
                    total_deduction = amount + fee
                    print("Giao dịch đang xử lý...")
                    execute_withdrawal(total_deduction, amount)
                    print(f"Phí giao dịch: {fee:,} VND")
                    print(f"Bạn đã rút thành công {amount:,} VND.")
                    print(f"Số dư tài khoản còn lại: {user_account_balance:,} VND.")

    elif choice == '4':
        print("Cảm ơn quý khách đã sử dụng dịch vụ!")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 4.")