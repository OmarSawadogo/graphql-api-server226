import graphene
from graphene_django import DjangoObjectType, DjangoListField 
from .models import Book 


class BookType(DjangoObjectType): 
    class Meta:
        model = Book
        fields = "__all__"


class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    book = graphene.Field(BookType, book_id=graphene.Int())

    def resolve_all_books(self, info, **kwargs):
        return Book.objects.all()

    def resolve_book(self, info, book_id):
        return Book.objects.get(pk=book_id)   

class BookInput(graphene.InputObjectType):
    id = graphene.ID()
    titre = graphene.String()
    auteur = graphene.String()
    annee_publication = graphene.String()
    pages = graphene.Int() 

class CreateBook(graphene.Mutation):
    class Arguments:
        book_data = BookInput(required=True)

    book = graphene.Field(BookType)

    @staticmethod
    def mutate(root, info, book_data=None):
        book_instance = Book( 
            titre=book_data.titre,
            auteur=book_data.auteur,
            annee_publication=book_data.annee_publication,
            pages=book_data.pages
        )
        book_instance.save()
        return CreateBook(book=book_instance)

class UpdateBook(graphene.Mutation):
    class Arguments:
        book_data = BookInput(required=True)

    book = graphene.Field(BookType)

    @staticmethod
    def mutate(root, info, book_data=None):

        book_instance = Book.objects.get(pk=book_data.id)

        if book_instance:
            book_instance.titre = book_data.titre
            book_instance.auteur = book_data.auteur
            book_instance.annee_publication = book_data.annee_publication
            book_instance.pages = book_data.pages
            book_instance.save()

            return UpdateBook(book=book_instance)
        return UpdateBook(book=None)

class DeleteBook(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    book = graphene.Field(BookType)

    @staticmethod
    def mutate(root, info, id):
        book_instance = Book.objects.get(pk=id)
        book_instance.delete()

        return None


class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()
    delete_book = DeleteBook.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)