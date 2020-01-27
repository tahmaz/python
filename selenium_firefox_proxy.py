from selenium import webdriver
import time


"Define Both ProxyHost and ProxyPort as String"
ProxyHost = "54.84.95.51" 
ProxyPort = "8083"



def ChangeProxy(ProxyHost ,ProxyPort):
    "Define Firefox Profile with you ProxyHost and ProxyPort"
    profile = webdriver.FirefoxProfile()
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.http", ProxyHost )
    profile.set_preference("network.proxy.http_port", int(ProxyPort))
    profile.update_preferences()
    return webdriver.Firefox(firefox_profile=profile)


def FixProxy():
    ""Reset Firefox Profile""
    profile = webdriver.FirefoxProfile()
    profile.set_preference("network.proxy.type", 0)
    return webdriver.Firefox(firefox_profile=profile)


driver = ChangeProxy(ProxyHost ,ProxyPort)
driver.get("http://whatismyipaddress.com")

time.sleep(5)

driver = FixProxy()
driver.get("http://whatismyipaddress.com")