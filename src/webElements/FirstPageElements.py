
class FirstPage:

    # Creating lists to be used for the navigation bar elements and the main home picture element
    def navigationBarElements(self):
        return {
            "homeButtonXpath": homeButtonXpath,
            "catagoriesDropDownXpah": catagoriesDropDownXpah,
            "contactButtonXpath": contactButtonXpath,
            "signInButtonXpath": signInButtonXpath,
        }
    
    # Creating a list to be used for the main home picture element
    def home_pic(self):
        return {
            "mainHomePictureButtonXpath": mainHomePictureButtonXpath
        }

    def sort_elements(self):
        return {
            "items_container_Xpath": items_container_Xpath,
            "sort_drop_down_button_Xpath": sort_drop_down_button_Xpath,
            "name_asc_option_Xpath": name_asc_option_Xpath,
            "name_desc_option_Xpath": name_desc_option_Xpath,
            "price_desc_option_Xpath": price_desc_option_Xpath,
            "prive_asc_option_Xpath": prive_asc_option_Xpath,
            "co2_asc_option_Xpath": co2_asc_option_Xpath,
            "co2_desc_option_Xpath": co2_desc_option_Xpath
        }

#Navigation bar elements
homeButtonXpath =  "//a[contains(text(),'Home')]"
catagoriesDropDownXpah = "//button[contains(text(),' Categories ')]"
contactButtonXpath = "//a[contains(text(),'Contact')]"
signInButtonXpath = "//a[contains(text(),'Sign in')]"
languageSelectionDropDownXpath = "//button[contains(text(),' EN ')]"


#Main home picture
mainHomePictureButtonXpath = "//*[@id='Layer_1']"

# Sort drop down elements
sort_drop_down_button_Xpath = "//select[@aria-label='sort']"
name_asc_option_Xpath = "//select[@aria-label='sort']//option[@value='name,asc']"
name_desc_option_Xpath = "//select[@aria-label='sort']//option[@value='name,desc']"
price_desc_option_Xpath = "//select[@aria-label='sort']//option[@value='price,desc']"
prive_asc_option_Xpath = "//select[@aria-label='sort']//option[@value='price,asc']"
co2_asc_option_Xpath = "//select[@aria-label='sort']//option[@value='co2_rating,asc']"
co2_desc_option_Xpath = "//select[@aria-label='sort']//option[@value='co2_rating,desc']"

# Items container
items_container_Xpath = "//div[@class='col-md-9']//div[@data-test='sorting_completed']"





