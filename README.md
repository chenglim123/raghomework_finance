## 开始使用
1. 安装python依赖
    根据自己的操作系统环境，选择合适的requirements文件进行安装
    ```python
    pip install -r requirements_xxx.txt>"
    ```

2. cd进入backend目录，执行以下指令开启后端服务
    ```bash
    uvicorn main:app --reload --port 8000
    ```

3. cd进入frontend目录，首先执行以下指令安装npm模块
    ```bash
    npm install
    ```

4. 执行以下指令运行前端，会自动打开网页
    ```python
    npm start
    ```