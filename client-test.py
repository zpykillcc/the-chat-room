import socket
import threading
import json  # json.dumps(some)打包   json.loads(some)解包
import tkinter as tk
import tkinter.messagebox
from tkinter.scrolledtext import ScrolledText  # 导入多行文本框用到的包
import time
import requests
from tkinter import filedialog
import vachat
import os
from time import sleep
from PIL import ImageGrab,ImageTk,Image
from netifaces import interfaces, ifaddresses, AF_INET6

IP = ''
PORT = ''
user = ''
listbox1 = ''  # 用于显示在线用户的列表框
ii = 0  # 用于判断是开还是关闭列表框
users = []  # 在线用户列表
chat = '------Group chat-------'  # 聊天对象, 默认为群聊
# 登陆窗口
root1 = tkinter.Tk()
root1.title('Log in')
root1['height'] = 110
root1['width'] = 270
root1.resizable(0, 0)  # 限制窗口大小

IP1 = tkinter.StringVar()
IP1.set('127.0.0.1:50007')  # 默认显示的ip和端口
User = tkinter.StringVar()
User.set('')

# 服务器标签
labelIP = tkinter.Label(root1, text='Server address')
labelIP.place(x=20, y=10, width=100, height=20)

entryIP = tkinter.Entry(root1, width=80, textvariable=IP1)
entryIP.place(x=120, y=10, width=130, height=20)

# 用户名标签
labelUser = tkinter.Label(root1, text='Username')
labelUser.place(x=30, y=40, width=80, height=20)

entryUser = tkinter.Entry(root1, width=80, textvariable=User)
entryUser.place(x=120, y=40, width=130, height=20)


# 登录按钮
def login(*args):
    global IP, PORT, user
    IP, PORT = entryIP.get().split(':')  # 获取IP和端口号
    PORT = int(PORT)                     # 端口号需要为int类型
    user = entryUser.get()
    if not user:
        tkinter.messagebox.showerror(
            'Name type error', message='Username Empty!')
    else:
        root1.destroy()                  # 关闭窗口


root1.bind('<Return>', login)            # 回车绑定登录功能
but = tkinter.Button(root1, text='登录', command=login)
but.place(x=100, y=70, width=70, height=30)

root1.mainloop()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))
if user:
    s.send(user.encode())  # 发送用户名
else:
    s.send('no'.encode())  # 没有输入用户名则标记no

# 如果没有用户名则将ip和端口号设置为用户名
addr = s.getsockname()  # 获取客户端ip和端口号
addr = addr[0] + ':' + str(addr[1])
if user == '':
    user = addr

# 聊天窗口
# 创建图形界面
root = tkinter.Tk()
root.title(user)  # 窗口命名为用户名
root['height'] = 400
root['width'] = 580
root.resizable(0, 0)  # 限制窗口大小

# 创建多行文本框
listbox = ScrolledText(root)
listbox.config(state=tk.DISABLED)
listbox.place(x=5, y=0, width=570, height=320)
# 文本框使用的字体颜色
listbox.tag_config('red', foreground='red')
listbox.tag_config('blue', foreground='blue')
listbox.tag_config('green', foreground='green')
listbox.tag_config('pink', foreground='pink')
listbox.config(state=tk.NORMAL)
listbox.insert(tkinter.INSERT, 'Welcome to the chat room!', 'blue')
listbox.config(state=tk.DISABLED)

# 表情功能代码部分
# 四个按钮, 使用全局变量, 方便创建和销毁
b1 = ''
b2 = ''
b3 = ''
b4 = ''
b5 = ''
b6 = ''
b7 = ''
b8 = ''
b9 = ''
b10 = ''

# 将图片打开存入变量中
p1 = tkinter.PhotoImage(file='./emoji/1.png')
p2 = tkinter.PhotoImage(file='./emoji/2.png')
p3 = tkinter.PhotoImage(file='./emoji/3.png')
p4 = tkinter.PhotoImage(file='./emoji/4.png')
p5 = tkinter.PhotoImage(file='./emoji/5.png')
p6 = tkinter.PhotoImage(file='./emoji/6.png')
p7 = tkinter.PhotoImage(file='./emoji/7.png')
p8 = tkinter.PhotoImage(file='./emoji/8.png')
p9 = tkinter.PhotoImage(file='./emoji/9.png')
p10 = tkinter.PhotoImage(file='./emoji/10.png')

