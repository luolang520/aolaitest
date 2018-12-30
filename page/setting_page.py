from base.base_actiton import BaseAciton
import page
#负责设置页面的相关逻辑

class SettingPage(BaseAciton):
    def __init__(self,driver):
        BaseAciton.__init__(self,driver)
        #退出当前登陆的账号
    def logout_account(self):
        # 滑动页面底端，才会看见退出按钮才能找到元素
        self.swipe_screen(1)
        # 点击退出按钮
        self.click_element(page.setting_center_login_out_btn)
        # 点击弹出的对话框确定按钮
        self.click_element(page.setting_center_login_dialog_confirm_btn)

