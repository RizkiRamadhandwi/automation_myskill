import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# test navigation
class TestNavigation():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}
    

    def teardown_method(self, method):
        self.driver.quit()
    
    def wait_for_window(self, timeout=2):
        time.sleep(round(timeout / 1200))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()


    def test_navigation(self):
        self.driver.get("https://myskill.id/")
        self.driver.set_window_size(1200, 700)
        time.sleep(5)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "E-learning"))
        ).click()
        time.sleep(5)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Bootcamp & Program"))
        ).click()
        time.sleep(5)
        
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Mentoring"))
        ).click()
        time.sleep(5)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Corporate Service"))
        ).click()
        time.sleep(5)

        self.vars["window_handles"] = self.driver.window_handles

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Blog"))
        ).click()
        time.sleep(5)

        self.vars["win466"] = self.wait_for_window(2000)
        self.vars["root"] = self.driver.current_window_handle
        self.driver.switch_to.window(self.vars["win466"])
        self.driver.close()
        self.driver.switch_to.window(self.vars["root"])

       
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Home"))
        ).click()
        time.sleep(5)

        self.driver.close()


# test register
class TestRegisterInvalidNotField():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_register_invalid_not_field(self):
        self.driver.get("https://myskill.id/")
        self.driver.set_window_size(1200, 700)

        
        masuk_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Daftar"))
        )
        masuk_link.click()
        time.sleep(2)
        
        register_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, ":r3:"))
        )
        register_button.click()

        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, ":r0:-helper-text"))
        )   
        assert error_message.text == "Email tidak valid"

        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, ":r1:-helper-text"))
        )   
        assert error_message.text == "Password harus terdiri dari setidaknya 6 karakter"
        time.sleep(2)

        self.driver.close()

class TestRegisterInvalidEmail():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_register_invalid_email(self):
        self.driver.get("https://myskill.id/")
        self.driver.set_window_size(1200, 700)

        
        masuk_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Daftar"))
        )
        masuk_link.click()
        time.sleep(2)

        
        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r0:"))
        )
        email_input.click()
        email_input.send_keys("admin@damn.com")

        time.sleep(2)

     
        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r1:"))
        )
        password_input.click()
        password_input.send_keys("1231313")
        time.sleep(2)

        confirm_password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r2:"))
        )
        confirm_password_input.click()
        confirm_password_input.send_keys("1231313")
        time.sleep(2)

        agree_checkbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".PrivateSwitchBase-input"))
        )
        agree_checkbox.click()
        time.sleep(2)
        
        register_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, ":r3:"))
        )
        register_button.click()

        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".MuiAlert-root"))
        )

        assert error_message.text == "Email yang kamu masukkan tidak valid, pastikan kamu sudah memasukkan alamat email dengan benar dan tidak menggunakan email sementara."
        time.sleep(2)

        self.driver.close()

class TestRegisterInvalidPasswordWeak():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_register_invalid_password_weak(self):
        self.driver.get("https://myskill.id/")
        self.driver.set_window_size(1200, 700)

        
        masuk_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Daftar"))
        )
        masuk_link.click()
        time.sleep(2)

        
        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r0:"))
        )
        email_input.click()
        email_input.send_keys("rizki.test0@gmail.com")

        time.sleep(2)

     
        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r1:"))
        )
        password_input.click()
        password_input.send_keys("Test")
        time.sleep(2)

        confirm_password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r2:"))
        )
        confirm_password_input.click()
        confirm_password_input.send_keys("Test")
        time.sleep(2)

        agree_checkbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".PrivateSwitchBase-input"))
        )
        agree_checkbox.click()
        time.sleep(2)
        
        register_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, ":r3:"))
        )
        register_button.click()

        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, ":r1:-helper-text"))
        )   

        assert error_message.text == "Password harus terdiri dari setidaknya 6 karakter"
        time.sleep(2)

        self.driver.close()

class TestRegisterInvalidPasswordNotMatch():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_register_invalid_password_not_match(self):
        self.driver.get("https://myskill.id/")
        self.driver.set_window_size(1200, 700)

        
        masuk_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Daftar"))
        )
        masuk_link.click()
        time.sleep(2)

        
        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r0:"))
        )
        email_input.click()
        email_input.send_keys("rizki.test0@gmail.com")

        time.sleep(2)

     
        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r1:"))
        )
        password_input.click()
        password_input.send_keys("Test12!@")
        time.sleep(2)

        confirm_password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r2:"))
        )
        confirm_password_input.click()
        confirm_password_input.send_keys("Test1212")
        time.sleep(2)

        agree_checkbox = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".PrivateSwitchBase-input"))
        )
        agree_checkbox.click()
        time.sleep(2)
        
        register_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, ":r3:"))
        )
        register_button.click()

        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, ":r2:-helper-text"))
        )   

        assert error_message.text == "Konfirmasi password harus sama dengan password"
        time.sleep(2)

        self.driver.close()

