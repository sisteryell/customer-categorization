from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from catboost import CatBoostClassifier
import numpy as np
import uvicorn



import warnings
warnings.filterwarnings('ignore')

app = FastAPI()

templates = Jinja2Templates(directory='templates')


model = CatBoostClassifier()
model.load_model("model/catboost_best_model.cbm")

app.mount("/static", StaticFiles(directory="static"), name="static")



@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("customer.html", {"request": request, "context": None})
    

@app.post("/", response_class=HTMLResponse)
async def predict_cluster(
    request: Request,
    Age: int = Form(...),
    Education: int = Form(...),
    Marital_Status: int = Form(...),
    Parental_Status: int = Form(...),
    Children: int = Form(...),
    Income: float = Form(...),
    Total_Spending: float = Form(...),
    Days_as_Customer: int = Form(...),
    Recency: int = Form(...),
    Wines: float = Form(...),
    Fruits: float = Form(...),
    Meat: float = Form(...),
    Fish: float = Form(...),
    Sweets: float = Form(...),
    Gold: float = Form(...),
    Web: int = Form(...),
    Catalog: int = Form(...),
    Store: int = Form(...),
    Discount_Purchases: int = Form(...),
    Total_Promo: int = Form(...),
    NumWebVisitsMonth: int = Form(...)
):
    input_data = np.array([[Age, Education, Marital_Status, Parental_Status, Children, Income, Total_Spending,
                            Days_as_Customer, Recency, Wines, Fruits, Meat, Fish, Sweets, Gold,
                            Web, Catalog, Store, Discount_Purchases, Total_Promo, NumWebVisitsMonth]])
    
    prediction = model.predict(input_data)[0]

    return templates.TemplateResponse("customer.html",{
        "request": request,
        "context": int(prediction)
    })
    

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)