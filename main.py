import webbrowser as wb
import datetime
from selenium import webdriver


PATH = "/Users/nicklam/Desktop/login/chromedriver"
driver = webdriver.Chrome(PATH)


# variables that are needed within this program
today = datetime.datetime.today()
username = ""
personal_email = ""
email_pass = ""
my_password = ""


# program execution starts
course = input("Enter course code: ")

weeks = {
    "Week 1": datetime.datetime(2022, 1, 16),
    "Week 2": datetime.datetime(2022, 1, 23),
    "Week 3": datetime.datetime(2022, 1, 30),
    "Week 4": datetime.datetime(2022, 1, 6),
    "Week 5": datetime.datetime(2022, 1, 13),
    "Week 6": datetime.datetime(2022, 1, 20),
    "Week 7": datetime.datetime(2022, 1, 27),
    "Week 8": datetime.datetime(2022, 1, 6),
    "Week 9": datetime.datetime(2022, 1, 13),
    "Week 10": datetime.datetime(2022, 1, 20),
    "Week 11": datetime.datetime(2022, 1, 27),
    "Week 12": datetime.datetime(2022, 1, 3),
    "Week 13": datetime.datetime(2022, 1, 10),
}

earthsci_lectures = {
    "Week 1": "Mercury and Venus",
    "Week 2": "Earth and its Moon",
    "Week 3": "Mars",
    "Week 4": "Asteroids and Meteorites",
    "Week 5": "Jupiter and its Moon's",
    "Week 6": "Saturn and its Moon's",
    "Week 7": "Volcanism",
    "Week 8": "Uranus and Neptune",
    "Week 9": "Comets",
    "Week 10": "Pluto",
    "Week 11": "Review",
}

today = datetime.datetime.today()
username = "nlam57"
personal_email = "nicholasalexanderlam@gmail.com"
email_pass = "Focus93!5"
my_password = "Focus93!2"


def findearthsciweek(week):
    for key, value in earthsci_lectures.items():
        if key == week:
            return value


def findweek():

    for key, value in weeks.items():
        if today <= value:
            return key

    return "Sorry, the date was not found!"


def getcurrentweek(course, week):
    if course.lower() == "2209":
        # open owl enter user name and password
        driver.get("https://owl.uwo.ca/portal")
        user = driver.find_element_by_id("eid")
        user.send_keys(username)

        password = driver.find_element_by_id("pw")
        password.send_keys(my_password)

        login_button = driver.find_element_by_id("submit")
        login_button.click()
        # ------------------------------------------------------- #

        stats = driver.find_element_by_link_text("COMPSCI 2209B 001 FW21")
        stats.click()

        content = driver.find_element_by_link_text("Course Content")
        content.click()

        week_content = driver.find_element_by_link_text(week)

        return week_content.click()

    elif course.lower() == "2212":
        # open owl enter user name and password
        driver.get("https://owl.uwo.ca/portal")
        user = driver.find_element_by_id("eid")
        user.send_keys(username)

        password = driver.find_element_by_id("pw")
        password.send_keys(my_password)

        login_button = driver.find_element_by_id("submit")
        login_button.click()
        # ------------------------------------------------------- #

        stats = driver.find_element_by_link_text("COMPSCI 2212B 001 FW21")
        stats.click()

        content = driver.find_element_by_link_text("Week By Week")
        content.click()

        week_content = driver.find_element_by_partial_link_text(week)
        week_content.click()

        video = driver.find_element_by_partial_link_text("Pre-Recorded Video Lectures")
        return video.click()

    elif course.lower() == "2232":
        # open owl enter user name and password
        driver.get("https://owl.uwo.ca/portal")
        user = driver.find_element_by_id("eid")
        user.send_keys(username)

        password = driver.find_element_by_id("pw")
        password.send_keys(my_password)

        login_button = driver.find_element_by_id("submit")
        login_button.click()
        # ------------------------------------------------------- #

        stats = driver.find_element_by_link_text("EARTHSCI 2232G 650 FW21")
        stats.click()

        content = driver.find_element_by_link_text("Lessons")
        content.click()

        curr = findweek()
        planet = findearthsciweek(curr)

        week_content = driver.find_element_by_partial_link_text(planet)
        return week_content.click()

    elif course.lower() == "2244":
        # open owl enter user name and password
        driver.get("https://owl.uwo.ca/portal")
        user = driver.find_element_by_id("eid")
        user.send_keys(username)

        password = driver.find_element_by_id("pw")
        password.send_keys(my_password)

        login_button = driver.find_element_by_id("submit")
        login_button.click()
        # ------------------------------------------------------- #

        stats = driver.find_element_by_link_text("STATS 2244B 001 FW21")
        stats.click()

        content = driver.find_element_by_link_text("Course Content")
        content.click()

        curr = findweek()
        planet = findearthsciweek(curr)

        week_content = driver.find_element_by_partial_link_text(planet)
        return week_content.click()


