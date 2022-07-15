from category import Category
from document import Document
from topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category in self.categories:
            return
        self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic in self.topics:
            return
        self.topics.append(topic)

    def add_document(self, document: Document):
        if document in self.documents:
            return
        self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = self.__find_obj_by_id(self.categories, category_id)
        category.edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = self.__find_obj_by_id(self.topics, topic_id)
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id, new_file_name):
        document = self.__find_obj_by_id(self.documents, document_id)
        document.edit(new_file_name)

    def delete_category(self, category_id):
        category = self.__find_obj_by_id(self.categories, category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.__find_obj_by_id(self.topics, topic_id)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.__find_obj_by_id(self.documents, document_id)
        self.documents.remove(document)

    def get_document(self, document_id):
        return self.__find_obj_by_id(self.documents, document_id)

    def __repr__(self):
        return '\n'.join(repr(d) for d in self.documents)

    @staticmethod
    def __find_obj_by_id(entities, obj_id):
        for entity in entities:
            if entity.id == obj_id:
                return entity
