from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import sys

# 日期
date=sys.argv[1]
# 货币代号
currency_code=sys.argv[2]
# 浏览器驱动位置
driver_path=r"C:\Users\15356\Desktop\solve\chromedriver.exe"
# 存储货币代号与中文名之间的映射关系
currency_dict={
    "GBP":"英镑",
    "HKD":"港币",
    "USD":"美元",
    "CHF":"瑞士法郎",
    "DEM":"德国马克",
    "FRF":"法国法郎",
    "SGD":"新加坡元",
    "SEK":"瑞典克朗",
    "DKK":"丹麦克朗",
    "NOK":"挪威克朗",
    "JPY":"日元",
    "CAD":"加拿大元",
    "AUD":"澳大利亚元",
    "EUR":"欧元",
    "MOP":"澳门元",
    "PHP":"菲律宾比索",
    "THP":"泰国铢",
    "NZD":"新西兰元",
    "KRW":"韩元",
    "SUR":"卢布",
    "MYR":"林吉特",
    "TWD":"新台币",
    "ESP":"西班牙比塞塔",
    "ITL":"意大利里拉",
    "NLG":"荷兰盾",
    "BEF":"比利时法郎",
    "FIM":"芬兰马克",
    "INR":"印度卢比",
    "IDR":"印尼卢比",
    "BRL":"巴西里亚尔",
    "AED":"阿联酋迪拉姆",
    "ZAR":"南非兰特",
    "SAR":"沙特里亚尔",
    "TRL":"土耳其里拉"
}
try:
    currency_code=currency_dict[currency_code]
except KeyError:
    print("请输入正确的货币代号")
    sys.exit(1)

# 开始爬取
try:
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get("https://www.boc.cn/sourcedb/whpj/")
    # 输入日期
    driver.find_element(By.CSS_SELECTOR,"[name='erectDate']").send_keys(date)
    driver.find_element(By.CSS_SELECTOR,"[name='nothing']").send_keys(date)
    # 选择货币
    select=Select(driver.find_element(By.ID,"pjname"))
    select.select_by_visible_text(currency_code)
    # 点击查询
    driver.find_element(By.XPATH,"//*[@id='historysearchform']/div/table/tbody/tr/td[7]/input").click()
    # 获取结果
    element=driver.find_element(By.XPATH,"/html/body/div[1]/div[4]/table/tbody/tr[2]/td[4]")
    with open("result.txt","w") as file:
        file.write(element.text)
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()