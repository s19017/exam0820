import tkinter as tk
import random

root = tk.Tk()
root.title("心に響く言葉")
root.geometry("900x300")

words = (
    'あなたの心が正しいと思うことをしなさい。どっちにしたって批判されるのだから。',
    '前進をしない人は、後退をしているのだ。',
    'どんなに悔いても過去は変わらない。どれほど心配したところで未来もどうなるものでもない。いま、現在に最善を尽くすことである。',
    '最も重要な決定とは、何をするかではなく、何をしないかを決めることだ。',
    '人生は楽ではない。そこが面白い。',
    '自分で自分をあきらめなければ、人生に「負け」はない。',
    '心の底からやりたいと思わないなら、やめておけ',
    '人生とは、人生以外のことを夢中で考えているときにあるんだよ',
    '一人前になるには50年はかかるんだ。功を焦るな。悲観するな。もっと根を深く張るんだ。根を深く張れ。',
    '努力は必ず報われる。もし報われない努力があるのならば、それはまだ努力と呼べない。',
    '微笑めば友達ができる。しかめっ面をすればしわができる。',
    '他人を押さえつけている限り、自分もそこから動くことはできない',
    '運命が決まるのは、あなたが決断する瞬間なのだ。',
    'しっかりと準備もしていないのに、目標を語る資格はない。'
)


def outputWords(event):

    value = txtBox.get()
    txtBox.configure(state='normal')

    if value:
        txtBox.delete(0, tk.END)

    txtBox.insert(tk.END, random.choice(words))
    txtBox.configure(state='readonly')


label = tk.Label(root, text="今のそなたに必要な言葉を授けよう")
label.pack()

txtBox = tk.Entry()
txtBox.configure(state='readonly', width=100)
txtBox.place(x=55, y=80)

button = tk.Button(text='言葉を聞く', width=30)
button.place(x=300, y=120)
button.bind('<Button-1>', outputWords)

root.mainloop()
