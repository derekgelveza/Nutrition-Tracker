from fastapi import APIRouter

router = APIRouter(prefix="/nutrition", tags=["Nutrition"])

@router.get("/bmi")
def calculate_bmi(height: float, weight: float):
    bmi = weight / (height ** 2)
    return {"bmi": round(bmi, 2)}
