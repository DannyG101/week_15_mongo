def get_engineering_high_salary_employees(collection):
    results = list(collection.find({"job_role.department": "Engineering", "salary": {"$gt": 65000} },
                                   {"_id":0, "employee_id":1, "name":1, "salary":1}))
    return results

def get_employees_by_age_and_role(collection):
    results = list(collection.find({"$and" : [ {"age":{"$gte": 30}},{"age":{"$lte": 45}} ]},
                                   {"_id":0}))
    return results


def get_top_seniority_employees_excluding_hr(collection):
    results = list(collection.find({"job_role.department": {"$nin": ["HR"]}},
                                   {"_id":0}).sort({"years_at_company": -1}).limit(7))
    return results


def get_employees_by_age_or_seniority(collection):
    results = list(collection.find({"$or": [{"age": {"$gt": 50}}, {"years_at_company": {"$lt": 3}}]},
                                   {"_id": 0, "employee_id": 1, "name": 1, "age": 1, "years_at_company": 1}))
    return results

def get_managers_excluding_departments(collection):
    results = list(collection.find(
        {"$and": [{"job_role.title": "Manager"}, {"job_role.department": {"$nin": ["Sales", "Marketing"]}}]},
        {"_id": 0}))
    return results


def get_employees_by_lastname_and_age(collection):
    results = list(collection.find({"name": {"$regex": "(Wright|Nelson)$"}, "age": {"$lt": 35}}))
    return results

