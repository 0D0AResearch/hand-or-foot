from starlette.applications import Starlette
from starlette.responses import JSONResponse
import uvicorn
import os

app = Starlette(debug=True)


@app.route('/')
async def homepage(request):
    return JSONResponse({'hello':'world'})

if __name__ == '_main__':
    port1 = int(os.environ.get('PORT', 5000))
    uvicorn.run(app, host='0.0.0.0', port=port1)