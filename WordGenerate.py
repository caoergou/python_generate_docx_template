#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import shutil
import wx
import wx.lib.scrolledpanel
from docxtpl import DocxTemplate
import rmb_upper
import os
import time

from decimal import Decimal

class MyFrame(wx.Frame):

    text_right_pad = 3
    input_right_pad = 20
    input_height = 22
    label_flag = wx.FIXED_MINSIZE | wx.RIGHT | wx.ALIGN_CENTER_VERTICAL
    input_flag = wx.RIGHT | wx.ALIGN_CENTER_VERTICAL


    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title,
            size=(1280, 768))
        self.label_font = wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.LIGHT)
        self.input_font = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.LIGHT)

        self.Centre()
        self.createUI()
        

    def createUI(self):

        rootBox = wx.BoxSizer(wx.VERTICAL)

        self.panel = wx.Panel(self, wx.ID_ANY)
        # self.panel = wx.lib.scrolledpanel.ScrolledPanel(self, -1, size=(1024, 400), pos=(0, 0), style=wx.SIMPLE_BORDER)
        # self.panel.SetupScrolling()
        # self.panel.SetBackgroundColour('#FFFFFF')

        panel_box = wx.GridSizer(14, 1, 5, 0)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox_temp = hbox1
        self.borrower_name1 = self.get_input_text(100)
        self.pack_input_text(hbox_temp, "借款人1姓名", self.borrower_name1)

        self.borrower_home1 = self.get_input_text(300)
        self.pack_input_text(hbox_temp, "借款人1住所地", self.borrower_home1)

        self.borrower_adress1 = self.get_input_text(300)
        # self.borrower_adress1.Bind(wx.EVT_TEXT, self.syn_borrower_address)
        self.borrower_adress1.Bind(wx.EVT_TEXT, self.syn_borrower_address)

        self.pack_input_text(hbox_temp, "借款人1通讯地址", self.borrower_adress1)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox_temp = hbox2
        self.borrower_id1 = self.get_input_text(200)
        self.pack_input_text(hbox_temp, "借款人1身份证编号", self.borrower_id1)

        self.borrower_phone1 = self.get_input_text(200)
        self.pack_input_text(hbox_temp, "借款人1电话", self.borrower_phone1)

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox_temp = hbox3
        self.borrower_name2 = self.get_input_text(100)
        self.pack_input_text(hbox_temp, "借款人2姓名", self.borrower_name2)

        self.borrower_home2 = self.get_input_text(300)
        self.pack_input_text(hbox_temp, "借款人2住所地", self.borrower_home2)

        self.borrower_adress2 = self.get_input_text(300)
        self.pack_input_text(hbox_temp, "借款人2通讯地址", self.borrower_adress2)

        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        hbox_temp = hbox4
        self.borrower_id2 = self.get_input_text(200)
        self.pack_input_text(hbox_temp, "借款人2身份证编号", self.borrower_id2)

        self.borrower_phone2 = self.get_input_text(200)
        self.pack_input_text(hbox_temp, "借款人2电话", self.borrower_phone2)

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        hbox_temp = hbox5
        self.loan_proportion = self.get_input_text(100)
        self.pack_input_text(hbox_temp, "几成购房贷款", self.loan_proportion)

        self.loan_number_small = self.get_input_text(150)
        self.loan_number_small.Bind(wx.EVT_TEXT, self.convert_loan_number)
        self.pack_input_text(hbox_temp, "贷款金额小写", self.loan_number_small)

        self.loan_number_big = self.get_input_text(300)
        self.pack_input_text(hbox_temp, "贷款金额大写", self.loan_number_big)

        self.house_price = self.get_input_text(100)
        self.pack_input_text(hbox_temp, "房屋售价", self.house_price)

        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        hbox_temp = hbox6
        self.house_location = self.get_input_text(100)
        self.pack_input_text(hbox_temp, "购房地址", self.house_location)

        self.house_area = self.get_input_text(100)
        self.pack_input_text(hbox_temp, "建筑面积", self.house_area)

        self.loan_duration_month = self.get_input_text(100)
        self.loan_duration_month.Bind(wx.EVT_TEXT, self.cal_end_date)
        self.pack_input_text(hbox_temp, "借款期限/月", self.loan_duration_month)

        self.start_year = self.get_input_text(100)
        self.start_year.Bind(wx.EVT_TEXT, self.cal_end_date)
        self.pack_input_text(hbox_temp, "起始年", self.start_year)

        self.start_month = self.get_input_text(100)
        self.start_month.Bind(wx.EVT_TEXT, self.cal_end_date)
        self.pack_input_text(hbox_temp, "-月", self.start_month)

        self.start_day = self.get_input_text(100)
        self.start_day.Bind(wx.EVT_TEXT, self.cal_end_date)
        self.pack_input_text(hbox_temp, "-日", self.start_day)

        hbox7 = wx.BoxSizer(wx.HORIZONTAL)
        hbox_temp = hbox7
        self.end_year = self.get_input_text(100)
        self.pack_input_text(hbox_temp, "截止年", self.end_year)

        self.end_month = self.get_input_text(100)
        self.pack_input_text(hbox_temp, "-月", self.end_month)

        self.end_day = self.get_input_text(100)
        self.pack_input_text(hbox_temp, "-日", self.end_day)

        self.standard_rate = self.get_input_text(100)
        self.standard_rate.SetLabelText("4.9")
        self.pack_input_text(hbox_temp, "基准利率", self.standard_rate)

        float_direction_arr = ["上", "下"]
        self.float_direction = self.get_choice(float_direction_arr)
        self.float_direction.Bind(wx.EVT_TEXT, self.cal_actual_rate)
        self.pack_input_text(hbox_temp, "浮动（上/下）", self.float_direction)

        self.float_num = self.get_input_text(100)
        self.float_num.Bind(wx.EVT_TEXT, self.cal_actual_rate)
        self.pack_input_text(hbox_temp, "浮动百分百", self.float_num)

        hbox8 = wx.BoxSizer(wx.HORIZONTAL)
        hbox_temp = hbox8
        self.actual_rate = self.get_input_text(100)
        self.pack_input_text(hbox_temp, "执行年利率", self.actual_rate)

        self.account_name = self.get_input_text(100)
        self.pack_input_text(hbox_temp, "户名", self.account_name)

        self.account_num = self.get_input_text(200)
        self.pack_input_text(hbox_temp, "账号", self.account_num)

        self.repayment_times = self.get_input_text(100)
        self.pack_input_text(hbox_temp, "还款期数", self.repayment_times)

        choice_arr = ["A", "B"]
        self.repayment_method = self.get_choice(choice_arr)
        self.pack_input_text(hbox_temp, "还款方式:（A/B）", self.repayment_method)

        hbox9 = wx.BoxSizer(wx.HORIZONTAL)
        hbox_temp = hbox9
        self.repayment_num_small = self.get_input_text(150)
        self.repayment_num_small.Bind(wx.EVT_TEXT, self.convert_repayment_num)
        self.pack_input_text(hbox_temp, "还款金额小写", self.repayment_num_small)

        self.repayment_num_big = self.get_input_text(300)
        self.pack_input_text(hbox_temp, "还款金额大写", self.repayment_num_big)

        self.pawn_num = self.get_input_text(200)
        self.pack_input_text(hbox_temp, "抵押物编号", self.pawn_num)

        hbox10 = wx.BoxSizer(wx.HORIZONTAL)
        hbox_temp = hbox10
        self.contract_num = self.get_input_text(100)
        self.pack_input_text(hbox_temp, "合同份数：大写", self.contract_num)

        self.loan_contract_id = self.get_input_text(300)
        self.pack_input_text(hbox_temp, "借款合同编号", self.loan_contract_id)

        self.contract_id = self.get_input_text(300)
        self.pack_input_text(hbox_temp, "合同编号", self.contract_id)

        panel_box.Add(hbox1)
        panel_box.Add(hbox2)
        panel_box.Add(hbox3)
        panel_box.Add(hbox4)
        panel_box.Add(hbox5)
        panel_box.Add(hbox6)
        panel_box.Add(hbox7)
        panel_box.Add(hbox8)
        panel_box.Add(hbox9)
        panel_box.Add(hbox10)
        self.panel.SetSizer(panel_box)

        rootBox.Add(self.panel, 1, wx.EXPAND | wx.ALL, 20)

        self.btn_generate_template = self.get_button("生成合同", self.generate_template)

        self.btn_set_save_path = self.get_button("设置文件保存路径", self.set_save_path)
        self.label_set_save_path = wx.StaticText(self, -1, label="当前路径")
        self.label_set_save_path.SetFont(self.input_font)
        cur_path = os.path.abspath(".")
        self.label_set_save_path.SetLabelText(cur_path)

        bottom_box = wx.BoxSizer(wx.HORIZONTAL)
        bottom_box2 = wx.BoxSizer(wx.HORIZONTAL)

        bottom_box.Add(self.btn_generate_template, 0, wx.ALIGN_LEFT | wx.ALL | wx.ALIGN_CENTER_VERTICAL, 10)
        bottom_box.Add(self.btn_set_save_path, 0, wx.ALIGN_LEFT | wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 30)
        bottom_box.Add(self.label_set_save_path, 0, wx.ALIGN_LEFT | wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
        # self.pack_label(bottom_box, self.input_save_path)

        # bottom_box2.Add(self.input_save_path, 0, wx.ALIGN_LEFT | wx.ALL, 10)


        rootBox.Add(bottom_box, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 20)

        self.SetSizer(rootBox)
        self.SetBackgroundColour(self.panel.GetBackgroundColour())


        # 创建定时器
        self.timer = wx.Timer(self)  # 创建定时器
        self.Bind(wx.EVT_TIMER, self.refresh_timer, self.timer)  # 绑定一个定时器事件
        self.timer.Start(1000)

        pass

    def refresh_timer(self, e):
        cur_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.SetTitle('合同自动生成器                        ' + cur_time)

    def get_button(self, text, on_button_method):
        button = wx.Button(self, wx.ID_ANY, text)
        button.Bind(wx.EVT_BUTTON, on_button_method)
        button.SetFont(self.label_font)
        return button

    # 注意这里 label的父容器是panel
    def get_label(self, label):
        label = wx.StaticText(self.panel, -1, label=label)
        label.SetFont(self.label_font)
        # label.SetForegroundColour((255, 0, 0))
        return label

    def get_input_text(self, width):
        input_edit_text = wx.TextCtrl(self.panel, size=(width, self.input_height), style=wx.TE_CENTRE)
        input_edit_text.SetFont(self.input_font)
        return input_edit_text

    def pack_label(self, hbox, label):
        hbox.Add(label, 0, self.label_flag, self.text_right_pad)

    def pack_input_text(self, hbox, input_text):
        hbox.Add(input_text, 0, self.input_flag, self.input_right_pad)

    def pack_input_text(self, hbox, label_name, input_text):
        hbox.Add(self.get_label(label_name), 0, self.label_flag, self.text_right_pad)
        hbox.Add(input_text, 0, self.input_flag, self.input_right_pad)

    def get_choice(self, arr):
        ch = wx.Choice(self.panel, size=(50, 22),  choices=arr)
        ch.Center()
        ch.SetStringSelection(arr[0])
        ch.SetFont(self.input_font)
        return ch

    def syn_borrower_address(self, e):
        self.borrower_adress2.SetLabelText(self.read_input_text(self.borrower_adress1))

    def convert_repayment_num(self, e):
        money = e.GetString()
        if len(money) == 0:
            self.repayment_num_big.SetLabelText("")
        else:
            self.repayment_num_big.SetLabelText(rmb_upper.cncurrency(e.GetString()))

    def convert_loan_number(self, e):
        money = e.GetString()
        if len(money) == 0:
            self.loan_number_big.SetLabelText("")
        else:
            self.loan_number_big.SetLabelText(rmb_upper.cncurrency(e.GetString()))

    def cal_actual_rate(self, e):
        statand = float(self.read_input_text(self.standard_rate).replace("%", ""))
        dir = self.read_choice_text(self.float_direction)
        float_num = float(self.read_input_text(self.float_num).replace("%", ""))
        actual_rate = 0.0
        if dir == '上':
            actual_rate = statand * (1 + float_num/100)
        else:
            actual_rate = statand * (1 - float_num / 100)
        self.actual_rate.SetLabelText(str(round(actual_rate, 3)))

    def cal_end_date(self, e):
        if len(self.read_input_text(self.loan_duration_month)) > 0:
            self.repayment_times.SetLabelText(self.read_input_text(self.loan_duration_month))

        start_year = int(self.read_input_text(self.start_year))
        start_month = int(self.read_input_text(self.start_month))
        start_day = int(self.read_input_text(self.start_day))
        duartion_month = int(self.read_input_text(self.loan_duration_month))


        print("start calculate end date")
        total_m = duartion_month
        end_year = start_year + int(total_m / 12)
        end_month = start_month + total_m % 12
        if end_month > 12:
            end_month = end_month - 12
            end_year = end_year + 1
        end_day = start_day

        self.end_year.SetLabelText(str(end_year))
        self.end_month.SetLabelText(str(end_month))
        self.end_day.SetLabelText(str(end_day))
        # if start_year.isdigit() and start_month.isdigit() and start_day.isdigit() and duartion_month.isdigit():
        #     print("cal")

    def set_save_path(self, e):
        # Create open file dialog
        dlg = wx.DirDialog(self, "选择文件保存路径", style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            print (dlg.GetPath())  # 文件夹路径
            self.label_set_save_path.SetLabelText(dlg.GetPath())

        dlg.Destroy()
        pass

    def reset_file_save_path(self, file_name):
        path = self.label_set_save_path.GetLabelText()
        new_file = os.path.join(path, file_name)
        print("move to ", new_file)
        shutil.move(file_name, new_file)

    def check_input_valid(self):
        # if len(str(shen_fen_zheng)) != 3:
        #     wx.MessageBox("身份证输入有误，请检查", "提示", wx.OK | wx.ICON_INFORMATION)
        return True

    def generate_template(self, e):
        progress = wx.ProgressDialog("正在生成", "请稍等", maximum=100, parent=self,
                                     style=wx.PD_SMOOTH | wx.PD_AUTO_HIDE)
        # percent = 20
        # progress.Update(percent)

        input_arr = ['borrower_name1', 'borrower_home1', 'borrower_adress1',
                     'borrower_id1', 'borrower_phone1', 'borrower_name2',
                     'borrower_home2', 'borrower_adress2', 'borrower_id2',
                     'borrower_phone2', 'loan_proportion', 'loan_number_big',
                     'loan_number_small', 'house_location', 'house_area',
                     'house_price', 'loan_duration_month', 'start_year',
                     'start_month', 'start_day', 'end_year',
                     'end_month', 'end_day', 'standard_rate',
                      'float_num', 'actual_rate',
                     'account_name', 'account_num', 'repayment_times',
                      'repayment_num_big', 'repayment_num_small',
                     'pawn_num', 'contract_num', 'loan_contract_id',
                     'contract_id'
                     ]
        choice_arr = ['float_direction', 'repayment_method']

        borrower_name1 = self.read_input_text(self.borrower_name1)


        doc = DocxTemplate("模板.docx")

        progress.Update(10)

        context = {
            # 'borrower_name1': borrower_name1
        }

        if not self.check_input_valid():
            return

        # eval(): 将字符串转成成表达式计算，并返回结果
        for index in range(len(input_arr)):
            read_command = 'self.read_input_text(self.' + input_arr[index] + ')'
            context.update({input_arr[index]: eval(read_command)})
            progress.Update(10 + index)

        # eval(): 将字符串转成成表达式计算，并返回结果
        for index in range(len(choice_arr)):
            read_command = 'self.read_choice_text(self.' + choice_arr[index] + ')'
            context.update({choice_arr[index]: eval(read_command)})

        print(context)

        file_name = borrower_name1 + "_资料.docx"
        doc.render(context)

        progress.Update(80)

        doc.save(file_name)

        progress.Update(95)

        self.reset_file_save_path(file_name)

        progress.Update(100)
        progress.Destroy()

        wx.MessageBox("文件生成成功", "提示", wx.OK | wx.ICON_INFORMATION)

    def read_input_text(self, input):
        return input.GetLineText(0)

    def read_choice_text(self, ch):
        return ch.GetString(ch.GetSelection())


def main():
    app = wx.App()
    ex = MyFrame(None, title='合同自动生成器')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
