import csv

data=[]
with open('movies.csv','r',encoding="utf-8") as f:
    reader = csv.reader(f)
    # for row in reader:
    #     if '\u' not in row:
    #         data.append(row)
    data = list(reader)
    # all_movies = data[1:]
    # headers = data[0]

# headers.append("poster_link")

with open("clean.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerows(data)