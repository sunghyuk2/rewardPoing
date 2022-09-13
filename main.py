import tkinter as tk
from tkinter import ttk


def set_init(win):
    win.title("회원 관리 프로그램")
    win.geometry("500x500+200+200")
    win.resizable(True, True)

def set_menubar(win):
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

def set_main_view(win):

    # ===================
    # 검색창 프레임 생성 및 배치
    frame_search = ttk.Frame(win, relief="solid")
    frame_search.pack(fill="x", padx=5, ipadx=5, ipady=5)

    # 검색창에 필요한 위젯
    label_search = ttk.Label(frame_search, text="회원 검색")
    entry_search = ttk.Entry(frame_search)
    button_search = ttk.Button(frame_search, text="검색")

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





if __name__ == "__main__":
   root = tk.Tk()
   set_init(root)
   set_menubar(root)
   set_main_view(root)
   root.mainloop()

