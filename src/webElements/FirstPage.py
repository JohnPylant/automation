
class FirstPage:

    def navigationBarElements(self):
        return {
            "homeButtonXpath": homeButtonXpath,
            "catagoriesDropDownXpah": catagoriesDropDownXpah,
            "contactButtonXpath": contactButtonXpath,
            "signInButtonXpath": signInButtonXpath,
        }
    
    def home_pic(self):
        return {
            "mainHomePictureButtonXpath": mainHomePictureButtonXpath
        }

#Navigation bar elements
homeButtonXpath =  "//a[contains(text(),'Home')]"
catagoriesDropDownXpah = "//button[contains(text(),' Categories ')]"
contactButtonXpath = "//a[contains(text(),'Contact')]"
signInButtonXpath = "//a[contains(text(),'Sign in')]"
languageSelectionDropDownXpath = "//button[contains(text(),' EN ')]"


#Main home picture
mainHomePictureButtonXpath = "//*[@id='Layer_1']"


