from datetime import datetime
from pydantic import BaseModel, Field
from typing import List, Optional

class ReportDetail(BaseModel):
    detailId: Optional[int] = 0
    clientCode: Optional[str] = ""
    shortName: Optional[str] = None
    storeCode: Optional[str] = None
    merchantCode: Optional[str] = None
    text: Optional[str] = None
    error: Optional[str] = None
    statusCode: Optional[str] = None
    fileDate: Optional[str] = None
    createdAt: Optional[datetime] = None
    endAt: Optional[datetime] = None
    isDone: Optional[bool] = False
    isRunning: Optional[bool] = False
    retrys: Optional[int] = 0
    # processId: Optional[int] = None
    # webhookId: Optional[int] = None  
    acquirer: Optional[str] = None

class DefaultResponseData(BaseModel):
    statusCode: Optional[int] = 200
    meta: Optional[dict] = {}
    messages: Optional[str] = None
    data: List[Optional[ReportDetail]]

class RequesProcess(BaseModel):
    merchantCode: str
    clientCode: str
    shortName: str
    storeCode: str
    files: List[str]