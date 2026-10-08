# 1) შექმენით Movie კლასი(movieTitle, director, year).
# გამოიყენეთ @classmethod, რომ f სტრინგით გამოიტანოთ display_info ფუნქციით ფილმის მონაცემები.


class Movie:
    def __init__(self,movieTitle, director, year ):
        self.movieTitle = movieTitle
        self.director = director
        self.year = year 
    
    @classmethod
    def display_info(cls, movieTitle, director, year ):
        return f"movie title is {movieTitle} , director is {director} and the movie published in {year}"
    
print(Movie.display_info("Abduction", "John Singleton", 2011))



# 2) შექმენით Profile კლასი (username, creationDate).
# გამოიყენეთ @staticmethod, რომ f სტრინგით გამოიტანოთ get_user_info მეთოდით მომხმარებლის პროფილის მონაცემები.


class Profile:
    def __init__(self, username, creationDate ):
        self.username = username
        self.creationDate = creationDate
        
    @staticmethod
    def get_user_info(username, creationDate):
        return f"Username is {username} and creation date is {creationDate}"
    
    
print(Profile.get_user_info("Alexo_22", "March 12"))