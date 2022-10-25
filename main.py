import mysql.connector
import datetime
# name = input("Please Enter your name :  ")
# Math = int(input(" Enter your Math Number :  "))
# English = int(input("Enter your English Number :  "))
# Urdu = int(input("Enter your Urdu Number :  "))
#
# total = Math + English + Urdu
#
# total_marks = (total*100) / 300
#
# current = datetime.datetime.now()
#
# print(f"{name} Your total number is : {total}\n tour percentage is :  {total_marks}%\n")
#
# f = open("C:\\Users\\asp\\Desktop\\admin\\studentrecord.txt","a")
# f.write (f"{name}\n Yor percentage is : {total_marks}%\n time is {current}\n total number is : {total}\n")
#
# f.close()
#
# DBcon =mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="student_record",
# )
# cursor = DBcon.cursor()
# insert_query ="INSERT INTO `student`(`name`, `math number`, `English number`, `urdu number`, `total number`, `percetage`, `current time`) VALUES(%s,%s,%s,%s,%s,%s,%s)"
# meri_value = [name,Math,English,Urdu,total,total_marks,current]
# cursor.execute(insert_query,meri_value)
# DBcon.commit()
# DBcon.close()
# import pandas
# from openpyxl.workbook import workbook
# import lxml
# khaadi = {
#     "name" :["Drop sholder","classic kurta","fabric","straight pant","narrow pant","classic Kameez,","bootcut","shirt"],
#     "price" :[3454,4354,3453,3456,5677,5467,7865,5677],
#     "discription" : ["bikar","bikar","bikar","bikar","bikar","bikar","bikar","bikar"],
# }
# print(khaadi)
# mubas =pandas.DataFrame(khaadi)
# print(mubas)
#
# #excel
# mubas.to_excel("Mubashir.xlsx",index=False)
#
# #xml
# mubas.to_xml("Mubashirxml")
#
# #csv
# mubas.to_csv("Mubashir.csv")
#
# #json
# mubas.to_json("Mubashir.js")

from pydriller import Repository
import pandas
import lxml
# make dishes
commitwalekaname, commitkidate, commitmsg = [], [], []
# fetch Date
for i in Repository(path_to_repo="https://github.com/Kaggle/kaggle-api.git").traverse_commits():
    commitwalekaname.append(i.committer.name)
    commitkidate.append(i.committer_date)
    commitmsg.append(i.msg)

#save data into Dictionary
GitHub_Dict = {
    "Commitername" : commitwalekaname,
    "commiterDate" : commitmsg,
    "Massege" : commitmsg
}
#save date into csv

convert_to_Table = pandas.DataFrame(GitHub_Dict)
convert_to_Table.to_csv("Repositrykadata.csv",index=False)
convert_to_Table.to_xml("Repositrykadata.xml")

print("Date Saved Successfully")