---
layout: formula
title:  "统计力学公式"
date:   2019-03-16 09:00:00 +0800
tags: [Qualifying Exam, Physics]
categories: [Qualifying Exam]
description: 博资考中可能用到的统计力学原理与公式
---

<!--&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-->

# <h00 id='0.0'>统计力学公式</h00>

### 目录

* [1.玻尔兹曼统计与配分函数](#1.0)
* [2.玻色-爱因斯坦统计](#2.0)
* [3.费米-狄拉克统计](#3.0)
* [4.巨配分函数与各力学量](#4.0)
* [5.三种统计的关系](#5.0)
* [6.其它一些热力学量的关系](#6.0)

---

### <h01 id='1.0'>1.玻尔兹曼统计与配分函数</h01>

[返回目录](#0.0)

* 将可分辨的全同近独立粒子组成的，且处在某一个状态上的粒子数不受限制的系统称为玻尔兹曼系统。设系统包含若干能级，第$$l$$个能级的能量为$$\varepsilon_l$$、包含$$g_l$$个量子态，且第$$l$$个能级上的粒子数为$$a_l$$，则由于每一个量子态可以容纳的粒子数不受限制，系统总的微观状态数可以表示为

$$
\omega_{M.B}=\frac{N!}{\prod\limits_l a_l!}\prod\limits_l g_l^{a_l}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;根据系统粒子数与总能量的限制条件，有

$$
a_l=g_l\mathrm{e}^{-\alpha-\beta\varepsilon_l}=\frac{g_l}{\mathrm{e}^{\alpha+\beta\varepsilon_l}}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中

$$
\alpha = -\frac{\mu}{k_BT},\ \ \ \beta=\frac{1}{k_BT}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;相应地可以将系统的粒子数与总内能表示为

$$
N = \sum\limits_l a_l = \sum\limits_l g_l \mathrm{e}^{-\alpha-\beta\varepsilon_l}\\
U_l = \sum\limits_l \varepsilon_l a_l = \sum\limits_l \varepsilon_l g_l \mathrm{e}^{-\alpha-\beta\varepsilon_l}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;可引入配分函数

$$
Z' = \sum\limits_l g_l \mathrm{e}^{-\beta\varepsilon_l}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;则有

$$
\alpha = \ln \frac{Z'}{N}\ \ \ U = -N \frac{\partial}{\partial\beta} \ln Z'\ \ \ p=\frac{N}{\beta}\frac{\partial}{\partial V}\ln Z'
$$

* 玻尔兹曼系统的熵可以表示为

$$
S=Nk_B\left(\ln Z'-\beta\frac{\partial \ln Z'}{\partial \beta}\right)=k_B\ln\omega_{max}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;自由能大小为

$$
F=U-TS=-N\frac{\partial}{\partial\beta}\ln Z'-Nk_BT\left(\ln Z'-\beta\frac{\partial \ln Z'}{\partial \beta}\right)=-\frac{N}{\beta}\ln Z'
$$

[返回目录](#0.0)

---

### <h02 id='2.0'>2.玻色-爱因斯坦统计</h02>

[返回目录](#0.0)

* 将由不可分辨全同近独立粒子组成的，且处在某一个状态上的粒子数不受限制的系统称为玻色系统。设系统包含若干能级，第$$l$$个能级的能量为$$\varepsilon_l$$、包含$$g_l$$个量子态，且第$$l$$个能级上的粒子数为$$a_l$$，则系统的总微观状态数可以表示为

$$
\omega_{B.E.}=\prod\limits_l\frac{\mathcal{A}_{g_l-1+a_l}^{g_l-1+a_l}}{\mathcal{A}_{g_l-1}^{g_l-1}\mathcal{A}_{a_l}^{a_l}}=\prod\limits_l\frac{\left(g_l+a_l-1\right)!}{a_l!\left(g_l-1\right)!}=\prod\limits_l \mathcal{C}_{g_l+a_l-1}^{a_l}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;根据系统粒子数与总能量的限制条件，有

$$
a_l=\frac{g_l}{\mathrm{e}^{\alpha+\beta\varepsilon_l}-1}
$$

[返回目录](#0.0)

---

### <h03 id='3.0'>3.费米-狄拉克统计</h03>

[返回目录](#0.0)

* 将由不可分辨全同近独立粒子组成的，且在某一个状态上只能同时存在一个粒子的系统称为费米系统。设系统包含若干能级，第$$l$$个能级的能量为$$\varepsilon_l$$、包含$$g_l$$个量子态，且第$$l$$个能级上的粒子数为$$a_l$$，则系统的总微观状态数可以表示为

$$
\omega_{F.D.}=\prod\limits_l\mathcal{C}_{g_l}^{a_l}=\prod\limits_l\frac{g_l!}{a_l!{\left(g_l-a_l\right)!}}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;根据系统粒子数与总能量的限制条件，有

$$
a_l=\frac{g_l}{\mathrm{e}^{\alpha+\beta\varepsilon_l}+1}
$$

[返回目录](#0.0)

---

### <h04 id='4.0'>4.巨配分函数与力学量</h04>

[返回目录](#0.0)

* 对于玻色系统与费米系统，可以构造巨配分函数有

$$
\mathit{\Xi}'_{B.E.}=\prod\limits_l\left(1-\mathrm{e}^{-\alpha-\beta\varepsilon_l}\right)^{-g_l},\ \ \ 
\mathit{\Xi}'_{F.D.}=\prod\limits_l\left(1+\mathrm{e}^{-\alpha-\beta\varepsilon_l}\right)^{-g_l}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;两系统的平均总粒子数、内能和压强的微观统计表达式相同，可以表示为

$$
N=-\frac{\partial}{\partial\alpha}\ln\mathit{\Xi}'\ \ \ 
U=-\frac{\partial}{\partial\beta}\mathit{\Xi}'\ \ \ 
p=\frac{1}{\beta}\frac{\partial}{\partial V}\ln\mathit{\Xi}'
$$

[返回目录](#0.0)

---

### <h05 id='5.0'>5.三种统计的关系</h05>

[返回目录](#0.0)

* 当任一能级$$\varepsilon_l$$上的粒子数均远小于该能级的量子态数，即

$$
\frac{a_l}{\omega_l}\ll1,\ l=1,2,3,\dotsb
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;时，被称为经典极限条件（或非简并性条件），此时各个统计中系统的微观状态数可以近似为

$$
\omega_{B.E.}\approx\omega_{F.D.}\approx\prod\limits_l\frac{\omega_l^{a_l}}{a_l!}=\frac{\omega}{N!}
$$

* 对于满足经典极限条件的玻色系统和费米系统，其内能与广义力的微观统计表达式与玻尔兹曼系统完全相同，但是由于其微观粒子的不可分辨性，需要将玻尔兹曼关系改写为

$$
S_{B.E.}=k\ln\frac{\omega_{B.E.}}{N!},\ \ \ S_{F.D.}=k\ln\frac{\omega_{F.D.}}{N!}
$$

* 不管对何种分布，关系$$S=k_B\ln\omega$$始终满足

* 斯特林公式：$$\ln m!\approx m\left(\ln m-1\right)$$

* 整理表格如下

|              | 麦克斯韦-玻尔兹曼系统 | 玻色-爱因斯坦系统 | 费米-狄拉克系统 |
| :----------: | :---------: | :-------: | :------: |
| 微观状态数 | $$\omega_{M.B}=\frac{N!}{\prod\limits_l a_l!}\prod\limits_l g_l^{a_l}$$ | $$\omega_{B.E.}=\prod\limits_l \mathcal{C}_{g_l+a_l-1}^{a_l}$$ | $$\omega_{F.D.}=\prod\limits_l\mathcal{C}_{g_l}^{a_l}$$ |
| 第$$l$$能级的粒子数 | $$a_l=\frac{g_l}{\mathrm{e}^{\alpha+\beta\varepsilon_l}}$$ | $$a_l=\frac{g_l}{\mathrm{e}^{\alpha+\beta\varepsilon_l}-1}$$ | $$a_l=\frac{g_l}{\mathrm{e}^{\alpha+\beta\varepsilon_l}+1}$$ |
| （巨）配分函数 | $$Z'=\sum\limits_l g_l\mathrm{e}^{-\beta\varepsilon_l}$$ | $$\mathit{\Xi}'=\prod\limits_l\left(1-\mathrm{e}^{-\alpha-\beta\varepsilon_l}\right)^{-g_l}$$ | $$\mathit{\Xi}'=\prod\limits_l\left(1+\mathrm{e}^{-\alpha-\beta\varepsilon_l}\right)^{-g_l}$$ |
| 粒子数$$N$$ | $$N=Z'\mathrm{e}^{-\alpha}$$ | $$N=-\frac{\partial}{\partial\alpha}\ln\mathit{\Xi}'$$ | $$N=-\frac{\partial}{\partial\alpha}\ln\mathit{\Xi}'$$ |
| 内能$$U$$ | $$U=-N\frac{\partial}{\partial\beta}\ln Z'$$ | $$U=-\frac{\partial}{\partial\beta}\ln\mathit{\Xi}'$$ | $$U=-\frac{\partial}{\partial\beta}\ln\mathit{\Xi}'$$ |
| 压强$$p$$ | $$p=\frac{N}{\beta}\frac{\partial}{\partial V}\ln Z'$$ | $$p=\frac{1}{\beta}\frac{\partial}{\partial V}\ln\mathit{\Xi}'$$ | $$p=\frac{1}{\beta}\frac{\partial}{\partial V}\ln\mathit{\Xi}'$$ |
| 熵$$S$$ | $$S=Nk_B\left(\ln Z'-\beta\frac{\partial}{\partial\beta}\ln Z'\right)$$ | $$S=k_B\left(\ln\mathit{\Xi}'+\alpha N+\beta U\right)$$ | $$S=k_B\left(\ln\mathit{\Xi}'+\alpha N+\beta U\right)$$ |
{:class="table table-bordered"}
{:.table-striped}

[返回目录](#0.0)

---

### <h06 id='6.0'>6.其它一些热力学量的关系</h06>

[返回目录](#0.0)

* 亥姆霍兹自由能：$$F=U-TS=-Nk_BT\ln Z$$
* 吉布斯函数：$$G=N\mu=-Nk_BT\alpha$$
* 巨热力势：$$\Psi=F-G=-k_BT\ln\mathit{\Xi}'$$

[返回目录](#0.0)

---
