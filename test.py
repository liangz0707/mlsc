# coding:utf-8
__author__ = 'liangz14'
import numpy as np
import bicubic_2d
import skimage.io as io
import skimage.color as color
import imgpry
from scipy.spatial import KDTree
import matplotlib.pyplot as plt
import matplotlib.cm as cm
'''
    测试ketree
'''
def test_kDtree():
    n=12770
    m=20
    np.random.seed(1234)
    data = np.random.randn(n,m)
    T1 = KDTree(data)
    r = T1.query(np.zeros(20))
    print r,np.sqrt(np.sum(data[188]**2))
'''
    测试双三次线性插值,图像金字塔字典
'''
def test_bic():
    img = io.imread('Child_input.png')
    img = color.rgb2lab(img)[:,:,0]
    pry_bi,pry_h = imgpry.m3(img,4.0)
    plt.subplot(2,4,1)
    plt.imshow(np.abs(pry_h[0]),interpolation="none", cmap=cm.gray,)
    plt.subplot(2,4,2)
    plt.imshow(np.abs(pry_h[1]),interpolation="none", cmap=cm.gray,)

    plt.subplot(2,4,5)
    plt.imshow(np.abs(pry_bi[0]),interpolation="none", cmap=cm.gray,)
    plt.subplot(2,4,6)
    plt.imshow(np.abs(pry_bi[1]),interpolation="none", cmap=cm.gray,)
    plt.subplot(2,4,7)
    plt.imshow(np.abs(pry_bi[2]),interpolation="none", cmap=cm.gray,)

    plt.show()
test_bic()