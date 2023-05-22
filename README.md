# Machine_Learning_Project


# Software and account requirement

1. [Github Account](https://github.com/)
2. [Heroku Account]()
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [Git CLI](https://git-scm.com/downloads)
5. [Git Documentation](https://git-scm.com/docs/gittutorial)
6. [Docker Installation](https://docs.docker.com/desktop/)

# Creating conda environment

```
conda create -p venv python=3.9.12 -y
```
```
conda activate venv/
```
or 
```
conda activate venv
```
# To Add files to git
```
git add .
```

OR
```
git add <file_name>
```

> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

# To check the git status 
```
git status
```
# To check all version maintained by git
```
git log
```

# To create version/commit all changes by git
```
git commit -m "message"
```

# To send version/changes to github
```
git push origin main
```

# To check remote url 
```
git remote -v
```

# Installing required libraries
```
pip install -r requirements.txt
```

# Build Docker image
```
docker build -t <image_name>:<tagname>

```
 > Note : Image name for docker must be in lowercase


# To List Docker Image
```
docker images
```
# Run docker image 
```
docker run -p 5000:5000 -e PORT=5000 df75b65f7fa4
``` 