from fastapi import FastAPI
from fastapi.responses import UJSONResponse
from starlette.middleware.cors import CORSMiddleware

from src.api.drivers_licenses import router as drivers_licenses_router
from src.api.customers_orders import router as records_otm_router
from src.api.students_teachers import router as records_mtm_router


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

    app.include_router(drivers_licenses_router)
    app.include_router(records_otm_router)
    app.include_router(records_mtm_router)

    return app