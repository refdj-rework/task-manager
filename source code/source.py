
import flet as ft
import controller

sucses = []
in_progress = []

with open("../list_inprgrss.txt", "r") as f:
    in_progress = f.read().splitlines()
with open("../list_sucsess.txt", "r") as f:
    sucses = f.read().splitlines()

print(in_progress)
print(sucses)

def main(page):
    page.title = 'TaskManager'
    page.scroll = 'adaptive'


    def add_clicked(e):
        new_task.border_color = ""
        new_task.update()
        stripped = new_task.value.strip()
        if len(stripped) > 0:
            tmpckr = str(time_picker.value)
            page.add(ft.Checkbox(label=stripped + " в " + str(tmpckr[0:5:1]), on_change=sucsess))
            in_progress.append(stripped + " в " + str(tmpckr[0:5:1]))
            new_task.value = ""
            new_task.focus()
            new_task.update()
            time_button.text = "Выбрать время"
            time_button.update()
        else:
            new_task.border_color = "RED"
            new_task.update()

    def sucsess(e):
        sucses.append(str(e.control.label))
        in_progress.remove(e.control.label)
        e.control.page.remove(e.control)

    def picktime(e):
        tmpckr = str(time_picker.value)
        time_button.text = tmpckr[0:5:1]
        time_button.update()

    def save_btn(e):
        my_file = open("../list_inprgrss.txt", "w+")
        i = 0
        while i < len(in_progress):
            my_file.write(in_progress[i] + "\n")
            i += 1
        my_file.close()
        my_file2 = open("../list_sucsess.txt", "w+")
        i = 0
        while i < len(sucses):
            my_file2.write(sucses[i] + "\n")
            i += 1
        my_file2.close()

    def was_sucsess_btn(e):
        def back(e):
            page.clean()
            main(page)
        def clear(e):
            sucses.clear()
            page.clean()
            was_sucsess_btn(e)
        def delet(e):
            e.control.page.remove(e.control)
        page.clean()
        page.add(ft.Row([ft.ElevatedButton("Назад",on_click=back,width=300), ft.ElevatedButton("Отчистить",on_click=clear, width=250)]))
        i = 0
        while i < len(sucses):
            page.add(ft.TextButton(sucses[i],on_click=delet, icon=ft.CupertinoIcons.TRASH))
            i += 1

    def clr_btn(e):
        my_file = open("../list_inprgrss.txt", "w+")
        my_file.write("")
        my_file.close()
        my_file2 = open("../list_sucsess.txt", "w+")
        my_file2.write("")
        my_file2.close()


    save_button = ft.Button("Сохранить задачи", expand=True, on_click=save_btn, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0), color="blue"))
    was_sucsess_button = ft.Button("Выполненные задачи", expand=True, on_click=was_sucsess_btn, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0), color="blue"))
    clr_button = ft.Button("Отчистить сохранённые задачи", expand=True, on_click=clr_btn, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0), color="blue"))
    page.add(ft.Row([save_button, clr_button, was_sucsess_button]))

    new_task = ft.TextField(hint_text="Чтобы вы хотели сделать?", expand=True)
    time_picker = ft.TimePicker(confirm_text="Выбрать", cancel_text="Отмена", help_text="Выбери время", on_change=picktime)
    time_button=ft.ElevatedButton("Выбрать время", on_click=lambda _: page.open(time_picker),width=120)
    page.add(ft.Row([new_task, time_button, ft.ElevatedButton("Добавить в список", width=200, on_click=add_clicked)]))
    i = 0
    while i < len(in_progress):
        page.add(ft.Checkbox(in_progress[i], on_change=sucsess))
        i += 1

ft.app(main)