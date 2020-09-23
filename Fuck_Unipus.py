from selenium import webdriver
from selenium.webdriver.common.by import By #用于指定 HTML 文件中 DOM 标签元素
from selenium.webdriver.support.ui import WebDriverWait #等待网页加载完成
from selenium.webdriver.support import expected_conditions as EC #指定等待网页加载结束条件
from time import sleep
from os import system
from random import randint




def log_in():
    account = input('Your account:\n')
    password = input('Your password:\n')
    item_login = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/form/div[1]/input')
    item_password = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/form/div[2]/input')
    item_login_button = browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/form/button')
    item_login.click()
    item_login.send_keys(account)
    item_password.click()
    item_password.send_keys(password)
    item_login_button.click()

def check_browser():
    check = browser.find_elements_by_xpath('/html/body/div[6]/div[3]/a')
    if check != []:
        check[0].click()
        windows = browser.window_handles
        browser.switch_to.window(windows[0])
    else:
        print('Check has been done.')
        return



def find_answer(unit,count_part,count_banked):
    answer_u1_s1_p1 = ['crumbled', 'discern', 'surpass', 'shrewd', 'conversion', 'distort', 'radiant', 'ingenious',
                       'stumped', 'proposition']
    answer_u1_s1_p2 = ['delicacy', 'bankruptcy', 'accountancy', 'secrecy', 'vacancy', 'urgency', 'atmospheric',
                       'magnet', 'metallic', 'gloom', 'guilt', 'mastery']
    answer_u1_s1_p3 = ['bankruptcies', 'atmospheric', 'delicacies', 'urgency', 'accountancy', 'gloom', 'magnet',
                       'metallic', 'mastery', 'vacancy', 'guilt', 'secrecy']
    answer_u1_s1_p4 = ['mentioned', 'determine', 'gained', 'responsible', 'heavily', 'artistic', 'opposite',
                       'analytical', 'distorted', 'stumped']
    answer_u1_s1_p5 = ['were dripping with', 'in exchange for', 'flared up', 'make an analogy between',
                       'set a date for','make','out of','made a pact','had appealed to']

    answer_u1_s2_p1 = ['triggering', 'obscure', 'hypothesis', 'formulate', 'threshold', 'incidence', 'refute', 'realm',
                       'decay', 'testimony']
    answer_u1_s2_p2 = ['play the odds', 'subject to', 'attributes', 'to', 'be factored into', 'call for',
                       'By virtue of', 'get stuck on', 'come into play']
    answer_u1_s2_p3 = []
    answer_u1_s3_p1 = ['available', 'erroneous', 'valid', 'intellectual', 'lightening', 'inaccurate', 'winning',
                       'distort', 'logic-proof', 'tremendous', 'watertight', 'cognitive']

    answer_u1_s = [answer_u1_s1_p1, answer_u1_s1_p2, answer_u1_s1_p3, answer_u1_s1_p4, answer_u1_s1_p5, answer_u1_s2_p1,
                   answer_u1_s2_p2, answer_u1_s2_p3,answer_u1_s3_p1]

    answer_u2_s1_p1 = ['deficient', 'prosecution', 'outrage', 'appeased', 'conformity', 'strand', 'complement',
                       'transient', 'appliances', 'outfit']
    answer_u2_s1_p2 = ['domination', 'orientation', 'confrontation', 'composer', 'binder', 'scanner', 'manufacturer',
                       'erase', 'imperialist', 'leftist', 'terrorist', 'humanist']
    answer_u2_s1_p3 = ['domination', 'scanners', 'humanist', 'confrontation', 'leftists', 'orientation', 'erased',
                       'terrorists', 'manufacturers', 'binder', 'imperialists', 'composers']
    answer_u2_s1_p4 = ['achieving', 'gorgeous', 'considered', 'context', 'accessories', 'appreciated', 'complexion',
                       'handsome', 'comment', 'admiration']
    answer_u2_s1_p5 = ['in hopes of', 'came up with', 'excused herself', 'was obsessed with', 'reaching out to',
                       'voice an opinion on', 'live up to', 'in terms of']

    answer_u2_s2_p1 = ['hampered', 'mortal', 'corrode', 'preface', 'embodies', 'interwoven', 'knitted', 'collide',
                       'costume', 'predominant']
    answer_u2_s2_p2 = ['enquired about', 'from a', 'perspective', 'on the rise', 'be accountable to', 'are wearing out',
                       'is exempt from', 'approve of', 'being addicted to']
    answer_u2_s2_p3 = []

    answer_u2_s = [answer_u2_s1_p1, answer_u2_s1_p2, answer_u2_s1_p3, answer_u2_s1_p4, answer_u2_s1_p5, answer_u2_s2_p1,
                   answer_u2_s2_p2, answer_u2_s2_p3]

    answer_u3_s1_p1 = ['exquisite', 'dispersed', 'decentralized', 'deduce', 'fixture', 'frugality', 'administrate',
                       'disjointed', 'Reviving', 'elapse']
    answer_u3_s1_p2 = ['punctuality', 'purity', 'scarcity', 'seniority', 'sensitivity', 'solemnity', 'specialty',
                       'superiority', 'validity', 'visibility', 'reassure', 'restructure']
    answer_u3_s1_p3 = ['seniority', 'purity', 'specialties', 'reassure', 'scarcity', 'punctuality', 'sensitivity',
                       'restructuring', 'superiority', 'validity', 'visibility', 'solemnity']
    answer_u3_s1_p4 = ['frequently', 'immersed', 'disrupted', 'stress', 'sphere', 'challenges', 'quantify', 'financial',
                       'administrate', 'addiction']
    answer_u3_s1_p5 = ['held', 'in high regard', 'In the interim', 'was onto something', 'in turn', 'from time to time',
                       'pick on','take a stab at','boil down to']

    answer_u3_s2_p1 = ['stimulus', 'magnitude', 'velocity', 'quota', 'stipulated', 'tease', 'eligible', 'premium',
                       'reminiscence', 'decree']
    answer_u3_s2_p2 = ['be embedded in', 'a trace of', 'is critical to', 'adjacent to', 'beat', 'down',
                       'remains committed to', 'conceive of', 'be eligible for']
    answer_u3_s2_p3 = []

    answer_u3_s3_p1 = ['compelling', 'Instant', 'sturdy', 'measurable', 'decent', 'trim']
    answer_u3_s3_p2 = ['instant', 'success', 'overwhelmingly', 'positive', 'outstanding', 'entrepreneurs',
                       'household','names',
                       'extremely', 'poor', 'low-income', 'family', 'rapid', 'expansion', 'extreme', 'frugality',
                       'harsh',
                       'memories', 'firmly', 'committed', 'crowning', 'success']

    answer_u3_s = [answer_u3_s1_p1, answer_u3_s1_p2, answer_u3_s1_p3, answer_u3_s1_p4, answer_u3_s1_p5, answer_u3_s2_p1,
                   answer_u3_s2_p2, answer_u3_s2_p3, answer_u3_s3_p1, answer_u3_s3_p2]

    answer_total = [answer_u1_s,answer_u2_s,answer_u3_s]

    try:
        return answer_total[unit][count_part][count_banked]
    except:
        print('Loss of answer')
        return ''

