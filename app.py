from fastapi import FastAPI
import uvicorn
import os, sys
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from text_classification.config.configuration import ConfigurationManager
from text_classification.components.model_prediction import ModelPrediction
from text_classification.exceptions import CustomException

text:str = "top round steak vegetable oil shiitake soy sauce fresh asparagus green onions"

app = FastAPI()

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training successful !!")

    except Exception as e:
        return Response(f"Error Occurred! {e}")


@app.post("/predict")
async def predict_route(text):
    try:
        config = ConfigurationManager()
        model_prediction_config = config.get_model_Prediction()
        model_prediction = ModelPrediction(config=model_prediction_config)
        output = model_prediction.predict(text=text)
        return output
    except Exception as e:
        raise CustomException(e, sys)


if __name__=="__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)

