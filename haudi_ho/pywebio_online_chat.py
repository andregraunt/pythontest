import asyncio
import sqlite3

from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import defer_call, info as session_info, run_async, run_js

chat_msgs = []
online_users = set()

MAX_MESSAGES_COUNT = 100

# Create a SQLite database to store the chat messages
conn = sqlite3.connect("chat_room.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS chat_messages (
    name text,
    message text
)""")
conn.commit()


async def main():
    global chat_msgs

    put_markdown(
        "## 🧊 Добро пожаловать в онлайн чат!\nИсходный код данного чата укладывается в 100 строк кода!")

    msg_box = output()
    put_scrollable(msg_box, height=300, keep_bottom=True)

    nickname = await input("Войти в чат", required=True, placeholder="Ваше имя", validate=lambda n: "Такой ник уже используется!" if n in online_users or n == '📢' else None)
    online_users.add(nickname)

    chat_msgs.append(('📢', f'`{nickname}` присоединился к чату!'))
    msg_box.append(put_markdown(f'📢 `{nickname}` присоединился к чату'))

    refresh_task = run_async(refresh_msg(nickname, msg_box))

 # Query all the messages from the SQLite database
    cursor.execute("SELECT name, message FROM chat_messages")
    for name, message in cursor.fetchall():
        chat_msgs.append((name, message))
        put_markdown('`%s`: %s' % (name, message),
                     sanitize=True, scope='msg-box')

    while True:
        data = await input_group("💭 Новое сообщение", [
            input(placeholder="Текст сообщения ...", name="msg"),
            actions(name="cmd", buttons=["Отправить", {
                    'label': "Выйти из чата", 'type': 'cancel'}])
        ], validate=lambda m: ('msg', "Введите текст сообщения!") if m["cmd"] == "Отправить" and not m['msg'] else None)

        if data is None:
            break

        msg_box.append(put_markdown(f"`{nickname}`: {data['msg']}"))
        chat_msgs.append((nickname, data['msg']))

 # Store the message to the SQLite database
        cursor.execute("INSERT INTO chat_messages VALUES (?, ?)",
                       (nickname, data['msg']))
        conn.commit()

    refresh_task.close()

    online_users.remove(nickname)
    toast("Вы вышли из чата!")
    msg_box.append(put_markdown(f'📢 Пользователь `{nickname}` покинул чат!'))
    chat_msgs.append(('📢', f'Пользователь `{nickname}` покинул чат!'))

    put_buttons(['Перезайти'], onclick=lambda btn: run_js(
        'window.location.reload()'))


async def refresh_msg(nickname, msg_box):
    global chat_msgs
    last_idx = len(chat_msgs)

    while True:
        await asyncio.sleep(1)

        for m in chat_msgs[last_idx:]:
            if m[0] != nickname:  # if not a message from current user
                msg_box.append(put_markdown(f"`{m[0]}`: {m[1]}"))

        # remove expired
        if len(chat_msgs) > MAX_MESSAGES_COUNT:
            chat_msgs = chat_msgs[len(chat_msgs) // 2:]

        last_idx = len(chat_msgs)


if __name__ == "__main__":
    start_server(main, debug=True, port=80, cdn=False)
