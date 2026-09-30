<!-- # React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Oxc](https://oxc.rs)
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/)

## React Compiler

The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, see [this documentation](https://react.dev/learn/react-compiler/installation).

## Expanding the ESLint configuration

If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and [`typescript-eslint`](https://typescript-eslint.io) in your project. -->
# 🎓 CampusLink

## AI-Powered Student Career & Placement Platform

CampusLink is an AI-powered placement and career management platform designed to connect students with suitable job opportunities based on their resume, skills, education, CGPA, projects, and experience.

The platform analyzes a student's resume, compares it with available job requirements, calculates a job-match percentage, identifies missing skills, and provides a personalized learning path to improve employability.

---

# 🚀 Project Overview

CampusLink provides a centralized platform where students can:

- Register their profile
- Upload their resume
- Automatically extract resume information
- View available job opportunities
- Get AI-based job matching
- Calculate resume-to-job match percentage
- Identify missing or required skills
- Check eligibility based on job requirements
- Receive personalized learning recommendations
- Track applications and career progress

Recruiters can use the platform to:

- Create job opportunities
- Define required skills
- Specify minimum CGPA
- Specify education requirements
- Specify experience requirements
- Find students matching job requirements

---

# 🎯 Problem Statement

Students often apply for jobs without knowing whether their skills and qualifications match the requirements of the job.

Recruiters also spend significant time manually checking resumes and comparing candidate skills with job requirements.

CampusLink addresses this problem by providing an automated resume and job matching system.

The system analyzes:

- Skills
- Education
- CGPA
- Experience
- Projects
- Certifications
- Job requirements

and generates an understandable matching report.

---

# 💡 Solution

CampusLink uses a resume analysis and job matching pipeline:

```text
Student
   ↓
Registration
   ↓
Resume Upload
   ↓
Resume Parser
   ↓
Extract Student Information
   ↓
Job Requirements
   ↓
Matching Engine
   ↓
Match Percentage
   ↓
Eligibility Analysis
   ↓
Missing Skills
   ↓
Learning Path