# 用字典将标记与表情图片一一对应, 用于后面接收标记判断表情贴图
dic = {'aa**': p1, 'bb**': p2, 'cc**': p3, 'dd**': p4,
       'ee**': p5, 'ff**': p6, 'gg**': p7, 'hh**': p8, 'ii**': p9,'jj**': p10}
zz = 0  # 判断表情面板开关的标志


# 发送表情图标记的函数, 在按钮点击事件中调用


def mark(exp):  # 参数是发的表情图标记, 发送后将按钮销毁
    global zz
    mes = exp + ':;' + user + ':;' + chat
    s.send(mes.encode())
    b1.destroy()
    b2.destroy()
    b3.destroy()
    b4.destroy()
    b5.destroy()
    b6.destroy()
    b7.destroy()
    b8.destroy()
    b9.destroy()
    b10.destroy()
    zz = 0


# 四个对应的函数
def bb1():
    mark('aa**')


def bb2():
    mark('bb**')


def bb3():
    mark('cc**')


def bb4():
    mark('dd**')


def bb5():
    mark('ee**')


def bb6():
    mark('ff**')


def bb7():
    mark('gg**')


def bb8():
    mark('hh**')


def bb9():
    mark('ii**')


def bb10():
    mark('jj**')



def express():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, zz
    if zz == 0:
        zz = 1
        b1 = tkinter.Button(root, command=bb1, image=p1,
                            relief=tkinter.FLAT, bd=0, width=70, height=70)
        b2 = tkinter.Button(root, command=bb2, image=p2,
                            relief=tkinter.FLAT, bd=0, width=70, height=70)
        b3 = tkinter.Button(root, command=bb3, image=p3,
                            relief=tkinter.FLAT, bd=0, width=70, height=70)
        b4 = tkinter.Button(root, command=bb4, image=p4,
                            relief=tkinter.FLAT, bd=0, width=70, height=70)
        b5 = tkinter.Button(root, command=bb5, image=p5,
                            relief=tkinter.FLAT, bd=0, width=70, height=70)
        b6 = tkinter.Button(root, command=bb6, image=p6,
                            relief=tkinter.FLAT, bd=0, width=70, height=70)
        b7 = tkinter.Button(root, command=bb7, image=p7,
                            relief=tkinter.FLAT, bd=0, width=70, height=70)
        b8 = tkinter.Button(root, command=bb8, image=p8,
                            relief=tkinter.FLAT, bd=0, width=70, height=70)
        b9 = tkinter.Button(root, command=bb9, image=p9,
                            relief=tkinter.FLAT, bd=0, width=70, height=70)
        b10 = tkinter.Button(root, command=bb10, image=p10,
                            relief=tkinter.FLAT, bd=0, width=70, height=70)

        b1.place(x=5, y=248)
        b2.place(x=75, y=248)
        b3.place(x=145, y=248)
        b4.place(x=215, y=248)
        b5.place(x=5, y=178)
        b6.place(x=75, y=178)
        b7.place(x=145, y=178)
        b8.place(x=215, y=178)
        b9.place(x=5, y=108)
        b10.place(x=75, y=108)
    else:
        zz = 0
        b1.destroy()
        b2.destroy()
        b3.destroy()
        b4.destroy()
        b5.destroy()
        b6.destroy()
        b7.destroy()
        b8.destroy()
        b9.destroy()
        b10.destroy()


# 创建表情按钮
eBut = tkinter.Button(root, text='表情', command=express)
eBut.place(x=5, y=320, width=60, height=30)


