# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#
# # Read in a page
html = scraperwiki.scrape("https://www.compare-school-performance.service.gov.uk/schools-by-type?step=default&table=schools&region=all-england&for=secondary&page=1")
# Print the variable html containing the webpage
# print(html)
#
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
# Store the matched links in "matchedlinks"
matchedlinks = root.cssselect("tr tbody")
# Print that
# print(matchedlinks)
#
# Create a dictionary called record
record = {}
# Loop through the items in matchedlinks, calling each one li
for li in matchedlinks:
  #Store the text contents of li in a new variable listtext
  listtext = li.text_content()
  # Print that
  print(listtext)
  # Store it in the 'record' dictionary under the key 'address'
  record['schools'] = listtext
  # Save the record to the datastore with 'schools' as unique key
  scraperwiki.sqlite.save(['schools'],record)
  
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