class TestRegisterInvalidExistingEmail():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_register_invalid_existing_email(self):
        self.driver.get("https://myskill.id/")
        self.driver.set_window_size(1200, 700)

        
        masuk_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Daftar"))
        )
        masuk_link.click()
        time.sleep(2)

        
        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r0:"))
        )
        email_input.click()
        email_input.send_keys("rizki.test0@gmail.com")

        time.sleep(2)

     
        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r1:"))
        )
        password_input.click()
        password_input.send_keys("Test1212")
        time.sleep(2)

        confirm_password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r2:"))
        )
        confirm_password_input.click()
        confirm_password_input.send_keys("Test1212")
        time.sleep(2)
        
        register_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, ":r3:"))
        )
        register_button.click()

        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".MuiAlert-root"))
        )

        assert error_message.text == "Kamu sudah terdaftar, silahkan login"
        time.sleep(2)

        self.driver.close()

class TestRegisterValid():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()
    
    def test_register_valid(self):
        self.driver.get("https://myskill.id/")
        self.driver.set_window_size(1200, 700)

        masuk_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Daftar"))
        )
        masuk_link.click()
        time.sleep(2)

        
        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r0:"))
        )
        email_input.click()
        # ganti akun kalau test ulang
        email_input.send_keys("rizki.test11@gmail.com")
        

        time.sleep(2)

     
        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r1:"))
        )
        password_input.click()
        password_input.send_keys("Test1234")
        time.sleep(2)

        confirm_password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r2:"))
        )
        confirm_password_input.click()
        confirm_password_input.send_keys("Test1234")
        time.sleep(2)

        
        register_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, ":r3:"))
        )
        register_button.click()
        # ganti email baru kalau failed

        success_message = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "notistack-snackbar"))
        )

        assert success_message.text == "Akun berhasil didaftarkan!"
        time.sleep(2)

        self.driver.close()


# test forgot password
class TestForgotPasswordInvalidEmail():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_login_forgot_password_invalid_email(self):
        self.driver.get("https://myskill.id/")
        self.driver.set_window_size(1200, 700)

        
        masuk_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Masuk"))
        )
        masuk_link.click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Lupa password?"))
        ).click()

        
        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r5:"))
        )
        email_input.click()
        email_input.send_keys("admin@damn.com")
        

        
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r6:"))
        ).click()


        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".MuiAlert-root"))
        )

        assert error_message.text == "Email yang ada masukkan tidak terdaftar."

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Kembali"))
        ).click()
      
        self.driver.close()

class TestForgotPasswordValid():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_login_forgot_password_valid(self):
        self.driver.get("https://myskill.id/")
        self.driver.set_window_size(1200, 700)

        
        masuk_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Masuk"))
        )
        masuk_link.click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Lupa password?"))
        ).click()

        
        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r5:"))
        )
        email_input.click()
        email_input.send_keys("rizki.test0@gmail.com")
        

        
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r6:"))
        ).click()


        success_message = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "notistack-snackbar"))
        )

        assert success_message.text == "Email reset password berhasil dikirimkan, silahkan cek inbox kamu!"

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Kembali"))
        ).click()
      
        self.driver.close()


# test Login
class TestLoginInvalidNotField():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_login_invalid_not_field(self):
        self.driver.get("https://myskill.id/")
        self.driver.set_window_size(1200, 700)

        
        masuk_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Masuk"))
        )
        masuk_link.click()
        
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, ":r2:"))
        )
        login_button.click()

        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, ":r0:-helper-text"))
        )   
        assert error_message.text == "Email must be a valid email address"

        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, ":r1:-helper-text"))
        )   
        assert error_message.text == "Password is required"

        time.sleep(2)

        self.driver.close()        

class TestLoginInvalidEmail():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_login_invalid_email(self):
        self.driver.get("https://myskill.id/")
        self.driver.set_window_size(1200, 700)

        
        masuk_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Masuk"))
        )
        masuk_link.click()

        
        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r0:"))
        )
        email_input.click()
        email_input.send_keys("admin@damn.com")

        time.sleep(2)

     
        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r1:"))
        )
        password_input.click()
        password_input.send_keys("1231313")
        time.sleep(2)
        
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, ":r2:"))
        )
        login_button.click()

        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".MuiAlert-root"))
        )

        assert error_message.text == "Email yang ada masukkan tidak terdaftar."

        time.sleep(2)

        self.driver.close()