# 图片功能代码部分
# 从图片服务端的缓存文件夹中下载图片到客户端缓存文件夹中
def fileGet(name):
    PORT3 = 50009
    ss2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss2.connect((IP, PORT3))
    message = 'get ' + name
    ss2.send(message.encode())
    fileName = os.path.join('./Client_image_cache/',name)
    print('Start downloading image!')
    print('Waiting.......')
    with open(fileName, 'wb') as f:
        while True:
            data = ss2.recv(1024)
            if data == 'EOF'.encode():
                print('Download completed!')
                break
            f.write(data)
    time.sleep(0.1)
    ss2.send('quit'.encode())
    return fileName


# 将图片上传到图片服务端的缓存文件夹中
def filePut(fileName):
    PORT3 = 50009
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss.connect((IP, PORT3))
    # 截取文件名
    print(fileName)
    name = fileName.split('/')[-1]
    print(name)
    message = 'put ' + name
    ss.send(message.encode())
    time.sleep(0.1)
    print('Start uploading image!')
    print('Waiting.......')
    with open(fileName, 'rb') as f:
        while True:
            a = f.read(1024)
            print(a)
            if not a:
                break
            ss.send(a)
        time.sleep(1)  # 延时确保文件发送完整
        ss.send('EOF'.encode())
        print('Upload completed')
    while True:
        data = ss.recv(1024)
        if data == 'Completed'.encode():
            break
    ss.send('quit'.encode())
    time.sleep(0.1)
    # 上传成功后发一个信息给所有客户端
    mes = '``#' + name + ':;' + user + ':;' + chat

    s.send(mes.encode())


def picture():
    # 选择对话框
    fileName = tkinter.filedialog.askopenfilename(title='Select upload image')
    # 如果有选择文件才继续执行
    if fileName:
        # 调用发送图片函数
        filePut(fileName)


# 创建发送图片按钮
pBut = tkinter.Button(root, text='图片', command=picture)
pBut.place(x=65, y=320, width=60, height=30)


# 文件功能代码部分
# 将在文件功能窗口用到的组件名都列出来, 方便重新打开时会对面板进行更新
list2 = ''  # 列表框
label = ''  # 显示路径的标签
upload = ''  # 上传按钮
close = ''  # 关闭按钮


def fileClient():
    PORT2 = 50008  # 聊天室的端口为50007
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT2))

    # 修改root窗口大小显示文件管理的组件
    root['height'] = 390
    root['width'] = 760

    # 创建列表框
    list2 = tkinter.Listbox(root)
    list2.place(x=580, y=25, width=175, height=325)

    # 将接收到的目录文件列表打印出来(dir), 显示在列表框中, 在pwd函数中调用
    def recvList(enter, lu):
        s.send(enter.encode())
        data = s.recv(4096)
        data = json.loads(data.decode())
        list2.delete(0, tkinter.END)  # 清空列表框
        lu = lu.split('\\')
        if len(lu) != 1:
            list2.insert(tkinter.END, 'Return to the previous dir')
            list2.itemconfig(0, fg='green')
        for i in range(len(data)):
            list2.insert(tkinter.END, ('' + data[i]))
            if '.' not in data[i]:
                list2.itemconfig(tkinter.END, fg='orange')
            else:
                list2.itemconfig(tkinter.END, fg='blue')

    # 创建标签显示服务端工作目录
    def lab():
        global label
        data = s.recv(1024)  # 接收目录
        lu = data.decode()
        try:
            label.destroy()
            label = tkinter.Label(root, text=lu)
            label.place(x=580, y=0, )
        except:
            label = tkinter.Label(root, text=lu)
            label.place(x=580, y=0, )
        recvList('dir', lu)

    # 进入指定目录(cd)
    def cd(message):
        s.send(message.encode())

    # 刚连接上服务端时进行一次面板刷新
    cd('cd same')
    lab()

    # 接收下载文件(get)
    def get(message):
        # print(message)
        name = message.split(' ')
        # print(name)
        name = name[1]  # 获取命令的第二个参数(文件名)
        # 选择对话框, 选择文件的保存路径
        fileName = tkinter.filedialog.asksaveasfilename(
            title='Save file to', initialfile=name)
        # 如果文件名非空才进行下载
        if fileName:
            s.send(message.encode())
            with open(fileName, 'wb') as f:
                while True:
                    data = s.recv(1024)
                    if data == 'EOF'.encode():
                        tkinter.messagebox.showinfo(title='Message',
                                                    message='Download completed!')
                        break
                    f.write(data)

    # 创建用于绑定在列表框上的函数
    def run(*args):
        indexs = list2.curselection()
        index = indexs[0]
        content = list2.get(index)
        # 如果有一个 . 则为文件
        if '.' in content:
            content = 'get ' + content
            get(content)
            cd('cd same')
        elif content == 'Return to the previous dir':
            content = 'cd ..'
            cd(content)
        else:
            content = 'cd ' + content
            cd(content)
        lab()  # 刷新显示页面

    # 在列表框上设置绑定事件
    list2.bind('<ButtonRelease-1>', run)

    # 上传客户端所在文件夹中指定的文件到服务端, 在函数中获取文件名, 不用传参数
    def put():
        # 选择对话框
        fileName = tkinter.filedialog.askopenfilename(
            title='Select upload file')
        # 如果有选择文件才继续执行
        if fileName:
            name = fileName.split('/')[-1]
            message = 'put ' + name
            s.send(message.encode())
            with open(fileName, 'rb') as f:
                while True:
                    a = f.read(1024)
                    if not a:
                        break
                    s.send(a)
                time.sleep(0.1)  # 延时确保文件发送完整
                s.send('EOF'.encode())
                tkinter.messagebox.showinfo(title='Message',
                                            message='Upload completed!')
        cd('cd same')
        lab()  # 上传成功后刷新显示页面

    # 创建上传按钮, 并绑定上传文件功能
    upload = tkinter.Button(root, text='上传文件', command=put)
    upload.place(x=600, y=353, height=30, width=80)

    # 关闭文件管理器, 待完善
    def closeFile():
        root['height'] = 390
        root['width'] = 580
        # 关闭连接
        s.send('quit'.encode())
        s.close()

    # 创建关闭按钮
    close = tkinter.Button(root, text='关闭', command=closeFile)
    close.place(x=685, y=353, height=30, width=70)


