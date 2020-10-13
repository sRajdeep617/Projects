import webbrowser as wb

def webAuto():

    chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
    URLS = (
                "google.com",
                "youtube.com"
           )
    
    for url in URLS:
        print("Opening :"+url)
        wb.get(chrome_path).open(url)
    
webAuto()
