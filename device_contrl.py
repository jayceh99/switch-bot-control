import uuid
from switchbot import SwitchBot

class device_contrl:
    def __init__(self,your_switch_bot_token,your_switch_bot_secret,device_mac) :
        self.switchbot = SwitchBot(token=your_switch_bot_token, secret=your_switch_bot_secret, nonce=str(uuid.uuid4()))
        self.device = self.switchbot.device(id=device_mac)
    def bot_status(self):
        if 'on' in str(self.device.status()):
            return '現在馬達開著'
        elif 'off' in str(self.device.status()):
            return '現在馬達關掉了'
        else :
            return '找不到機器人'
    def bot_on (self):
        self.device.command('turn_on')
        if 'on' in str(self.device.status()):
            print ('good')
    def bot_off (self):
        self.device.command('turn_off')
        if 'on' in str(self.device.status()):
            print ('good')
    
