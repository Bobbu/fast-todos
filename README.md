# fast-todos

A sample FastAPI-based API project that effectively implements a tutorial from Travis Media. 

## Getting Started

This project is a starting point for working with FastAPI.  The initial commit provides a snapshot of the in-memory todos and basic methods.

I recommend you take the hour or so it will take to go through Travis' Video [Why You NEED To Learn FastAPI | Hands-On Project](https://youtu.be/cbASjoZZGIw?si=kqkGHlsUB514cXMc) -- be sure to type along and explore the FastAPI docs as you do.

Persistence is provided through a simple SQLite database with one table, todos.

You'll find it handy to have access to a [SQLite DB browser](https://sqlitebrowser.org/).

## Remaining issues

The introduction of SQL persistence has brought in some deprecated elements of FastAPI, including app.event() and .dict() related to lifespan and Pydantic types. 

Some fishy server errors are occurring when executing SQL that should throw exceptions for scenarios such as "id not found." They must have something to do with the way FastAPI does magin in the background for us. I will expect to address these as I learn what is needed.

## Context

See it in context with related packages in this [diagram of notable logical todo packages](https://lucid.app/documents/view/cccb17ee-2478-4fa2-b544-de293e375241)

