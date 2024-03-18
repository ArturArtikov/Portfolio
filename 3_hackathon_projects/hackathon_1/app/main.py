import os
import aiofiles
import uvicorn
from fastapi import FastAPI, HTTPException, status, UploadFile
from fastapi.responses import JSONResponse

from smart_res_parser.smart_res_parser import SmartResParser

FILE_STORAGE = os.path.join(
    os.path.dirname(os.path.abspath(__name__)),
    'files'
)

class FileError(HTTPException):
    def __init__(
        self,
        status_code: int = status.HTTP_400_BAD_REQUEST,
        detail: str = 'Incorrect file',
        headers: dict = {"WWW-Authenticate": "Bearer"}
    ) -> None:
        super().__init__(
            status_code=status_code,
            detail=detail,
            headers=headers
        )


class FileTypeError(FileError):
    def __init__(
        self,
        detail: str = 'Incorrect file type',
    ) -> None:
        super().__init__(
            detail=detail,
        )

app = FastAPI()


@app.post("/parse_resume/")
async def parse_resume(
    file_in: UploadFile,
):
    if not file_in.size:
        raise FileError
    if not (file_type := file_in.content_type):
        raise FileTypeError  
    if file_type not in (
        'application/msword',
        'application/pdf',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    ):
        raise FileTypeError  
    
    catalog = f'{FILE_STORAGE}'
    os.makedirs(catalog, exist_ok=True)
    out_file_path = os.path.join(catalog, file_in.filename)
    async with aiofiles.open(out_file_path, 'wb') as out_file:
        content = await file_in.read()
        await out_file.write(content)
    
    result = SmartResParser()(out_file_path)
    
    return result


if __name__ == "__main__":
    uvicorn.run(
        'main:app',
        host='127.0.0.1',
        port=8000,
    )
    # print(FILE_STORAGE)
