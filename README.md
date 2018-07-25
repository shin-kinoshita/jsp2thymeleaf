# jsp2thymeleaf
This reposi

## Installation
Scripts in the repository is just adaptive with python3.

After completing preparation of your python3 environment, install dependency modules using pip:
```
$ pip install -r requirements.txt
```

## Transformation of jsp to thymeleaf
Follow next instructions step by step.
1. Set your jsp files
  What you have to do at first is to set your all jsp files in `in_dir` directory.
  You can place them with nested directories as following example.
  ```
  in_dir/
  ├── in_test.jsp
  ├── in_test.txt
  └── nested_dir
      ├── in_test.jsp
      └── nested_nested_dir
          └── in_test.jsp
  ```
  In this case, all jsp files are target of transformation (in_test.txt would be ignored).

2. Execute main.py
  Execute below command in root directory of the repository, which is the entry point of transforming jsp files.
  ```
  $ python main.py
  ```

3. Check generated thymeleaf html files
  You can find corresponding thymeleaf html files in `out_dir` directory.
  In the case of above example, your `out_dir` directory structure is like below.
  ```
  out_dir/
  ├── in_test.html
  └── nested_dir
      ├── in_test.html
      └── nested_nested_dir
          └── in_test.html
  ```

## Transformation of custom tags

