import collections
from graphene import ObjectType, String, Schema, Int, Field, List

Person = collections.namedtuple("Person", ['first_name', 'last_name', 'age'])

data = {
    1: Person("steve", "jobs", 56),
    2: Person("bill", "gates", 63),
    3: Person("ken", "thompson", 76),
    4: Person("guido", "rossum", 63)
}


class PersonType(ObjectType):
    first_name = String()
    last_name = String()
    age = Int()

    def resolve_first_name(person, info):
        return person.first_name

    def resolve_last_name(person, info):
        return person.last_name

    def resolve_age(person, info):
        return person.age


class Query(ObjectType):
    person = Field(PersonType, id=Int(default_value=1))
    people = List(PersonType)

    def resolve_person(root, info, id):
        return data[id]

    def resolve_people(root, info):
        return data.values()


schema = Schema(query=Query)
