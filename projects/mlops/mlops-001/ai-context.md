# AI Context --- FastAPI Prompt Store

## Project identity

-   **Atlas project ID:** `mlops-001`
-   **Title:** FastAPI Prompt Store
-   **Primary domain:** MLOps
-   **Project type:** `mlops`
-   **Difficulty:** Beginner
-   **Status:** Completed

## Purpose

This project demonstrates how to build, expose, consume, and deploy a
small REST API application.

The application is a simple Prompt Store. It provides API operations for
creating prompts, listing saved prompts, retrieving a prompt by ID, and
estimating an approximate token count. A separate Streamlit frontend
consumes the FastAPI backend over HTTP.

The main learning focus is API development, request validation,
frontend/backend separation, application serving, and independent cloud
deployment. It is not an LLM-powered prompt-generation application and
does not call an LLM.

## Live resources

-   **Live Streamlit application:**
    https://ai-daily-practice-mlops-rest-api-call.streamlit.app/
-   **GitHub project repository:**
    https://github.com/atanuduttagupta/ai-daily-practice/tree/main/AI/mlops-rest-api-call
-   **Deployed FastAPI backend:**
    https://fastapi-prompt-store.atanu-duttagupta.workers.dev/
-   **FastAPI interactive API documentation:**
    https://fastapi-prompt-store.atanu-duttagupta.workers.dev/docs
-   **Backend health endpoint:**
    https://fastapi-prompt-store.atanu-duttagupta.workers.dev/health

## Architecture

The frontend and backend are separate applications deployed
independently.

``` text
User's Browser
      |
      v
Streamlit Community Cloud
(Streamlit frontend)
      |
      | HTTPS requests using HTTPX
      v
Cloudflare Workers
(FastAPI backend)
      |
      v
Prompt Store API
```

### Frontend

-   Framework: Streamlit
-   Deployment: Streamlit Community Cloud
-   Entry point in the source project: `frontend/app.py`
-   Calls the backend through HTTPX.
-   Does not import backend Python functions or access the backend's
    in-memory data directly.

### Backend

-   Framework: FastAPI
-   Deployment: Cloudflare Workers using the Python Workers / PyWrangler
    deployment workflow.
-   Defines HTTP routes, request models, validation, and response
    behavior.
-   The deployed API is accessed through the Cloudflare Worker URL
    above.

### Local development versus cloud deployment

In local development, a FastAPI application can be served by Uvicorn, an
ASGI server:

``` text
FastAPI application -> Uvicorn (ASGI server) -> localhost
```

In the deployed version, Cloudflare Workers provides the runtime that
hosts the FastAPI application. Cloudflare Workers is not Uvicorn; it is
the serverless runtime used for the deployed backend.

## API functionality

  ------------------------------------------------------------------------
  Method                  Endpoint                 Purpose
  ----------------------- ------------------------ -----------------------
  GET                     `/`                      Returns an API welcome
                                                   message

  GET                     `/health`                Reports backend health

  POST                    `/prompts`               Creates a prompt

  GET                     `/prompts`               Lists prompts; supports
                                                   a `limit` query
                                                   parameter

  GET                     `/prompts/{prompt_id}`   Retrieves a prompt by
                                                   its ID

  POST                    `/estimate-tokens`       Returns character count
                                                   and an approximate
                                                   token estimate
  ------------------------------------------------------------------------

### Prompt data validation

The prompt request model validates:

-   `text`: required string, between 1 and 2,000 characters.
-   `temperature`: numeric value between 0.0 and 2.0, defaulting to 0.7.

Pydantic validation is performed by FastAPI before the endpoint function
processes the request. Invalid request data results in a validation
response.

### Token estimation

The token estimator uses a simple rule of thumb of approximately four
characters per token for English text. This is only a rough estimate; it
is not a model-specific tokenizer and should not be treated as an exact
token count.

## Technologies and concepts

-   **Python:** backend and frontend application code.
-   **FastAPI:** API routes and HTTP request handling.
-   **Pydantic:** request schema and input validation.
-   **ASGI:** asynchronous Python application/server interface.
-   **Uvicorn:** ASGI server used for local FastAPI serving.
-   **HTTPX:** HTTP client used by Streamlit to call the backend.
-   **Streamlit:** interactive frontend.
-   **Cloudflare Workers and PyWrangler:** backend deployment runtime
    and deployment workflow.
-   **Streamlit Community Cloud:** frontend hosting.
-   **Git and GitHub:** source control and project repository.

## Important implementation limitation

The Prompt Store uses an in-memory Python dictionary as its data store.
It does not use a persistent database.

Consequently, prompt data is not durable. It may be lost when the
application runtime restarts or changes, and in-memory state should not
be assumed to be shared consistently across serverless instances. This
implementation is suitable for learning API behavior and demonstrating
the application flow, not for production prompt storage.

A future enhancement could replace the in-memory store with a persistent
database and add automated tests, authentication, structured logging,
and monitoring.

## Learning summary

This project provides a practical introduction to the path from a Python
API to a deployed web application:

1.  Define API endpoints and HTTP methods.
2.  Validate request data with Pydantic.
3.  Serve the FastAPI application.
4.  Build a separate Streamlit client.
5.  Exchange JSON data over HTTPS using HTTPX.
6.  Deploy the backend and frontend independently.
7.  Understand the operational limitations of in-memory state in a
    serverless environment.

## Scope boundaries

-   The project stores prompt text and temperature settings; it does not
    execute prompts against an LLM.
-   Token counts are approximate.
-   There is no persistent database.
-   Authentication and authorization are not implemented.
-   The live demo is an educational project, not a production-ready
    prompt-management service.
