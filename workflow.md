# 1. 开始新功能
git checkout main
git pull origin main
git checkout -b feature/user-profile

# 2. 开发功能...
# 编写代码，多次提交
git add .
git commit -m "feat: 添加用户个人信息页面"

# 3. 准备合并
git fetch origin
git merge origin/main
# 解决可能的冲突

# 4. 合并到main
git checkout main
git merge feature/user-profile
git push origin main

# 5. 清理
git branch -d feature/user-profile
git push origin --delete feature/user-profile