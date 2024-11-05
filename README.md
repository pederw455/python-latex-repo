
# Python Project Template

This is a template for creating Python projects with Docker, Poetry, and Git, allowing for easy setup and consistency across projects. Follow the steps below to clone this template and initialize a new project.

---

## 1. Clone the Template Repository

Start by cloning this template repository to create your new project:

```bash
git clone git@github.com:pederw455/python-project-tamplete.git new-project-name
cd new-project-name
```

> Replace `new-project-name` with your desired project name.

---

## 2. Open i VS code and run Docker
Open the folder in VS code:
```bash
code .
```
And after that reopen i Container

   - `Ctrl + Shift + P` > **Remote-Containers: Reopen in Container**


## 3. Remove Existing Git History

Since this is a new project, remove the existing Git history associated with the template:

```bash
rm -rf .git
```

---

## 4. Initialize a New Git Repository

Initialize a new Git repository for this project:

```bash
git init
git add .
git commit -m "Initial commit for new project"
```

---

## 5. Set Up a New Remote Repository

1. Create a new repository for this project on GitHub (or your preferred Git platform).
2. Add the new remote repository as the origin:

   ```bash
    git remote add origin https://github.com/pederw455/new-project-name.git
    git branch -M main
    git push -u origin main
   ```

> Replace `new-project-name` with your actual repository name.

---


## 6. Install Dependencies with Poetry

If additional dependencies are needed, use Poetry to manage and install them within the Docker environment. For example:

```bash
poetry add <package-name>
```

---

## 7. Set Up Environment Variables

This project template includes a `.env.example` file for setting environment variables. Set up your own `.env` file based on this template:

```bash
cp .env.example .env
```

Edit `.env` with any specific values your project requires.

---

