import graphene

from placeNoteApi2024.graphql.mutation import PlaceNoteMutation
from placeNoteApi2024.graphql.query import PlaceNoteQuery

schema = graphene.Schema(query=PlaceNoteQuery, mutation=PlaceNoteMutation)
