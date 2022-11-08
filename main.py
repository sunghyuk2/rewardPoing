import tkinter as tk
from tkinter import ttk, messagebox
import pickle


win = tk.Tk()
win.title("회원 관리 프로그램")
win.geometry("400x190+200+200")
win.resizable(False, False)

member_list = {}


custom_data= "data.pickle"
try :
    with open(custom_data, "rb") as fr:
        member_list = pickle.load(fr)
except Exception as e :
    member_list['이정국'] = {'전화번호': '010-1111-2222', '회원번호': 1, '누적금액': 0, '포인트': 0}
    print(e)

def use_point(name: str):
    """
    누적된 포인트를 사용한다.
    :param name: 회원이름
    :return: 없음
    """
    if name in member_list:
        if member_list[name]['포인트'] < 10000:
            messagebox.showinfo(title="에러", message=f"{name}님의 잔여 포인트가 부족합니다. (1만점 단위)", icon='warning')
            return

        member_list[name]['포인트'] -= 10000
        messagebox.showinfo(title="포인트 사용", message=f"{name}님 1만 포인트를 사용하였습니다")

        with open(custom_data,"wb") as fw:
            pickle.dump(member_list,fw)

        search_cmd(name)

def use_service(name: str, charge: int):
    """
    서비스 이용버튼. 누적금액과 포인트를 적립한다.
    :param name: 회원이름
    :param charge: 서비스 이용 금액
    :return: 없음
    """
    if name in member_list:
        point = int(charge/10)
        member_list[name]['누적금액'] += charge
        member_list[name]['포인트'] += point

        messagebox.showinfo(title="포인트 적립",message=f"{name}님 {point}점 적립 되었습니다.")

        with open(custom_data,"wb") as fw:
            pickle.dump(member_list,fw)


        search_cmd(name)

def search_cmd(name: str):
    """
    검색창에 회원이름을 적으면 검색해서 회원정보란에 값을 채워줌
    :param name: 회원이름
    :return: 없음
    """
    #print(name)
    #print(member_list[name])

    if name in member_list:
        entry_id.config(state="normal")
        entry_id.delete(0, "end")
        entry_id.insert(0, member_list[name]['회원번호'])
        entry_id.config(state="readonly")

        entry_name.config(state="normal")
        entry_name.delete(0, "end")
        entry_name.insert(0, name)
        entry_name.config(state="readonly")

        entry_number.config(state="normal")
        entry_number.delete(0, "end")
        entry_number.insert(0, member_list[name]['전화번호'])
        entry_number.config(state="readonly")

        entry_cumulative.config(state="normal")
        entry_cumulative.delete(0, "end")
        entry_cumulative.insert(0, member_list[name]['누적금액'])
        entry_cumulative.config(state="readonly")

        entry_mileage.config(state="normal")
        entry_mileage.delete(0, "end")
        entry_mileage.insert(0, member_list[name]['포인트'])
        entry_mileage.config(state="readonly")
    else:
        print("값이 없습니다")
        entry_id.config(state="normal")
        entry_id.delete(0, "end")

        entry_id.config(state="readonly")

        entry_name.config(state="normal")
        entry_name.delete(0, "end")

        entry_name.config(state="readonly")

        entry_number.config(state="normal")
        entry_number.delete(0, "end")

        entry_number.config(state="readonly")

        entry_cumulative.config(state="normal")
        entry_cumulative.delete(0, "end")

        entry_cumulative.config(state="readonly")

        entry_mileage.config(state="normal")
        entry_mileage.delete(0, "end")

        entry_mileage.config(state="readonly")

menubar = tk.Menu(win)
member_menu = tk.Menu(menubar, tearoff=0)
member_menu.add_command(label="회원가입")
member_menu.add_command(label="회원탈퇴")
member_menu.add_separator()
member_menu.add_command(label="환경설정")
member_menu.add_separator()
member_menu.add_command(label="종료")

info_menu = tk.Menu(menubar,tearoff=0)
info_menu.add_command(label="서비스 통계")
info_menu.add_separator()
info_menu.add_command(label="업데이트 확인")
info_menu.add_command(label="프로그램 정보")

