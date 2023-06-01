# 데이터베이스 사용 방법

# 1. Connection 맺기  (DB =================Python)
# IP      : 컴퓨터 주소
# Port    : 27017 (==어떤 프로그램을 접근 할 것인지, 여기선 MongoDB)
# ID & PW : 계정정보
# 2. 명령 보내기       (Python ------------->DB)
# 3. 결과 받기         (Python <--------------DB)
# 4. Connection 끊기  (Python   XXXXXX       DB)


# MongoDB  구조
#  - MongoDB(DBMS): 데이터베이스 관리 시스템
#   ㄴ DB(NAVER): 프로젝트 단위
#       ㄴ Collection(회원) - CRUD
#       ㄴ Collection(카페) - CRUD
#       ㄴ Collection(쇼핑) - CRUD
#       ㄴ Collection(메일) - CRUD
#   ㄴ DB(KAKAO): 프로젝트 단위
#   ㄴ DB0(BLOG): 프로젝트 단위

# MongoDB 데이터 주고 받기
# - MongoDB는 BSON Type으로 데이터를 주고 받음
# - BSON(Binary Json) = JSON과 거의 동일
# - 그냥 JSON Type으로 사용하면 됨(문제 없음)
# - Python에서 JSON은 Dict type 사용! (Python Dict = JSON)
from pymongo import MongoClient


# MongoDB Connection
def conn():
    #                                        mongodb_web: ip+ prot +idpw
    # Python-Mongodb  연결 => client
    client = MongoClient("mongodb+srv://cnu01:cnu1234@moviecnu01.yk0z4cz.mongodb.net/")  # IP, Port, ID&PW
    db=client["review"]  # 이게 DB 선택= 리뷰라는 디비에 접근하겠다

    collection=db.get_collection("movie")  # 이게 Collection 선택 = 무비라는 컬렉션에 접근하겠다
    return collection


