

class const:
    HOST = "localhost"
    USERNAME = "scraping_user"
    PASSWORD = ""
    DATABASE = "scraping_sample"
    link_str = "browse-movie-link"
    name_str = "browse-movie-title"
    


class homescrp:
        
    def home_url(root, i): 
        website = f'{root}?page={i}'
        return website


        
    
    