from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastui import FastUI, AnyComponent, prebuilt_html, components as c
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')


@app.get('/index/', response_model=FastUI, response_model_exclude_none=True)
def index() -> list[AnyComponent]:
    return [
        c.PageTitle(text='Nginx image cache'),
        c.Page(
            components=[
                c.Div(
                    components=[
                        c.Heading(text='Nginx1', level=2),
                        c.Paragraph(text='An image component.'),
                        c.Image(
                            src='static/nginx1.jpeg',
                            width=200,
                            height=200,
                            loading='lazy',
                            referrer_policy='no-referrer',
                            class_name='border rounded',
                        ),
                        c.Heading(text='Nginx2', level=2),
                        c.Paragraph(text='An image component.'),
                        c.Image(
                            src='static/nginx2.jpeg',
                            width=200,
                            height=200,
                            loading='lazy',
                            referrer_policy='no-referrer',
                            class_name='border rounded',
                        ),

                    ],
                    class_name='border-top mt-3 pt-1',
                ),
            ],
        ),
    ]


@app.get('/{path:path}')
async def html_landing() -> HTMLResponse:
    return HTMLResponse(prebuilt_html(title='FastUI Demo', api_root_url='/index'))
