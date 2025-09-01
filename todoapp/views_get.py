from django.http import JsonResponse
from .models import NewTodo, Categories

def get_all_todo(request):
    is_status = request.GET.get('is_status', None)
    todo_type = request.GET.get('todo_type', None)

    all_to = NewTodo.objects.all()

    if is_status is not None:
        if is_status.lower() == "true":
            is_status = True
        elif is_status.lower() == "false":
            is_status = False
        else:
            res = {
                "status": "error",
                "message": "is_status must be true or false",
                "code": 400,
                "data": []
            }
            return JsonResponse(res, status=400)
        all_to = all_to.filter(is_status=is_status)

    if todo_type is not None:
        todo_type = todo_type.upper()  

        if todo_type not in [Categories.LEARN, Categories.UN_KNOW]:
            res = {
                "status": "error",
                "message": "todo_type must be LEARN or UN_KNOW",
                "code": 400,
                "data": []
            }
            return JsonResponse(res, status=400)

        all_to = all_to.filter(todo_type=todo_type)

    if not all_to.exists():
        res = {
            "status": "success",
            "message": "Not found data todo",
            "code": 200,
            "data": []
        }
        return JsonResponse(res, status=200)

    todo_list = list(all_to.values(
        'id', 'title', 'description', 'date_time', 'is_status', 'todo_type'
    ))

    res = {
        "status": "success",
        "message": "data !!!",
        "code": 200,
        "data": todo_list
    }
    return JsonResponse(res, status=200)
