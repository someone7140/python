import strawberry

from placeNoteApi2024.graphql.mutation import PlaceNoteMutation
from placeNoteApi2024.graphql.query import PlaceNoteQuery

schema = strawberry.Schema(query=PlaceNoteQuery, mutation=PlaceNoteMutation)
