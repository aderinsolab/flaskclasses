from flask import Flask,render_template,redirect,url_for,jsonify,request
import json

webapp = Flask(__name__)

@webapp.route("/",methods=["GET"])



def webhome():
	return render_template("base.html"),200

# #-----------------------------------------------------------------

@webapp.route("/user",methods=["GET"])

def getuserpage():
	return render_template("user_dashboard.html"), 200

#------------------------------------------------------------------
@webapp.route("/admin",methods=["GET"])

def getadminpage():
	return redirect(url_for('getuserpage')),301


# #-------------------------------------------------------------
@webapp.route("/allusers", methods=["GET"])
def getusers():
    users = { 
        "userdata": [
            {
                "firstname": "john",
                "lastname": "ann",
                "status": "user"
            },
            {
                "firstname": "Becky",
                "lastname": "Ann",
                "status": "admin"
            }
        ]
    }
    with open("allusers.json", "w") as file:
        json.dump(users, file, ensure_ascii=False)

    return jsonify(users), 200

def searchUser():
    d = requests.args.to_dict()
    username = d["name"]

    with open("allusers.json","r") as file:
            content = json.load(file)
            for item in item["userdata"]:
                if item["userdata"]["firstname"] == username:
                    userinfo = item


    return username






#---------------------------------------------------------------------------------

@webapp.route('/submitmovie',methods=['POST','GET'])

# def getusermovie():
# 	d = request.args.to_dict()
# 	username = d['name']
# 	username = d['movie']


if request.method == 'POST':
		username = request.form['name']
		usermovie=request.form['movie']

    return render_template("user_movie_request.html",usermovie=usermovie,username=username)

	# return render_template("user_movie_request.html",username=username,usermovie=usermovie),200
	







#---------------------------------------------------------------------------------

@webapp.route('/processage',methods=['GET'])

def processUserAge():
	movie ="The conjuring"
	age = 15
	return render_template("watchstatus.html",usermovie=movie,userage=age),200







#-----------------------------------------------------------------------------------


# @webapp.rout("/admin",methods=["GET"])

# def getAdmiPage():
# 	return redirect(url for('getUserPage')),301

	
    
	




if __name__=="__main__":
	webapp.run(port=4800,debug=True)
