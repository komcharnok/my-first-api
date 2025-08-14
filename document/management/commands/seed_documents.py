from django.core.management.base import BaseCommand
from document.models import Document

class Command(BaseCommand):
    help = 'Seed initial documents with content as list of dict'

    def handle(self, *args, **kwargs):
        seed_documents = [
            {
                "title": "Tailwind CSS",
                "content": [
                    {"id": 1, "description": "เทส1", "type": "position1"},
                    {"id": 2, "description": "เทส2", "type": "position2"}
                ],
                "categories": "CSS_FRAMEWORK"
            },
            {
                "title": "Django Basics",
                "content": [
                    {"id": 1, "description": "Django Model", "type": "backend"},
                    {"id": 2, "description": "Django Views", "type": "backend"}
                ],
                "categories": "LIBRARY"
            },
            {
                "title": "React UI",
                "content": [
                    {"id": 1, "description": "React Components", "type": "frontend"},
                    {"id": 2, "description": "React State", "type": "frontend"}
                ],
                "categories": "UI_FRAMEWORK"
            }
        ]

        for doc in seed_documents:
            Document.objects.create(**doc)

        self.stdout.write(self.style.SUCCESS('Seed data completed!'))
