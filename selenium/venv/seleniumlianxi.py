from selenium import webdriver

def main():
    # url = "https://blog.csdn.net/taolusi/article/details/81074102?utm_source=blogxgwz6"
    dirver = webdriver.Chrome
    html = dirver.get("https://blog.csdn.net/taolusi/article/details/81074102?utm_source=blogxgwz6")
    html_text = dirver.page_source
    print(html_text)
    dirver.quit()
if __name__ == '__main__':
    main()