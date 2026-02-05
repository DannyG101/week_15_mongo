from fastapi import FastAPI
from connection import DBConnect
import dal
import uvicorn



app = FastAPI()


db = DBConnect()

@app.on_event("startup")
def startup():
    db.connect()
    db.load_file()

@app.get("/employees/engineering/high-salary")
def get_engineering_high_salary_employees():
    db.connect()
    return dal.get_engineering_high_salary_employees(db.coll)

@app.get("/employees/by-age-and-role")
def get_employees_by_age_and_role():
    db.connect()
    return dal.get_employees_by_age_and_role(db.coll)


@app.get("/employees/top-seniority")
def get_top_seniority_employees_excluding_hr():
    db.connect()
    return dal.get_top_seniority_employees_excluding_hr(db.coll)


@app.get("/employees/age-or-seniority")
def get_employees_by_age_or_seniority():
    db.connect()
    return dal.get_employees_by_age_or_seniority(db.coll)

@app.get("/employees/managers/excluding-departments")
def get_managers_excluding_departments():
    db.connect()
    return dal.get_managers_excluding_departments(db.coll)


@app.get("/employees/by-lastname-and-age")
def get_employees_by_lastname_and_age():
    db.connect()
    return dal.get_employees_by_lastname_and_age(db.coll)



uvicorn.run(app)





















































# from fastapi import File, UploadFile
# import pandas as pd
#
# @app.post("/upload")
# def upload_file(file: UploadFile = File(...)):
#     # read CSV
#     df = pd.read_csv(file.file)
#
#     # convert to list of dicts
#     records = df.to_dict("records")
#
#     # insert into Mongo
#     db.connect()
#     db.coll.insert_many(records)
#
#     # close file
#     file.file.close()
#
#     return {"status": "success", "inserted_records": len(records)}
