# Displays IMDB's Top 100 movies that match a search string.
def main():
    searchWord = getWord()
    file = open("imdb.txt")
    line = search(file, searchWord)
    
    if(len(line) > 0):
        print("Rating\tYear\tTitle")
        matches = 0
        while(len(line) > 0):
            display(line)
            line = search(file, searchWord)
            matches += 1
        print(matches, "matches.")
        
def getWord():
    searchWord = input("Movie Name: ").lower()
    print()
    return searchWord


def search(file, searchWord):
    for line in file:
        lineLower = line.lower()
        if (searchWord in line):
            return line
    return ""   

def display(line):
    parts = line.split()
    rating = parts[0]
    year = parts[-1]
    title = ""
    for i in range(1, len(parts)-1):
        title += parts[i] + " "
    print(rating + "\t" + year[1:-1] + "\t" + title)
        


            
    
    
main()