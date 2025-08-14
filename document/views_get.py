from django.http import JsonResponse
from .models import Document

def get_all_doc(request):
    category = request.GET.get('category', None)
    documents = Document.objects.all()

    if category:
        documents = documents.filter(categories=category)

    if not documents.exists():  # เช็คว่าง
        response = {
            "status": "success",
            "message": "No documents found",
            "code": 200,
            "data": []
        }
        return JsonResponse(response, status=200)

    # ถ้ามีข้อมูล
    documents_list = list(documents.values(
        'id', 'title', 'content', 'categories', 'created_at', 'updated_at'
    ))

    response = {
        "status": "success",
        "message": "Documents retrieved successfully",
        "code": 200,
        "data": documents_list
    }
    return JsonResponse(response, status=200)


def get_by_id_doc(request, id):
    try:
        doc = Document.objects.get(pk=id)

        if not doc.content:
            response = {
                "data": [],
                "status": "success",
                "message": "No data content!!",
                "code": 200
            }
            return JsonResponse(response, status=200)       

        content_with_id = []
        for index, item in enumerate(doc.content):
            content_with_id.append({
                "id": item.get("id", index + 1),
                "description": item.get("description", ""),
                "type": item.get("type", "")
            })

        response = {         
            "status": "success",
            "message": "Data response success !!",
            "code": 200,
               "data": {
                "id": doc.id,
                "title": doc.title,
                "content": content_with_id,
                "categories": doc.categories,
                "created_at": doc.created_at,
                "updated_at": doc.updated_at
            },
        }
        return JsonResponse(response, status=200)

    except Document.DoesNotExist:
        response = {
            "data": None,
            "status": "error",
            "message": "Document not found",
            "code": 404
        }
        return JsonResponse(response, status=404)



