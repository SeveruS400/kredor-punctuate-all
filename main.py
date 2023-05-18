import time
import requests
import keyboard

API_URL = "https://api-inference.huggingface.co/models/kredor/punctuate-all"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

words = []
word = ""
finish = False
print("Enter words (For exit press 'q'):")

special_keys = [
    "backspace", "tab", "shift", "ctrl", "alt", "pause", "caps lock", "esc",
    "page up", "page down", "end", "home", "left", "up", "right", "down","enter",
    "insert", "delete", "win", "print screen", "scroll lock", "num lock", "menu",
    "f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10", "f11", "f12"
]
while True:
    event = keyboard.read_event()

    if event.event_type == 'down':
        key = event.name

        if key == 'q':
            break

        elif key == 'space':
            words.append(word)
            word = ""

        elif key in special_keys:
            key = ""

        else:
            word += key

    elif event.event_type == 'up' and event.name == 'space':
        finish = True

    if finish:
        if word != "":
            words.append(word)
        word = ""
        while True:
            try:
                output = query({"inputs": f"{words}"})
                i=len(output)-1
                if output[i]["entity_group"]==".":
                    for m in range(len(words)):
                        print(words[m], end=' ')
                finish = False
                break
            except:
                continue



# status=query("test")
# print(status)
# try:
#     if status["error"]=="Model kredor/punctuate-all is currently loading":
#         print("Connecting...")
#         print(status)
#         while True:
#             try:
#                 status = query("test")
#                 print(status)
#                 if status["error"]=="Model kredor/punctuate-all is currently loading":
#
#                     time.sleep(5)
#                 else:
#                     print("Connected")
#                     break
#
#             except:
#                 print("aa")
#                 continue
#     else:
#         print("Connected")
# except:
#     print("Connected")
