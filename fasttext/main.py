from fastapi import FastAPI
from starlette.responses import RedirectResponse
from pydantic import BaseModel
from categoryclf import categoryCLF
import uvicorn

import json
import logging

logging.basicConfig(format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)


#Initialize FastAPI
app = FastAPI()

#load model
classifier = categoryCLF()

#class Item
class Item(BaseModel):
    text:str


@app.get("/")
def root():
    #response = RedirectResponse(url="/redoc")
    #return response

    return {"message":"Hello world"}

@app.post("/classification")
def classification(item: Item):
    #get detected_user_label
    text = item.text
    results = classifier.category_classification(text)
    
    #return predictions
    return results


#서버가 실행될 때, 이 서버가 모든 네트워크 인터페이스에서 들어오는 연결을 수락한다는 의미 0.0.0.0
if __name__ =='__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000)

#localhost = 127.0.0.1

#Docker 의 내부 네트워크에서 컨테이너가 할당받는 프라이빗 IP -> 이 주소는 Docker 호스트 또는 다른 컨테이너들이 접근할 때만 사용 (이를 사용하여, 외부 네트워크나 인터넷에서 컨테이너 접근은 불가능)
#docker ip : 172.17.0.2