import requests
from selenium import webdriver
import time
def main():
    n = 14
    while n < 48:
        url_main = "http://www.baobao88.com/youshen/en/03/261273%s.html"%n
        # url_main ="http://www.baobao88.com/youshen/en/01/031835%s.html"%n
        # url_main =  "http://www.baobao88.com/youshen/en/03/271274%s.html"%n
        # url_main = "http://www.baobao88.com/youshen/en/03/301275%s.html"%n
        print(url_main)
        # url_main = "http://www.baobao88.com/youshen/en/03/30127565.html"
        driver = webdriver.Chrome()
        html = driver.get(url_main)
        html_text = driver.page_source
        # print(html_text)
        # b = driver.find_elements_by_id('playicon')
        # for all_src1 in b:
        #     src1 = all_src1.get_attribute("src")
        #     print(src1)
        c = driver.find_elements_by_xpath("//*[@id='jp_audio_0']")
        d = driver.find_elements_by_xpath("//*[@id='cright']/span/img")
        for all_name in d:
            name = all_name.get_attribute("alt")
            print(name)
        for all_src in c:
            src = all_src.get_attribute("src")
            # print(src)
            with open("%s.mp3"%name, "ab") as f:
                r = requests.get(src)
                f.write(r.content)
                print("下载成功")


        n+=1
        print(n)

        driver.quit()
        time.sleep(5)
    else:
        print("下载完成")



        # url = "http://play.baobao88.com/vbaobao88/vid-dd900d87d6cb14678c022bd958fac795/bbfile/media/000004/冀教/冀教12版三下Unit1 Again/49e97d7e.mp3"
        # with open("1again.mp3","ab") as f:
        #     r = requests.get(url)
        #     f.write(r.content)


if __name__ == '__main__':
    main()