# 创建文件按钮
fBut = tkinter.Button(root, text='文件', command=fileClient)
fBut.place(x=125, y=320, width=60, height=30)

# 创建多行文本框, 显示在线用户
listbox1 = tkinter.Listbox(root)
listbox1.place(x=445, y=0, width=130, height=320)


def users():
    global listbox1, ii
    if ii == 1:
        listbox1.place(x=445, y=0, width=130, height=320)
        ii = 0
    else:
        listbox1.place_forget()  # 隐藏控件
        ii = 1


# 查看在线用户按钮
button1 = tkinter.Button(root, text='在线用户列表', command=users)
button1.place(x=455, y=320, width=120, height=30)

# 创建输入文本框和关联变量
a = tkinter.StringVar()
a.set('')
entry = tkinter.Entry(root, width=120, textvariable=a)
entry.place(x=5, y=350, width=570, height=40)


def call_robot(url, apikey, msg):
    data = {
        "reqType": 0,
        "perception": {
            # 用户输入文文信息
            "inputText": {  # inputText文本信息
                "text": msg
            },
            # 用户输入图片url
            "inputImage": {  # 图片信息，后跟参数信息为url地址，string类型
                "url": "https://cn.bing.com/images/"
            },
            # 用户输入音频地址信息
            "inputMedia": {  # 音频信息，后跟参数信息为url地址，string类型
                "url": "https://www.1ting.com/"
            },
            # 客户端属性信息
            "selfInfo": {  # location 为selfInfo的参数信息，
                "location": {  # 地理位置信息
                    "city": "杭州",  # 所在城市，不允许为空
                    "province": "浙江省",  # 所在省份，允许为空
                    "street": "灵隐街道"  # 所在街道，允许为空
                }
            },
        },
        "userInfo": {
            "apiKey": "ee19328107fa41e987a42a064a68d0da",  # 你注册的apikey,机器人标识,32位
            "userId": "Brandon"  # 随便填，用户的唯一标识，长度小于等于32位
        }
    }
    headers = {'content-type': 'application/json'}  # 必须是json
    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r.json()