class TestLoginInvalidPassword():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_login_invalid_password(self):
        self.driver.get("https://myskill.id/")
        self.driver.set_window_size(1200, 700)

        
        masuk_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Masuk"))
        )
        masuk_link.click()

        
        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r0:"))
        )
        email_input.click()
        email_input.send_keys("rizki.test0@gmail.com")
        time.sleep(2)

        
        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r1:"))
        )
        password_input.click()
        password_input.send_keys("Test1212")
        time.sleep(2)

    
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, ":r2:"))
        )
        login_button.click()
        
        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".MuiAlert-root"))
        )

        assert error_message.text == "Password yang kamu masukkan tidak valid."

        time.sleep(2)
      
        self.driver.close()

class TestLoginValid():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_login_valid(self):
        self.driver.get("https://myskill.id/")
        self.driver.set_window_size(1200, 700)

        
        masuk_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Masuk"))
        )
        masuk_link.click()

        
        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r0:"))
        )
        email_input.click()
        email_input.send_keys("rizki.test0@gmail.com")
        time.sleep(2)

        
        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r1:"))
        )
        password_input.click()
        password_input.send_keys("Test1234")
        time.sleep(2)

    
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, ":r2:"))
        )
        login_button.click()

        success_message = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "notistack-snackbar"))
        )

        assert success_message.text == "Login berhasil!"

        time.sleep(2)
      
        self.driver.close()


# test Home page
class TestHomePageViewProgram():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_elements_on_home_page(self):
        self.driver.get("https://myskill.id/")
        self.driver.set_window_size(1200, 700)
        time.sleep(5)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiGrid-root:nth-child(1) > .MuiBox-root > .mui-style-goxg3h"))
        ).click()
        time.sleep(2)
        
        self.driver.close()

class TestHomePageViewStory():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_elements_on_home_page(self):
        self.driver.get("https://myskill.id/")
        self.driver.set_window_size(1200, 700)
        time.sleep(5)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Baca Cerita"))
        ).click()
        time.sleep(5)
        
        self.driver.close()

class TestHomePageViewMateriByInstructor():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_elements_on_home_page(self):
        self.driver.get("https://myskill.id/")
        self.driver.set_window_size(1200, 700)
        time.sleep(5)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Lihat Materi"))
        ).click()
        time.sleep(5)
        
        self.driver.close()

class TestHomePageViewQuetion():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_elements_on_home_page(self):
        self.driver.get("https://myskill.id/")
        self.driver.set_window_size(1200, 700)
        time.sleep(5)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiPaper-root:nth-child(1) .MuiAccordionSummary-content"))
        ).click()
        time.sleep(2)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiPaper-root:nth-child(2) > .MuiButtonBase-root .MuiTypography-root"))
        ).click()
        time.sleep(2)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiPaper-root:nth-child(3) > .MuiButtonBase-root .MuiTypography-root"))
        ).click()
        time.sleep(2)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiPaper-root:nth-child(4) > .MuiButtonBase-root .MuiTypography-root"))
        ).click()
        time.sleep(2)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiPaper-root:nth-child(5) > .MuiButtonBase-root .MuiTypography-root"))
        ).click()
        time.sleep(2)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiPaper-root:nth-child(1) .MuiAccordionSummary-content"))
        ).click()
        time.sleep(2)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiPaper-root:nth-child(2) > .MuiButtonBase-root .MuiTypography-root"))
        ).click()
        time.sleep(2)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiPaper-root:nth-child(3) > .MuiButtonBase-root .MuiTypography-root"))
        ).click()
        time.sleep(2)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiPaper-root:nth-child(4) > .MuiButtonBase-root .MuiTypography-root"))
        ).click()
        time.sleep(2)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".Mui-expanded > .MuiTypography-root"))
        ).click()
        time.sleep(2)
        
        self.driver.close()

class TestHomePageCallWhatsApp():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_elements_on_home_page(self):
        self.driver.get("https://myskill.id/")
        self.driver.set_window_size(1200, 700)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "WhatsApp"))
        ).click()
        
        self.driver.close()


