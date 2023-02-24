MENU_PROMPT="\n Enter 'a' to add a movies,'s' to see your movies 'f' to find a movie by title,or 'q' to quit: "
movies=[]
def add_movie():
    user_choise=int(input("How many movies do you want store:"))
    for x in range(user_choise):   
        title=input(f"Enter the {x+1}-movie title: ")
        director=input(f"Enter the {x+1}-movie director: ")
        year=input(f"Enter the movie {x+1}-release year: ")
        movies.append({
            'title':title,
            'director':director,
            'year':year
        })
    print(movies)
def see_movies():
        for movie in movies:
            title=movie['title']
            director=movie['director']
            year=movie['year']
        print(f"{title} in {year}  has been saved to {director}")  
    
    
def find_movies():
    search_movie=input("Which movie do you want to find : ")    
    for movie in movies:
        if movie['title']==search_movie:
            print(movie)
         
         
def delete_movies():
    name_of_movie=input("Which movie do you want to delte :")     
    for movie in movies:
        if movie['title']==name_of_movie:
            print(movies.pop(name_of_movie))    
            
            
def menu():
    
    choise=input("\n Enter 'a' to add a movies,'s' to see your movies 'f' to find a movie by title,or 'q' to quit: ")
    
    while choise!='q':
        if choise=='a':
            add_movie() 
        elif choise=='s':
            see_movies()
        elif choise=='f':
            find_movies()
        elif choise=='d':
            delete_movies()  
        else:
            print("unknown") 
        choise=input("\n Enter 'a' to add a movies,'s' to see your movies 'f' to find a movie by title,or 'q' to quit: ")    
                        

print(menu())