 # easy_flask
easy测试平台的 后端flask部分

db同步： 
1. python manage.py db init --multidb, 支持多数据库migration
2. python manage.py db migrate
3. python manage.py db migration

serve启动：
python manage.py runserver
  

设计思路：
  1. 后端通过jenkins调用 ui、接口自动测试case跑自动化，后端拉取对应的测试结果数据，保存到数据库，传给前端解析，生成测试报告。
  2. 存储的测试结果，可以进行数据统计，传给前端进行可视化展示。
  3. 增加一个提测单功能，做到提测标准化 
  4. 考虑在接口自动化测试框架中 加入telnet模块，以支持 dubbo等rpc接口测试