menubar.add_cascade(label="회원관리",menu=member_menu)
menubar.add_cascade(label="정보", menu=info_menu)
win.config(menu=menubar)



    # ===================
    # 검색창 프레임 생성 및 배치
frame_search = ttk.Frame(win, relief="solid")
frame_search.pack(fill="x", padx=5, ipadx=5, ipady=5)

    # 검색창에 필요한 위젯
label_search = ttk.Label(frame_search, text="회원 검색")
entry_search = ttk.Entry(frame_search)
button_search = ttk.Button(frame_search, text="검색", command=lambda: search_cmd(entry_search.get()))

    # 검색창 내 위젯 배치
label_search.pack(side="left", padx=5)
entry_search.pack(side="left", padx=5,pady=5 , fill="x", expand= True)
button_search.pack(side="left",padx=5)

    # ======================================
    # 검색 결과 프레임 생성 및 배치
    # ======================================
frame_info = ttk.Frame(win, relief= "solid")
frame_info.pack(fill="x", padx=5, pady=5)
frame_info.grid_columnconfigure(1, weight=1)
frame_info.grid_columnconfigure(3, weight=1)
frame_info.grid_columnconfigure(3, weight=1)

    # 검색결과 내 필요 위젯
label_id = ttk.Label(frame_info, text="회원번호", relief="flat", anchor="e")
entry_id = ttk.Entry(frame_info, state="readonly", width=10)
label_name = ttk.Label(frame_info, text="이름", relief= "flat", anchor= "e")
entry_name = ttk.Entry(frame_info, state="readonly", width=10)
label_number = ttk.Label(frame_info, text="전화번호",relief="flat", anchor= "e")
entry_number = ttk.Entry(frame_info, state="readonly", width=10)
label_cumulative=ttk.Label(frame_info, text="누적금액", relief= "flat", anchor= "e")
entry_cumulative = ttk.Entry(frame_info, state="readonly", width=10)
label_mileage = ttk.Label(frame_info, text="포인트", relief= "flat", anchor= "e" )
entry_mileage = ttk.Entry(frame_info, state="readonly", width=10)


    # 검색결과 내 위젯 배치
label_id.grid(row=0, column=0, padx=5,pady=5, sticky="EW")
entry_id.grid(row=0, column=1, padx=5, pady=5, sticky="EW")
label_name.grid(row=0, column=2, padx=5, pady=5, sticky="EW")
entry_name.grid(row=0, column=3, padx=5, pady=5, sticky="EW")
label_number.grid(row=1, column=0, padx=5, pady=5, sticky="EW")
entry_number.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky="EW")
label_cumulative.grid(row=2, column=0, padx=5, pady=5, sticky="EW")
entry_cumulative.grid(row=2, column=1, padx=5, pady=5, sticky="EW")
label_mileage.grid(row=2, column=2, padx=5, pady=5, sticky="EW")
entry_mileage.grid(row=2, column=3, padx=5, pady=5, sticky="EW")

# ======================================
# 서비스 이용 버튼 프레임 생성 및 배치
frame_menu = ttk.Frame(win, relief= "solid")
frame_menu.pack(fill= "x", padx=5, pady=5)

# 서비스 이용버튼 내 필요 위젯
button_svc1 = ttk.Button(frame_menu, text="남성커트", command=lambda : use_service(name=entry_search.get(),charge=10000))
button_svc2 = ttk.Button(frame_menu, text="염색", command=lambda : use_service(name=entry_search.get(),charge=30000))
button_svc3 = ttk.Button(frame_menu, text="펌", command=lambda : use_service(name=entry_search.get(),charge=50000))
button_svc4 = ttk.Button(frame_menu, text="포인트 사용", command=lambda : use_point(name=entry_search.get()))

# 서비스 이용 버튼 내 위젯 배치
button_svc1.grid(row=0, column=0, padx=5, pady=5, sticky="EW")
button_svc2.grid(row=0, column=1, padx=5, pady=5, sticky="EW")
button_svc3.grid(row=0, column=2, padx=5, pady=5, sticky="EW")
button_svc4.grid(row=0, column=3, padx=5, pady=5, sticky="EW")

win.mainloop()


