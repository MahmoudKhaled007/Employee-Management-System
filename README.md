
#Employee Management System

An Employee Management System is a Full-Stack web application for managing
the staff data within a small company or organization. The system as such as it has been
developed is called the Employee Management System. It consists of functionally related
GUI (application program) and database.

##Tools used 


## Project Dependencies
*  Python
- Flask
- HTML
- CSS
- Javascript
- Bootstrap
- MySql
- jinja2

## Getting Started

1. Open the terminal in the project directory 
2. Run  pip install -r requirements.txt
3. Activate virtual environment: env\Scripts\activate
4. After activating virtual env run: python app.py
5. Add "/" to the localhost URL to run the full app 

## How it Works

The scraper uses Selenium to automate browsing the Property Finder website, and Beautiful Soup to parse the HTML data returned. The `scraper.py` script navigates the Property Finder search page by specifying various filters such as location, property type, and price range. Then it iterates through the search results pages, extracts the relevant fields, and writes them to a CSV file, and pkl file.

## Fields Extracted

The scraper extracts the following fields for each property:
- Title
- Location
- Property Type
- Bedrooms
- Bathrooms
- Area (in sqm)
- Price
- Date Added
- Amenties 
- Description


## Important Considerations

When engaging in web scraping, it's important to keep in mind that not all websites allow it. Some sites may block your IP address or take legal action if they detect automated scraping activity.

Additionally, web scraping can put a significant strain on the resources of the website being scraped, which may impact its performance and availability for other users.

Therefore, it's important to always be respectful of the website being scraped, adhere to any terms of use or access policies that they have in place and use appropriate methods to limit the load on their servers.


## Challenges
This website was using HoneyPot Trap for scrappers so, you cannot Request a normal request from Requests library you should act as a normal user thats why i used selenium with user agent

## Pros of this scrapper 
- Deque Algorithm to Reduce memory usage by half comparing to normal python lists 
- Joblib dumb and load to Continue scrapping from the last point if the scrapper interrupted
- Optimized Code 

## Conclusion

This project demonstrates how to scrape data from a real estate website using Python libraries BeautifulSoup4 and Selenium. By following best practices and using appropriate techniques, you can engage in responsible web scraping while minimizing the negative impact on others.
## Authors

- [@MahmoudKhaled007](https://www.github.com/MahmoudKhaled007)


## License

[GNU](https://www.gnu.org/licenses/gpl-3.0.en.html)

