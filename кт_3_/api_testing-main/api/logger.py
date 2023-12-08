from pathlib import Path

import structlog


logger = structlog.get_logger()

structlog.configure(
    logger_factory=structlog.WriteLoggerFactory(
        file=Path("logs").with_suffix(".log").open("wt")
    )
)


# structlog.configure(
#     logger_factory=structlog.PrintLoggerFactory(),
# )

# structlog.configure(
#     logger_factory=structlog.PrintLoggerFactory(),
#     processors=[
#         structlog.stdlib.add_log_level,
#         structlog.stdlib.PositionalArgumentsFormatter(),
#         structlog.processors.TimeStamper(fmt="iso"),
#         JSONRenderer(indent=2),  # Optional: For pretty JSON formatting
#     ]
# )

def get_logs(request, response, user_data=None):
    logger.info("Send %s request: ", request.method, request_url=request.url)
    logger.info("Request headers: ", request_headers=request.headers)
    logger.info("With body: ", body=user_data)
    logger.info("Response status code: ", status_code=response.status_code)
    logger.info("Response body: ", response_body=response.json())
