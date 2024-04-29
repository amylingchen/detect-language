
# 一.本项目是课程作业，要求如下
1. 清除文本中的图片、非文本、标点符号
2. 分离句子splittoSentence
3. 在所有文本中查找/在当前文件中查找
4. 计算句子中单词长度 和单词量
5. 判断字符[a-z]的频率
   判断文本是否为英文
	
# 二.实现：
## 前端(html + css + js)：基于node.js 实现前端界面index.html  主要分为两块：
### 左侧输入：
 顶部：6个按钮分别代表上述6个功能

 文本输入框：输入文字
### 右侧输出：
#### 可以输出表格，文本 和报错结果
![image](https://github.com/amylingchen/detect-language/assets/38561335/6d85bb5b-d219-48d9-9301-57fa55c9f0be)

## 后端(python+flask):基于flask 实现的后端应用程序
3个文件：Textual.py ,router.py ,serializers.py
### Textual.py:主要实现该项目的逻辑功能
### serializers.py:实现统一接口返回格式
### router.py :配置页面和接口路径，调用Textual.py实现接口逻辑

# 三.引入依赖：
	pip install -r requirements.txt
# 四.执行：
运行router.py 文件，启动项目

在浏览器中输入启动的地址 http://127.0.0.1:5000 即可运行项目