def get_sections(chapter):
    #等待元素加载完毕
    sleep(2)
    sections = browser.find_elements_by_xpath('//*[@id="menuBox"]/ul[{}]/li/div[1]/div/div/i[@class="icon-bixiu iconCust'
                                              'umStyle iconfont"]'.format(chapter))
    return sections

def deal_section(sections,unit):
    count_part = 0
    for j in range(len(sections)):
        item = sections[j]
        #进入每一节
        try:
            item.click()
        except:
            print('Section Wrong')
        sleep(4)
        WebDriverWait(browser, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'dialog-header-pc--dialog-header-2qsXD')))
        asure_button = browser.find_elements_by_xpath('/html/body/div/div/div[1]/div/div/div[3]/div/button/div/div/span')
        asure_button[-1].click()
        sleep(1)
        try:
            check_microphone = browser.find_elements_by_xpath('/html/body/div/div/div[1]/div/div/div[3]/div/button/div/div/span')
            if check_microphone != []:
                check_microphone[0].click()
                sleep(2)
            else:
                pass
        except:
            pass

        #选择大题
        blanks = browser.find_elements_by_xpath('//*[@id="header"]/div/ul[1]/li')
        for blank in blanks:
            blank.click()
            sleep(2)
        #检查“确认”按钮
            try:
                button = browser.find_elements_by_xpath('/html/body//button/div/div/span')
                if button != []:
                    button[0].click()
                    sleep(1)
            except:
                pass
        #选择小题
            parts = browser.find_elements_by_xpath('//*[@id="header"]/div/ul[2]/li/a')
            for part in parts:
                part.click()
                sleep(2)

                WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'submit-bar-pc--con'
                                                                                                     'tainer-1nNVp')))

                banked = browser.find_elements_by_xpath(
                    '//*[@id="main-top"]/div[2]/div/div[1]//span/input[@type="text"]')
                if banked == []:
                    continue
                else:
                    count_part += 1
                    count_bankd = 0
                    for bank in banked:
                        count_click = 0
                        while True:
                            try:
                                count_click += 1
                                bank.click()
                                sleep(randint(5,10))
                                bank.send_keys(find_answer(unit,count_part - 1, count_bankd))
                                break
                            except:
                                if count_click >= 3:
                                    print('Attention:A bank has been skiped')
                                    break
                                else:
                                    continue
                        count_bankd += 1


        print('Section finished.')
        system('mshta vbscript:msgbox("本脚本仅辅助填题，为避免隐藏的BUG给您的成绩带来毁灭性的打击，请检查答案后手动提交已填'
                  '题目。作者不会为您的粗心带来的问题承担任何责任！",64,"手动提交提醒")(window.close)')
        input('如您已提交答案，请输入回车继续')
        WebDriverWait(browser, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'layoutHeaderStyle--menuList-Ef90e')))
        home = browser.find_element_by_xpath('//*[@id="header"]/div/div/div/div/ul/li[1]')
        home.click()
        WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'name')))
        #刷新Section列表
        sections = get_sections(unit + 1)

if __name__ == '__main__':

    sections = []

    browser = webdriver.Chrome()
    browser.get('https://u.unipus.cn/user/student?school_id=8316')
    WebDriverWait(browser,10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,'form-group')))
    #登陆
    log_in()
    sleep(2)
    #检查环境
    WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'my_course_cover')))
    check_browser()
    sleep(2)
    #点击书本进行学习
    my_book = browser.find_element_by_xpath('/html/body/div[2]/div/div[3]/div[2]/div/div[2]/div/img')
    my_book.click()
    WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'name')))
    for i in range(4):
        sections = get_sections(i+1)
        deal_section(sections,i)
    system('mshta vbscript:msgbox("刷完啦！",64,"任务完成")(window.close)')





