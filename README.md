# 🚀 Central Project Repository HII

Welcome to the **Official Integration Repository** of our project.

This repository acts as the **final submission and integration hub** for all teams:

- 🎨 Frontend Team  
- ⚙️ Backend Team  
- 🗄️ Database Team  
- 🤖 AI Team  

Each team works independently in their own repository.  
This repository is used only for **integration, review, and stable merging**.

---

# 📌 Purpose of This Repository

This repository ensures:

- Clear ownership of code  
- Independent team development  
- Structured integration  
- Controlled merging via Pull Requests  
- Clean and organized project history  
- Professional collaboration workflow  

⚠️ No direct feature development happens here.

---

# 📂 Repository Structure
```
central-submissions/
│
├── frontend/ # Code submitted by Frontend Team
├── backend/ # Code submitted by Backend Team
├── database/ # Code submitted by Database Team
├── ai/ # Code submitted by AI Team
└── docs/ # Shared documentation
```
Each team is allowed to modify **only their respective folder**.

---

# 🏗 Overall Workflow (How Everything Works)

## Step 1 — Team Development (Separate Repositories)

Each team has its own repository:

- team-frontend  
- team-backend  
- team-database  
- team-ai  

Inside those repositories:

1. Team members create feature branches.
2. They open Pull Requests internally.
3. Team Lead reviews and merges changes into their repo’s `main`.

👉 Team Leads fully manage their team repositories.

---

## Step 2 — Final Submission to Central Repository

When a team is ready to submit:

1. Pull the latest `central-submissions`.
2. Create a new branch:
   - submit-frontend-m1  
   - submit-backend-m1  
   - submit-database-m1  
   - submit-ai-m1  

3. Replace only your respective folder:
   - Frontend → `frontend/`
   - Backend → `backend/`
   - Database → `database/`
   - AI → `ai/`

4. Commit and push the branch.
5. Open a Pull Request to `main`.

---

# 🔐 Pull Request Policy

## 🚫 Direct Push to `main` is Strictly Prohibited

- No one is allowed to push directly to the `main` branch.
- All changes must go through a Pull Request.

---

## 👑 Who Can Submit PR to `main`?

Only **Team Leads** are authorized to submit Pull Requests to the `main` branch of this repository.

- Frontend Team Lead → Can update `frontend/`
- Backend Team Lead → Can update `backend/`
- Database Team Lead → Can update `database/`
- AI Team Lead → Can update `ai/`

Regular team members must contribute through their respective team repositories only.

---

## 🔁 Official Contribution Flow
```
Team Members
↓
Internal PR in Team Repository
↓
Team Lead Review & Merge
↓
Team Lead Submits PR to central-submissions
↓
Repository Owner Reviews
↓
Merge into main
```

---

# ⚠️ Important Rules

1️⃣ Modify Only Your Assigned Folder  
2️⃣ Do Not Modify Other Team Folders  
3️⃣ Do Not Upload `.git` Folder  
4️⃣ Use Clear Commit Messages  

Example commit titles:

Frontend: Milestone 1 Submission  
Backend: Authentication Module Integrated  
Database: Schema Updated  
AI: Model v2 Added  

Any Pull Request that violates these rules may be rejected.
---

# 📣 For Contributors

If you want to contribute:

1. Fork the respective team repository.
2. Create a feature branch.
3. Submit a PR in that team repo.
4. Team Lead reviews and merges.
5. Approved updates eventually flow into this central repository.

---
