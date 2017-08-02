class CategoryMap(object):

    def incomeCategoryMapList(self,sourceList):
        incomeCategory = {
                            '利息收入':['1','1'],
                            '回收借出资金(收入)':['2','1'],
                            '收到临时借入款(收入)':['2','2'],
                            '收回投资利息(收入)':['3','1'],
                            '收回投资本金(收入)':['3','2'],
                            '收到投资款':['3','3'],
                            '银行贷款(收入)':['3','4'],
                            '应收账款':['4','1']
                          }
        for key,value in zip(incomeCategory.keys(),incomeCategory.values()):
            if key == sourceList[3]:
                sourceList[3] = value
        return sourceList