# function that goes to the specific zoom link of the specified course
def lectures(course):
    if course == "2212":
        # open owl enter user name and password
        driver.get("https://owl.uwo.ca/portal")
        user = driver.find_element_by_id("eid")
        user.send_keys(username)

        password = driver.find_element_by_id("pw")
        password.send_keys(my_password)

        login_button = driver.find_element_by_id("submit")
        login_button.click()
        # ------------------------------------------------------- #

        # go to the course's zoom
        stats = driver.find_element_by_link_text("COMPSCI 2212B 001 FW21")
        stats.click()
        driver.maximize_window()
        content = driver.find_element_by_xpath(
            '//*[@id="toolMenu"]/ul/li[16]/a/span[2]'
        )
        content.click()
        # ------------------------------------------------------- #

        driver.execute_script("window.open('about:blank', 'tab2');")
        driver.switch_to.window("tab2")
        driver.get(
            "https://westernuniversity.zoom.us/j/99748336765?uname=Nicholas+Alexander+Lam#success"
        )
        # -------------------------------------------------------------------------------------------------------------- #

    elif course.lower() == "2209":

        wb.open("https://westernuniversity.zoom.us/j/2064952056")
        # ------------------------------------------------------- #


def main():
    if course.lower() == "2244":
        wb.open(
            "https://owl.uwo.ca/portal/site/6b8cebe1-988b-4fa7-8eaa-d9503ecbb5f3/tool/cf03f60b-ea46-4a7e-a024-826aebbd199b"
        )
        wb.open(
            "https://drive.google.com/drive/folders/1BatojKCgZSv8fwgk19xzcMV_A1gt3MEc"
        )

    elif course.lower() == "2209":

        wb.open(
            "https://owl.uwo.ca/portal/site/99f1046a-cac3-41f5-9199-a69c1ded7657/tool/f09fd509-b3d8-4a76-8e55-1487224c7462"
        )
        wb.open(
            "https://drive.google.com/drive/folders/1forWBuqd8WqFnIcmOyw2FVep3Xrc8o91"
        )
        wb.open("https://web.stanford.edu/class/cs103/tools/truth-table-tool/")
        wb.open(
            "https://spot-cardamom-d6e.notion.site/Propositional-Logic-4f4896574622440eb8ff0a589ead1d7d"
        )

        curr_week = findweek()
        getcurrentweek(course, curr_week)

        lecture = input("Proceed to lecture? ")
        if lecture.lower() == "yes":
            lectures(course)

    elif course.lower() == "2212":
        wb.open(
            "https://owl.uwo.ca/portal/site/357e3429-e551-4966-9bac-dcf1af759a8c/tool/4ac7391e-70cc-48ef-bc74-ce558198f56f"
        )
        wb.open(
            "https://drive.google.com/drive/folders/1nkilMmSjWk52iGiaoI1Y-VVO7RJd31vL"
        )
        curr_week = findweek()
        getcurrentweek(course, curr_week)

        lecture = input("Proceed to lecture? ")
        if lecture.lower() == "yes":
            lectures(course)

    elif course.lower() == "biz":
        wb.open(
            "https://owl.uwo.ca/portal/site/0a84b539-5b11-4116-8db3-915a20a97018/tool/c460347b-b657-43f6-bf80-cbbfec1eccb9"
        )
        wb.open(
            "https://owl.uwo.ca/access/lessonbuilder/item/184922311/group/0a84b539-5b11-4116-8db3-915a20a97018/Assignment%20Schedule/Evening%202nd%20Term%20Assignment%20Schedule%202021-22%20_January%20only_-1.pdf"
        )
        wb.open(
            "https://drive.google.com/drive/folders/1TMRDjnqGzQIOOJSqZ9u9EjKOCcoceNua"
        )
        wb.open(
            "https://bibliu.com/app/#/view/books/1001281231618/pdf2htmlex/index.html#page_179"
        )
    elif course.lower() == "2232":
        wb.open(
            "https://owl.uwo.ca/portal/site/4572e1fe-5c56-4010-a845-3dc2b8e5e96e/tool/a01334f0-7a32-47c1-b881-2bbc97f4487e"
        )
        wb.open(
            "https://drive.google.com/drive/folders/1uHigKLnrfBbQvLPInlWHtNNVHVtI8E83"
        )
        curr_week = findweek()
        getcurrentweek(course, curr_week)
    else:
        driver.close()


main()
