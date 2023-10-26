from kivymd.uix.screen import MDScreen
from kivy.animation import Animation


class LoginScreen(MDScreen):
    def login_action(self):
        user_input = self.ids.input_user
        psw_input = self.ids.input_psw
        error_label = self.ids.error_label
        # Lógica para verificar as credenciais (substitua por sua própria lógica)
        if user_input.text != '1' or psw_input.text != '2':
            error_label.text = "Usuário ou senha incorretos"
            self.shake_textfields([user_input, psw_input], error_label)
        else:
            error_label.text = ""
            self.on_enter()

    def shake_textfields(self, textfields, label):
        # Cria uma animação para chacoalhar os campos
        anim = Animation(pos_hint={'center_x': 0.48}, duration=0.1) + Animation(pos_hint={'center_x': 0.52}, duration=0.1) + Animation(pos_hint={'center_x': 0.5}, duration=0.1) 
        anim2 = Animation(color=(1, 0, 0, 1), duration=0.1) + Animation(color=(0, 0, 0, 0), duration=0.1) + Animation(color=(1, 0, 0, 1), duration=0.1) + Animation(color=(0, 0, 0, 0), duration=0.1) + Animation(color=(1, 0, 0, 1), duration=0.1)
        for textfield in textfields:
            anim.start(textfield)
            anim2.start(label)
        textfields[1].text = ""
        pass
    def show_psw(self):
        # Alterna a visibilidade da senha
        psw_input = self.ids.input_psw
        button = self.ids.show_psw
        if psw_input.password:
            psw_input.password = False
            button.icon = "eye"
        else:
            psw_input.password = True
            button.icon = "eye-off"
    pass
