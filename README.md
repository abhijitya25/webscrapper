# webscrapper
The main idea is to pass a list of url to a website and to 

We will provide a list of URL as the example attached in the CSV. The scraper should go to the website and extract specific information listed above (with the same approach of changing user agent and sleeping at every request).
The input is a CSV with a list of URLs and the Output is a JSON where each element as the original URL and the rest are information taken from the webpage. (see last page for a full example of one element).
Each element will have:

    "URL_text”: it is the original URL
    
    "Scrape_date":  a stringified version of Today() function, in format “DD/MM/YYYY”
    
    "Number_of_Results":  an integer which represents the total numbers of definitions found.
    
    "Dictionary": a list of results found in each page. Each element has the following shape:
          "ID": a simple counter that goes to 1 to N
          "Definition": a simple string found inside the text (see below)
          "Length":  an integer found in the text (see below)
          "Solution":  a simple string found inside the text (see below)

