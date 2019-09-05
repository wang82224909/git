import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def main():
    url = "http://www.baobao88.com/plus/search.php?kwtype=0&keyword=%BC%BD%BD%CC12%B0%E6&x=0&y=0"

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

    html = requests.get(url, headers=header)
    soup = BeautifulSoup(html.text)
    ret = soup.find("div", class_="search_nr").find_all("a", target="_blank")
    for li in ret:
        # downurl = li["href"]
        # downhtml = requests.get(downurl, headers=header)
        # downsoup = BeautifulSoup(downhtml.text)
        # print(downsoup)
        driver = webdriver.chrome()
        downurl2 = ("http://dt.baobao88.com/au_play.php?id=127993")
        # 调用本地的火狐浏览器，Chrom 甚至 Ie 也可以的
        driver.get(downurl2)  # 请求页面，会打开一个浏览器窗口
        html_text = driver.page_source
        print(heml_text)
        driver.quit()


if __name__ == "__main__":
    main()
