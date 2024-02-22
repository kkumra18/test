import PySimpleGUI as sg

label1 = sg.Text("Username", size=8)
input1 = sg.InputText(key="username")

label2 = sg.Text("Password", size=8)
input2 = sg.InputText(key="password")


login_btn = sg.Button("Login", key="login_btn")

window = sg.Window(title="Login", layout=[[label1, input1],
                                          [label2, input2],
                                          [login_btn]])

event, values = window.read()
print(event, values)
print(f"Username: {values["username"]}")
print(f"Password: {values["password"]}")
window.close()