# test Elerning page
class TestElerningPageStartSubcribe():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    
    def teardown_method(self, method):
        self.driver.quit()


    def test_elements_on_elerning_page(self):
        self.driver.get("https://myskill.id/")
        self.driver.set_window_size(1200, 700)
        
        masuk_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Masuk"))
        )
        masuk_link.click()

        
        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r0:"))
        )
        email_input.click()
        email_input.send_keys("rizki.test0@gmail.com")

        
        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r1:"))
        )
        password_input.click()
        password_input.send_keys("Test1234")

    
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, ":r2:"))
        )
        login_button.click()
        time.sleep(5)


        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "E-learning"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".mui-style-1upjqve"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".mui-style-18rjq1w"))
        ).click()

        message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".mui-style-1tppb6j"))
        )

        assert message.text == "Berlangganan E-Learning"
        
        time.sleep(5)

        self.driver.close()

class TestElerningPageViewMateri():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    
    def teardown_method(self, method):
        self.driver.quit()


    def test_elements_on_elerning_page(self):
        self.driver.get("https://myskill.id/")
        self.driver.set_window_size(1200, 700)


        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "E-learning"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".mui-style-12dexbr"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiGrid-root:nth-child(7) .MuiCardContent-root > .MuiTypography-root"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiBox-root:nth-child(1) > div:nth-child(2) > .MuiBox-root:nth-child(1) > .MuiGrid-root:nth-child(1) > .MuiGrid-root:nth-child(1) .MuiBox-root:nth-child(4)"))
        ).click()

        message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".MuiTypography-h2"))
        )

        assert message.text == "Quality Assurance Introduction"
        
        time.sleep(5)

        self.driver.close()

class TestElerningPageViewStoryMember():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_elements_on_elerning_page(self):
        self.driver.get("https://myskill.id/")
        self.driver.set_window_size(1200, 700)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "E-learning"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Baca Cerita"))
        ).click()

        self.driver.close()

class TestElerningPageViewMateriByInstructor():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_elements_on_elerning_page(self):
        self.driver.get("https://myskill.id/")
        self.driver.set_window_size(1200, 700)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "E-learning"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Lihat Materi"))
        ).click()
        # time.sleep(5)

        self.driver.close()

class TestElerningPageViewPortofolioMember():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_elements_on_elerning_page(self):
        self.driver.get("https://myskill.id/")
        self.driver.set_window_size(1200, 700)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "E-learning"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiGrid-root:nth-child(3) .MuiStack-root > .MuiButtonBase-root"))
        ).click()
        # time.sleep(5)

        self.driver.close()

class TestElerningPageCallWhatsApp():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_elements_on_elerning_page(self):
        self.driver.get("https://myskill.id/")
        self.driver.set_window_size(1200, 700)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "E-learning"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "WhatsApp"))
        ).click()

        self.driver.close()

class TestElerningPageTrainingForCorporate():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_elements_on_elerning_page(self):
        self.driver.get("https://myskill.id/")
        self.driver.set_window_size(1200, 700)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "E-learning"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Hubungi Tim MySkill"))
        ).click()

        # time.sleep(5)

        self.driver.close()


# test bootcamp page
class TestBootcampPageStartBootcamp():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    
    def teardown_method(self, method):
        self.driver.quit()


    def test_elements_on_bootcamp_page(self):
        self.driver.get("https://myskill.id/")
        self.driver.set_window_size(1200, 700)
        
        masuk_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Masuk"))
        )
        masuk_link.click()

        
        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r0:"))
        )
        email_input.click()
        email_input.send_keys("rizki.test0@gmail.com")

        
        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r1:"))
        )
        password_input.click()
        password_input.send_keys("Test1234")

    
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, ":r2:"))
        )
        login_button.click()
        time.sleep(5)


        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Bootcamp & Program"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiButton-sizeLarge"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiGrid-root:nth-child(3) .MuiBox-root > .MuiBox-root > .MuiBox-root > .MuiBox-root"))
        ).click()
    

        self.driver.close()

class TestBootcampPageViewStoryAlumnus():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_elements_on_bootcamp_page(self):
        self.driver.get("https://myskill.id/")
        self.driver.set_window_size(1200, 700)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Bootcamp & Program"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Baca Cerita"))
        ).click()

        self.driver.close()

class TestBootcampPageCallWhatsApp():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_elements_on_bootcamp_page(self):
        self.driver.get("https://myskill.id/")
        self.driver.set_window_size(1200, 700)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Bootcamp & Program"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "WhatsApp"))
        ).click()

        self.driver.close()

class TestBootcampPageTrainingForCorporate():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_elements_on_bootcamp_page(self):
        self.driver.get("https://myskill.id/")
        self.driver.set_window_size(1200, 700)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Bootcamp & Program"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Hubungi Tim MySkill"))
        ).click()

        # time.sleep(5)

        self.driver.close()


