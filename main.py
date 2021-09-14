from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from dialog_main import Ui_Dialog
from login_page import Ui_MainWindow
from daily_dialog import Ui_Dialog as daily
from week_dialog import Ui_Dialog as week
from question_dialog import Ui_Dialog as question
from single_month_dialog import Ui_single_month
from every_month_dialog import Ui_Dialog as every_month
from login_enter import Ui_Dialog as enter
from final_words import Ui_Dialog as success
from home_login import Ui_Dialog as my_page
from daily_usage import Ui_Dialog as my_daily_money
from weekly_usage import Ui_Dialog as my_weekly_money
from every_month_usage import Ui_Dialog as my_monthly_money
from edit_profile import Ui_Dialog as profile
from edit_account import Ui_Dialog as account
from second_final_words import Ui_Dialog as edit_success
import json
import matplotlib.pyplot as plt

# signup home page 
class dialog(QDialog):
    def __init__(self,perent=None):
        super(dialog, self).__init__(perent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

# For user signup with daily salary
class daily_wage(QDialog):
    def __init__(self,perent=None):
        super(daily_wage, self).__init__(perent)
        self.ui1 = daily()
        self.ui1.setupUi(self)
        self.ui1.buttonBox.accepted.connect(self.accept)
        self.ui1.buttonBox.rejected.connect(self.reject)

# For user signup with weekly salary
class weekly_wage(QDialog):
    def __init__(self,perent=None):
        super(weekly_wage, self).__init__(perent)
        self.ui2 = week()
        self.ui2.setupUi(self)
        self.ui2.buttonBox.accepted.connect(self.accept)
        self.ui2.buttonBox.rejected.connect(self.reject)
        
# querying about user's monthly salary
class question_wage(QDialog):
    def __init__(self,perent=None):
        super(question_wage, self).__init__(perent)
        self.ui3 = question()
        self.ui3.setupUi(self)

# For user signup with constant monthly salary
class constant_monthly_wage(QDialog):
    def __init__(self,perent=None):
        super(constant_monthly_wage, self).__init__(perent)
        self.ui4 = Ui_single_month()
        self.ui4.setupUi(self)
        self.ui4.ok_monthly_wage.accepted.connect(self.accept)
        self.ui4.ok_monthly_wage.rejected.connect(self.reject)

# For user signup with varying monthly salary
class varying_monthly_wage(QDialog):
    def __init__(self,perent=None):
        super(varying_monthly_wage, self).__init__(perent)
        self.ui5 = every_month()
        self.ui5.setupUi(self)

# User can enter gmail & password to login
class enter_page(QDialog):
    def __init__(self,parent=None):
        super(enter_page,self).__init__(parent)
        self.ui6 = enter()
        self.ui6.setupUi(self)

# It is to show the signup process is completed successfully
class final_success(QDialog):
    def __init__(self,parent=None):
        super(final_success,self).__init__(parent)
        self.ui7 = success()
        self.ui7.setupUi(self)

# user can enter to home page
class my_home_page(QDialog):
    def __init__(self,parent=None):
        super(my_home_page,self).__init__(parent)
        self.ui8 = my_page()
        self.ui8.setupUi(self)

# Daily money usage of user
class my_daily_usage(QDialog):
    def __init__(self,parent=None):
        super(my_daily_usage,self).__init__(parent)
        self.ui9 = my_daily_money()
        self.ui9.setupUi(self)
        self.ui9.buttonBox.accepted.connect(self.accept)
        self.ui9.buttonBox.rejected.connect(self.reject)

# Weekly money usage of user
class my_weekly_usage(QDialog):
    def __init__(self,parent=None):
        super(my_weekly_usage, self).__init__(parent)
        self.ui10 = my_weekly_money()
        self.ui10.setupUi(self)
        self.ui10.buttonBox.accepted.connect(self.accept)
        self.ui10.buttonBox.rejected.connect(self.reject)

# Monthly money usage of user
class my_monthly_usage(QDialog):
    def __init__(self,parent=None):
        super(my_monthly_usage, self).__init__(parent)
        self.ui11 = my_monthly_money()
        self.ui11.setupUi(self)
        self.ui11.buttonBox.accepted.connect(self.accept)
        self.ui11.buttonBox.rejected.connect(self.reject)

# Editing user's profile
class edit_my_profile(QDialog):
    def __init__(self,parent=None):
        super(edit_my_profile, self).__init__(parent)
        self.ui12 = profile()
        self.ui12.setupUi(self)
        self.ui12.buttonBox.accepted.connect(self.accept)
        self.ui12.buttonBox.rejected.connect(self.reject)

# Editing user's account
class edit_my_account(QDialog):
    def __init__(self,parent=None):
        super(edit_my_account, self).__init__(parent)
        self.ui13 = account()
        self.ui13.setupUi(self)
        self.ui13.buttonBox.accepted.connect(self.accept)
        self.ui13.buttonBox.rejected.connect(self.reject)

# It is to show the editing monthly salary process is completed successfully
class final_edit_success(QDialog):
    def __init__(self,parent=None):
        super(final_edit_success, self).__init__(parent)
        self.ui14 = edit_success()
        self.ui14.setupUi(self)


class display(QMainWindow,Ui_MainWindow):
    def __init__(self,perent=None):
        super(display, self).__init__(perent)
        self.setupUi(self)

        self.pushButton.clicked.connect(lambda : login())
        self.pushButton_2.clicked.connect(lambda : signup_page())

        # signup button
        def signup_page():
            sgn = dialog()
            sgn.ui.continue_2.clicked.connect(lambda : salary_page(sgn.ui.salary_text.currentText(),sgn))
            sgn.exec()

        # Getting information about salary package from user
        def salary_page(wage,sgn):
            if wage == "Daily wage":
                dly = daily_wage()
                dly.ui1.buttonBox.accepted.connect(lambda: daily_salary_list(dly,sgn,wage))
                dly.exec()


            elif wage == "Weekly wage":
                wky = weekly_wage()
                wky.ui2.buttonBox.accepted.connect(lambda: weekly_salary_list(wky,sgn,wage))
                wky.exec()

            elif wage == "Monthly wage":
                qst = question_wage()
                qst.ui3.yes_month_input.clicked.connect(lambda: constant_salary(sgn,wage))
                qst.ui3.no_month_input.clicked.connect(lambda: unconstant_salary(sgn,wage))
                qst.exec()

        # creating a list of user's daily salary and loading the information about user in dictionary
        def daily_salary_list(dly,sgn,wage):
            daily_salary = [dly.ui1.day_1_input.value(),
                            dly.ui1.day_2_input.value(),
                            dly.ui1.day_3_input.value(),
                            dly.ui1.day_4_input.value(),
                            dly.ui1.day_5_input.value(),
                            dly.ui1.day_6_input.value(),
                            dly.ui1.day_7_input.value()]

            my_daily_salary = {
                'name': sgn.ui.name_text.text(),
                'age': sgn.ui.age_text.value(),
                'job': sgn.ui.job_text.text(),
                'salary': daily_salary,
                'salary_type': wage,
                'gmail':sgn.ui.lineEdit.text(),
                'password': sgn.ui.password_text.text()
            }
            saving_storage(my_daily_salary)

        # creating a list of user's weekly salary and loading the information about user in dictionary
        def weekly_salary_list(wky,sgn,wage):
            weekly_salary = [wky.ui2.week_1_input.value(),
                             wky.ui2.week_2_input.value(),
                             wky.ui2.week_3_input.value(),
                             wky.ui2.week_4_input.value()]
            my_weekly_salary = {
                'name': sgn.ui.name_text.text(),
                'age': sgn.ui.age_text.value(),
                'job': sgn.ui.job_text.text(),
                'salary': weekly_salary,
                'salary_type': wage,
                'gmail': sgn.ui.lineEdit.text(),
                'password': sgn.ui.password_text.text()
            }
            saving_storage(my_weekly_salary)

        # creating a list of user's Monthly salary(constant salary) and loading the information about user in dictionary
        def constant_salary(sgn,wage):
            cnt = constant_monthly_wage()
            cnt.ui4.ok_monthly_wage.accepted.connect(lambda: constant_salary_list(cnt,sgn,wage))
            cnt.exec()

        def constant_salary_list(cnt,sgn,wage):
            constant_list = []

            for i in range(12):
                constant_list.append(cnt.ui4.single_monthly_input.value())

            my_constant_salary = {
                'name': sgn.ui.name_text.text(),
                'age': sgn.ui.age_text.value(),
                'job': sgn.ui.job_text.text(),
                'salary': constant_list,
                'salary_type': wage,
                'monthly_salary_type': "constant",
                'gmail': sgn.ui.lineEdit.text(),
                'password': sgn.ui.password_text.text()
            }
            saving_storage(my_constant_salary)

        # creating a list of user's Monthly salary(varying salary) and loading the information about user in dictionary
        def unconstant_salary(sgn,wage):
            ucnt = varying_monthly_wage()
            ucnt.ui5.buttonBox.accepted.connect(lambda : unconstant_salary_list(ucnt,sgn,wage))
            ucnt.exec()

        def unconstant_salary_list(ucnt,sgn,wage):
            unconstant_salary = [ucnt.ui5.month_1_wage.value(),
                                 ucnt.ui5.month_2_wage.value(),
                                 ucnt.ui5.month_3_wage.value(),
                                 ucnt.ui5.month_4_wage.value(),
                                 ucnt.ui5.month_5_wage.value(),
                                 ucnt.ui5.month_6_wage.value(),
                                 ucnt.ui5.month_7_wage.value(),
                                 ucnt.ui5.month_8_wage.value(),
                                 ucnt.ui5.month_9_wage.value(),
                                 ucnt.ui5.month_10_wage.value(),
                                 ucnt.ui5.month_11_wage.value(),
                                 ucnt.ui5.month_12_wage.value()]
            my_unconstant_salary = {
                'name': sgn.ui.name_text.text(),
                'age': sgn.ui.age_text.value(),
                'job': sgn.ui.job_text.text(),
                'salary': unconstant_salary,
                'salary_type': wage,
                'monthly_salary_type': "not constant",
                'gmail': sgn.ui.lineEdit.text(),
                'password': sgn.ui.password_text.text()
            }
            saving_storage(my_unconstant_salary)

        # saving the dictionary in file using json module
        def saving_storage(mydetails):
            info = []
            try:
                text = open('detail1.dat', 'r')
                text = json.loads(text.read())
                for i in text:
                    info.append(i)
            except:
                pass

            info.append(mydetails)

            information1 = []
            for i in info:
                information1.append(i)

            try:
                text = open('detail1.dat', 'w')
                text.write(json.dumps(information1, indent=4))
                text.close()
                suc = final_success()
                suc.exec()

            except:
                pass

        # Login using user's gmail & password
        def login():
            lgn = enter_page()
            lgn.ui6.login_continue.clicked.connect(lambda : load_gmail(lgn))
            lgn.exec()

        # Opening home page of user's account
        def load_gmail(lgn):
            try:
                text = open('detail1.dat','r')
                text = json.loads(text.read())
            except:
                pass

            try:
                for my_gmail in text:
                    if my_gmail['gmail'] == lgn.ui6.login_gmail.text():
                        if my_gmail['password'] == lgn.ui6.login_password.text():
                            mpg = my_home_page()
                            mpg.ui8.pushButton.clicked.connect(lambda : money_usage(my_gmail))
                            mpg.ui8.pushButton_5.clicked.connect(lambda : my_graph(my_gmail))
                            mpg.ui8.pushButton_4.clicked.connect(lambda : edit_salary(my_gmail))
                            mpg.ui8.pushButton_2.clicked.connect(lambda: edit_profile(my_gmail))
                            mpg.ui8.pushButton_3.clicked.connect(lambda : edit_account(my_gmail,mpg))
                            mpg.ui8.lineEdit.setText(my_gmail['name'])
                            mpg.ui8.lineEdit_2.setText(str(my_gmail['age']))
                            mpg.ui8.lineEdit_3.setText(my_gmail['job'])
                            mpg.ui8.lineEdit_4.setText(my_gmail['gmail'])
                            mpg.ui8.lineEdit_5.setText(my_gmail['password'])
                            mpg.exec()
            except:
                pass

        # verifying money usage
        def money_usage(my_gmail):
            if my_gmail['salary_type'] == 'Daily wage':
                dug = my_daily_usage()
                dug.ui9.buttonBox.accepted.connect(lambda: daily_usage_list(my_gmail, dug))
                dug.exec()
            elif my_gmail['salary_type'] == 'Weekly wage':
                wug = my_weekly_usage()
                wug.ui10.buttonBox.accepted.connect(lambda: weekly_usage_list(my_gmail, wug))
                wug.exec()
            elif my_gmail['salary_type'] == 'Monthly wage':
                mug = my_monthly_usage()
                mug.ui11.buttonBox.accepted.connect(lambda: monthly_usage_list(my_gmail, mug))
                mug.exec()

        # creating a list of monthly money usage
        def monthly_usage_list(my_gmail,mug):
            my_monthly_usage_list = [
                mug.ui11.month_1_usage.value(),
                mug.ui11.month_2_usage.value(),
                mug.ui11.month_3_usage.value(),
                mug.ui11.month_4_usage.value(),
                mug.ui11.month_5_usage.value(),
                mug.ui11.month_6_usage.value(),
                mug.ui11.month_7_usage.value(),
                mug.ui11.month_8_usage.value(),
                mug.ui11.month_9_usage.value(),
                mug.ui11.month_10_usage.value(),
                mug.ui11.month_11_usage.value(),
                mug.ui11.month_12_usage.value()
            ]
            save_money_usage_list(my_gmail,my_monthly_usage_list)

        # creating a list of weekly money usage
        def weekly_usage_list(my_gmail,wug):
            my_weekly_money_usage = [
                wug.ui10.week_1_usage.value(),
                wug.ui10.week_2_usage.value(),
                wug.ui10.week_3_usage.value(),
                wug.ui10.week_4_usage.value(),
            ]
            save_money_usage_list(my_gmail,my_weekly_money_usage)

        # creating a list of daily money usage
        def daily_usage_list(my_gmail,dug):
            my_daily_money_usage = [
                dug.ui9.day_1_usage.value(),
                dug.ui9.day_2_usage.value(),
                dug.ui9.day_3_usage.value(),
                dug.ui9.day_4_usage.value(),
                dug.ui9.day_5_usage.value(),
                dug.ui9.day_6_usage.value(),
                dug.ui9.day_7_usage.value()
            ]
            save_money_usage_list(my_gmail,my_daily_money_usage)

        # saving money usage list to user's dictionary
        def save_money_usage_list(my_gmail,usage):
            text = open('detail1.dat','r')
            text = json.loads(text.read())

            text1 =[]

            for i in text:
                if i['name'] == my_gmail['name']:
                    i['usage'] = usage
                text1.append(i)

            try:
                text = open('detail1.dat','w')
                text.write(json.dumps(text1, indent=4))
                text.close()
            except:
                pass

        # Editing user's salary 
        def edit_salary(my_gmail):
            if my_gmail['salary_type'] == "Daily wage":
                dly = daily_wage()
                dly.ui1.buttonBox.accepted.connect(lambda: edit_daily_salary(dly,my_gmail))
                dly.exec()
            elif my_gmail['salary_type'] == "Weekly wage":
                wky = weekly_wage()
                wky.ui2.buttonBox.accepted.connect(lambda: edit_weekly_salary(wky,my_gmail))
                wky.exec()
            elif my_gmail['salary_type'] == "Monthly wage":
                if my_gmail['monthly_salary_type'] == "constant":
                    cnt = constant_monthly_wage()
                    cnt.ui4.ok_monthly_wage.accepted.connect(lambda: edit_constant_salary(my_gmail,cnt))
                    cnt.exec()
                elif my_gmail['monthly_salary_type'] == "not constant":
                    ucnt = varying_monthly_wage()
                    ucnt.ui5.buttonBox.accepted.connect(lambda: edit_unconstant_salary(my_gmail,ucnt))
                    ucnt.exec()

        # Creating a list of user's Edited constant monthly salary
        def edit_constant_salary(my_gmail,cnt):
            constant_salary = []
            for i in range(12):
                constant_salary.append(cnt.ui4.single_monthly_input.value())
            edit_money(my_gmail,constant_salary)

        # Creating a list of user's Edited varying monthly salary
        def edit_unconstant_salary(my_gmail,ucnt):
            unconstant_salary = [ucnt.ui5.month_1_wage.value(),
                                 ucnt.ui5.month_2_wage.value(),
                                 ucnt.ui5.month_3_wage.value(),
                                 ucnt.ui5.month_4_wage.value(),
                                 ucnt.ui5.month_5_wage.value(),
                                 ucnt.ui5.month_6_wage.value(),
                                 ucnt.ui5.month_7_wage.value(),
                                 ucnt.ui5.month_8_wage.value(),
                                 ucnt.ui5.month_9_wage.value(),
                                 ucnt.ui5.month_10_wage.value(),
                                 ucnt.ui5.month_11_wage.value(),
                                 ucnt.ui5.month_12_wage.value()]
            edit_money(my_gmail,unconstant_salary)

        # Creating a list of user's Edited daily salary
        def edit_daily_salary(dly,my_gmail):
            daily_salary = [dly.ui1.day_1_input.value(),
                            dly.ui1.day_2_input.value(),
                            dly.ui1.day_3_input.value(),
                            dly.ui1.day_4_input.value(),
                            dly.ui1.day_5_input.value(),
                            dly.ui1.day_6_input.value(),
                            dly.ui1.day_7_input.value()]
            edit_money(my_gmail,daily_salary)

        # Creating a list of user's Edited weekly salary
        def edit_weekly_salary(wky,my_gmail):
            weekly_salary = [wky.ui2.week_1_input.value(),
                             wky.ui2.week_2_input.value(),
                             wky.ui2.week_3_input.value(),
                             wky.ui2.week_4_input.value()]
            edit_money(my_gmail,weekly_salary)

        # saving updated salary package
        def edit_money(my_gmail,edit):
            text = open('detail1.dat','r')
            text = json.loads(text.read())

            text1 =[]

            for i in text:
                if i['name'] == my_gmail['name']:
                    i['salary'] = edit
                text1.append(i)

            try:
                text = open('detail1.dat','w')
                text.write(json.dumps(text1, indent=4))
            except:
                pass

        # Generating user's profit/lose graph
        def my_graph(my_gmail):

            info = open('detail1.dat','r')
            info = json.loads(info.read())

            for i in info:
                if i['name'] == my_gmail['name']:

                    x = i['salary']
                    y = i['usage']
                    fig, axes = plt.subplots(figsize=(12, 3), dpi=100)
                    axes.plot(x, 'g.-')
                    axes.plot(y, 'r--')
                    fig
                    plt.show()

        # Editing user's profile
        def edit_profile(my_gmail):
            epl = edit_my_profile()
            epl.ui12.name_text.setText(my_gmail['name'])
            epl.ui12.age_text.setValue(my_gmail['age'])
            if my_gmail['salary_type'] == "Daily wage":
                epl.ui12.salary_text.addItems(['Daily wage', 'Weekly wage', 'Monthly wage'])
            elif my_gmail['salary_type'] == "Weekly wage":
                epl.ui12.salary_text.addItems(['Weekly wage', 'Daily wage', 'Monthly wage'])
            elif my_gmail['salary_type'] == "Monthly wage":
                epl.ui12.salary_text.addItems([ 'Monthly wage','Weekly wage', 'Daily wage'])
            epl.ui12.job_text.setText(my_gmail['job'])
            epl.ui12.buttonBox.accepted.connect(lambda: identify(epl,my_gmail))
            epl.exec()

        # To identify type of monthly salary of user 
        def identify(epl,my_gmail):
            if epl.ui12.salary_text.currentText() == "Monthly wage":
                edit_profile_monthly_wage(epl,my_gmail)
            else:
                save_edit_profile(epl,my_gmail)

        def edit_profile_monthly_wage(epl,my_gmail):
            mqw = question_wage()
            mqw.ui3.yes_month_input.clicked.connect(lambda: save_constant_salary(epl,mqw,my_gmail))
            mqw.ui3.no_month_input.clicked.connect(lambda: save_unconstant_salary(epl,mqw,my_gmail))
            mqw.exec()

        # saving the modified profile(if constant monthly salary is selected)
        def save_constant_salary(epl,mqw,my_gmail):
            all_profile= open('detail1.dat','r')
            all_profile= json.loads(all_profile.read())

            info = []
            
            for my_profile in all_profile:
                if my_profile['name'] == my_gmail['name']:
                    my_profile['name'] = epl.ui12.name_text.text()
                    my_profile['age'] = epl.ui12.age_text.value()
                    my_profile['job'] = epl.ui12.job_text.text()
                    my_profile['salary_type'] = epl.ui12.salary_text.currentText()   
                    my_profile['monthly_salary_type'] = "constant"                     
                info.append(my_profile)

            all_profile = open('detail1.dat', 'w')
            all_profile.write(json.dumps(info))
            suc = final_edit_success()
            suc.exec()

        # saving the modified profile(if varying monthly salary is selected)
        def save_unconstant_salary(epl,mqw,my_gmail):
            all_profile= open('detail1.dat','r')
            all_profile= json.loads(all_profile.read())

            info = []
            
            for my_profile in all_profile:
                if my_profile['name'] == my_gmail['name']:
                    my_profile['name'] = epl.ui12.name_text.text()
                    my_profile['age'] = epl.ui12.age_text.value()
                    my_profile['job'] = epl.ui12.job_text.text()
                    my_profile['salary_type'] = epl.ui12.salary_text.currentText()   
                    my_profile['monthly_salary_type'] = "not constant"                     
                info.append(my_profile)

            all_profile = open('detail1.dat', 'w')
            all_profile.write(json.dumps(info))
            suc = final_edit_success()
            suc.exec()

        # saving the modified profile(if daily/weekly salary is selected)
        def save_edit_profile(epl,my_gmail):

            all_profile= open('detail1.dat','r')
            all_profile= json.loads(all_profile.read())

            info = []

            for my_profile in all_profile:
                if my_profile['name'] == my_gmail['name']:
                    my_profile['name'] = epl.ui12.name_text.text()
                    my_profile['age'] = epl.ui12.age_text.value()
                    my_profile['job'] = epl.ui12.job_text.text()
                    my_profile['salary_type'] = epl.ui12.salary_text.currentText()                        
                info.append(my_profile)

            all_profile = open('detail1.dat', 'w')
            all_profile.write(json.dumps(info))

        # Edit account(gmail and password)
        def edit_account(my_gmail,mpg):
            eal = edit_my_account()
            eal.ui13.lineEdit.setText(my_gmail['gmail'])
            eal.ui13.password_text.setText(my_gmail['password'])
            eal.ui13.buttonBox.accepted.connect(lambda: save_edit_account(eal,my_gmail,mpg))
            eal.exec()

        # saving the modified account
        def save_edit_account(eal,my_gmail,mpg):
            all_account = open('detail1.dat', 'r')
            all_account = json.loads(all_account.read())

            info = []

            for my_account in all_account:
                if my_account['name'] == my_gmail['name']:
                    my_account['gmail'] = eal.ui13.lineEdit.text()
                    my_account['password'] = eal.ui13.password_text.text()
                info.append(my_account)

            all_acc = open('detail1.dat', 'w')
            all_acc.write(json.dumps(info))

app = QApplication([])
window = display()
window.show()
app.exec()