import PyScrappy as ps
############## ECommereceScrapper ############## 
class ECommerceScrapper():
        
    obj = ps.ECommerceScrapper()
    """

    ECommerece Scrapper: Helps in scrapping data from E-Comm websites
        1. Alibaba
        2. Amazon
        3. Flipkart
        4. Snapdeal

    Type: class

    Note
    ------
    Create an object of this class to proceed further.

    Example
    ---------
    >>> obj = PyScrappy.ECommerceScrapper()

    """
 ############## Flipkart Scrapper ############## 
    def flipkart_scrapper(self, product_name, n_pages):
        print(product_name)

        """

        Flipkart Scrapper: Helps in scrapping Flikart data ('Name', 'Price', 'Original Price', 'Description', 'Rating').
        return type: DataFrame

        Parameters
        ------------
        product_name: Enter the name of the desired product, which you want to scrape the data of
            Type: str

        n_pages: Enter the number of pages that you want to scrape
            Type: int

        Note
        ------
        Both the arguments are a compulsion. 
        If n_pages == 0: A prompt will ask you to enter a valid page number and the scrapper will re-run. 
        
        Example
        ---------
        >>>  obj.flipkart_scrapper("Product Name", 3) 
        out: Name   Price   Original Price  Description Rating
             abc    ₹340    ₹440            Product     4.2
             aec    ₹140    ₹240            Product     4.7

        """

        import flipkart 
        self.product_name=product_name
        self.n_pages=n_pages
        
        obj = ps.ECommerceScrapper()
        obj.flipkart_scrapper(product_name, n_pages)
        return flipkart.scrappi(product_name, n_pages)

    ############## Snapdeal Scrapper ##############
    def snapdeal_scrapper(self, product_name, n_pages):
        print(product_name)
        """

        Snapdeal Scrapper: Helps in scrapping Snapdeal data ('Name', 'Price', 'Original Price', 'Number of Ratings').
        return type: DataFrame

        Parameters
        ------------
        product_name: Enter the name of the desired product, which you want to scrape the data of.
            Type: str

        n_pages: Enter the number of pages that you want to scrape
            Type: int

        Note
        ------
        Both the arguments are a compulsion. 
        If n_pages == 0: A prompt will ask you to enter a valid page number and the scrapper will re-run.
        
        Example
        ---------
        >>>  obj.snapdeal_scrapper('product', 3)
        out: Name   Price   Original Price   Number of Ratings
             abc    ₹340    ₹440             40
             aec    ₹140    ₹240             34
  
        """

        import snapdeal
        self.product_name=product_name
        self.n_pages=n_pages

        obj = ps.ECommerceScrapper()
        obj.snapdeal_scrapper(product_name, n_pages)
        return snapdeal.scrappi(product_name, n_pages)
  

