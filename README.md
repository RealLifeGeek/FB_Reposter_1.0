# FB_Reposter_1.0
A basic program that uses web scraping techniques to crawl the website, extract the relevant articles nad repost them to Facebook account or page.
The first step in the program is to specify the website - https://seznamzpravy.cz.  Than there are identified the HTML elements that contain the article data - header and URL. Once the data are identified, they are extracted  and stored in lists.  The data are clean and preprocessed.

Next, theprogram is able to post the extracted articles to a Facebook account or page. To do this, it is using the Facebook Graph API, which allows you to programmatically create posts on a Facebook account or page. You need to authenticate with Facebook and obtain an access token, which would grant your program permission to post on behalf of the account or page. You have to also know your page or account ID.

There are some posibilities to improve the program, such as creating database by using sqlite module instead of storing the data in lists. Good idea could be schedule the program to run at regular intervals, so that it can scrape the website and post new articles automatically.
