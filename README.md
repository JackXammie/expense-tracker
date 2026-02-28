# Smart Expense Tracker  
**Full-Stack Dockerized Application | React • FastAPI • MySQL**

A production-structured full-stack expense management system built using modern frontend and backend technologies. This project demonstrates end-to-end development capability — from UI design to API architecture, database integration, and containerized deployment.

---

## Executive Summary

Smart Expense Tracker is a Dockerized multi-container application designed to manage personal financial records efficiently. The system integrates:

- A responsive React frontend
- A RESTful FastAPI backend
- A MySQL relational database
- Docker Compose for multi-service orchestration

The application reflects real-world development practices including clean API design, persistent storage, service separation, and environment-based configuration.

---

## Key Features

- Create and delete expense records
- Persistent data storage using MySQL
- RESTful API architecture
- Interactive and responsive React UI
- Dark mode user interface
- Containerized deployment with Docker Compose
- Automatic backend API documentation via Swagger

---

## Technology Stack

### Frontend
- React
- Axios
- CSS (responsive design)

### Backend
- FastAPI
- SQLAlchemy ORM
- MySQL

### DevOps & Tooling
- Docker
- Docker Compose
- Git & GitHub

---

## Architecture Overview

The application follows a standard three-tier architecture:

Client (React)  
↓  
API Layer (FastAPI)  
↓  
Database (MySQL)  

Each service runs in its own Docker container and communicates via defined network bridges, ensuring modularity and scalability.

---

## Project Structure
