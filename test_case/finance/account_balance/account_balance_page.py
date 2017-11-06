from selenium import webdriver
import time

class AccountBalancePage(object):
    def __init__(self,driver):
        self.driver = webdriver.Chrome()
        # self.driver = driver

    # 获得row_num行次，xpath tr_num 
    def get_row_tr_num(self,asset_name):
        if asset_name == '货币资金':
            return row_num = 1,tr_num = 2
        elif asset_name == '短期投资' :
            return row_num = 2,tr_num = 3 
        elif asset_name == '应收票据':
            return row_num = 3,tr_num = 4
        elif asset_name == '应收账款':
            return row_num = 4,tr_num = 5
        elif asset_name == '预付款项:
            return row_num = 5 ,tr_num = 6
        elif asset_name == '应收股利':
            return row_num = 6, tr_num = 7
        elif asset_name == '应收利息':
            return row_num = 7, tr_num = 8
        elif asset_name == '其他应收款':
            return row_num = 8, tr_num = 9
        elif asset_name == '存货':
            return row_num = 9,tr_num = 10
        elif asset_name == '其中：原材料':
            return row_num = 10,tr_num = 11
        elif asset_name == '在产品':
            return row_num = 11, tr_num = 12
        elif asset_name == '库存商品':
            return row_num = 12,tr_num = 13
        elif asset_name == '周转材料':
            return row_num = 13,tr_num = 14 
        elif asset_name == '其他流动资产':
            return row_num = 14,tr_num = 15
        elif asset_name == '流动资产合计':
            return row_num = 15,tr_num = 16
        elif asset_name == '长期债券投资':
            return row_num = 16,tr_num = 18
        elif asset_name == '长期股权投资':
            return row_num = 17,tr_num = 19
        elif asset_name == '固定资产原价':
            return row_num = 18,tr_num = 20
        elif asset_name == '减：累积折旧':
            return row_num = 19,tr_num = 21
        elif asset_name == '固定资产帐面价值':
            return row_num = 20,tr_num = 22
        elif asset_name == '在建工程':
            return row_num = 21,tr_num = 23
        elif asset_name == '工程物资':
            return row_num = 22,tr_num = 24
        elif asset_name == '固定资产清理':
            return row_num = 23,tr_num = 25
        elif asset_name == '生产性生物资产':
            return row_num = 24,tr_num = 26
        elif asset_name == '无形资产':
            return row_num = 25,tr_num = 27
        elif asset_name == '开发支出':
            return row_num = 26,tr_num = 28
        elif asset_name == '长期待摊费用':
            return row_num = 27,tr_num = 29
        elif asset_name == '其他非流动资产':
            return row_num = 28,tr_num = 30
        elif asset_name == '非流动资产合计':
            return row_num = 29,tr_num = 31
        elif asset_name == '资产合计':
            return row_num = 30,tr_num = 32