def send(*args):
    # 没有添加的话发送信息时会提示没有聊天对象
    users.append('------Group chat-------')
    users.append('Robot')
    print(chat)
    if chat not in users:
        tkinter.messagebox.showerror(
            'Send error', message='There is nobody to talk to!')
        return
    if chat == 'Robot':
        print('Robot')
    if chat == user:
        tkinter.messagebox.showerror(
            'Send error', message='Cannot talk with yourself in private!')
        return
    mes = entry.get() + ':;' + user + ':;' + chat  # 添加聊天对象标记
    s.send(mes.encode())
    a.set('')  # 发送后清空文本框


# 创建发送按钮
button = tkinter.Button(root, text='发送', command=send)
button.place(x=515, y=353, width=60, height=30)
root.bind('<Return>', send)  # 绑定回车发送信息

# 视频聊天部分
IsOpen = False    # 判断视频/音频的服务器是否已打开
Resolution = 0    # 图像传输的分辨率 0-4依次递减
Version = 4       # 传输协议版本 IPv4/IPv6
ShowMe = True     # 视频聊天时是否打开本地摄像头
AudioOpen = True  # 是否打开音频聊天


def video_invite():
    global IsOpen, Version, AudioOpen
    host_name = socket.gethostbyname(socket.getfqdn(socket.gethostname()))
    print(host_name)
    if Version == 4 or "4":
        host_name = socket.gethostbyname(socket.getfqdn(socket.gethostname()))
    else:
        host_name = [i['addr'] for i in ifaddresses(interfaces()[-2]).setdefault(AF_INET6, [{'addr': 'No IP addr'}])][
            -1]
    print(host_name)
    invite = 'INVITE' + host_name + ':;' + user + ':;' + chat
    s.send(invite.encode())
    if not IsOpen:
        vserver = vachat.Video_Server(10087, Version)
        if AudioOpen:
            aserver = vachat.Audio_Server(10088, Version)
            aserver.start()
        vserver.start()
        IsOpen = True


def video_accept(host_name):
    global IsOpen, Resolution, ShowMe, Version, AudioOpen

    vclient = vachat.Video_Client(
        host_name, 10087, ShowMe, Resolution, Version)
    if AudioOpen:
        aclient = vachat.Audio_Client(host_name, 10088, Version)
        aclient.start()
    vclient.start()
    IsOpen = False


def video_invite_window(message, inviter_name):
    invite_window = tkinter.Toplevel()
    invite_window.geometry('300x100')
    invite_window.title('Invitation')
    label1 = tkinter.Label(invite_window, bg='#f0f0f0',
                           width=20, text=inviter_name)
    label1.pack()
    label2 = tkinter.Label(invite_window, bg='#f0f0f0',
                           width=20, text='invites you to video chat!')
    label2.pack()

    def accept_invite():
        invite_window.destroy()
        video_accept(message[message.index('INVITE') + 6:])

    def refuse_invite():
        invite_window.destroy()

    Refuse = tkinter.Button(
        invite_window, text="拒绝", command=refuse_invite)
    Refuse.place(x=60, y=60, width=60, height=25)
    Accept = tkinter.Button(
        invite_window, text="接受", command=accept_invite)
    Accept.place(x=180, y=60, width=60, height=25)


