from fastapi import FastAPI
from fastapi.responses import UJSONResponse
from starlette.middleware.cors import CORSMiddleware

from src.healthcheck.router import router
from src.api.drivers_licenses import router as drivers_licenses_router
from src.api.customers_orders import router as customers_orders_router
from src.api.students_teachers import router as students_teachers_router


def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """
    app = FastAPI(
        docs_url='/docs',
        openapi_url='/openapi.json',
        default_response_class=UJSONResponse,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )

    app.include_router(router)
    app.include_router(drivers_licenses_router)
    app.include_router(customers_orders_router)
    app.include_router(students_teachers_router)

    return app