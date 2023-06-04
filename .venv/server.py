from flask import Flask, render_template,request,redirect
import csv
app = Flask(__name__)

#my home
@app.route("/")
def myhome():
    return render_template("index.html")

#this method didnt work with me i dont know why
# @app.route("/string:<page_name>")
# def html_page(page_name):
#     return render_template("page_name")



#there home
@app.route("/index.html")
def home():
    return render_template("index.html")

#about
@app.route("/about.html")
def about():
    return render_template("about.html")

#works
@app.route("/works.html")
def works():
    return render_template("works.html")

#work
@app.route("/work.html")
def work():
    return render_template("work.html")

#contact
@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/yoyo.html")
def re():
    return render_template("yoyo.html")




#function to store and save the data coming sent to your server
def write_to_file(data):
    with open("mydataBase.txt",mode="a") as databasee:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        de="*"*100
        file=databasee.write(f"\nemail={email}\nsubject={subject}\n{message}\n{de}")

#store data in csv file instead of txt file
def write_to_csv(data):
    with open("database2.csv",mode="a") as databace2:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        csv_file=csv.writer(databace2,quoting=csv.QUOTE_MINIMAL)
        csv_file.writerow([email,subject,message])
        


#making connect stuff 
@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
        if request.method=="POST":
            data=request.form.to_dict()
            write_to_csv(data)
            # write_to_file(data)
        return redirect("index.html")




# @app.route("/")
# def userpage():
#     return render_template("about.html")






if __name__=="__main__":
    app.run(debug=True,port=9000)