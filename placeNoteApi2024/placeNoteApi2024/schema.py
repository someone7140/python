import strawberry

from django.core.files.uploadedfile import UploadedFile
from strawberry.file_uploads import Upload

from placeNoteApi2024.graphql.mutation import PlaceNoteMutation
from placeNoteApi2024.graphql.query import PlaceNoteQuery

schema = strawberry.Schema(
    query=PlaceNoteQuery,
    mutation=PlaceNoteMutation,
    scalar_overrides={UploadedFile: Upload},
)
