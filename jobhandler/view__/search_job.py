from ..models import Job

def search_job_results(search_string: str):
    search_result: dict[str: list] = {"posans" : [], "cpnyans" : [], "reqans" : []}
    for obj in Job.objects.filter(position__contains = search_string):
        context = {
            'id' : obj.job_id,
            'Position' : obj.position,
            'Company' : obj.company,
            'Posted_by' :  obj.posted_by.get_username(),
            'salary_min' : obj.salary_min,
            'salary_max' : obj.salary_max,
            'requirements' : obj.requirements,
            'application_link': '/apply/' + str(obj.job_id) + '/'
        }
        search_result["posans"].append(context)
    for obj in Job.objects.filter(company__contains = search_string):
        context = {
            'id' : obj.job_id,
            'Position' : obj.position,
            'Company' : obj.company,
            'Posted_by' :  obj.posted_by.get_username(),
            'salary_min' : obj.salary_min,
            'salary_max' : obj.salary_max,
            'requirements' : obj.requirements,
            'application_link': '/apply/' + str(obj.job_id) + '/'
        }
        search_result["cpnyans"].append(context)
    for obj in Job.objects.filter(requirements__contains = search_string):
        context = {
            'id' : obj.job_id,
            'Position' : obj.position,
            'Company' : obj.company,
            'Posted_by' :  obj.posted_by.get_username(),
            'salary_min' : obj.salary_min,
            'salary_max' : obj.salary_max,
            'requirements' : obj.requirements,
            'application_link': '/apply/' + str(obj.job_id) + '/'
        }
        search_result["reqans"].append(context)
    return search_result