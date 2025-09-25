import bypasser
import ddl
from ddl import ddllist
import re
from texts import HELP_TEXT

# print()
# print(HELP_TEXT.replace("*","").replace("-","").replace("_",""))
# print("\n------------------------------------------------\n")

while True:
  print("\n------------------------------------------------\n")
  url = input("URL: ")
  if url.lower() in ["quit","exit"]: 
    print("\nBye bye\n")
    break
  
  temp = ""  # Initialize temp variable
  
  if re.search(r"https?:\/\/(?:[\w.-]+)?\.\w+\/\d+:", url):
      result = bypasser.scrapeIndex(url)
      if result:
          for page in result: print(page)
      else:
          print("No results found")
      continue  # Skip to next iteration
  elif bypasser.ispresent(ddllist,url):
      try: temp = ddl.direct_link_generator(url)
      except Exception as e: temp = "**Error**: " + str(e)
  else:    
      try: temp = bypasser.shortners(url)
      except Exception as e: temp = "**Error**: " + str(e)
  
  link = temp

  print()
  print("Result:",link)