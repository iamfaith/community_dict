'''
调试代码运行的执行文件
    为了与正式运行的执行文件分开
'''

from src import 吉屋, 贝壳, 贝壳新房

# obj = 吉屋.吉屋()
# obj = 贝壳.贝壳()
# obj.run()


if __name__ == "__main__":
    clawer = 贝壳新房.BeikeNewHouse()
    clawer.getNewHouse()