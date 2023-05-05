from selenium.webdriver.common.by import By


class CautareProdus:
    SEARCH_BAR = (By.CSS_SELECTOR, "#search")
    PANTOFI_SPORT = (By.CSS_SELECTOR, "#product-collection-image-50885")
    PANTOFI_SPORT_PRICE = (By.CSS_SELECTOR, "span[id='product-price-50885'] span[class='price']")
    ADAUGARE_IN_COS = (By.CSS_SELECTOR, "li[class='item nth-child-2np1 nth-child-5np1'] div[class='actions'] span")
    MARIMEA = (By.CSS_SELECTOR, "a[id='swatch30'] span[class='swatch-label']")
    ADD_CART = (By.CSS_SELECTOR, "button[title='Adăugare în Coș'] span span")
    FINALIZARE_COMANDA = (By.CSS_SELECTOR,
                          "div[class='totals'] div ul[class='checkout-types'] li button[title='Continuare cu"
                          " Finalizarea Comenzii'] span span")
    TEXT_FINALIZARE = (By.CSS_SELECTOR, "div[class='page-title'] h1")
    ERROR_MSG = (By.CSS_SELECTOR, ".note-msg")