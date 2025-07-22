from urllib.parse import urljoin

class Urls:
    MAIN_PAGE = "https://stellarburgers.nomoreparties.site/"

    LOGIN_PAGE = urljoin(MAIN_PAGE, "/login")

    ORDER_FEED_PAGE =  urljoin(MAIN_PAGE, "/feed")