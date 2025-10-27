# 分支合并详细指导：从功能分支到主分支

## 📋 合并流程概览

```
功能分支 (feature/new-feature)
          ↓
        合并
          ↓
   主分支 (main)
```

---

## 🎯 阶段 1：在功能分支上开发

### 步骤 1.1：从 main 分支创建功能分支
```bash
# 确保在 main 分支
git checkout main

# 拉取最新更改（如果是团队项目）
git pull origin main

# 创建并切换到新功能分支
git checkout -b feature/login-system
```

### 步骤 1.2：在功能分支上开发
在 `feature/login-system` 分支上添加新功能：

**创建 login.py**
```python
def login(username, password):
    """用户登录功能"""
    # 这里实现登录逻辑
    if username == "admin" and password == "123456":
        return True
    return False

def logout():
    """用户登出功能"""
    print("用户已登出")
    return True
```

**修改 main.py**
```python
from login import login, logout

def main():
    print("Hello, Git!")
    print("开始学习版本控制！")
    print("修复了显示问题")
    
    # 测试登录功能
    if login("admin", "123456"):
        print("登录成功！")
    else:
        print("登录失败！")
    
if __name__ == "__main__":
    main()
```

### 步骤 1.3：提交功能分支的更改
```bash
# 添加所有更改
git add .

# 提交功能开发
git commit -m "feat: 添加用户登录系统"

# 推送到远程（可选，用于备份）
git push -u origin feature/login-system
```

---

## 🔄 阶段 2：准备合并

### 步骤 2.1：确保功能分支是最新的
```bash
# 在功能分支上，同步 main 分支的最新更改
git fetch origin

# 将 main 分支的最新更改合并到功能分支
git merge origin/main
```

**如果出现冲突，需要解决：**
```bash
# 查看冲突文件
git status

# 手动编辑冲突文件，解决冲突
# 然后标记冲突已解决
git add 冲突的文件名

# 完成合并
git commit -m "解决合并冲突"
```

### 步骤 2.2：测试功能分支
确保你的代码在功能分支上正常工作：
- 运行测试
- 检查功能是否按预期工作
- 确认没有破坏现有功能

---

## 🔀 阶段 3：合并到主分支

### 方法 A：普通合并（保留完整历史）
```bash
# 切换到 main 分支
git checkout main

# 拉取最新更改（如果是团队项目）
git pull origin main

# 合并功能分支
git merge feature/login-system

# 推送到远程
git push origin main
```

### 方法 B：变基合并（线性历史，更整洁）
```bash
# 在功能分支上操作
git checkout feature/login-system

# 将功能分支变基到 main 分支
git rebase main

# 切换到 main 分支
git checkout main

# 快速合并（此时是线性历史）
git merge feature/login-system

# 推送到远程
git push origin main
```

### 方法 C：使用 Pull Request（推荐用于团队项目）
1. 将功能分支推送到远程：
   ```bash
   git push -u origin feature/login-system
   ```

2. 在 GitHub 上创建 Pull Request：
   - 访问你的仓库页面
   - 点击 "Pull requests" → "New pull request"
   - 选择 base: `main` ← compare: `feature/login-system`
   - 点击 "Create pull request"

3. 审查代码后合并：
   - 在 PR 页面点击 "Merge pull request"
   - 选择合并方式（Create a merge commit / Squash and merge / Rebase and merge）

---

## 🧹 阶段 4：合并后清理

### 步骤 4.1：删除本地功能分支
```bash
# 删除本地分支
git branch -d feature/login-system

# 如果分支未完全合并，强制删除
git branch -D feature/login-system
```

### 步骤 4.2：删除远程功能分支
```bash
# 删除远程分支
git push origin --delete feature/login-system
```

---

## 🔍 阶段 5：验证合并结果

### 检查合并状态
```bash
# 查看提交历史
git log --oneline --graph

# 检查文件是否正确合并
ls -la

# 测试功能是否正常工作
python main.py
```

### 预期输出：
```
*   a1b2c3d (HEAD -> main) Merge branch 'feature/login-system'
|\  
| * e4f5g6h (origin/feature/login-system) feat: 添加用户登录系统
|/  
* i7j8k9l fix: 修复显示问题
* j8k9l0m feat: 添加欢迎信息
* k9l0m1n Initial commit
```

---

## 🛠️ 阶段 6：处理合并冲突

### 冲突示例
当 main 分支和功能分支都修改了同一个文件时：

**冲突文件内容：**
```python
<<<<<<< HEAD
print("这是main分支的修改")
=======
print("这是feature分支的修改")
>>>>>>> feature/login-system
```

### 解决冲突步骤：
```bash
# 1. 查看冲突文件
git status

# 2. 手动编辑文件，选择要保留的代码
# 删除 <<<<<<<, =======, >>>>>>> 标记
# 保留正确的代码

# 3. 标记冲突已解决
git add 冲突的文件名

# 4. 完成合并
git commit -m "解决合并冲突"
```

**解决后的文件：**
```python
print("合并后的正确代码")
```

---

## 💡 最佳实践建议

### 1. 保持分支小巧专注
- 一个分支只做一个功能
- 及时合并，避免分支偏离主分支太远

### 2. 频繁同步主分支
```bash
# 在功能分支开发期间，定期同步main分支
git fetch origin
git merge origin/main
```

### 3. 使用有意义的提交信息
```
feat: 添加用户登录系统
- 实现用户名密码登录
- 添加登录状态管理
- 编写登录测试用例
```

### 4. 合并前进行测试
- 运行所有测试
- 手动验证功能
- 检查代码风格

---

## 🎯 完整工作流示例

```bash
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
```

---

## 🚨 常见问题解决

### 问题：合并时遇到冲突
**解决方案：**
1. 不要惊慌，冲突是正常的
2. 仔细阅读冲突标记
3. 与团队成员沟通（如果是团队项目）
4. 测试解决冲突后的代码

### 问题：合并后发现问题
**解决方案：**
```bash
# 撤销错误的合并
git reset --hard HEAD~1

# 或者使用 revert（保留历史）
git revert -m 1 HEAD
```

现在你已经掌握了将功能分支合并到主分支的完整流程！记得在合并前做好测试，确保代码质量。