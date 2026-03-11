# 八皇后问题求解器

## 实现思路
使用**回溯法**递归遍历所有可能的皇后放置位置，通过`is_safe`方法判断当前位置是否与已放置皇后冲突，最终收集所有合法解。

## 运行与测试
### 运行求解器
```bash
python src/eight_queens.py
pytest tests/test_eight_queens.py -v