def video_connect_option():
    global Resolution, ShowMe, Version, AudioOpen

    video_connect_option = tkinter.Toplevel()
    video_connect_option.geometry('200x550')
    video_connect_option.title('连接选项')

    var1 = tkinter.StringVar()
    label1 = tkinter.Label(video_connect_option,
                           bg='#f0f0f0', width=20, text='方案   ')
    label1.pack()

    def print_resolution():
        global Resolution
        Resolution = var1.get()
        label1.config(text='方案   ' + Resolution)

    r0 = tkinter.Radiobutton(video_connect_option, text='0',
                             variable=var1, value='0', command=print_resolution)
    r0.pack()
    r0.select()
    print_resolution()

    r1 = tkinter.Radiobutton(video_connect_option, text='1',
                             variable=var1, value='1', command=print_resolution)
    r1.pack()
    r2 = tkinter.Radiobutton(video_connect_option, text='2',
                             variable=var1, value='2', command=print_resolution)
    r2.pack()
    r3 = tkinter.Radiobutton(video_connect_option, text='3',
                             variable=var1, value='3', command=print_resolution)
    r3.pack()
    r4 = tkinter.Radiobutton(video_connect_option, text='4',
                             variable=var1, value='4', command=print_resolution)
    r4.pack()

    var2 = tkinter.StringVar()
    label2 = tkinter.Label(video_connect_option, bg='#f0f0f0',
                           width=20, text='协议版本   ')
    label2.pack()

    def print_version():
        global Version
        Version = var2.get()
        label2.config(text='协议版本   IPv' + Version)

    v0 = tkinter.Radiobutton(video_connect_option, text='IPv4',
                             variable=var2, value='4', command=print_version)
    v0.pack()
    v0.select()
    print_version()

    v1 = tkinter.Radiobutton(video_connect_option, text='IPv6',
                             variable=var2, value='6', command=print_version)
    v1.pack()

    var3 = tkinter.StringVar()
    label3 = tkinter.Label(video_connect_option, bg='#f0f0f0',
                           width=20, text='显示自己   ')
    label3.pack()

    def print_show():
        global ShowMe
        if var3.get() == '1':
            ShowMe = True
            txt = 'Yes'
        else:
            ShowMe = False
            txt = 'No'
        label3.config(text='显示自己   ' + txt)

    s0 = tkinter.Radiobutton(
        video_connect_option, text='Yes', variable=var3, value='1', command=print_show)
    s0.pack()
    s0.select()
    print_show()

    s1 = tkinter.Radiobutton(
        video_connect_option, text='No', variable=var3, value='0', command=print_show)
    s1.pack()

    var4 = tkinter.StringVar()
    label4 = tkinter.Label(video_connect_option,
                           bg='#f0f0f0', width=20, text='打开音频   ')
    label4.pack()

    def print_audio():
        global AudioOpen
        if var4.get() == '1':
            AudioOpen = True
            txt = 'Yes'
        else:
            AudioOpen = False
            txt = 'No'
        label4.config(text='打开音频   ' + txt)

    a0 = tkinter.Radiobutton(
        video_connect_option, text='Yes', variable=var4, value='1', command=print_audio)
    a0.pack()
    a0.select()
    print_audio()

    a1 = tkinter.Radiobutton(
        video_connect_option, text='No', variable=var4, value='0', command=print_audio)
    a1.pack()

    def option_enter():
        video_connect_option.destroy()

    Enter = tkinter.Button(video_connect_option,
                           text="关闭", command=option_enter)
    Enter.place(x=10, y=500, width=60, height=35)
    Start = tkinter.Button(video_connect_option,
                           text="开始", command=video_invite)
    Start.place(x=80, y=500, width=60, height=35)


vbutton = tkinter.Button(root, text="视频", command=video_connect_option)
vbutton.place(x=185, y=320, width=60, height=30)


# 私聊功能
def private(*args):
    global chat
    # 获取点击的索引然后得到内容(用户名)
    indexs = listbox1.curselection()
    index = indexs[0]
    if index > 0:
        chat = listbox1.get(index)
        # 修改客户端名称
        if chat == '------Group chat-------':
            root.title(user)
            return
        ti = user + '  -->  ' + chat
        root.title(ti)


# 在显示用户列表框上设置绑定事件
listbox1.bind('<ButtonRelease-1>', private)


