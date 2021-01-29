'''projectName: HtmlCoder
projectStartDate: 2020/01/27
projectAuthor: Bahman-Ahmadi
projectProgrammingLanguage: python3
projectInfo: a program for help programmer in writing html codes!
projectVersion: 1.0.0Alpha'''

def addTag(tagName,attrs,content,wantClose):
	if wantClose == "y":
		step1 = f"<{tagName} "
		for attr in attrs:
			step1 += attr
		result = step1+">"+content+f"</{tagName}>"
		return result
	else:
		step1 = f"<{tagName} "
		for attr in attrs:
			step1 += attr
		result = step1+f"value=\"{content}\" />"
		return result
		
themeColor = input(">>> theme color(hex): ")
links = ""
addLinksLoop = input(">>> do u want add a link to head? (y/n): ").lower()
while addLinksLoop != "n":
	links += f"<link href=\"{input('>>> href: ')}\" rel=\"{input('>>> rel: ')}\">\n"
	print(links)
	addLinksLoop = input(">>> do u want add a link to head? (y/n): ").lower()


programContent = ""
addbodyTagsLoop = input(">>> do u want add a tag to body? (y/n): ").lower()
while addbodyTagsLoop != "n":
	tagAttrs , addAttrsLoop = [] , input(">>> add attr(y/n): ").lower()
	
	while addAttrsLoop != "n":
		tagAttrs.append(input(">>> add a new attribute(tamplate: attrName=\"value\"): ")+" ")
		addAttrsLoop = input(">>> add attr(y/n): ").lower()	
	programContent += addTag(input(">>> tag name: "),tagAttrs,input(">>> inner html: "),input(">>> your tag want a close tag? (y/n): ").lower())
	addbodyTagsLoop = input(">>> do u want add a tag to body? (y/n): ").lower()

htmlCodes = f"""
<html>
  <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <meta name="theme-color" content="{themeColor}"> 
    <meta name="msapplication-navbutton-color" content="{themeColor}">
    <meta name="apple-mobile-web-app-status-bar-style" content="{themeColor}">
    {links}
    </head>
    <body>
        {programContent}
    </body>
</html>
"""
from os import system
from langlib1 import style

system("clear")
print(style(htmlCodes,"lyellow"))
try:
	open("htmlCodes.html","x")
	open("htmlCodes.html","w").write(htmlCodes)
except:
	open("htmlCodes.html","w").write(htmlCodes)
finally:
	input()
print(style("html codes saved at htmlCodes.html","lgreen"))
