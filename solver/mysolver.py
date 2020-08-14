import json
from helper.point import *
from helper.rec import *
from helper.dbhlpr import dbHlpr 
import time

class mySolver:
    def __init__(self,file = b""):
        # ctor for solver
        self.file=file
        # decode file that is bytes to utf-8
        self.file = self.file.decode("utf-8")
        #create empty list as output
        self.output = []
        # connect to db
        self.dbhlpr = dbHlpr()
    def run(self):
        # main method to run the algorithm for rectangles located by input file
        sql = "INSERT INTO data (x,y,w,h) VALUES (%s,%s,%s,%s)"
        print("--------------")
        print("running algo")
        print("--------------")
        # convert sent file to json
        self.file = json.loads(self.file)
        # create main rec 
        self.mainrec = rec(self.file["main"]["x"],self.file["main"]["y"],self.file["main"]["width"],self.file["main"]["height"])
       # loop for all recs in input
        for elmnt in self.file["input"]:
            tmp = rec(elmnt["x"],elmnt["y"],elmnt["width"],elmnt["height"])
            print("checking an input rec")
            if  self.has_valid_intrs(tmp):
                # check if this rec has intersect with main rec
                #print(tmp.points)
                tmpdic = {}
                tmpdic["x"] = tmp.points["up_left"].x
                tmpdic["y"] = tmp.points["up_left"].y
                tmpdic["width"] = tmp.points["up_right"].y - tmp.points["up_left"].y
                tmpdic["height"] = tmp.points["down_left"].x - tmp.points["up_left"].x
                self.output.append(tmpdic)
                # save this rec to db
                val = (tmpdic["x"],tmpdic["y"],tmpdic["width"],tmpdic["height"])
                self.dbhlpr.insrt(val,sql)
        # commit changes to db
        self.dbhlpr.cmt()
        print("--------------")
        print("end algo")
        # print output on terminal for debugging
        #print(self.output)
        #save output as an external file (can be commented)
        with open("./tests/output.json", 'w') as outfile:
            json.dump(self.output, outfile)
        print("--------------")
        return "Done!"
    def has_valid_intrs(self,input_rec):

        # check if this rec has intersect with main rec

        # If one rectangle is on left side of other 
        if((input_rec.points["up_left"].y >= self.mainrec.points["down_right"].y) or (self.mainrec.points["up_left"].y >= input_rec.points["down_right"].y)):
            return False
  
        # If one rectangle is above other 
        if((input_rec.points["up_left"].x >= self.mainrec.points["down_right"].x) or (self.mainrec.points["up_left"].x >= input_rec.points["down_right"].x)): 
            return False
  
        return True
    def getoutput(self):
        #returns the data stored in the db(intersected rects)
        result = self.dbhlpr.slctAndFetch()
        res = []
        # convert result list to dictionary
        for elmnt in result:
          res.append({"x":elmnt[1],"y":elmnt[2],"width":elmnt[3],"height":elmnt[4],"time":str(elmnt[5])})
        return res
        # can be used to return data stored in a seprate file(uncomment if needed)
        #with open("./output.json") as jsfl:
            #return json.load(jsfl)
