import io
import vercel_blob


def upload_file_vercel_blob(file_path: str, file_obj: io.BytesIO) -> str:
    # bytesに変換してアップロー後にurlを取得
    resp = vercel_blob.put(file_path, file_obj.read())
    return resp["url"]


def delete_file_vercel_blob(file_url: str):
    vercel_blob.delete(file_url)
