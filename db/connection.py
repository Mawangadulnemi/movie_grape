# 데이터베이스 사용 방법

# 1. Connection 맺기  (DB =================Python)
# IP      : 컴퓨터 주소
# Port    : 27017 (==어떤 프로그램을 접근 할 것인지, 여기선 MongoDB)
# ID & PW : 계정정보
# 2. 명령 보내기       (Python ------------->DB)
# 3. 결과 받기         (Python <--------------DB)
# 4. Connection 끊기  (Python   XXXXXX       DB)

from pymongo import MongoClient


# MongoDB Connection
def conn():
    client = MongoClient("mongodb+srv://cnu01:wlals1209@moviecnu01.yk0z4cz.mongodb.net/")  # IP, Port, ID&PW
    db=client["movie"]

    collection=db.get_collection("movie")
    return collection