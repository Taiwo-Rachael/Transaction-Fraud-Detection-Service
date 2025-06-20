from pydantic import BaseModel
from datetime import datetime
# using Pydantic's baseModel class, defining JSON payload input structure. 
# This definition means these are the datatypes accepted for the imput variables. 
# and it will guide the user on what data to supply to the service in order to get a response.

class TransactionInput(BaseModel):
    amount: float
    oldbalanceOrg: float
    newbalanceOrig: float
    oldbalanceDest: float
    newbalanceDest: float
    type: str   
    timestamp: datetime    
