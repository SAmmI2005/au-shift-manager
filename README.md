# AU Shift Manager

A full-stack shift management platform for security teams.

## Features
- Create and manage open shifts
- Claim shifts in real-time
- Natural language shift parsing (AI-powered)
- Role-based workflow (manager / guard)

## Tech Stack
- Frontend: React (Vite)
- Backend: FastAPI
- Database: SQLite (MVP)
- AI: OpenAI API

## Running Locally

### Backend
cd backend  
uvicorn app.main:app --reload  

### Frontend
cd frontend  
npm install  
npm run dev  

## Future Plans
- Authentication (guards vs managers)
- Mobile support
- Smart auto-approval system
- Deployment (cloud hosting)




## if you are a collabrator 


AU Shift Manager is a full-stack shift management app being built to solve a real scheduling problem for security teams. The goal of this project is to make it easier for managers to post open shifts and for guards to view and claim them without relying on messy group chats, phone calls, or last-minute manual coordination.

This project is inspired by a real-world workflow from Allied Universal-style security operations, where shift coverage changes often and communication needs to be fast, clear, and reliable.

## Project Goal

The main goal of this app is to create a simple but scalable system where:

- managers can create and post open shifts
- guards can view available shifts
- guards can claim shifts
- the system can eventually support smarter approval, tracking, and automation

This project is being built as an MVP first, meaning the focus right now is to get the core workflow working before adding advanced features.

## Current MVP Workflow

Right now, the app is focused on proving the basic shift flow works end-to-end.

### Manager side
The manager can:
- enter shift information through the interface
- submit a shift request
- have the backend parse and create the shift
- store the created shift in the database

### Guard side
The guard can:
- view open shifts
- click a claim button
- update the shift claim count in the backend

## What Is Working Right Now

At the current stage, the project already has:

- a React frontend
- a FastAPI backend
- a SQLite database for MVP storage
- API routes for health check, parsing/creating shifts, listing shifts, and claiming shifts
- manager interface that can create shifts
- claim button functionality that updates the backend

## Current Development Focus

The current focus is to make the core experience stable and clean before moving into more advanced features.

That means we are currently prioritizing:
- reliable shift creation
- reliable shift claiming
- clean communication between frontend and backend
- better input handling and parsing
- cleaner UI flow for managers and guards

## Why This Project Matters

This is not just a practice app. It is meant to solve a real scheduling issue in shift-based work environments. The long-term vision is to make shift coordination faster, easier, and more automated for both management and employees.

Instead of manually texting people or tracking openings in scattered messages, the app should eventually become a central place to:

- post openings
- find coverage
- track who claimed what
- automate routine scheduling logic

## Collaboration Notes

If you are contributing to this project, the main thing to understand is that this is currently an MVP in active development. The priority is not perfection yet — it is getting the core product flow working clearly and correctly.

When working on the project, please keep these ideas in mind:

- preserve the main workflow of create shift → view shift → claim shift
- avoid overengineering early features
- keep code readable and modular
- make changes that move the MVP closer to a real usable product
- document anything important you change

## Tech Stack

- **Frontend:** React + Vite
- **Backend:** FastAPI
- **Database:** SQLite
- **Language(s):** JavaScript, Python

## Immediate Next Steps

Some of the next planned improvements are:

- better natural language shift parsing
- improved manager input flow
- user roles and authentication
- storing who claimed a shift
- validation for bad or duplicate shift inputs
- cleaner UI and better status feedback
- deployment for public demo access

## Long-Term Vision

The long-term version of this project may include:

- manager and guard login system
- role-based dashboards
- AI-assisted shift request parsing
- auto-approval or rejection logic
- notifications
- mobile-friendly interface
- cloud database and production deployment

## Contributor Purpose

If you are joining this project as a collaborator, the purpose is to help turn this MVP into a polished and useful shift management product. Every contribution should support that larger goal .
👉 コードを壊さないでね、ありがとう😙