#  test mentoring page
class TestMentoringPageStartRegister():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    
    def teardown_method(self, method):
        self.driver.quit()


    def test_elements_on_mentoring_page(self):
        self.driver.get("https://myskill.id/")
        self.driver.set_window_size(1200, 700)
        
        masuk_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Masuk"))
        )
        masuk_link.click()

        
        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r0:"))
        )
        email_input.click()
        email_input.send_keys("rizki.test0@gmail.com")

        
        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r1:"))
        )
        password_input.click()
        password_input.send_keys("Test1234")

    
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, ":r2:"))
        )
        login_button.click()
        time.sleep(5)


        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Mentoring"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiButton-sizeLarge"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Daftar Sekarang"))
        ).click()

        message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".mui-style-1tppb6j"))
        )

        assert message.text == "Berlangganan Review CV"
        
        time.sleep(5)

        self.driver.close()

class TestMentoringPageViewStoryTestimoni():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_elements_on_mentoring_page(self):
        self.driver.get("https://myskill.id/")
        self.driver.set_window_size(1200, 700)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Mentoring"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Baca Cerita"))
        ).click()

        self.driver.close()

class TestMentoringPageCallWhatsApp():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_elements_on_mentoring_page(self):
        self.driver.get("https://myskill.id/")
        self.driver.set_window_size(1200, 700)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Mentoring"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "WhatsApp"))
        ).click()

        self.driver.close()


# test corporate service page
class TestCorporatePageStartConsultationCorporateTraning():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    
    def teardown_method(self, method):
        self.driver.quit()


    def test_elements_on_corporate_page(self):
        self.driver.get("https://myskill.id/")
        self.driver.set_window_size(1200, 700)


        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Corporate Service"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Corporate Training"))
        ).click()
        time.sleep(5)

        self.driver.close()     

class TestCorporatePageStartConsultationPerformace():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    
    def teardown_method(self, method):
        self.driver.quit()


    def test_elements_on_corporate_page(self):
        self.driver.get("https://myskill.id/")
        self.driver.set_window_size(1200, 700)


        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Corporate Service"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Performance Management Software"))
        ).click()
        time.sleep(5)

        self.driver.close()  
        
class TestCorporatePageCallWhatsApp():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_elements_on_corporate_page(self):
        self.driver.get("https://myskill.id/")
        self.driver.set_window_size(1200, 700)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Corporate Service"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "WhatsApp"))
        ).click()

        self.driver.close()

class TestCorporatePageTrainingForCorporate():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_elements_on_corporate_page(self):
        self.driver.get("https://myskill.id/")
        self.driver.set_window_size(1200, 700)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Corporate Service"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div:nth-child(3) > .MuiGrid-root .MuiButtonBase-root"))
        ).click()

        # time.sleep(5)

        self.driver.close()


# test profile
class TestProfilePageNavigation():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_elements_on_profile_page(self):
        self.driver.get("https://myskill.id/")
        self.driver.set_window_size(1200, 700)

        masuk_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Masuk"))
        )
        masuk_link.click()

        
        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r0:"))
        )
        email_input.click()
        email_input.send_keys("rizki.test0@gmail.com")

        
        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r1:"))
        )
        password_input.click()
        password_input.send_keys("Test1234")

    
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, ":r2:"))
        )
        login_button.click()
        time.sleep(5)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiAvatar-root"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Profil"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiButtonBase-root:nth-child(2) .MuiTypography-root"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiButtonBase-root:nth-child(3) .MuiTypography-root"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiButtonBase-root:nth-child(4) .MuiTypography-root"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiButtonBase-root:nth-child(1) .MuiTypography-root"))
        ).click()
        time.sleep(5)


        self.driver.close()

class TestProfilePageCallWhatsApp():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_elements_on_profile_page(self):
        self.driver.get("https://myskill.id/")
        self.driver.set_window_size(1200, 700)

        masuk_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Masuk"))
        )
        masuk_link.click()

        
        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r0:"))
        )
        email_input.click()
        email_input.send_keys("rizki.test0@gmail.com")

        
        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r1:"))
        )
        password_input.click()
        password_input.send_keys("Test1234")

    
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, ":r2:"))
        )
        login_button.click()
        time.sleep(5)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".MuiAvatar-root"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Profil"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "WhatsApp"))
        ).click()

        self.driver.close()



if __name__ == "__main__":
    pytest.main()
