import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from ui_asinfetcher import Ui_MainWindow
from ui_asinfetchersettings import Ui_SettingsWindow
from PySide6.QtCore import QTimer, QCoreApplication, QThread, Signal
from email_password import check_account, check_username
from scan_asin import asin_scan_fnc

class Worker(QThread):
    """
    Arka planda uzun süren işlemi gerçekleştiren sınıf.
    """

    finished = Signal()

    def __init__(self, location, log_screen, yukleme_ekrani):
        super().__init__()
        self.location = location
        self.log_screen = log_screen
        self.yukleme_ekrani = yukleme_ekrani

    def run(self):
        """
        Uzun süren işlemi gerçekleştirir ve işlem tamamlandığında finished sinyalini gönderir.
        """
        try:
            asin_scan_fnc(self.location, self.log_screen, self.yukleme_ekrani)
        except Exception as e:
            print("An error occurred in Worker run method:", e)
        finally:
            self.finished.emit()

class MainWindow(QMainWindow):
    def __init__(self):
        try:
            super().__init__()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.show()
            self.ui.pushButton.clicked.connect(self.print_asin)
        except Exception as e:
            print("An error occurred in MainWindow __init__:", e)

    def print_asin(self):
        try:
            QTimer.singleShot(2000, self.run_selenium)
        except Exception as e:
            print("An error occurred in print_asin:", e)

    def run_selenium(self):
        try:
            email = self.ui.lineEdit.text()
            password = self.ui.lineEdit_2.text()
            status = check_account(email, password)
            print(status)

            if status == False:
                self.close()
                return

            account_name, product_limit, user_product_limit, your_product = check_username(email, password)
            print(account_name)
            print(product_limit)
            print(user_product_limit)
            print(your_product)

            if status == True:
                self.open_settings(account_name, product_limit, user_product_limit, your_product)
        except Exception as e:
            print("An error occurred in run_selenium:", e)

    def open_settings(self, account_name, product_limit, user_product_limit, your_product):
        try:
            self.ui = Ui_SettingsWindow()
            self.ui.setupUi(self)
            self.show()
            self.ui.username.setText(QCoreApplication.translate("MainWindow", f"{account_name}", None))
            self.ui.product_count.setText(QCoreApplication.translate("MainWindow", f"{your_product}", None))
            self.ui.product_limit_count.setText(QCoreApplication.translate("MainWindow", f"{product_limit}", None))
            self.ui.daily_scanner_count.setText(QCoreApplication.translate("MainWindow", f"{user_product_limit}", None))

            self.ui.asin_folder_button.clicked.connect(self.browseFiles)
            self.ui.start_button.clicked.connect(self.start_button_clicked)
        except Exception as e:
            print("An error occurred in open_settings:", e)

    def browseFiles(self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Open File', 'D:', 'Excel Files (*.xlsx)')
            self.ui.asin_dosya_konumu.setText(fname[0])
            return fname[0]
        except Exception as e:
            print("An error occurred in browseFiles:", e)
    
    def start_button_clicked(self):
        try:
            self.ui.yukleme_ekrani.setValue(0)
            self.ui.log_screen.clear()
            location = self.ui.asin_dosya_konumu.text()
            if not location:
                self.ui.asin_dosya_konumu.setStyleSheet(u"border: 1px solid red;\n"
                                                        "border-radius: 15px;\n"
                                                        "background-color:white;")
                return
            else:
                print(location)
                self.ui.asin_dosya_konumu.setStyleSheet(u"border-radius: 15px;\n"
                                                        "background-color:white;")
                # Worker sınıfını kullanarak uzun süren işlemi arka planda çalıştır
                worker = Worker(location, self.ui.log_screen, self.ui.yukleme_ekrani)
                worker.finished.connect(worker.deleteLater)  # Worker nesnesini silmek için finished sinyalini bağla
                worker.finished.connect(self.handle_finished)
                worker.start()
        except Exception as e:
            print("An error occurred in start_button_clicked:", e)
    
    def handle_finished(self):
        """
        Uzun süren işlem tamamlandığında çağrılır ve gerekirse gerekli işlemleri yapar.
        """
        pass

if __name__ == "__main__":
    try:
        app = QApplication([])
        window = MainWindow()   
        app.exec()
    except Exception as e:
        print("An error occurred in main:", e)
