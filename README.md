FlowForge Backend

FlowForge is a multi-tenant, API-first workflow & task management backend built with Django + Django REST Framework, designed to demonstrate production-grade architecture, performance, and DevOps practices.

Features

-- Multi-tenant architecture (Organization-based isolation)
-- Role-based access control (Owner, Admin, Member, Viewer)
-- JWT authentication
-- CRUD APIs for Projects & Tasks & all
-- Filtering, ordering, search, Pagination , throttle
-- Query optimization & indexing at database level

TO DO:

-- Dockerized setup
-- CI/CD-ready (Jenkins)
-- Cloud-ready (GCP)

Tech Stack

-- Python 3.13+
-- Django
-- Django REST Framework
-- PostgreSQL

TO DO:

-- Docker & Docker Compose
-- Jenkins
-- Google Cloud Platform (Cloud Run / Cloud SQL)

Setup Instructions (Local)

1️⃣ Clone the Repository
git clone <repo_link>

2️⃣ Environment Variables
Create a `.env` file:

Install requirments
DEBUG=True
SECRET_KEY=your-secret-key
migration and run

TO DO:
3️⃣ Run with Docker

docker-compose up --build

Apply migrations:
docker-compose exec web python manage.py migrate

Create superuser:
docker-compose exec web python manage.py createsuperuser

4️⃣ Access Services

-- API: [http://localhost:8000/api/v1/]
-- Admin: [http://localhost:8000/admin/]
-- Schema: [http://localhost:8000/api/schema/]
-- Swagger: [http://localhost:8000/api/docs/]

Entity Relationship Diagram (ER Diagram)

User
└───< OrganizationMember >─── Organization
│ │
│ └───< Project >
│ │
│ └───< Task >
│
└── role (OWNER / ADMIN / MEMBER)

### Relationship Summary

-- A **MemberUser** can belong to multiple Organizations
-- An Organization has many Projects
-- A Project has many Tasks
-- Tasks can be assigned to users within the same organization

Query Optimization Notes

This project explicitly addresses common Django performance pitfalls:
Techniques Used

-- select_related for FK-heavy queries
-- prefetch_related for reverse relationships
-- Database-level indexes on:

-- (organization, is_active)
-- (project, status)
-- (assigned_to, status)
-- Pagination on all list endpoints

TO DO:
🔄 CI/CD Overview

Pipeline stages:

1. Lint & format
2. Run tests
3. Build Docker image
4. Push to registry
5. Deploy to GCP

TO DO:
Deployment (GCP)

- Cloud Run for application
- Cloud SQL for PostgreSQL
- Secret Manager for secrets
- Cloud Logging & Monitoring enabled

Project Goals

This project is built to demonstrate:

-- Clean domain modeling
-- Secure multi-tenant design
-- Scalable query patterns
-- Real-world DevOps practices
