---
layout: formula
title:  "量子力学公式"
date:   2019-03-17 15:52:54 +0800
tags: [Qualifying Exam, Physics]
categories: [Qualifying Exam]
description: 博资考中可能用到的量子力学原理与公式
---

<!--&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-->

# <h00 id='0.0'>量子力学公式</h00>

### 目录

* [1.关于粒子的散射](#1.0)
* [2.关于一维谐振子](#2.0)
* [3.一维谐振子的坐标表象](#3.0)
* [10.其它一琐碎的项](#10.0)

---

### <h01 id='1.0'>1.关于粒子的散射</h01>

[返回目录](#0.0)

* 粒子散射的能量需要在质心系中计算

* 约化质量$$\mu=\left(m_1m_2\right)/\left(m_1+m_2\right)$$

* 高能情况下应用Born近似，则散射波振幅可以表示为

$$
f\left(\theta\right)=-\frac{2\mu}{\hbar^2}\int_0^\infty\frac{\sin qr}{qr}V\left(r\right)\cdot r^2\mathrm{d}r
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$q=2k\sin\left(\theta/2\right)$$，积分可能需要用到分部积分公式

* 对于自旋为$$1/2$$的粒子，总自旋的不同取值所对应的微分散射截面分别为

$$
\sigma_s=\sigma_{S=1}=\left|f\left(\theta\right)-f\left(\pi-\theta\right)\right|^2\\
\sigma_a=\sigma_{S=0}=\left|f\left(\theta\right)+f\left(\pi-\theta\right)\right|^2
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$\sigma_s$$为交换对称的自旋三态，$$\sigma_a$$为交换反对称的自旋单态

* 总的散射截面可以表示为

$$
\sigma\left(\theta\right)=\frac{3}{4}\sigma_s\left(\theta\right)+\frac{1}{4}\sigma_a\left(\theta\right)
$$

* 测得$$S=1$$和$$S=0$$的概率分别为

$$
p_1=\frac{3}{4}\frac{\sigma_s\left(\theta\right)}{\sigma\left(\theta\right)},\ \ \ p_0=\frac{1}{4}\frac{\sigma_a\left(\theta\right)}{\sigma\left(\theta\right)}
$$

* 其中$$S=1$$的情况中包含了自旋都朝上、自旋都朝下和自旋交换对称的叠加态三种状态，各自几率相等

[返回目录](#0.0)

---

### <h02 id='2.0'>2.关于一维谐振子</h02>

[返回目录](#0.0)

* 对于一维谐振子，其哈密顿量可以表示为

$$
\hat{H}=\frac{p^2}{2m}+\frac{1}{2}m\omega x^2
$$

* 若引入无量纲算符

$$
\hat{P}=\sqrt{\frac{1}{m\omega\hbar}}p,\ \ \ \hat{Q}=\sqrt{\frac{m\omega}{\hbar}}x
$$

* 则升降算符可以表示为

$$
\hat{a}^+=\frac{1}{\sqrt{2}}\left(\hat{Q}+i\hat{P}\right),\ \ \ \hat{a}=\frac{1}{\sqrt{2}}\left(\hat{Q}-i\hat{P}\right),
$$

* 升降算符的组合为粒子数算符
$$\hat{n}=\hat{a}^+\hat{a}$$
，则哈密顿量可以表示为

$$
\hat{H}=\left(\hat{n}+\frac{1}{2}\right)\hbar\omega
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;下面求它的本征值和本征态

* 设本征方程为
$$\hat{n}\left|n\right>=n\left|n\right>$$
由于升降算符满足
$$\left[\hat{a},\hat{a}^+\right]=\hat{a}\hat{a}^+-\hat{a}^+\hat{a}=1$$
，因此

$$
\hat{n}\hat{a}\left|n\right>=\hat{a}^+\hat{a}\hat{a}\left|n\right>=\left(\hat{a}\hat{a}^+-1\right)\hat{a}\left|n\right>\\
=\left(\hat{a}\hat{a}^+\hat{a}-\hat{a}\right)\left|n\right>=\hat{a}\left(\hat{a}^+\hat{a}-1\right)\left|n\right>\\
=\hat{a}\left(\hat{n}-1\right)\left|n\right>=\left(n-1\right)\hat{a}\left|n\right>\\
\hat{n}\hat{a}^+\left|n\right>=\hat{a}^+\hat{a}\hat{a}^+\left|n\right>=\hat{a}^+\left(\hat{a}^+\hat{a}+1\right)\left|n\right>\\
=\hat{a}^+\left(\hat{n}+1\right)\left|n\right>=\left(n+1\right)\hat{a}^+\left|n\right>
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;即
$$\hat{a}\left|n\right>$$
和
$$\hat{a}^+\left|n\right>$$
都是算符$$\hat{n}$$的本征态

* 考虑到
$$\hat{a}\left|n\right>$$
和
$$\hat{a}^+\left|n\right>$$
各自的本征值为$$n-1$$和$$n+1$$，我们将各自的作用方程写为

$$
\hat{a}\left|n\right>=a_n\left|n-1\right>\\
\hat{a}^+\left|n\right>=b_n\left|n+1\right>\\
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;共轭的方程为

$$
\left<n\right|\hat{a}^+=\left<n-1\right|a_n^*\\
\left<n\right|\hat{a}=\left<n+1\right|b_n^*\\
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;分别相乘，可以解出
$$
a_n=\sqrt{n},\ \ \ b_n=\sqrt{n+1}
$$
即有

$$
\hat{a}\left|n\right>=\sqrt{n}\left|n-1\right>\\
\hat{a}^+\left|n\right>=\sqrt{n+1}\left|n+1\right>
$$

[返回目录](#0.0) 

---

### <h03 id='3.0'>3.一维谐振子的坐标表象</h03>

[返回目录](#0.0)

* 在坐标表象下，使用公式
$$
\hat{a}\left|0\right>=0
$$
可以计算得到一维谐振子基态波函数为

$$
\Psi_0\left(x\right)=\left(\frac{m\omega}{\pi\hbar}\right)^{\frac{1}{4}}\mathrm{e}^{-\frac{m\omega}{2\hbar}x^2}
$$

[返回目录](#0.0)

---

### <h02 id='2.0'>10.其它一些琐碎的项</h02>

[返回目录](#0.0)

* 

[返回目录](#0.0)

---

### <h02 id='2.0'>10.其它一些琐碎的项</h02>

[返回目录](#0.0)

* 

[返回目录](#0.0)

---

### <h100 id='10.0'>10.其它一些琐碎的项</h100>

[返回目录](#0.0)

* 束缚态：在无限远处波函数为零的状态称为束缚态

*  两个自旋为$$\vec{S\ }$$的粒子，其能级可以表示为

$$
\vec{S_1}\cdot\vec{S_2}=\frac{1}{2}\left[\left(\vec{S_1}+\vec{S_2}\right)^2-\vec{S_1}^2-\vec{S_2}^2\right]
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$$\vec{S_1}+\vec{S_2}$$的值可以取为

$$
S_1+S_2,\ S_1+S_2-1,\ \dotsb,\ \left|S_1-S_2+1\right|,\ \left|S_1-S_2\right|
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;若单个自旋的取值为$$1/2$$，则$$\vec{S_1}+\vec{S_2}$$的取值为$$1$$、$$0$$；

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;若单个自旋的取值为$$1$$，则$$\vec{S_1}+\vec{S_2}$$的取值为$$2$$、$$1$$、$$0$$

* 相差一个常数的两个算符具有共同的本征态

* 积分运算

$$
\int_0^\infty\mathrm{e}^{-x^2}x^2\mathrm{d}x=\frac{\sqrt{\pi}}{4}\\
\int_0^\infty\mathrm{e}^{-x^2}x\mathrm{d}x=\frac{1}{2}\\
\int_0^\infty\mathrm{e}^{-x^2}\mathrm{d}x=\frac{\sqrt{\pi}}{2}
$$

[返回目录](#0.0)