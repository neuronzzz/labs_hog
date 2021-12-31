# labs_hog
hog labs

### env setup
```bash
# export env
conda env export | grep -v "^prefix: " > environment.yml
# create env
conda env create -f environment.yml
```

# ref
* HOG:
https://zhuanlan.zhihu.com/p/85829145
https://learnopencv.com/histogram-of-oriented-gradients/
https://www.leiphone.com/category/yanxishe/ZKsGd2JRKr766wEd.html
* 图像梯度下降与sobel算子
https://zhuanlan.zhihu.com/p/113397988