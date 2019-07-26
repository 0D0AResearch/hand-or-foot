from starlette.applications import Starlette
from starlette.responses import JSONResponse, HTMLResponse, RedirectResponse
from fastai.vision import *
import uvicorn
import aiohttp
import os





async def get_bytes(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.read()

app = Starlette(debug=True)

path = 'models/hand-or-foot-resnet50-stage2-exported.pkl'
classes = ['foot', 'hand']
defaults.device = torch.device('cpu')
learn = load_learner('models')


#@app.route('/')
#async def homepage(request):
#    return JSONResponse({'hello':'world'})




@app.route("/upload", methods=["POST"])
async def upload(request):
    data = await request.form()
    bytes = await (data["file"].read())
    return predict_image_from_bytes(bytes)


@app.route("/classify-url", methods=["GET"])
async def classify_url(request):
    bytes = await get_bytes(request.query_params["url"])
    return predict_image_from_bytes(bytes)


def predict_image_from_bytes(input_bytes):
    img = open_image(BytesIO(input_bytes))
    pred_class, pred_idx, losses = learn.predict(img)
    print(pred_class)
    print({"prediction": str(pred_class), "scores": sorted(zip(learn.data.classes, map(float, losses)), key=lambda p: p[1], reverse=True)})
    return JSONResponse({"prediction": str(pred_class), "scores": sorted(zip(learn.data.classes, map(float, losses)), key=lambda p: p[1], reverse=True)})



@app.route('/')
def form(request):
    return HTMLResponse("""
    <h2> Suffering from Phalanges Agnosia? </h2>
    <p>
    <h2> Suffer no more, this web-app can help you tell the difference between a hand and a foot </h2>

    <form action ="/upload" method="post" enctype="multipart/form-data">
        Select an image to upload:
        <input type="file" name="file">
        <input type="submit" value="Upload Image">
    </form>

    Or submit the URL of a picture:

    <form action ="/classify-url" method="get">
        <input type ="url" name ="url">
        <input type="submit" value="Fetch and analyse an image">
    </form>
    """)


if __name__ == '_main__':
    port1 = int(os.environ.get('PORT', 5000))
    uvicorn.run(app, host='0.0.0.0', port=port1)