# 用于时刻接收服务端发送的信息并打印
def recv():
    global users
    while True:
        data = s.recv(1024)
        data = data.decode()
        # 没有捕获到异常则表示接收到的是在线用户列表
        try:
            data = json.loads(data)
            users = data
            listbox1.delete(0, tkinter.END)  # 清空列表框
            number = ('   Users online: ' + str(len(data)))
            listbox1.insert(tkinter.END, number)
            listbox1.itemconfig(tkinter.END, fg='green', bg="#f0f0ff")
            listbox1.insert(tkinter.END, '------Group chat-------')
            listbox1.insert(tkinter.END, 'Robot')
            listbox1.itemconfig(tkinter.END, fg='green')
            for i in range(len(data)):
                listbox1.insert(tkinter.END, (data[i]))
                listbox1.itemconfig(tkinter.END, fg='green')
        except:
            data = data.split(':;')
            data1 = data[0].strip()  # 消息
            data2 = data[1]  # 发送信息的用户名
            data3 = data[2]  # 聊天对象
            if 'INVITE' in data1:
                if data3 == 'Robot':
                    tkinter.messagebox.showerror(
                        'Connect error', message='不支持与机器人视频')
                elif data3 == '------Group chat-------':
                    tkinter.messagebox.showerror(
                        'Connect error', message='不支持群组视频')
                elif (data2 == user and data3 == user) or (data2 != user):
                    video_invite_window(data1, data2)
                continue
            markk = data1.split('：')[1]
            # 判断是不是图片
            pic = markk.split('#')
            # 判断是不是表情
            # 如果字典里有则贴图
            if (markk in dic) or pic[0] == '``':
                data4 = '\n' + data2 + '：'  # 例:名字-> \n名字：
                if data3 == '------Group chat-------':
                    if data2 == user:  # 如果是自己则将则字体变为蓝色
                        listbox.config(state=tk.NORMAL)
                        listbox.insert(tkinter.END, data4, 'blue')
                        listbox.config(state=tk.DISABLED)
                    else:
                        listbox.config(state=tk.NORMAL)
                        listbox.insert(tkinter.END, data4,
                                       'green')  # END将信息加在最后一行
                        listbox.config(state=tk.DISABLED)
                elif data2 == user or data3 == user:  # 显示私聊
                    listbox.config(state=tk.NORMAL)
                    listbox.insert(tkinter.END, data4, 'red')  # END将信息加在最后一行
                    listbox.config(state=tk.DISABLED)
                if pic[0] == '``':
                    # 从服务端下载发送的图片
                    imageName = fileGet(pic[1])
                    memPic = ImageTk.PhotoImage(Image.open(imageName).resize((200,200)))
                    listbox.image_create(tkinter.END, image=memPic)
                else:
                    # 将表情图贴到聊天框
                    listbox.image_create(tkinter.END, image=dic[markk])
            else:
                data1 = '\n' + data1
                if data3 == '------Group chat-------':
                    if data2 == user:  # 如果是自己则将则字体变为蓝色
                        listbox.config(state=tk.NORMAL)
                        listbox.insert(tkinter.END, data1, 'blue')
                        listbox.config(state=tk.DISABLED)
                    else:
                        listbox.config(state=tk.NORMAL)
                        listbox.insert(tkinter.END, data1,
                                       'green')  # END将信息加在最后一行
                        listbox.config(state=tk.DISABLED)
                    if len(data) == 4:
                        listbox.config(state=tk.NORMAL)
                        listbox.insert(tkinter.END, '\n' + data[3], 'pink')
                        listbox.config(state=tk.DISABLED)
                elif data3 == 'Robot' and data2 == user:
                    print('Here:Robot')
                    apikey = 'ee19328107fa41e987a42a064a68d0da'
                    url = 'http://openapi.tuling123.com/openapi/api/v2'
                    print('msg = ', data1)
                    listbox.config(state=tk.NORMAL)
                    listbox.insert(tkinter.END, data1, 'blue')
                    listbox.config(state=tk.DISABLED)
                    reply = call_robot(url, apikey, data1.split('：')[1])
                    reply_txt = '\nRobot:' + \
                        reply['results'][0]['values']['text']
                    listbox.config(state=tk.NORMAL)
                    listbox.insert(tkinter.END, reply_txt, 'pink')
                    listbox.config(state=tk.DISABLED)
                elif data2 == user or data3 == user:  # 显示私聊
                    listbox.config(state=tk.NORMAL)
                    listbox.insert(tkinter.END, data1, 'red')  # END将信息加在最后一行
                    listbox.config(state=tk.DISABLED)
            listbox.see(tkinter.END)  # 显示在最后


r = threading.Thread(target=recv)
r.start()  # 开始线程接收信息

root.mainloop()
s.close()  # 关闭图形界面后关闭TCP连接
