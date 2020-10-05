from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class WhatsAppWebAPI:
	def __init__(self, chrome_userdata_path, chromedriver_path):
		self.options = webdriver.ChromeOptions()
		self.options.add_argument("--disable-session-crashed-bubble")
		self.options.add_argument("--disable-infobars")
		self.options.add_argument("user-data-dir=" + chrome_userdata_path)
		self.driver = webdriver.Chrome(executable_path=chromedriver_path, options=self.options)

	def talk_to(self, cellphone_number):
		self.driver.get('https://web.whatsapp.com/send?phone=' + cellphone_number)

	def send_msg(self, msg):
		timeout = 20
		try:
			element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'))
			WebDriverWait(self.driver, timeout).until(element_present)
		except TimeoutException:
			print("Timed out waiting for page to load...")
		# select message box
		msg_box = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
		# send messages with line breaks
		for line in msg.splitlines():
			msg_box.send_keys(line)
			ActionChains(self.driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).perform()
		# click send button
		# self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
		# or just click enter
		ActionChains(self.driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

	def get_driver(self):
		return self.driver

# TEST
if __name__=="__main__":
	chrome_userdata_path = "<DRIVER>:\\Users\\<USERNAME>\\AppData\\Local\\Google\\Chrome\\User Data"
	chromedriver_path = "chromedriver.exe"
	whatsapp_api = WhatsAppWebAPI(chrome_userdata_path, chromedriver_path)

	whatsapp_api.talk_to("<NUMBER>")

	whatsapp_api.send_msg("<MESSAGE>")

	whatsapp_api.get_driver().quit()