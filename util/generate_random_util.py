import random

class GenerateRandom(object):

    #生成8位随机整数
    def generateRandom(self):
        invoiceNum = ''
        for i in range(0,8) :
            invoiceNum = invoiceNum + str(random.randint(0,9))
        return invoiceNum

    def invoiceNumList(self,invoiceSum):
        invoiceNumList = []
        for i in range(0,invoiceSum):
            invoiceNumList.append(self.generateRandom())
        return invoiceNumList