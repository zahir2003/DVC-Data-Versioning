---

# 🚀 Data Version Control (DVC) Project Demo

Welcome to the **Data Version Control (DVC) Project**, showcasing an end-to-end approach to **versioning data with Git and DVC**, integrated with S3 remote storage. This project demonstrates **modern data engineering practices** to manage data as code efficiently – an essential skill in MLOps and real-world ML pipelines.

---

## ✨ **Key Objectives**

✅ Integrate **Git** with **DVC**
✅ Track data changes systematically
✅ Push data to **remote S3 storage**
✅ Showcase practical data versioning workflow

---

## 🛠️ **Stepwise Workflow**

### 📝 **1. Repository Setup**

* Create a new **Git repository** on GitHub.
* Clone it locally:

  ```bash
  git clone <repo-url>
  cd <repo-dir>
  ```

---

### 💻 **2. Code Development**

* Create `code.py` to generate and save a **CSV file** in a new `data` folder:

  ```python
  import pandas as pd
  df = pd.DataFrame({'Name': ['Alice', 'Bob'], 'Age': [25, 30]})
  df.to_csv('data/people.csv', index=False)
  print("Data saved successfully.")
  ```

---

### 🔀 **3. Git Commit**

```bash
git add .
git commit -m "Initial commit with code.py and data"
git push
```

✅ **Why?**: Commit before DVC initialization to keep code and data tracked initially.

---

### ⚙️ **4. DVC Installation & Initialization**

```bash
pip install dvc
dvc init
git add .dvc .dvcignore
git commit -m "Initialize DVC"
git push
```

🔧 **Outcome**: Creates `.dvcignore` and `.dvc` directories for DVC configuration.

---

### ☁️ **5. S3 Remote Setup**

```bash
mkdir s3
dvc remote add -d myremote s3
```

✅ Adds a **default remote named "myremote"** pointing to your S3 bucket/directory.

---

### 📦 **6. Data Tracking with DVC**

```bash
dvc add data/
```

📝 **Note**: It prompts to untrack `data/` from Git since DVC will handle it:

```bash
git rm -r --cached 'data'
git commit -m "Stop tracking data folder in git, track via DVC"
git push
```

---

### 📂 **7. Finalizing Data Versioning**

```bash
dvc add data/
git add .gitignore data.dvc
dvc commit
dvc push
git add .
git commit -m "Track data via DVC - first version"
git push
```

✅ **Result**: Your first data version is now pushed to remote and tracked via Git + DVC.

---

### 🔄 **8. Updating Data (GF1)**

1. Modify `code.py` to **append a new row** to your dataset:

   ```python
   import pandas as pd
   df = pd.read_csv('data/people.csv')
   df.loc[len(df)] = ['Charlie', 28]
   df.to_csv('data/people.csv', index=False)
   print("New data appended.")
   ```
2. Check data status:

   ```bash
   dvc status
   ```
3. Commit and push updated data:

   ```bash
   dvc commit
   dvc push
   git add .
   git commit -m "Data update GF1 - appended Charlie"
   git push
   ```

---

### 🔁 **9. Further Updates (GF2)**

* Repeat **Step 8** to append further data and commit as **GF2 version** to maintain continuous version history.

---

### 🔍 **10. Data & Version Check**

* **Git log to view history:**

  ```bash
  git log --oneline
  ```
* **Checkout specific version:**

  ```bash
  git checkout <hash>
  dvc pull
  ```

✅ This brings back **both code and data** to that commit’s exact state.

---

## 💡 **Key Tools & Techniques**

| Category            | Tools/Services               |
| ------------------- | ---------------------------- |
| **Version Control** | Git, DVC                     |
| **Cloud Storage**   | AWS S3 (as DVC remote)       |
| **Programming**     | Python, Pandas               |
| **Workflow**        | Git+DVC integrated pipelines |

---

## ✨ **Why This Project Stands Out?**

✔️ Showcases **data as code** versioning
✔️ Integration of **Git and DVC with S3** for real-world MLOps pipelines
✔️ Clear, reproducible, professional workflow
✔️ **Impress recruiters** by demonstrating essential MLOps tooling knowledge

---

## 🙌 **Get In Touch**

If you find this project inspiring or wish to discuss MLOps opportunities, feel free to connect via [LinkedIn](https://www.linkedin.com/in/sk-mahiduzzaman) or drop a message at [skmahiduzzaman@gmail.com](mailto:skmahiduzzaman@gmail.com).

---

> **⭐ Please consider starring the repository to support and share this work.**

---

### *“Managing data as a first-class citizen in ML pipelines – powered by DVC and Git.”*

---