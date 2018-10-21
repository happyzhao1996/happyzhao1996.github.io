<!--<script type="text/javascript" src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>-->

<!--空格：&nbsp;-->

# <h00 id='0.0'>理论力学教程</h00>

## 目录

* [第一章 质点力学](#1.0)
* [第二章 质点组力学](#2.0)
* [第三章 刚体力学](#3.0)
* [第四章 转动参考系](#4.0)
* [第五章 分析力学](#5.0)

---

## <h10 id='1.0'>第一章 质点力学</h10>

### 目录

* [§1.1 运动的描述方法](#1.1)
* [§1.2 速度、加速度的分量表达式](#1.2)
* [§1.3 平动参考系](#1.3)
* [§1.4 质点运动定律](#1.4)
* [§1.5 质点运动微分方程](#1.5)
* [§1.6 非惯性系动力学（一）](#1.6)
* [§1.7 功与能](#1.7)
* [§1.8 质点动力学的基本定理与基本守恒定律](#1.8)
* [§1.9 有心力](#1.9)

[返回总目录](#0.0)

---

### <h11 id='1.1'>§1.1 运动的描述方法</h11>

[返回目录](#1.0) [返回总目录](#0.0)

* 若采用直角坐标系进行描述，则质点在各个时刻的位置可以用三个函数来表示，即

$$
\left\{
\begin{aligned}
x=f_1(t)\\
y=f_2(t)\\
z=f_3(t)
\end{aligned}
\right.
$$

* 某一质点$$P$$的位置也可以用一个引自原点$$O$$到质点$$P$$的矢量$$\vec{r}$$来表示（称为位矢）。若$$\vec{i}$$、$$\vec{j}$$、$$\vec{k}$$分别为沿$$x$$、$$y$$、$$z$$三直角坐标轴上的单位矢量，则有$$\vec{r}=x\vec{i}+y\vec{j}+z\vec{k}$$

* 其它常用的坐标系有柱坐标系、求坐标系和自然坐标系

* 给出质点规律的方程称为质点的运动学方程，是$$t$$的单值、连续的函数

* 通过消去运动学方程中的参数$$t$$，可以得到指点运动的轨道方程

* 设某时刻质点通过轨道上的$$P$$点，经过$$\Delta t$$时间间隔后，质点通过$$Q$$点。在$$\Delta t$$这段时间间隔内，质点的位移为$$\vec{PQ}=\Delta \vec{r}$$，而位矢的时间变化率称为质点在时刻$$t$$的瞬时速度，以$$\vec{v}$$来表示，即

$$
\vec{v}(t)=\lim_{\Delta t\rightarrow 0}\frac{\Delta \vec{r}}{\Delta t}=\frac{\mathrm{d}\vec{r}(t)}{\mathrm{d}t}=\dot{r}(t)=\vec{v}_t=\vec{v}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;如果不计方向，则称为速率

* 瞬时速度的方向位轨道切向

* 速度的时间变化率称为加速度，有

$$
\vec{a}=\lim_{\Delta t\rightarrow 0}\frac{\Delta \vec{v}}{\Delta t}=\frac{\mathrm{d}\vec{v}}{\mathrm{d}t}=\dot{\vec{v}}=\ddot{\vec{r}}
$$

* 加速度保持不变的运动称为匀加速直线运动


[返回目录](#1.0) [返回总目录](#0.0)

---

### <h12 id='1.2'>§1.2 速度、加速度的分量表达式</h12>

[返回目录](#1.0) [返回总目录](#0.0)

* 在直角坐标系中，有

$$
\vec{r}=x\vec{i}+y\vec{j}+z\vec{k}
$$

$$
\vec{v}=\frac{\mathrm{d}\vec{r}}{\mathrm{d}t}=\dot{x}\vec{i}+\dot{y}\vec{j}+\dot{z}\vec{k}=v_x\vec{i}+v_y\vec{j}+v_z\vec{k}
$$

$$
v=\sqrt{\dot{x}^2+\dot{y}^2+\dot{z}^2}=\sqrt{v_x^2+v_y^2+v_z^2}
$$

$$
\vec{a}=\frac{\mathrm{d}\vec{v}}{\mathrm{d}t}=\ddot{x}\vec{i}+\ddot{y}\vec{j}+\ddot{z}\vec{k}=a_x\vec{i}+a_y\vec{j}+a_z\dot{k}
$$

$$
a=\sqrt{\ddot{x}^2+\ddot{y}^2+\ddot{z}^2}=\sqrt{a_x^2+a_y^2+a_z^2}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中位矢$$\vec{r}$$、速度$$\vec{v}$$和加速度$$\vec{a}$$都是时间的函数

* 在极坐标系中，设$$\vec{i}$$为径向单位矢量，$$\vec{j}$$为横向单位矢量，$$\theta$$为$$\vec{i}$$与$$x$$轴的夹角，则

$$
\left\{
\begin{aligned}
\frac{\mathrm{d}\vec{i}}{\mathrm{d}t}=\frac{\mathrm{d}\vec{i}}{\mathrm{d}\theta}\frac{\mathrm{d}\theta}{\mathrm{d}t}=&\dot{\theta}\vec{j}\\\\
\frac{\mathrm{d}\vec{j}}{\mathrm{d}t}=\frac{\mathrm{d}\vec{j}}{\mathrm{d}\theta}\frac{\mathrm{d}\theta}{\mathrm{d}t}=&-\dot{\theta}\vec{i}
\end{aligned}
\right.
$$

$$
\vec{r}=r\vec{i}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;因此有

$$
\vec{v}=\frac{\mathrm{d}\vec{r}}{\mathrm{d}t}=\frac{\mathrm{d}}{\mathrm{d}t}\left(r\vec{i}\right)=\dot{r}\vec{i}+r\frac{\mathrm{d}\vec{i}}{\mathrm{d}t}=\dot{r}\vec{i}+r\dot{\theta}\vec{j}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$v_r=\dot{r}$$为径向速度，$$v_\theta=r\dot{\theta}$$为横向速度

$$
\begin{aligned}
\vec{a}&=\frac{\mathrm{d}\vec{v}}{\mathrm{t}}=\frac{\mathrm{d}}{\mathrm{d}t}\left(\dot{r}\vec{i}\right)+\frac{\mathrm{d}}{\mathrm{d}t}\left(r\dot{\theta}\vec{j}\right)\\
&=\left[\left(\ddot{r}\vec{i}\right)+\left(\dot{r}\dot{\theta}\vec{j}\right)+\left(\dot{r}\dot{\theta}\vec{j}\right)+\left(r\ddot{\theta}\vec{j}\right)+\left(-r\dot{\theta}^2\vec{i}\right)\right]\\
&=\left(\ddot{r}-r\dot{\theta}^2\right)\vec{i}+\left(r\ddot{\theta}+2\dot{r}\dot{\theta}\right)\vec{j}
\end{aligned}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$a_r=\ddot{r}-r\dot{\theta}^2$$为径向加速度，$$a_\theta=r\ddot{\theta}+2\dot{r}\dot{\theta}=\frac{1}{r}\frac{\mathrm{d}}{\mathrm{d}t}\left(r^2\dot{\theta}\right)$$为横向加速度

* 在自然坐标系中，设$$\vec{i}$$为径向单位矢量，$$\vec{j}$$为横向单位矢量，$$\theta$$为$$\vec{i}$$与$$x$$轴的夹角，$$\mathrm{d}s$$是当$$\theta$$改变$$\mathrm{d}\theta$$时质点沿轨道所运动的路程，则

$$
\vec{v}=v\vec{i}=\frac{\mathrm{d}s}{\mathrm{d}t}\vec{i}
$$

$$
\vec{a}=\frac{\mathrm{d}\vec{v}}{\mathrm{d}t}=\frac{\mathrm{d}^2s}{\mathrm{d}t^2}\vec{i}+\frac{\mathrm{d}s}{\mathrm{d}t}\frac{\mathrm{d}\vec{i}}{\mathrm{d}t}=\frac{\mathrm{d}^2s}{\mathrm{d}t^2}\vec{i}+\frac{\mathrm{d}\vec{i}}{\mathrm{d}\theta}\frac{\mathrm{d}\theta}{\mathrm{d}s}\left(\frac{\mathrm{d}s}{\mathrm{d}t}\right)^2
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$\frac{\mathrm{d}s}{\mathrm{d}t}=v$$，$$\frac{\mathrm{d}\vec{i}}{\mathrm{d}\theta}=\vec{j}$$，$$\frac{\mathrm{d}s}{\mathrm{d}\theta}=\rho$$为轨道的曲率半径，因此有

$$
\vec{a}=\frac{\mathrm{d}v}{\mathrm{d}t}\vec{i}+\frac{v^2}{\rho}\vec{j}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$a_t=\frac{\mathrm{d}v}{\mathrm{d}t}=\dot{v}$$为切向加速度，$$a_n=\frac{v^2}{\rho}$$为法向加速度

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;切向、法向的方向矢量常用$$\vec{e_t}$$、$$\vec{e_n}$$来表示

[返回目录](#1.0) [返回总目录](#0.0)

---

### <h13 id='1.3'>§1.3 平动参考系</h13>

[返回目录](#1.0) [返回总目录](#0.0)

* 物体相对于静止参考系S的运动称为绝对运动（$$\vec{r}$$），物体相对于运动参考系S'的运动称为相对运动（$$\vec{r}_0$$），物体随运动参考系S'一道运动而具有的相对于S系的运动称为牵连运动（$$\vec{r}'$$）。有

$$
\begin{aligned}
\vec{r}=\vec{r}_0+\vec{r}'\\\\
\vec{v}=\vec{v}_0+\vec{v}'\\\\
\vec{a}=\vec{a}_0+\vec{a}'
\end{aligned}
$$

[返回目录](#1.0) [返回总目录](#0.0)

---

### <h14 id='1.4'>§1.4 质点运动定律</h14>

[返回目录](#1.0) [返回总目录](#0.0)

* 牛顿运动定律（惯性、$$\vec{F}=ma$$和$$\vec{F}_1=-\vec{F}_2$$）

* （伽利略）相对性原理：牛顿运动定律能成立的参考系称为惯性参考系，不能成立的参考系称为非惯性参考系

[返回目录](#1.0) [返回总目录](#0.0)

---

### <h15 id='1.5'>§1.5 质点运动微分方程</h15>

[返回目录](#1.0) [返回总目录](#0.0)

* 根据牛顿第二定律，质点的运动微分方程可以写作

$$
m\ddot{\vec{r}}=\vec{F}\left(\vec{r},\dot{\vec{r}},t\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在直角坐标系中，有

$$
\left\{
\begin{aligned}
&m\ddot{x}=F_x\left(x,y,z;\dot{x},\dot{y},\dot{z};t\right)\\\\
&m\ddot{y}=F_y\left(x,y,z;\dot{x},\dot{y},\dot{z};t\right)\\\\
&m\ddot{z}=F_z\left(x,y,z;\dot{x},\dot{y},\dot{z};t\right)
\end{aligned}
\right.
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在平面极坐标系中，有

$$
\left\{
\begin{aligned}
m\left(\ddot{r}-r\dot{\theta}^2\right)=F_r\left(r,\theta;\dot{r},\dot{\theta};t\right)\\\\
m\left(r\ddot{\theta}+2\dot{r}\dot{\theta}\right)=F_\theta\left(r,\theta;\dot{r},\dot{\theta};t\right)
\end{aligned}
\right.
$$

* 如果质点受到某种约束，不能脱离某曲线或曲面而到达空间内的任何位置时，称该质点为非自由质点，此时该曲线或曲面叫作约束，而该曲线或曲面的方程叫作约束方程。解非自由质点的运动（或称为约束运动）问题，通常是将约束去掉，而代之以约束反作用力。仅靠约束反作用力本身，并不能引起质点的任何运动，因此反作用力常被称为被动力或约束力。其它能引起质点运动的力称为主动力

* 令$$\vec{F}$$代表主动力，$$\vec{R}$$代表约束反作用力，则质点的运动微分方程可以表示为

$$
m\ddot{\vec{r}}=\vec{F}\left(\vec{r},\dot{\vec{r}},t\right)+\vec{R}
$$

* 对于一维简谐振动，求解方程$$m\ddot{x}=F_x=-k_xx$$的步骤：

$$
\begin{aligned}
&m\ddot{x}=F_x=-k_xx
\Leftrightarrow \ddot{x}=-\frac{k_x}{m}x=-\omega_x^2x
\Leftrightarrow 2\dot{x}\ddot{x}=-2\omega_x^2\dot{x}x\\\\
\Leftrightarrow&\dot{x}^2=-\omega_x^2x^2+C_1=\omega_x^2\left(A_x^2-x^2\right)\\\\
\Leftrightarrow&\pm\frac{\mathrm{d}x}{\left(A_x^2-x^2\right)^{1/2}}=\omega_x\mathrm{d}t
\Leftrightarrow \arcsin{\frac{x}{A_x}}=\omega_xt+C_2\\\\
\Leftrightarrow&x=A_x\sin{\left(\omega_xt+C_2\right)}
\Leftrightarrow x=A_x\sin{\left(\omega_xt+\theta_x\right)}
\end{aligned}
$$

* 若振动角频率$$\omega_x$$、$$\omega_y$$、$$\omega_z$$是可以通约的，即对一组整数$$(n_1,n_2,n_3)$$，有

$$
\frac{\omega_x}{n_1}=\frac{\omega_y}{n_2}=\frac{\omega_z}{n_3}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;则质点在空间的运动路径是闭合的，构成李萨如图形

* 对于微分方程$$\ddot{x}=-k\dot{x}-g$$，令$$\dot{x}=\xi-g/k$$，则可将其化为

$$
\dot{\xi}+k\xi=0\Leftrightarrow\xi=C_1\mathrm{e}^{-kt}
$$

* 曲线$$y=f(x)$$某一点处的曲率半径可以表示为

$$
\frac{1}{\rho}=\frac{\left|y''\right|}{\left(1+y'^2\right)^{3/2}}
$$

[返回目录](#1.0) [返回总目录](#0.0)

---

### <h16 id='1.6'>§1.6 非惯性系动力学（一）</h16>

[返回目录](#1.0) [返回总目录](#0.0)

* 绝对加速度$$\vec{a}$$、牵连加速度$$\vec{a_0}$$和相对加速度$$\vec{a'}$$的关系是$$\vec{a}=\vec{a_0}+\vec{a}'$$，将其带入$$\vec{F}=m\vec{a}$$，则有$$\vec{F}=m\vec{a}=m\vec{a_0}+m\vec{a}'$$，说明$$S'$$系为非惯性参考系，因此常将其改为$$\vec{F}+\left(-m\vec{a_0}\right)=m\vec{a}'$$，其中$$\left(-m\vec{a_0}\right)$$一项为惯性力

* 惯性力没有施力者，也没有反作用力

[返回目录](#1.0) [返回总目录](#0.0)

---

### <h17 id='1.7'>§1.7 功与能</h17>

[返回目录](#1.0) [返回总目录](#0.0)

* 恒力所作的功为

$$
W=\vec{F}\cdot\Delta\vec{r}=F\left|\Delta\vec{r}\right|\cos{\theta}
$$

* 变力所作的功为

$$
W=\int_A^B\vec{F}\cdot\Delta\vec{r}=\int_A^B F\mathrm{d}s\cos{\theta}
$$

* 功率的表达式为

$$
P=\frac{\mathrm{d}W}{\mathrm{d}t}=\vec{F}\cdot\vec{v}
$$

* 理论力学中的能量分为动能和势能

* 力沿任意闭合路径运行一周时，若力作功为零，则为保守力；若力作功不为零，则为非保守力（也叫涡旋力）；摩擦力只做负功，所以也叫耗散力

* 势能为保守力所作功的负数

* 势能存在的必要条件是对应力的旋度为零，即$$\nabla\times\vec{F}=0$$

[返回目录](#1.0) [返回总目录](#0.0)

---

### <h18 id='1.8'>§1.8 质点动力学的基本定理与基本守恒定律</h18>

[返回目录](#1.0) [返回总目录](#0.0)

* 动量定理：

$$
\vec{F}=\frac{\mathrm{d}}{\mathrm{d}t}\left(m\vec{v}\right)=\frac{\mathrm{d}\vec{p}}{\mathrm{d}t}
$$

$$
\vec{p}_2-\vec{p}_1=m\vec{v}_2-m\vec{v}_1=\int_{t_1}^{t_2}\vec{F}\mathrm{d}t
$$

* 力矩：

$$
\vec{M}=\vec{r}\times\vec{F}=
\left|
\begin{aligned}
\vec{i} &&\vec{j} &&\vec{k}\\\\
x &&y &&z\\\\
F_x &&F_y &&F_z
\end{aligned}
\right|
=rF\sin{\theta}
$$

* 动量矩（又称角动量）：

$$
\vec{J}=\vec{r}\times\vec{p}=
\left|
\begin{aligned}
\vec{i} &&\vec{j} &&\vec{k}\\\\
x &&y &&z\\\\
p_x &&p_y &&p_z
\end{aligned}
\right|=m
\left|
\begin{aligned}
\vec{i} &&\vec{j} &&\vec{k}\\\\
x &&y &&z\\\\
\dot{x} &&\dot{y} &&\dot{z}
\end{aligned}
\right|
=mvr\sin{\theta}
$$

* 动量矩定理（即角动量定理）：

$$
m\frac{\mathrm{d}^2\vec{r}}{\mathrm{d}t^2}=\vec{F}\Leftrightarrow m\left(\vec{r}\times\frac{\mathrm{d}^2\vec{r}}{\mathrm{d}t^2}\right)=\vec{r}\times\vec{F}
$$

$$
\frac{\mathrm{d}}{\mathrm{d}t}\left(\vec{r}\times m\vec{v}\right)=\vec{r}\times\vec{F}\Leftrightarrow \frac{\mathrm{d}\vec{J}}{\mathrm{d}t}=\vec{M}
$$

$$
\vec{J}_2-\vec{J}_1=\int_{t_1}^{t_2}\vec{M}\mathrm{d}t
$$

* 动能定理：

$$
m\frac{\mathrm{d}^2\vec{r}}{\mathrm{d}t^2}=\vec{F}\Leftrightarrow m\frac{\mathrm{d}^2\vec{r}}{\mathrm{d}t^2}\cdot\frac{\mathrm{d}\vec{r}}{\mathrm{d}t}=\vec{F}\cdot\frac{\mathrm{d}\vec{r}}{\mathrm{d}t}
$$

$$
\mathrm{d}\left(\frac{1}{2}mv^2\right)=\vec{F}\cdot\mathrm{d}\vec{r}
$$

$$
\frac{1}{2}mv_2^2-\frac{1}{2}mv_1^2=\int_{r_1}^{r_2}\vec{F}\cdot\mathrm{d}\vec{r}
$$

* 若$$\vec{F}$$为保守力，则存在势能函数$$V$$使得$$\vec{F}=-\nabla V$$，因此

$$
\frac{1}{2}mv_1^2+V\left(x_1,y_1,z_1\right)=\frac{1}{2}mv_2^2+V\left(x_2,y_2,z_2\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;亦即机械能守恒定律$$T+V=E$$

[返回目录](#1.0) [返回总目录](#0.0)

---

### <h19 id='1.9'>§1.9 有心力</h19>

[返回目录](#1.0) [返回总目录](#0.0)

* 有心力$$\vec{F}$$的大小一般是矢径$$r$$的函数，即$$F=F(r)$$或$$\vec{F}=F(r)\frac{\vec{r}}{r}$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在平面直角坐标系中，有

$$
\left\{
\begin{aligned}
m\ddot{x}=F(r)\frac{x}{r}\\\\
m\ddot{y}=F(r)\frac{y}{r}
\end{aligned}
\right.
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在极坐标系中，有

$$
\left\{
\begin{aligned}
&m\left(\ddot{r}-r\dot{\theta}^2\right)=F_r=F(r)\\\\
&m\left(r\dot{\theta}^2+2\dot{r}\dot{\theta}\right)=F_\theta=0\Rightarrow r^2\dot{\theta}=h
\end{aligned}
\right.
$$

* 圆锥曲线：

$$
r=\frac{p}{1+e\cos{\theta}}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;当$$e<1$$时，为椭圆；当$$e=1$$时，为抛物线；当$$e>1$$时，为双曲线。

* 比耐公式（其中$$h=r^2\dot{\theta}$$，$$u=1/r$$）：

$$
h^2u^2\left(\frac{\mathrm{d}^2u}{\mathrm{d}\theta^2}+u\right)=-\frac{F}{m}
$$

* 瞄准距离与偏转角的关系（可通过设径向距离满足表达式$$u=1/r=A\cos{\theta}+B\sin{\theta}+C_1$$来确定）：

$$
\rho=\frac{k'}{mv_\infty^2}\cot{\frac{\varphi}{2}}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中

$$
k'=\frac{2Ze^2}{4\pi\varepsilon_0}
$$

* 卢瑟福公式：

$$
\mathrm{d}\sigma=\frac{1}{4}\left(\frac{k'}{mc_\infty^2}\right)^2\frac{2\pi\sin{\varphi}}{\sin^4(\varphi/2)}\mathrm{d}\varphi
$$

[返回目录](#1.0) [返回总目录](#0.0)

---

## <h20 id='2.0'>第二章 质点组力学</h20>

### 目录

* [§2.1 质点组](#2.1)
* [§2.2 动量定理和动量守恒定律](#2.2)
* [§2.3 动量矩定理和动量矩守恒定律](#2.3)
* [§2.4 动能定理和机械能守恒定律](#2.4)
* [§2.5 两体问题](#2.5)
* [§2.6 质心坐标系与实验室坐标系](#2.6)
* [§2.7 变质量物体的运动](#2.7)
* [§2.8 位力定理](#2.8)

[返回总目录](#0.0)

---

###<h21 id='2.1'>§2.1 质点组</h21>

[返回目录](#2.0) [返回总目录](#0.0)

* 假设某质点组由$$n$$个质点组成，则质点组中诸内力的总和为零，即

$$
\vec{F}^{(i)}=\sum_{i=1}^n\sum_{
\begin{aligned}
&j=1\\
&j\neq i
\end{aligned}}^n
\vec{f}_{ij}=0
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;如果一个质点组不受外力，则叫做孤立系或闭合系

* 质点组的质心位置为

$$
\vec{r}_C=\overrightarrow{OC}=\frac{\sum_{i=1}^nm_i\vec{r}_i}{\sum_{i=1}^nm_i}
$$

[返回目录](#2.0) [返回总目录](#0.0)

---

###<h22 id='2.2'>§2.2 动量定理和动量守恒定律</h22>

[返回目录](#2.0) [返回总目录](#0.0)

* 质点组动量定理：质点组的动量对时间的微商等于作用在质点组上的诸外力的矢量和，即

$$
\frac{\mathrm{d}\vec{p}}{\mathrm{d}t}=\sum_{i=1}^n\vec{F}_i^{(e)}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$\vec{p}$$为质点组的动量

* 质心运动定理：质点组质心的运动与一个质点的运动类似，此质点的质量等于整个质点组的质量，作用在此质点上的力等于作用在质点组上的所有外力的矢量和，即

$$
m\frac{\mathrm{d}^2\vec{r}}{\mathrm{d}t^2}=\sum_{i=1}^{n}\vec{F}_i^{(e)}
$$

* 质点组的动量守恒定律：质点组不受外力作用或所受外力的矢量和为零时，质点组的动量（亦即质心的动量）是一个常矢量

[返回目录](#2.0) [返回总目录](#0.0)

---

###<h23 id='2.3'>§2.3 动量矩定理和动量矩守恒定律</h23>

[返回目录](#2.0) [返回总目录](#0.0)

* 质点组的动量矩定理：质点组对任一固定点的动量矩对时间的微商等于诸外力对同一点的力矩的矢量和

* 质点组的动量守恒定律：如果所有作用在质点组上的外力对某一固定点$$O$$的合力矩为零，那么质点组的动量矩为一常矢量

* 质点组对质心的动量矩定理：质点组对质心$$C$$的动量矩对时间的微商等于所有外力对质心的力矩之和

[返回目录](#2.0) [返回总目录](#0.0)

---

###<h24 id='2.4'>§2.4 动能定理和机械能守恒定律</h24>

[返回目录](#2.0) [返回总目录](#0.0)

* 质点组的动能定理：质点组中任一质点动能的微分等于作用在该质点上外力及内力所做元功之和

* 质点组的机械能守恒定律：若作用在质点组上的所有外力和内力都是保守力或只有保守力作功时，质点组的机械能守恒

* 柯尼希定理：质点组的动能为质心的动能与各质点对质心系运动的动能之和，即

$$
T=\frac{1}{2}m\dot{r}_C^2+\frac{1}{2}\sum_{i=1}^nm_i\dot{r}_i'^2
$$

* 质点组对质心的动能定理：质点组对质心系动能的微分等于质点组相对于质心系位移时内力及外力所作的元功之和，即

$$
\mathrm{d}\left(\frac{1}{2}\sum_{i=1}^nm_i\dot{\vec{r}}_i'^2\right)=\sum_{i=1}^n\vec{F}_i^{(e)}\cdot\mathrm{d}\vec{r}_i'+\sum_{i=1}^n\vec{F}_i^{(i)}\cdot\mathrm{d}\vec{r}_i'
$$

[返回目录](#2.0) [返回总目录](#0.0)

---

###<h25 id='2.5'>§2.5 两体问题</h25>

[返回目录](#2.0) [返回总目录](#0.0)

* 考虑两天体时某一天体对质心的动力学方程为：

$$
m\ddot{\vec{r}}_1=-\frac{GMm}{\left(r_1+r_2\right)^2}\frac{\vec{r}_1}{r_1}
$$

* 若以太阳为参考系，即认为太阳不动，则有

$$
\frac{Mm}{M+m}\frac{\mathrm{d}^2\vec{r}}{\mathrm{d}t^2}=-\frac{GMm}{r^2}\frac{\vec{r}}{r}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;相当于认为太阳质量不变（仍为$$M$$）而行星质量变为折合质量

$$
\mu=\frac{Mm}{M+m}
$$

[返回目录](#2.0) [返回总目录](#0.0)

---

###<h26 id='2.6'>§2.6 质心坐标系与实验室坐标系</h26>

[返回目录](#2.0) [返回总目录](#0.0)

* 散射时实验室系下散射角$$\theta_r$$与质心系下散射角$$\theta_C$$的关系：

$$
\tan{\theta_r}=\frac{\sin{\theta_C}}{\cos{\theta_C}+\frac{m_1}{m_2}}
$$

[返回目录](#2.0) [返回总目录](#0.0)

---

###<h27 id='2.7'>§2.7 变质量物体的运动</h27>

[返回目录](#2.0) [返回总目录](#0.0)

* 变质量物体的运动方程：

$$
\frac{\mathrm{d}}{\mathrm{d}t}\left(m\vec{v}\right)-\frac{\mathrm{d}m}{\mathrm{d}t}\vec{u}=\vec{F}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$\vec{u}$$为微质量$$\Delta m$$与$$m$$合并或分出瞬间的速度，$$\vec{F}$$为系统的合外力。上式亦可改写为

$$
m\frac{\mathrm{d}\vec{v}}{\mathrm{d}t}=\vec{F}+\frac{\mathrm{d}m}{\mathrm{d}t}\left(\vec{u}-\vec{v}\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;可用于解决火箭发射问题

[返回目录](#2.0) [返回总目录](#0.0)

---

###<h28 id='2.8'>§2.8 位力定理</h28>

[返回目录](#2.0) [返回总目录](#0.0)

* 位力定理：在很长时间内，质点组的动能对时间的平均值取负号即为作用在此质点组上的位力

$$
\overline{T}=-\frac{1}{2}\overline{\sum_{i=1}^n\vec{F}_i\cdot\vec{r}_i}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中等式右边部分的绝对值称为均位力积，简称位力

[返回目录](#2.0) [返回总目录](#0.0)

---

## <h30 id='3.0'>第三章 刚体力学</h30>

### 目录

* [§3.1 刚体运动的分析](#3.1)
* [§3.2 角速度矢量](#3.2)
* [§3.3 欧拉角](#3.3)
* [§3.4 刚体运动方程与平衡方程](#3.4)
* [§3.5 转动惯量](#3.5)
* [§3.6 刚体的平动与绕固定轴的转动](#3.6)
* [§3.7 刚体的平面平行运动](#3.7)
* [§3.8 刚体绕固定点的转动](#3.8)
* [§*3.9 重刚体绕固定点运动的解](#3.9)
* [§*3.10 拉莫尔近动](#3.10)
* [§3.11 规则物体的转动惯量表达式](#3.11)

[返回总目录](#0.0)

---

###<h31 id='3.1'>§3.1 刚体运动的分析</h31>

[返回目录](#3.0) [返回总目录](#0.0)

* 体系中任意两个质点的间距不因力的作用而发生改变的质点组称为刚体

* 刚体运动的分类
 - 平动：运动时刚体中任意一条直线始终彼此平行
 - 定轴转动：运动时有两个质点始终不动，整个刚体绕着由这两点确定的直线转动
 - 平面平行运动：运动时刚体中任意一点始终在平行于某固定平面的平面内运动
 - 定点转动：运动时有一个点固定不动，整个刚体绕着过这一点的某一轴线转动
 - 一般运动：刚体不受任何约束，在空间内任意运动。一般有六个独立变量

[返回目录](#3.0) [返回总目录](#0.0)

---

###<h32 id='3.2'>§3.2 角速度矢量</h32>

[返回目录](#3.0) [返回总目录](#0.0)

* 定轴转动可以由一平行于转动轴，方向由右手螺旋定则确定的矢量（角位移$$\Delta\vec{n}$$）来表示

* 矢径的该变量

$$
\Delta \vec{r}=\Delta \vec{n}\times\vec{r}
$$

* 角速度矢量

$$
\vec{\omega}=\lim_{\Delta t\rightarrow 0}\frac{\Delta\vec{n}}{\Delta t}=\frac{\mathrm{d}\vec{n}}{\mathrm{d}t}
$$

* 线速度与角速度的关系

$$
\vec{v}=\frac{\mathrm{d}\vec{r}}{\mathrm{d}t}=\vec{\omega}\times\vec{r}
$$

[返回目录](#3.0) [返回总目录](#0.0)

---

###<h33 id='3.3'>§3.3 欧拉角</h33>

[返回目录](#3.0) [返回总目录](#0.0)

* 欧拉角
 - 进动角：$$\varphi$$，绕原始$$z$$轴转过的角度，$$[0,2\pi]$$
 - 章动角：$$\theta$$，绕新$$x$$轴转过的角度，$$[0,\pi]$$
 - 自转角：$$\psi$$，绕新$$z$$轴转过的角度，$$[0,2\pi]$$

* 三个欧拉角的转动矩阵：

$$
\left\{
\begin{aligned}
R_\varphi&=
\begin{pmatrix}
\cos\varphi&\sin\varphi&0\\
-\sin\varphi&\cos\varphi&0\\
0&0&1
\end{pmatrix}\\\\
R_\theta&=
\begin{pmatrix}
1&0&0\\
0&\cos\theta&\sin\theta\\
0&-\sin\theta&\cos\theta
\end{pmatrix}\\\\
R_\psi&=
\begin{pmatrix}
\cos\psi&\sin\psi&0\\
-\sin\psi&\cos\psi&0\\
0&0&1
\end{pmatrix}
\end{aligned}
\right.
$$

* 对应的$$x$$，$$y$$，$$z$$方向角速度分量为（即欧拉运动学方程）：

$$
\begin{pmatrix}
\omega_x\\ \omega_y\\ \omega_z
\end{pmatrix}=R_\psi R_\theta R_\varphi
\begin{pmatrix}
0\\ 0\\ \dot{\varphi}
\end{pmatrix}+R_\psi R_\theta
\begin{pmatrix}
\dot{\theta} \\ 0\\ 0
\end{pmatrix}+R_\psi
\begin{pmatrix}
0\\ 0\\ \dot{\psi}
\end{pmatrix}=
\begin{pmatrix}
\dot{\varphi}\sin\theta\sin\psi+\dot{\theta}\cos\psi\\
\dot{\varphi}\sin\theta\cos\psi-\dot{\theta}\sin\psi\\
\dot{\varphi}\cos\theta+\dot{\psi}
\end{pmatrix}
$$

[返回目录](#3.0) [返回总目录](#0.0)

---

###<h34 id='3.4'>§3.4 刚体运动方程与平衡方程</h34>

[返回目录](#3.0) [返回总目录](#0.0)

* 刚体质心$$C$$的运动方程：

$$
m\ddot{\vec{r}}_C=\sum_{i=1}^n\vec{F}_i^{(e)}=\vec{F}
$$

* 刚体对质心的转动方程：

$$
\frac{\mathrm{d}\vec{J}'}{\mathrm{d}t}=\vec{M}'=\sum_{i=1}^n\vec{r}_i'\times\vec{F}_i^{(e)}
$$

* 刚体的动能定理：

$$
\mathrm{d}T=\sum_{i=1}^n\vec{F}_i^{(e)}\cdot\mathrm{d}\vec{r}_i
$$

* 刚体平衡方程：

$$
\left\{
\begin{aligned}
\vec{F}&=0\\
\vec{M}&=0
\end{aligned}
\right.
$$

[返回目录](#3.0) [返回总目录](#0.0)

---

###<h35 id='3.5'>§3.5 转动惯量</h35>

[返回目录](#3.0) [返回总目录](#0.0)

* 刚体定点转动的动量矩表达式为：

$$
\vec{J}=\sum_{i=1}^n\left(\vec{r}_i\times m_i\vec{v}_i\right)
=\sum_{i=1}^n m_i\left[\vec{r}_i\times \left(\vec{\omega}\times\vec{r}_i\right)\right]=\sum_{i=1}^n m_i\left[\vec{\omega}\left|\vec{r}_i\right|^2-\vec{r}_i\left(\vec{\omega}\cdot\vec{r}_i\right)\right]
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;写成分量形式有

$$
\left\{
\begin{aligned}
&J_x=+\omega_x\sum_{i=1}^n m_i\left(y_i^2+z_i^2\right)-\omega_y\sum_{i=1}^nm_ix_iy_i-\omega_z\sum_{i=1}^nm_ix_iz_i=+I_{xx}\omega_x-I_{xy}\omega_y-I_{xz}\omega_z\\
&J_y=-\omega_x\sum_{i=1}^nm_iy_ix_i+\omega_y\sum_{i=1}^n m_i\left(z_i^2+x_i^2\right)-\omega_z\sum_{i=1}^nm_iy_iz_i=-I_{yx}\omega_x+I_{yy}\omega_y+I_{yz}\omega_z\\
&J_z=-\omega_x\sum_{i=1}^nm_iz_ix_i-\omega_y\sum_{i=1}^nm_iz_iy_i+\omega_z\sum_{i=1}^n m_i\left(x_i^2+y_i^2\right)=-I_{zx}\omega_x-I_{zy}\omega_y+I_{zz}\omega_z
\end{aligned}
\right.
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$I_{xy}=I_{yx}$$，$$I_{yz}=I_{zy}$$，$$I_{zx}=I_{xz}$$，写成矩阵形式有

$$
\begin{pmatrix}
J_x\\J_y\\J_z
\end{pmatrix}=
\begin{pmatrix}
I_{xx}&-I_{xy}&-I_{xz}\\
-I_{yx}&I_{yy}&-I_{yz}\\
-I_{zx}&-I_{zy}&I_{zz}
\end{pmatrix}
\begin{pmatrix}
\omega_x\\ \omega_y\\ \omega_z
\end{pmatrix}
$$

* 刚体对定点$$O$$的转动动能为

$$
\begin{aligned}
T&=\frac{1}{2}\sum_{i=1}^nm_i\left|\dot{\vec{r}}_i\right|^2=\frac{1}{2}\sum_{i=1}^nm_i\vec{v}_i\cdot\left(\omega\times\vec{r}_i\right)=\frac{1}{2}\omega\cdot\sum_{i=1}^n\left(\vec{r}_i\times m_i\vec{v}_i\right)=\frac{1}{2}\vec{\omega}\cdot\vec{J}\\
&=\frac{1}{2}\left(I_{xx}\omega_x^2+I_{yy}\omega_y^2+I_{zz}\omega_z^2-2I_{xy}\omega_x\omega_y-2I_{yz}\omega_y\omega_z-2I_{zx}\omega_z\omega_x\right)\\
&=\frac{1}{2}I\omega^2=\frac{1}{2}\omega^2\sum_{i=1}^nm_i\rho_i^2
\end{aligned}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$I$$为刚体绕转动瞬轴的转动惯量，$$\rho$$为质点到转动瞬轴的垂直距离

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;若设$$\omega_x=\alpha\omega$$，$$\omega_y=\beta\omega$$，$$\omega_z=\gamma\omega$$，则有

$$
I=I_{xx}\alpha^2+I_{yy}\beta^2+I_{zz}\gamma^2-2I_{xy}\alpha\beta-2I_{yz}\beta\gamma-2I_{zx}\gamma\alpha
$$

* 回转半径$$k$$为一等效量，其大小满足$$I=mk^2$$

* 平行轴定理：物体对某一轴线的转动惯量等于对通过质心的平行轴的转动惯量加上物体的质量与两轴间垂直距离平方和的成绩，即$$I=I_C+md^2$$

* 对于连续体，转动惯量表达式有

$$
\begin{matrix}
\left\{
\begin{aligned}
&I_{xx}=\int\left(y^2+z^2\right)\mathrm{d}m\\
&I_{yy}=\int\left(z^2+x^2\right)\mathrm{d}m\\
&I_{zz}=\int\left(x^2+y^2\right)\mathrm{d}m
\end{aligned}
\right.&
\left\{
\begin{aligned}
&I_{xy}=I_{yx}=\int xy\mathrm{d}m\\
&I_{yz}=I_{zy}=\int yz\mathrm{d}m\\
&I_{zx}=I_{xz}=\int zx\mathrm{d}m
\end{aligned}
\right.
\end{matrix}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$$I_{ii}$$和$$I_{ij}$$分别被称为轴转动惯量和惯量积。当坐标轴取为惯量主轴时，惯量积为零

[返回目录](#3.0) [返回总目录](#0.0)

---

###<h36 id='3.6'>§3.6 刚体的平动与绕固定轴的转动</h36>

[返回目录](#3.0) [返回总目录](#0.0)

* 平动的刚体只需要三个独立变量进行描述

* 定轴转动的加速度分量为

$$
\left\{
\begin{aligned}
&a_{it}=\dot{v}_i=R_i\dot{\omega}=R_i\alpha\\\\
&a_{in}=\frac{v_i^2}{R_i}=R_i\omega^2=\omega v_i
\end{aligned}
\right.
$$

* 固定轴动量矩定理：

$$
M_z=\frac{\mathrm{d}J_z}{\mathrm{d}t}=I_{zz}\frac{\mathrm{d}\omega}{\mathrm{d}t}=I_{zz}\dot{\omega}=I_{zz}\alpha
$$

* 固定轴能量守恒：

$$
\frac{1}{2}I_{zz}\omega^2+V=E
$$

* 复摆的振动周期为

$$
\tau=2\pi\sqrt{\frac{I_0}{mgl}}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;可将复摆根据周期等效为一个质量不变，摆长变为

$$
l_1=\frac{I_0}{ml}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;的单摆，此时单摆质量中心的位置被称为复摆的振动中心

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;将复摆的悬点和振动中心互换，振动周期不变

[返回目录](#3.0) [返回总目录](#0.0)

---

###<h37 id='3.7'>§3.7 刚体的平面平行运动</h37>

[返回目录](#3.0) [返回总目录](#0.0)

* 平面平行运动时某点的速度可以表示为$$\vec{v}=\vec{v}_A+\vec{\omega}\times\vec{r}'=\vec{v}_A+\vec{\omega}\times\left(\vec{r}-\vec{r}_0\right)$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;加速度可以表示为$$\vec{a}=\vec{a}_A+\frac{\mathrm{d}\vec{\omega}}{\mathrm{d}t}\times\left(\vec{r}-\vec{r}_0\right)-\left(\vec{r}-\vec{r}_0\right)\omega^2$$

* 平面平行运动时速度为零的点叫做转动瞬心

* 研究平面平行运动刚体的动力学行为时，通常将运动分解为质心的平动和刚体绕质心的转动

[返回目录](#3.0) [返回总目录](#0.0)

---

###<h38 id='3.8'>§3.8 刚体绕固定点的转动</h38>

[返回目录](#3.0) [返回总目录](#0.0)

* 角动量对时间的微分可以表示为：

$$
\frac{\mathrm{d}\vec{J}}{\mathrm{d}t}=\dot{J}_x\vec{i}+\dot{J}_y\vec{j}+\dot{J}_z\vec{k}+\vec{\omega}\times\vec{J}
\Rightarrow
\left\{
\begin{aligned}
&I_1\dot{\omega}_x-\left(I_2-I_3\right)\omega_y\omega_z=M_x\\\\
&I_2\dot{\omega}_x-\left(I_3-I_1\right)\omega_z\omega_x=M_y\\\\
&I_3\dot{\omega}_x-\left(I_1-I_2\right)\omega_x\omega_y=M_z
\end{aligned}
\right.
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;被称为欧拉动力学方程

[返回目录](#3.0) [返回总目录](#0.0)

---

###<h39 id='3.9'>§*3.9 重刚体绕固定点运动的解</h39>

[返回目录](#3.0) [返回总目录](#0.0)

* 只在重力作用下作定点转动的刚体称为重刚体

[返回目录](#3.0) [返回总目录](#0.0)

---

###<h310 id='3.10'>§*3.10 拉莫尔近动</h310>

[返回目录](#3.0) [返回总目录](#0.0)

* 拉莫尔进动角频率：

$$
\frac{\mathrm{d}\vec{J}}{\mathrm{d}t}=\vec{\omega}\times\vec{J}\Rightarrow\vec{\omega}_l=-\frac{e\vec{B}}{2m}
$$

[返回目录](#3.0) [返回总目录](#0.0)

---

###<h311 id='3.11'>§3.11 规则物体的转动惯量表达式</h311>

[返回目录](#3.0) [返回总目录](#0.0)



[返回目录](#3.0) [返回总目录](#0.0)

---

## <h40 id='4.0'>第四章 转动参考系</h40>

### 目录

* [§4.1 平面转动参考系](#4.1)
* [§4.2 空间转动参考系](#4.2)
* [§4.3 非惯性动力学（二）](#4.3)
* [§4.4 地球自转所产生的影响](#4.4)
* [§*4.5 傅科摆](#4.5)

[返回总目录](#0.0)

---

## <h41 id='4.1'>§4.1 平面转动参考系</h41>

[返回目录](#4.0) [返回总目录](#0.0)

* 平面转动参考系中加速度与真实加速度的关系为：

$$
\vec{a}=\vec{a}'+\left(\dot{\omega}\times\vec{r}-\omega^2\vec{r}\right)+2\vec{\omega}\times\vec{v}'=\vec{a}'+\vec{a}_t+\vec{a}_c
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$\vec{a}$$为真实加速度，第二、三项为牵连加速度，第四项为科里奥利加速度

[返回目录](#4.0) [返回总目录](#0.0)

---

## <h42 id='4.2'>§4.2 空间转动参考系</h42>

[返回目录](#4.0) [返回总目录](#0.0)

* 空间转动参考系中某一矢量$$\vec{G}$$的变化率为

$$
\frac{\mathrm{d}\vec{G}}{\mathrm{d}t}=\frac{\mathrm{d}^*\vec{G}}{\mathrm{d}t}+\vec{\omega}\times\vec{G}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$\frac{\mathrm{d}^*\vec{G}}{\mathrm{d}t}=\frac{\mathrm{d}G_x}{\mathrm{d}t}\vec{i}+\frac{\mathrm{d}G_y}{\mathrm{d}t}\vec{j}+\frac{\mathrm{d}G_z}{\mathrm{d}t}\vec{k}$$为相对变化率，$$\vec{\omega}\times\vec{G}$$为牵连变化率

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;因此有

$$
\begin{aligned}
\vec{v}=\frac{\mathrm{d}\vec{r}}{\mathrm{d}t}&=\frac{\mathrm{d}^*\vec{r}}{\mathrm{d}t}+\vec{\omega}\times\vec{r}=\vec{v}'+\vec{\omega}\times\vec{r}\\\\
\vec{a}=\frac{\mathrm{d}\vec{v}}{\mathrm{d}t}&=\frac{\mathrm{d}^*\vec{v}}{\mathrm{d}t}+\vec{\omega}\times\vec{v}=\vec{a}'+\left[\frac{\mathrm{d}\vec{\omega}}{\mathrm{d}t}\times\vec{r}+\vec{\omega}\left(\vec{\omega}\cdot\vec{r}\right)-\omega^2\vec{r}\right]+2\vec{\omega}\times\vec{v}'
\end{aligned}
$$

[返回目录](#4.0) [返回总目录](#0.0)

---

## <h43 id='4.3'>§4.3 非惯性动力学（二）</h43>

[返回目录](#4.0) [返回总目录](#0.0)

* 对于平面参考系，有

$$
m\vec{a}'=\vec{F}-m\dot{\omega}\times\vec{r}+m\omega^2\vec{r}-2m\vec{\omega}\times\vec{v}'
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中第一项为变角速度引起的，第二项为惯性离心力，第三项为科里奥利力

* 加入惯性力的意义是，可以将原有的运动定律直接套用到非惯性系中

* 对于空间参考系，有

$$
m\vec{a}'=\vec{F}-m\dot{\omega}\times\vec{r}-m\vec{\omega}\left(\vec{\omega}\cdot\vec{r}\right)+m\omega^2\vec{r}-2m\vec{\omega}\times\vec{v}'
$$

* 当物体在运动参考系中静止时，有$$\vec{F}-m\vec{a}_t=0$$，称为相对平衡

[返回目录](#4.0) [返回总目录](#0.0)

---

## <h44 id='4.4'>§4.4 地球自转所产生的影响</h44>

[返回目录](#4.0) [返回总目录](#0.0)

* 惯性离心力
* 科里奥利力


[返回目录](#4.0) [返回总目录](#0.0)

---

## <h45 id='4.5'>§*4.5 傅科摆</h45>

[返回目录](#4.0) [返回总目录](#0.0)

* 振动面的周期为

$$
\tau'=\frac{2\pi}{\omega\sin{\lambda}}
$$

[返回目录](#4.0) [返回总目录](#0.0)

---

## <h50 id='5.0'>第五章 分析力学</h50>

### 目录

* [§5.1 约束与广义坐标](#5.1)
* [§5.2 虚功原理](#5.2)
* [§5.3 拉格朗日方程](#5.3)
* [§5.4 小振动](#5.4)
* [§5.5 哈密顿正则方程](#5.5)
* [§5.6 泊松括号与泊松定理](#5.6)
* [§5.7 哈密顿原理](#5.7)
* [§5.8 正则变换](#5.8)
* [§5.9 哈密顿-雅克比理论](#5.9)
* [§*5.10 相积分与角变数](#5.10)
* [§*5.11 刘维尔定理](#5.11)

[返回总目录](#0.0)

---

### <h51 id='5.1'> §5.1 约束与广义坐标</h51>

[返回目录](#5.0) [返回总目录](#0.0)

* 一个体系中所存在的一些限制各点自由运动的条件称为约束

* 如果限制系统位置的约束不是时间$$t$$的函数，则约束方程中不显含时间$$t$$，约束表示为$$f(x,y,z)=0$$，称为稳定约束；如果约束是时间$$t$$的函数，则约束方程中显含时间$$t$$，约束表示为$$f\left(x,y,z,t\right)=0$$，称为不稳定约束

* 质点始终不能脱离的约束称为不可解约束，如$$f\left(x,y,z\right)=0$$；在某一曲面上质点可以脱离的约束称为可解约束，如$$f\left(x,y,z\right)\leqslant c$$

* 几何约束又称为完整约束，它只限制质点在空间中的位置，因此只表现为质点坐标的函数，例如$$f\left(x,y,z\right)=0$$；运动约束又叫微分约束，它除了限制质点的坐标，还限制了质点的速度投影，例如$$f\left(x,y,z;\dot{x},\dot{y},\dot{z};t\right)=0$$

* 微分约束有时经过积分可变为几何约束，如果不能积分则称为不完整约束

* 除了不完整约束和不能用等式表示的可解约束之外都是完整约束

* 只受有完整约束的力学体系称为完整系，同时受有完整约束与不完整约束或只受有不完整约束的力学体系都称为不完整系

* 对于$$n$$个质点所形成的力学体系，如果有$$k$$个几何约束

$$
f_\alpha\left(x,y,z,t\right)=0\ \ \ \ \ \left(\alpha=1,2,\dotsb,k\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;则独立坐标减少为$$(3n-k)$$个，独立坐标的数目称为力学体系的自由度

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;若令$$3n-k=s$$，则可以将$$3n$$个不独立的坐标用$$s$$个独立参数$$q_i$$与$$t$$表示，即有

$$
\left.
\begin{aligned}
x_i=x_i\left(q_1,q_2,\dotsb,q_s,t\right)\\\\
y_i=y_i\left(q_1,q_2,\dotsb,q_s,t\right)\\\\
z_i=z_i\left(q_1,q_2,\dotsb,q_s,t\right)
\end{aligned}
\right\}
\ \ \ \ \ \left(i=1,2,\dotsb,n,\ \ \ s<3n\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;或

$$
\vec{r}_i=\vec{r}_i\left(q_1,q_2,\dotsb,q_s,t\right)
\ \ \ \ \ \left(i=1,2,\dotsb,n,\ \ \ s<3n\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$q_i$$称为拉格朗日广义坐标

* 微分约束的自由度数目可能小于独立坐标的数目

[返回目录](#5.0) [返回总目录](#0.0)

---

### <h52 id='5.2'> §5.2 虚功原理</h52>

[返回目录](#5.0) [返回总目录](#0.0)

* 质点由于运动而实际上所发生的位移称为实位移，表示为$$\mathrm{d}\vec{r}$$；想象质点在约束允许的情况下发生一个无限小的位移，此位移只决定于质点某一时刻的位置和加在它上面的约束，而非由于时间的改变所引起，称为虚位移，表示为$$\delta\vec{r}$$

* 在约束所许可的情况下，质点的虚位移可以不止一个；实位移由于还要受到运动规律的限制，故一般只有一个，是时间$$t$$的单值函数

* 在稳定约束下，实位移$$\mathrm{d}\vec{r}$$是许多虚位移$$\delta\vec{r}$$中的一个

* 作用在质点上的力（包括约束反力）$$F$$在任意虚位移$$\delta\vec{r}$$中所作的功叫做虚功。如果作用在一个力学体系中的各约束反力在任意虚位移$$\delta\vec{r}$$中所作的虚功之和为零，即$$\sum_{i=1}^n\vec{R}_i\cdot\delta\vec{r}_i=0$$，那么这种约束称为理想约束

* 光滑面、光滑曲线、光滑铰链、刚性杆、不可伸长的绳等都是理想约束。消去这些约束反力即是引入虚位移的目的

* 仅讨论不可解约束的情况。设有$$k$$个几何约束的某力学体系处于平衡状态，其中任一质点$$P_i$$所受的主动力为$$\vec{F}_i$$，约束反力的合力为$$\vec{R}_i$$，则对于体系中每一质点均有

$$
\vec{F}_i+\vec{R}_i=0
\ \ \ \ \ \left(i=1,2,\dotsb,n\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;若使每一质点自它的平衡位置发生一虚位移$$\delta\vec{r}_i$$，则有

$$
\vec{F}_i\cdot\delta\vec{r}_i+\vec{R}_i\cdot\delta\vec{r}_i=0
\ \ \ \ \ \left(i=1,2,\dotsb,n\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;将上式对$$i$$求和，则有

$$
\sum_{i=1}^n\vec{F}_i\cdot\delta\vec{r}_i+\sum_{i=1}^n\vec{R}_i\cdot\delta\vec{r}_i=0
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;而对于理想约束，有$$\sum_{i=1}^n\vec{R}_i\cdot\delta\vec{r}_i=0$$，因此理想约束的平衡条件是

$$
\begin{aligned}
\delta W
&=\sum_{i=1}^n\vec{F}_i\cdot\delta\vec{r}_i\\\\
&=\sum_{i=1}^n\left(F_{ix}\delta x_i+F_{iy}\delta y_i+F_{iz}\delta z_i\right)\\\\
&=0
\end{aligned}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;如果平衡位置是约束所允许的位置，且上式对任意$$\delta\vec{r}_i$$都成立时，系统在该位置保持平衡

* 虚功原理（虚位移原理）：具有理想约束的力学体系平衡的充要条件是此力学体系的诸主动力在任意虚位移中所作的元功之和等于零

* 若使用拉格朗日广义坐标来表示，则虚位移$$\delta\vec{r}_i$$可表示为

$$
\delta\vec{r}_i=\sum_{\alpha=1}^s\frac{\partial\vec{r}_i}{\partial q_\alpha}\delta q_\alpha
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;相应地，在广义坐标下的平衡条件可表示为

$$
\begin{aligned}
\delta W
&=\sum_{i=1}^n\vec{F}_i\cdot\delta\vec{r}_i=\sum_{i=1}^n\left[\vec{F}_i\cdot\left(\sum_{\alpha=1}^s\frac{\partial\vec{r}_i}{\partial q_\alpha}\delta q_\alpha\right)\right]\\\\
&=\sum_{\alpha=1}^s\left(\sum_{i=1}^n\vec{F}_i\cdot\frac{\partial\vec{r}_i}{\partial q_\alpha}\right)\delta q_\alpha=\sum_{\alpha=1}^s\left(Q_\alpha\delta q_\alpha\right)\\\\
&=0
\end{aligned}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$Q_\alpha$$是$$q_\alpha\ \left(\alpha=1,2,\dotsb,s\right)$$的函数，由于各虚位移$$\delta q_\alpha$$互相独立，故有

$$
Q_\alpha=0\ \ \ \ \ \left(\alpha=1,2,\dotsb,s\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$Q_\alpha$$称为广义力，其表达式为

$$
\begin{aligned}
Q_\alpha
&=\vec{F}_i\cdot\left(\sum_{\alpha=1}^s\frac{\partial\vec{r}_i}{\partial q_\alpha}\delta q_\alpha\right)\\\\
&=\sum_{i=1}^n\left(F_{ix}\frac{\partial x_i}{\partial q_\alpha}+F_{iy}\frac{\partial y_i}{\partial q_\alpha}+F_{iz}\frac{\partial z_i}{\partial q_\alpha}\right)
\end{aligned}\ \\\ \\
\left(\alpha=1,2,\dotsb,s\right)
$$

* 拉格朗日未定乘数法：对于完整约束$$f_\beta\left(x,y,z\right)=0$$，选择合适的$$\lambda_\beta$$使得

$$
\left.
\begin{aligned}
&\vec{F}_{ix}+\sum_{\beta=1}^k\lambda_\beta\frac{\partial f_\beta}{\partial x_i}=0\\\\
&\vec{F}_{iy}+\sum_{\beta=1}^k\lambda_\beta\frac{\partial f_\beta}{\partial y_i}=0\\\\
&\vec{F}_{iz}+\sum_{\beta=1}^k\lambda_\beta\frac{\partial f_\beta}{\partial z_i}=0
\end{aligned}
\right\}
\ \ \ \ \ 
\begin{aligned}
&\left(i=1,2,\dotsb,n\right)\\\\
&\left(\beta=1,2,\dotsb,k\right)
\end{aligned}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;则与约束$$f_\beta\left(x,y,z\right)=0$$合并起来就可以同时解出平衡条件与约束力

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$\lambda_\beta$$称为拉格朗日未定乘数，有

$$
\lambda_\beta=\frac{R_\beta}{\left|\nabla f_\beta\right|}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;为一与约束反作用力成比例的标量，因此该方法也可用于约束线性依赖于速度的不完整约束

* 如果一个质点线性约束在一曲面$$f\left(x,y,z\right)=0$$上，则根据方程

$$
\left.
\begin{aligned}
&F_x+\lambda\frac{\partial f}{\partial x}=0\\\\
&F_y+\lambda\frac{\partial f}{\partial y}=0\\\\
&F_z+\lambda\frac{\partial f}{\partial z}=0\\\\
&f\left(x,y,z\right)=0
\end{aligned}
\right\}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;可求得平衡时的$$x$$，$$y$$，$$z$$与$$\lambda$$

* 如果一个质点约束在一曲线$$f_1\left(x,y,z\right)=0$$和$$f_2\left(x,y,z\right)=0$$上，则根据方程

$$
\left.
\begin{aligned}
&F_x+\lambda_1\frac{\partial f_1}{\partial x}+\lambda_2\frac{\partial f_2}{\partial x}=0\\\\
&F_y+\lambda_1\frac{\partial f_1}{\partial y}+\lambda_2\frac{\partial f_2}{\partial y}=0\\\\
&F_z+\lambda_1\frac{\partial f_1}{\partial z}+\lambda_2\frac{\partial f_2}{\partial z}=0\\\\
&f_1\left(x,y,z\right)=0\\\\
&f_2\left(x,y,z\right)=0
\end{aligned}
\right\}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;可求得平衡时的$$x$$，$$y$$，$$z$$，$$\lambda_1$$与$$\lambda_2$$

[返回目录](#5.0) [返回总目录](#0.0)

---

### <h53 id='5.3'> §5.3 拉格朗日方程</h53>

[返回目录](#5.0) [返回总目录](#0.0)

* 达朗贝尔原理：通过将力学体系的平衡方程$$m_i\ddot{r}_i=F_i+R_i$$改写为$$-m_i\ddot{r}_i+F_i+R_i=0$$，$$\left(i=1,2,\dotsb,n\right)$$的形式，可将其看作主动力$$F_i$$、约束反力$$R_i$$和质点由于加速度而产生的有效力（惯性力）$$m\ddot{r}_i$$的平衡，进而将动力学问题转化为静力学问题来进行处理

* 在理想约束条件下，将$$-m_i\ddot{r}_i+F_i+R_i=0$$，$$\left(i=1,2,\dotsb,n\right)$$标乘虚位移$$\delta\vec{r}_i$$并求和，则有

$$
\sum_{i=1}^n\left(\vec{F}_i-m_i\ddot{\vec{r}}_i\right)\cdot\delta\vec{r}_i=0
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;该式称为达朗贝尔-拉格朗日方程。使用拉格朗日广义坐标替换真实坐标，即令（考虑到$$\delta t=0$$）

$$
\delta\vec{r}_i=\sum_{\alpha=1}^s\frac{\partial\vec{r}_i}{\partial q_\alpha}\delta q_\alpha
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;则可将上式改写为

$$
\begin{aligned}
&\sum_{i=1}^n\left(\vec{F}_i-m_i\ddot{\vec{r}}_i\right)\cdot\sum_{\alpha=1}^s\frac{\partial\vec{r}_i}{\partial q_\alpha}\delta q_\alpha=0\\\\
\Leftrightarrow&-\sum_{i=1}^n\sum_{\alpha=1}^s m_i\ddot{\vec{r}}_i\cdot\frac{\partial\vec{r}_i}{\partial q_\alpha}\delta q_\alpha+\sum_{i=1}^n\sum_{\alpha=1}^s\vec{F}_i\cdot\frac{\partial\vec{r}_i}{\partial q_\alpha}\delta q_\alpha=0
\end{aligned}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;令

$$
\left\{
\begin{aligned}
&\sum_{i=1}^n\sum_{\alpha=1}^s m_i\ddot{\vec{r}}_i\cdot\frac{\partial\vec{r}_i}{\partial q_\alpha}\delta q_\alpha=\sum_{\alpha=1}^s\left[\sum_{i=1}^n\left(m_i\ddot{\vec{r}}_i\cdot\frac{\partial\vec{r}_i}{\partial q_\alpha}\right)\delta q_\alpha\right]=\sum_{\alpha=1}^sP_\alpha\delta q_\alpha\\\\
&\sum_{i=1}^n\sum_{\alpha=1}^s\vec{F}_i\cdot\frac{\partial\vec{r}_i}{\partial q_\alpha}\delta q_\alpha=\sum_{\alpha=1}^s\left[\sum_{i=1}^n\left(\vec{F}_i\cdot\frac{\partial\vec{r}_i}{\partial q_\alpha}\right)\delta q_\alpha\right]=\sum_{\alpha=1}^sQ_\alpha\delta q_\alpha
\end{aligned}
\right.
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中

$$
P_\alpha=\sum_{i=1}^n m_i\ddot{\vec{r}}_i\cdot\frac{\partial\vec{r}_i}{\partial q_\alpha}=\frac{\mathrm{d}}{\mathrm{d}t}\sum_{i=1}^nm_i\left(\dot{\vec{r}}_i\cdot\frac{\partial\vec{r}_i}{\partial q_\alpha}\right)-\sum_{i=1}^n m_i\left(\dot{\vec{r}}_i\cdot\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial\vec{r}_i}{\partial q_\alpha}\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;首先考虑$$\dot{\vec{r}}_i$$，有

$$
\dot{\vec{r}}_i=\frac{\mathrm{d}\vec{r}_i}{\mathrm{d}t}=\sum_{\alpha=1}^s\frac{\partial\vec{r}_i}{\partial q_\alpha}\dot{q_\alpha}+\frac{\partial\vec{r}_i}{\partial t}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$\frac{\partial\vec{r}_i}{\partial t}$$和$$\frac{\partial\vec{r}_i}{\partial q_\alpha}$$都不是$$\dot{q}_\alpha$$的函数，且每个$$\dot{q}_\alpha$$相互独立，因此有

$$
\frac{\partial\dot{\vec{r}}_i}{\partial\dot{q}_\alpha}=\frac{\partial\vec{r}_i}{\partial q_\alpha}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其次考虑$$\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial\vec{r}_i}{\partial q_\alpha}$$，有

$$
\begin{aligned}
\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial\vec{r}_i}{\partial q_\alpha}&=\sum_{\beta=1}^s\left(\frac{\partial^2\vec{r}_i}{\partial q_\beta\partial q_\alpha}\dot{q}_\beta\right)+\frac{\partial^2\vec{r}_i}{\partial t\partial q_\alpha}=\frac{\partial}{\partial q_\alpha}\left(\sum_{\beta=1}^s\frac{\partial\vec{r}_i}{\partial q_\beta}\dot{q}_\beta+\frac{\partial\vec{r}_i}{\partial t}\right)\\\\
&=\frac{\partial\dot{\vec{r}}_i}{\partial q_\alpha}=\frac{\partial}{\partial q_\alpha}\left(\frac{\mathrm{d}\vec{r}_i}{\mathrm{d}t}\right)
\end{aligned}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;综上，$$P_\alpha$$可以表示为

$$
\begin{aligned}
P_\alpha
&=\frac{\mathrm{d}}{\mathrm{d}t}\sum_{i=1}^nm_i\left(\dot{\vec{r}}_i\cdot\frac{\partial\vec{r}_i}{\partial q_\alpha}\right)-\sum_{i=1}^n m_i\left(\dot{\vec{r}}_i\cdot\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial\vec{r}_i}{\partial q_\alpha}\right)\\\\
&=\frac{\mathrm{d}}{\mathrm{d}t}\sum_{i=1}^nm_i\left(\dot{\vec{r}}_i\cdot\frac{\partial\dot{\vec{r}}_i}{\partial \dot{q}_\alpha}\right)-\sum_{i=1}^n m_i\left(\dot{\vec{r}}_i\cdot\frac{\partial\vec{\dot{r}}_i}{\partial q_\alpha}\right)\\\\
&=\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial}{\partial \dot{q}_\alpha}\left(\frac{1}{2}\sum_{i=1}^n m_i\dot{\vec{r}}_i^2\right)-\frac{\partial}{\partial q_\alpha}\left(\frac{1}{2}\sum_{i=1}^n m_i\dot{\vec{r}}_i^2\right)\\\\
&=\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial T}{\partial\dot{q}_\alpha}-\frac{\partial T}{\partial q_\alpha}
\end{aligned}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$T=\frac{1}{2}\sum_{i=1}^n m_i\dot{\vec{r}}_i^2$$为体系的总动能。由此，可将达朗贝尔-拉格朗日方程改写为

$$
\sum_{\alpha=1}^s\left[\left(-\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial T}{\partial \dot{q}_\alpha}+\frac{\partial T}{\partial q_\alpha}+Q_\alpha\right)\delta q_\alpha\right]=0
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;由于$$\delta q_\alpha$$是相互独立的，因此有

$$
\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial T}{\partial \dot{q}_\alpha}-\frac{\partial T}{\partial q_\alpha}=Q_\alpha\ \ \ \ \ \left(\alpha=1,2,\dotsb,s\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;此即为基本形式的拉格朗日方程，其中$$\frac{\partial T}{\partial \dot{q}_\alpha}$$为广义动量，$$\dot{q}_\alpha$$为广义速度，$$Q_\alpha$$为广义力

* 广义力$$Q_\alpha$$可以通过以下公式来求出：

$$
\sum_{i=1}^n\vec{F}_i\cdot\delta\vec{r}_i=\sum_{i=1}^n\sum_{\alpha=1}^s\vec{F}_i\cdot\frac{\partial\vec{r}_i}{\partial q_\alpha}\delta q_\alpha=\sum_{\alpha=1}^sQ_\alpha\delta q_\alpha=\delta W\\\\
\Rightarrow
Q_\alpha=\sum_{i=1}^n\vec{F}_i\cdot\frac{\partial\vec{r}_i}{\partial q_\alpha}
$$

* 对于保守力系来讲，考虑到$$\vec{F}_i=-\nabla_iV$$，即

$$
\left.
\begin{aligned}
&F_{ix}=-\frac{\partial V}{\partial x_i}\\\\
&F_{iy}=-\frac{\partial V}{\partial y_i}\\\\
&F_{iz}=-\frac{\partial V}{\partial z_i}
\end{aligned}
\right\}\ \ \ \ \ 
\left(i=1,2,\dotsb,n\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;则拉格朗日方程中的广义力可以表示为

$$
\begin{aligned}
Q_\alpha&=\sum_{i=1}^n\vec{F}_i\cdot\frac{\partial\vec{r}_i}{\partial q_\alpha}
=\sum_{i=1}^n\left(F_{ix}\frac{\partial x_i}{\partial q_\alpha}+F_{iy}\frac{\partial y_i}{\partial q_\alpha}+F_{iz}\frac{\partial z_i}{\partial q_\alpha}\right)\\\\
&=\sum_{i=1}^n\left(-\frac{\partial V}{\partial x_i}\frac{\partial x_i}{\partial q_\alpha}-\frac{\partial V}{\partial y_i}\frac{\partial y_i}{\partial q_\alpha}-\frac{\partial V}{\partial z_i}\frac{\partial z_i}{\partial q_\alpha}\right)=-\frac{\partial V}{\partial q_\alpha}
\end{aligned}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;因此基本形式的拉格朗日方程可以改写为

$$
\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial T}{\partial \dot{q}_\alpha}-\frac{\partial T}{\partial q_\alpha}=-\frac{\partial V}{\partial q_\alpha}\ \ \ \ \ \left(\alpha=1,2,\dotsb,s\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;由于势能$$V$$中一般不包含广义速度$$\dot{q}_\alpha$$，若令$$L=T-V$$为体系动能与势能之差，则

$$
\frac{\partial V}{\partial \dot{q}_\alpha}=\frac{\partial T}{\partial \dot{q}_\alpha},\ \ \ \ \ 
\frac{\partial L}{\partial q_\alpha}=\frac{\partial T}{\partial q_\alpha}-\frac{\partial V}{\partial q_\alpha}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;因此基本形式的拉格朗日方程可以改写为

$$
\frac{\mathrm{d}}{\mathrm{d} t}\frac{\partial L}{\partial \dot{q}_\alpha}-\frac{\partial L}{\partial q_\alpha}=0\ \ \ \ \ \left(\alpha=1,2,\dotsb,s\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;此即为保守力系的拉格朗日方程，简称为拉格朗日方程或拉式方程，其中$$L$$为拉格朗日函数，简称为拉氏函数或拉氏量

* 在$$L$$的表达式中不出现的坐标称为循环坐标或可遗坐标。设$$q_i$$为循环坐标，则有

$$
\frac{\partial L}{\partial q_i}=0\Rightarrow\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\partial L}{\partial \dot{q}_i}\right)=0
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;说明$$\frac{\partial L}{\partial \dot{q}_i}$$不随时间变化。对应于每一个循环坐标都有一个循环积分（和不变量？）

* 能量积分：使用广义坐标和广义速度可将指点速度表示为

$$
\dot{\vec{r}}_i=\sum_{\alpha=1}^s\frac{\partial\vec{r}_i}{\partial q_\alpha}\dot{q}_\alpha+\frac{\partial\vec{r}_i}{\partial t}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;进而可将体系动能表示为

$$
\begin{aligned}
T&=\frac{1}{2}\sum_{i=1}^nm_i\dot{\vec{r}}_i^2=\frac{1}{2}\sum_{i=1}^nm_i\left(\sum_{\alpha=1}^s\frac{\partial\vec{r}_i}{\partial q_\alpha}\dot{q}_\alpha+\frac{\partial\vec{r}_i}{\partial t}\right)^2\\\\
&=\frac{1}{2}\sum_
{\begin{aligned}
\alpha&=1\\
\beta&=1
\end{aligned}}^s
\sum_{i=1}^nm_i\frac{\partial\vec{r}_i}{\partial q_\alpha}\cdot\frac{\partial\vec{r}_i}{\partial q_\beta}\dot{q}_\alpha\dot{q}_\beta
+\sum_{\alpha=1}^s\sum_{i=1}^nm_i\frac{\partial\vec{r}_i}{\partial q_\alpha}\cdot\frac{\partial \vec{r}_i}{\partial t}\dot{q}_\alpha+\frac{1}{2}\sum_{i=1}^nm_i\left(\frac{\partial\vec{r}_i}{\partial t}\right)^2\\
&=\frac{1}{2}\sum_
{\begin{aligned}
\alpha&=1\\
\beta&=1
\end{aligned}}^s
a_{\alpha\beta}\dot{q}_\alpha\dot{q}_\beta+\sum_{\alpha=1}^sa_\alpha\dot{q}_\alpha+\frac{1}{2}a\\\\
&=T_2+T_1+T_0
\end{aligned}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$T_2$$、$$T_1$$和$$T_0$$分别为广义速度$$\dot{q}_\alpha$$的二次、一次和零次的函数，$$a_{\alpha\beta}$$、$$a_\alpha$$和$$a$$一般是$$q_\alpha$$和$$t$$的函数

* 如果力学体系是稳定的，则有$$\frac{\partial\vec{r}_i}{\partial t}=0$$，即$$a_\alpha=a=0$$，此时动能$$T$$仅为广义速度的二次齐次函数，即$$T=T_2$$。当$$T=T_2$$且$$V=V\left(q_1,q_2,\dotsb,q_s\right)$$不显含$$t$$时，方程

$$
\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial T}{\partial \dot{q}_\alpha}-\frac{\partial T}{\partial q_\alpha}=-\frac{\partial V}{\partial q_\alpha}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;可进行以下变形：

$$
\begin{aligned}
&\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial T}{\partial \dot{q}_\alpha}-\frac{\partial T}{\partial q_\alpha}=-\frac{\partial V}{\partial q_\alpha}\\\\
\Leftrightarrow
&\sum_{\alpha=1}^s\left(\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial T}{\partial \dot{q}_\alpha}-\frac{\partial T}{\partial q_\alpha}\right)=\sum_{\alpha=1}^s-\frac{\partial V}{\partial q_\alpha}\\\\\Leftrightarrow
&\sum_{\alpha=1}^s\left(\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial T}{\partial \dot{q}_\alpha}-\frac{\partial T}{\partial q_\alpha}\right)\dot{q}_\alpha=\sum_{\alpha=1}^s\left(-\frac{\partial V}{\partial q_\alpha}\right)\dot{q}_\alpha\\\\
\Leftrightarrow
&\sum_{\alpha=1}^s\left(\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial T}{\partial\dot{q}_\alpha}\right)\dot{q}_\alpha-\sum_{\alpha=1}^s\frac{\partial T}{\partial q_\alpha}\dot{q}_\alpha=\sum_{\alpha=1}^s-\frac{\partial V}{\partial q_\alpha}\dot{q}_\alpha\\\\
\Leftrightarrow
&\left[\sum_{\alpha=1}^s\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\partial T}{\partial\dot{q}_\alpha}\dot{q}_\alpha\right)-\sum_{\alpha=1}^s\frac{\partial T}{\partial \dot{q}_\alpha}\ddot{q}_\alpha\right]-\sum_{\alpha=1}^s\frac{\partial T}{\partial q_\alpha}\dot{q}_\alpha=\sum_{\alpha=1}^s-\frac{\partial V}{\partial q_\alpha}\dot{q}_\alpha\\\\
\Leftrightarrow
&\sum_{\alpha=1}^s\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\partial T}{\partial\dot{q}_\alpha}\dot{q}_\alpha\right)-\left(\sum_{\alpha=1}^s\frac{\partial T}{\partial \dot{q}_\alpha}\ddot{q}_\alpha+\sum_{\alpha=1}^s\frac{\partial T}{\partial q_\alpha}\dot{q}_\alpha\right)=\sum_{\alpha=1}^s-\frac{\partial V}{\partial q_\alpha}\dot{q}_\alpha
\end{aligned}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;考虑到$$T$$是广义速度的二次齐次函数，即有

$$
\sum_{\alpha=1}^s\frac{\partial T}{\partial \dot{q}_\alpha}\dot{q}_\alpha=2T
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;而$$T$$和$$V$$都不是时间$$t$$的显函数，因此有

$$
\left.
\begin{aligned}
&\sum_{\alpha=1}^s\left(\frac{\partial T}{\partial q_\alpha}\dot{q}_\alpha+\frac{\partial T}{\partial \dot{q}_\alpha}\ddot{q}_\alpha\right)=\frac{\mathrm{d}T}{\mathrm{d}t}\\\\
&\sum_{\alpha=1}^s\frac{\partial V}{\partial q_\alpha}\dot{q}_\alpha=\frac{\mathrm{d}V}{\mathrm{d}t}
\end{aligned}
\right\}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;故原方程可以写作

$$
\frac{\mathrm{d}}{\mathrm{d}t}\left(2T\right)-\frac{\mathrm{d}T}{\mathrm{d}t}=-\frac{\mathrm{d}V}{\mathrm{d}t}\Leftrightarrow
\frac{\mathrm{d}T}{\mathrm{d}t}=-\frac{\mathrm{d}V}{\mathrm{d}t}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;即有$$T+V=E$$，这就是力学体系的能量积分

* 如动能是广义速度的二次非齐次函数，则还有对应的广义能量积分

* 球坐标中路径微分可以表示为

$$
\left(\mathrm{d}s\right)^2=\left(\mathrm{d}r\right)^2+r^2\left(\mathrm{d}\theta\right)^2+r^2\sin^2{\theta}\left(\mathrm{d}\varphi\right)^2	
$$

* 使用拉矢量求解力学问题的步骤：
 * 确定力学体系的自由度
 * 适当选取描写体系运动的广义坐标
 * 写出力学体系的动能$$T$$及势能$$V$$，进而写出体系的拉格朗日函数$$L$$
 * 把$$L$$代入拉格朗日方程，得出力学体系的运动微分方程
 * 解方程并讨论

* 若将广义力$$Q_\alpha$$作用下力学体系的基本形式拉格朗日方程

$$
\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial T}{\partial \dot{q}_\alpha}-\frac{\partial T}{\partial q_\alpha}=Q_\alpha\ \ \ \ \ \left(\alpha=1,2,\dotsb,s\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;从时间$$t_1$$到$$t_2$$进行积分，则有

$$
\int_{t_1}^{t_2}\left(\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial T}{\partial \dot{q}_\alpha}\right)\mathrm{d}t-\int_{t_1}^{t_2}\frac{\partial T}{\partial q_\alpha}\mathrm{d}t=\int_{t_1}^{t_2}Q_\alpha\mathrm{d}t\ \\\ \\
\Leftrightarrow
\left[\left(\frac{\partial T}{\partial \dot{q}_\alpha}\right)_{t_2}-\left(\frac{\partial T}{\partial \dot{q}_\alpha}\right)_{t_1}\right]-\int_{t_1}^{t_2}\frac{\partial T}{\partial q_\alpha}\mathrm{d}t=\int_{t_1}^{t_2}Q_\alpha\mathrm{d}t=I_\alpha\ \ \ \ \ \left(\alpha=1,2,\dotsb,s\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;由于$$\frac{\partial T}{\partial q_\alpha}$$是一有限值，而$$t_2-t_1$$甚小，因此上式中等式左侧第二项可以略去不计，上式可化为

$$
\left(\frac{\partial T}{\partial \dot{q}_\alpha}\right)_{t_2}-\left(\frac{\partial T}{\partial \dot{q}_\alpha}\right)_{t_1}=I_\alpha
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;此即为冲击运动的拉格朗日方程

* 对于不完整约束的力学体系，设体系除受有$$k$$个完整约束外，还受有下列$$r$$个线性依赖于速度的微分约束

$$
\sum_{i=1}^n\left(a_{\rho i}\dot{x}_i+b_{\rho i}\dot{y}_i+c_{\rho i}\dot{z}_i\right)+a_\rho=0\ \ \ \ \ \left(\rho=1,2,\dotsb,r\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;或

$$
\sum_{i=1}^n\left(a_{\rho i}\mathrm{d}x_i+b_{\rho i}\mathrm{d}y_i+c_{\rho i}\mathrm{d}z_i\right)+a_\rho\mathrm{d}t=0\ \ \ \ \ \left(\rho=1,2,\dotsb,r\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;由于$$a_{\rho i}$$、$$b_{\rho i}$$、$$c_{\rho i}$$和$$a_\rho$$都是$$x_i$$、$$y_i$$、$$z_i$$$$\left(i=1,2,\dotsb,n\right)$$的函数，可使用$$q_\alpha\left(\alpha=1,2,\dotsb,s\right)$$将上式代换为

$$
\sum_{\alpha=1}^s\left(A_{\rho\alpha}\mathrm{d}q_\alpha\right)+A_\rho\mathrm{d}t=0\ \ \ \ \ \left(\rho=1,2,\dotsb,r\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$A_{\rho\alpha}$$$$\left(\alpha=1,2,\dotsb,s\right)$$和$$A_\rho$$都是$$q_\alpha\left(\alpha=1,2,\dotsb,s\right)$$的函数

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;同时，对广义坐标平衡时各个虚位移应当满足

$$
\sum_{\alpha=1}^sA_{\rho\alpha}\delta q_\alpha=0\ \ \ \ \ \left(\rho=1,2,\dotsb,r\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中有$$r$$个$$\delta q_\alpha$$是不独立的。将上式乘以$$\mu_\rho$$，对$$\rho$$求和再与式

$$
\sum_{\alpha=1}^s\left[\left(-\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial T}{\partial \dot{q}_\alpha}+\frac{\partial T}{\partial q_\alpha}+Q_\alpha\right)\delta q_\alpha\right]=0
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;相加，可得到

$$
\sum_{\alpha=1}^s\left[-\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\partial T}{\partial \dot{q}_\alpha}\right)+\frac{\partial T}{\partial q_\alpha}+Q_\alpha+\sum_{\rho=1}^r\mu_\rho A_{\rho\alpha}\right]\delta q_\alpha=0\ \ \ \ \ \left(\alpha=1,2,\dotsb,s\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;通过选择$$r$$个未定乘数$$\mu_\rho$$，使得虚位移前的乘数均为零，则可得到$$s$$个方程

$$
\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\partial T}{\partial \dot{q}_\alpha}\right)-\frac{\partial T}{\partial q_\alpha}=Q_\alpha+\sum_{\rho=1}^r\mu_\rho A_{\rho\alpha}\ \ \ \ \ \left(\alpha=1,2,\dotsb,s\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;此式称为罗斯方程。结合此式与

$$
\sum_{\alpha=1}^s\left(A_{\rho\alpha}\mathrm{d}q_\alpha\right)+A_\rho\mathrm{d}t=0\ \ \ \ \ \left(\rho=1,2,\dotsb,r\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;的$$r$$个方程，共$$s+r$$个方程即可求解出$$s+r$$个未知变量$$q_1,q_2\dotsb,q_s;\mu_1,\mu_2,\dotsb,\mu_r$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;可以证明，$$\mu_\rho$$是与约束力成正比例的标量。若同时添加一组$$\sum_{\beta=1}^k\lambda_\beta\frac{\partial\varphi_\beta}{\partial q_\alpha}$$则可利用乘数$$\lambda_\beta$$求出广义力

* 常用的系数：
 * $$k$$个完整约束
 * $$r$$个不完整约束
 * $$3n-k=s$$个广义坐标

[返回目录](#5.0) [返回总目录](#0.0)

---

### <h54 id='5.4'> §5.4 小振动</h54>

[返回目录](#5.0) [返回总目录](#0.0)

* 保守力系平衡时的条件是势能具有稳定值，即

$$
\frac{\partial V}{\partial q_\alpha}=-Q_\alpha=0\ \ \ \ \ \left(\alpha=1,2,\dotsb,s\right)
$$

* 可使用拉格朗日方程研究多自由度微小振动问题。设平衡位置时力学体系的广义坐标均等于零，将势能函数在平衡位置附近进行泰勒展开，即有

$$
V=V_0+\sum_{\alpha=1}^s\left(\frac{\partial V}{\partial q_\alpha}\right)_0q_\alpha+\frac{1}{2}\sum_{
\begin{aligned}
&\alpha=1\\
&\beta=1
\end{aligned}}^s
\left(\frac{\partial^2V}{\partial q_\alpha \partial q_\beta}\right)_0q_\alpha q_\beta+o\left(q_i^3\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;可略去二次以上的高阶项并令$$V_0=0$$，则有

$$
V=\frac{1}{2}\sum_{
\begin{aligned}
&\alpha=1\\
&\beta=1
\end{aligned}}^s
c_{\alpha\beta}q_\alpha q_\beta
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中

$$
c_{\alpha\beta}=\left(\frac{\partial^2 V}{\partial q_\alpha q_\beta}\right)_0
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;稳定约束下，体系动能$$T$$只是速度的二次齐次函数，即

$$
T=\frac{1}{2}\sum_{
\begin{aligned}
&\alpha=1\\
&\beta=1
\end{aligned}}^s
a_{\alpha\beta}\dot{q}_\alpha\dot{q}_\beta
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;因此拉格朗日方程可以表示为

$$
\begin{aligned}
&\frac{\mathrm{d}}{\mathrm{d}t}\frac{\partial T}{\partial \dot{q}_\alpha}-\frac{\partial T}{\partial q_\alpha}=-\frac{\partial V}{\partial q_\alpha}\\\\
\Leftrightarrow
&\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{1}{2}\sum_{\beta=1}^sa_{\alpha\beta}\dot{q}_\beta\right)-0=-\frac{1}{2}\sum_{\beta=1}^sc_{\alpha\beta}q_\beta\\\\
\Leftrightarrow
&\frac{1}{2}\sum_{\beta=1}^sa_{\alpha\beta}\ddot{q}_\beta=-\frac{1}{2}\sum_{\beta=1}^sc_{\alpha\beta}q_\beta\\\\
\Leftrightarrow
&\sum_{\beta=1}^s\left(a_{\alpha\beta}\ddot{q}_\beta+c_{\alpha\beta}q_\beta\right)=0\ \ \ \ \ \left(\alpha=1,2,\dotsb,s\right)
\end{aligned}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;它的解具有$$q_\beta=A_\beta e^{\lambda t}$$的形式，其中$$A_\beta$$和$$\lambda$$为常数。将其带入上式，有

$$
\sum_{\beta=1}^sA_\beta\left(a_{\alpha\beta}\lambda^2+c_{\alpha\beta}\right)=0\ \ \ \ \ \left(\alpha=1,2,\dotsb,s\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;将$$A_\beta$$看作未知量，则非零解存在的条件是

$$
\begin{aligned}
&\det\left(a_{\alpha\beta}\lambda^2+c_{\alpha\beta}\right)=0\\\\
\Leftrightarrow&
\begin{vmatrix}
a_{11}\lambda^2+c_{11}&a_{12}\lambda^2+c_{12}&\dotsb&a_{1s}\lambda^2+c_{1s}\\
a_{21}\lambda^2+c_{21}&a_{22}\lambda^2+c_{22}&\dotsb&a_{2s}\lambda^2+c_{2s}\\
\vdots&\vdots& &\vdots\\
a_{s1}\lambda^2+c_{s1}&a_{s2}\lambda^2+c_{s2}&\dotsb&a_{ss}\lambda^2+c_{ss}
\end{vmatrix}=0
\end{aligned}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;此时可解出$$2s$$个本征值$$\lambda_l$$，每个本征值又对应一组解$$q_\beta$$，进而$$q_\beta$$可以表示为

$$
\begin{aligned}
q_\beta&=\sum_{l=1}^{2s}A_\beta^{(l)}e^{\lambda_l t}=
\sum_{l=1}^s\left(A_\beta^{(l)}e^{i\omega t}+{A'}_\beta^{(l)}e^{-i\omega t}\right)\\\\
&=\sum_{l=1}^s\left(a_\beta^{(l)}\cos\omega_l t+b_\beta^{(l)}\sin\omega_l t\right)\ \ \ \ \ \left(\beta=1,2,\dotsb,s\right)
\end{aligned}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;即会在平衡位置作复杂振动，而不会偏离平衡位置。其中$$\omega_l$$为简正频率，共有$$s$$个，与力学体系自由度数相等

* 多自由度体系的小振动问题之所以复杂，是因为动能与势能的表达式中存在广义坐标的交叉项$$q_\alpha q_\beta$$和$$\dot{q}_\alpha\dot{q}_\beta$$。根据线性代数理论，可以通过线性变换

$$
q_\beta=\sum_{l=1}^sg_{\beta l}\xi_l
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;消除交叉项，使得$$T$$和$$V$$同时变为正则形式。变换后有

$$
\left.
\begin{aligned}
T&=\frac{1}{2}\sum_{l=1}^sa_l^0\dot{\xi}_l^2\\\\
V&=\frac{1}{2}\sum_{l=1}^sc_l^0\xi_l^2
\end{aligned}
\right\}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;此时变量由$$q_\alpha$$变为$$\xi_l$$，相应的拉格朗日方程变为

$$
\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\partial T}{\partial\dot{\xi}_l}\right)-\frac{\partial T}{\partial \xi_l}+\frac{\partial V}{\partial \xi_l}=0\ \ \ \ \ \left(l=1,2,\dotsb,s\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;将变换后的$$T$$与$$V$$的表达式代入，可得

$$
a_l^0\ddot{\xi}_l+c_l^0\xi_l=0\ \ \ \ \ \left(l=1,2,\dotsb,s\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;积分可得

$$
\begin{aligned}
\xi_l&=A_l\cos\left(\omega_lt\right)+B_l\sin\left(\omega_l t\right)\\\\
&=C_l\cos\left(\omega_lt+\varepsilon_l\right)\ \ \ \ \ \left(l=1,2,\dotsb,s\right)
\end{aligned}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$\omega_l=\sqrt{\frac{c_l^0}{a_l^0}}$$为简正频率，坐标$$\xi_l$$叫作简正坐标

[返回目录](#5.0) [返回总目录](#0.0)

---

### <h55 id='5.5'> §5.5 哈密顿正则方程</h55>

[返回目录](#5.0) [返回总目录](#0.0)

* 勒让德变换是由一组独立变数变为另一组独立变数的变换。对于两个变量的勒让德变换，首先设$$f=f\left(x,y\right)$$，则有$$\mathrm{d}f=u\mathrm{d}x+v\mathrm{d}y$$，其中

$$
u=\frac{\partial f}{\partial x},\ \ \ \ \ v=\frac{\partial f}{\partial y}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;若欲将$$u$$和$$y$$作为独立变量，则有$$x=x\left(u,y\right)$$，$$y=y\left(u,y\right)$$，函数$$f$$可表示为

$$
\bar{f}\left(u,y\right)=f\left[x\left(u,y\right),y\right]
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;求其对独立变量$$u$$和$$y$$的偏导数可得

$$
\left\{
\begin{aligned}
&\frac{\partial\bar{f}}{\partial u}=\frac{\partial f}{\partial x}\frac{\partial x}{\partial u}=u\frac{\partial x}{\partial u}\\\\
&\frac{\partial\bar{f}}{\partial y}=\frac{\partial f}{\partial x}\frac{\partial x}{\partial y}+\frac{\partial f}{\partial y}=v+u\frac{\partial f}{\partial y}
\end{aligned}
\right.
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;上式可化为

$$
\left\{
\begin{aligned}
&v=-\frac{\partial}{\partial y}\left(-\bar{f}+ux\right)=-\frac{\partial g}{\partial y}\\\\
&x=\frac{\partial}{\partial u}\left(-\bar{f}+ux\right)=\frac{\partial g}{\partial u}
\end{aligned}
\right.
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中

$$
g\left(u,y\right)=-\bar{f}+ux=\left(-f+\frac{\partial f}{\partial x}x\right)_{x=x\left(u,y\right)}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;有

$$
\mathrm{d}g\left(u,y\right)=\frac{\partial g}{\partial u}\mathrm{d}u+\frac{\partial g}{\partial y}\mathrm{d}y=x\mathrm{d}u-v\mathrm{d}v
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;新的函数等于不要的变量乘以原来的函数对该变量的偏微商再减去原来的函数

* 在拉格朗日方程

$$
\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\partial L}{\partial \dot{q}_\alpha}\right)-\frac{\partial L}{\partial q_\alpha}=0\ \ \ \ \ \left(\alpha=1,2,\dotsb,s\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;中，若令

$$
p_\alpha=\frac{\partial L}{\partial \dot{q}_\alpha}=\frac{\partial T}{\partial \dot{q}_\alpha}\ \ \ \ \ \left(\alpha=1,2,\dotsb,s\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;作为独立变量，则有

$$
\dot{p}_\alpha=\frac{\partial L}{\partial q_\alpha}\ \ \ \ \ \left(\alpha=1,2,\dotsb,s\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;可解出$$\dot{q}_\alpha$$作为$$p_\beta$$、$$q_\beta$$与$$t$$的函数，即有

$$
\dot{q}_\alpha=\dot{q}_\alpha\left(p_1,p_2,\dotsb,p_s;q_1,q_2,\dotsb,q_s;t\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;若将其代入拉氏量$$L$$的表达式中，则$$L$$可表示为

$$
\bar{L}=\bar{L}\left(p_1,p_2,\dotsb,p_s;q_1,q_2,\dotsb,q_s;t\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;引入新函数$$H$$使得

$$
H\left(p,q,t\right)=-L+\sum_{\alpha=1}^sp_\alpha\dot{q}_\alpha
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;而

$$
\begin{aligned}
\mathrm{d}H&=-\mathrm{d}L+\sum_{\alpha=1}^s\left(p_\alpha\mathrm{d}\dot{q}_\alpha+\dot{q}_\alpha\mathrm{d}p_\alpha\right)\\\\
&=-\left[\sum_{\alpha=1}^s\left(\frac{\partial L}{\partial q_\alpha}\mathrm{d}q_\alpha+\frac{\partial L}{\partial \dot{q}_\alpha}\mathrm{d}\dot{q}_\alpha\right)+\frac{\partial L}{\partial t}\mathrm{d}t\right]+\sum_{\alpha=1}^s\left(p_\alpha\mathrm{d}\dot{q}_\alpha+\dot{q}_\alpha\mathrm{d}p_\alpha\right)\\\\
&=-\left[\sum_{\alpha=1}^s\left(\dot{p}_\alpha\mathrm{d}q_\alpha+p_\alpha\mathrm{d}\dot{q}_\alpha\right)+\frac{\partial L}{\partial t}\mathrm{d}t\right]+\sum_{\alpha=1}^s\left(p_\alpha\mathrm{d}\dot{q}_\alpha+\dot{q}_\alpha\mathrm{d}p_\alpha\right)\\\\
&=\sum_{\alpha=1}^s\left(\dot{q}_\alpha\mathrm{d}p_\alpha-\dot{p}_\alpha\mathrm{d}q_\alpha\right)-\frac{\partial L}{\partial t}\mathrm{d}t=\sum_{\alpha=1}^s\left(\frac{\partial H}{\partial q_\alpha}\mathrm{d}q_\alpha+\frac{\partial H}{\partial p_\alpha}\mathrm{d}p_\alpha\right)+\frac{\partial H}{\partial t}\mathrm{d}t
\end{aligned}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;因此有

$$
\left.
\begin{aligned}
\dot{q}_\alpha&=\frac{\partial H}{\partial p_\alpha}\\\\
\dot{p}_\alpha&=-\frac{\partial H}{\partial q_\alpha}\\\\
\frac{\partial H}{\partial t}&=-\frac{\partial L}{\partial t}
\end{aligned}
\right\}\ \ \ \ \ \left(\alpha=1,2,\dotsb,s\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;此即为哈密顿正则方程，简称正则方程。$$H$$为哈密顿函数，$$p_\alpha$$、$$q_\alpha$$为正则变量

* 对$$H$$求微商，则有

$$
\mathrm{d}H=\sum_{\alpha=1}^s\left(\frac{\partial H}{\partial q_\alpha}\mathrm{d}q_\alpha+\frac{\partial H}{\partial p_\alpha}\mathrm{d}p_\alpha\right)+\frac{\partial H}{\partial t}\mathrm{d}t
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;因此

$$
\begin{aligned}
\frac{\mathrm{d}H}{\mathrm{d}t}&=\sum_{\alpha=1}^s\left(\frac{\partial H}{\partial q_\alpha}\dot{q}_\alpha+\frac{\partial H}{\partial p_\alpha}\dot{p}_\alpha\right)+\frac{\partial H}{\partial t}\mathrm{d}t\\\\
&=\sum_{\alpha=1}^s\left(\frac{\partial H}{\partial q_\alpha}\frac{\partial H}{\partial p_\alpha}-\frac{\partial H}{\partial p_\alpha}\frac{\partial H}{\partial q_\alpha}\right)+\frac{\partial H}{\partial t}=\frac{\partial H}{\partial t}
\end{aligned}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;若$$H$$中不显含$$t$$，即$$\frac{\partial H}{\partial t}=0$$，则有$$\frac{\mathrm{d}H}{\mathrm{d}t}=0$$，因而对应该正则方程有一积分$$H=h$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;若体系约束为稳定约束，则可将动能表示为广义速度的二次齐次函数，因此有

$$
H=-L+\sum_{\alpha=1}^sp_\alpha\dot{q}_\alpha=-L+\sum_{\alpha=1}^s\frac{\partial T}{\partial \dot{q}_\alpha}\dot{q}_\alpha=-\left(T-V\right)+2T=T+V
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;此即为$$H$$的能量积分。在稳定约束时$$H$$的值与体系总能量$$E=T+V$$相等；不稳定时为$$T_2-T_0+V$$

* 由方程

$$
\left.
\begin{aligned}
\dot{q}_\alpha&=\frac{\partial H}{\partial p_\alpha}\\\\
\dot{p}_\alpha&=-\frac{\partial H}{\partial q_\alpha}\\\\
\frac{\partial H}{\partial t}&=-\frac{\partial L}{\partial t}
\end{aligned}
\right\}\ \ \ \ \ \left(\alpha=1,2,\dotsb,s\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;可知，若$$H$$中不显含某一广义坐标（例如$$q_\alpha$$），则对应的偏微分系数不随时间发生变化，即

$$
\dot{p}_\alpha=-\frac{\partial H}{\partial q_\alpha}=0
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;因此该广义坐标为一循环坐标，偏微分系数所对应的物理量守恒

[返回目录](#5.0) [返回总目录](#0.0)

---

### <h56 id='5.6'> §5.6 泊松括号与泊松定理</h56>

[返回目录](#5.0) [返回总目录](#0.0)

* 假如函数$$\varphi$$是正则变量$$p_\alpha$$、$$q_\alpha$$及时间$$t$$的函数，即

$$
\varphi=\varphi\left(p_1,p_2,\dotsb,p_\alpha;q_1,q_2,\dotsb,q_\alpha;t\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;则$$\varphi$$对$$t$$的微商为

$$
\frac{\mathrm{d}\varphi}{\mathrm{d}t}=\frac{\partial\varphi}{\partial t}+\sum_{\alpha=1}^s\left(\frac{\partial \varphi}{\partial q_\alpha}\dot{q}_\alpha+\frac{\partial \varphi}{\partial p_\alpha}\dot{p}_\alpha\right)=\frac{\partial\varphi}{\partial t}+\sum_{\alpha=1}^s\left(\frac{\partial \varphi}{\partial q_\alpha}\frac{\partial H}{\partial p_\alpha}-\frac{\partial \varphi}{\partial p_\alpha}\frac{\partial H}{\partial q_\alpha}\right)=\frac{\partial \varphi}{\partial t}+\left[\varphi,H\right]
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$\left[\varphi,H\right]$$称为泊松括号，有

$$
\left[\varphi,H\right]=\sum_{\alpha=1}^s\left(\frac{\partial \varphi}{\partial q_\alpha}\frac{\partial H}{\partial p_\alpha}-\frac{\partial \varphi}{\partial p_\alpha}\frac{\partial H}{\partial q_\alpha}\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;泊松括号需要满足的条件是所有$$q$$和$$p$$都是相互独立的，即有

$$
\frac{\partial p_\alpha}{\partial q_\alpha}=0,\ \frac{\partial p_\alpha}{\partial p_\beta}=0,\ \frac{\partial q_\alpha}{\partial p_\beta}=0,\ \frac{\partial q_\alpha}{\partial q_\beta}=0,\ \frac{\partial p_\alpha}{\partial p_\alpha}=1,\ \frac{\partial q_\alpha}{\partial q_\alpha}=1
$$

* 利用泊松括号，正则方程可以表示为

$$
\left.
\begin{aligned}
\dot{p}_\alpha=\left[p_\alpha,H\right]\\\\
\dot{q}_\alpha=\left[q_\alpha,H\right]
\end{aligned}
\right\}\ \ \ \ \ \left(\alpha=1,2,\dotsb,s\right)
$$

* 若力学体系的某一函数$$\varphi=\varphi\left(p_1,p_2,\dotsb,p_\alpha;q_1,q_2,\dotsb,q_\alpha;t\right)$$不随时间变化，则方程$$\varphi\left(p_\alpha,q_\alpha,t\right)=C$$称为体系的一个运动积分（也成为第一积分）。当$$\varphi=C$$成立时，有

$$
\frac{\mathrm{d}\varphi}{\mathrm{d}t}=\frac{\partial \varphi}{\partial t}+\left[\varphi,H\right]=0
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;与之对应的常微分方程组为

* 泊松括号具有以下特性：

$$
\begin{aligned}
&(1)\ \ \ \left[c,\psi\right]=0\ \ \ (\mathrm{c\ is\ constant})\\\\
&(2)\ \ \ \left[\varphi,\psi\right]+\left[\psi,\varphi\right]=0\\\\
&(3)\ \ \ \mathrm{if}\ \psi=\sum_{j=1}^n\psi_i,\ \mathrm{then}\ \left[\varphi,\psi\right]=\sum_{j=1}^n\left[\varphi,\psi_j\right]\\\\
&(4)\ \ \ \left[-\varphi,\psi\right]=-\left[\varphi,\psi\right]\\\\
&(5)\ \ \ \frac{\partial}{\partial t}\left[\varphi,\psi\right]=\left[\frac{\partial\varphi}{\partial t},\psi\right]+\left[\varphi,\frac{\partial\psi}{\partial t}\right]\\\\
&(6)\ \ \ \left[\theta,\left[\varphi,\psi\right]\right]+\left[\varphi,\left[\psi,\theta\right]\right]+\left[\psi,\left[\theta,\varphi\right]\right]=0\\\\
&(7)\ \ \ \left[q_\alpha,p_\beta\right]=\delta_{\alpha\beta}=\left\{
\begin{aligned}
&1&\left(\alpha=\beta\right)\\
&0&\left(\alpha\neq\beta\right)
\end{aligned}
\right.
\end{aligned}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$\psi$$和$$\theta$$也是正则变量与时间的函数。上式中第(6)式被称为泊松恒等式，也叫雅克比恒等式

* 设正则方程的两个运动积分为

$$
\left\{
\begin{aligned}
\varphi\left(p_1,p_2,\dotsb,p_s;q_1,q_2,\dotsb,q_s;t\right)=C_1\\\\
\psi\left(p_1,p_2,\dotsb,p_s;q_1,q_2,\dotsb,q_s;t\right)=C_2
\end{aligned}
\right.
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;则有

$$
\frac{\mathrm{d}\varphi}{\mathrm{d}t}=\frac{\partial \varphi}{\partial t}+\left[\varphi,H\right]=0,\ \ \ \ \ \frac{\mathrm{d}\psi}{\mathrm{d}t}=\frac{\partial \psi}{\partial t}+\left[\psi,H\right]=0
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;利用泊松恒等式，有

$$
\begin{aligned}
&\left[H,\left[\varphi,\psi\right]\right]+\left[\varphi,\left[\psi,H\right]\right]+\left[\psi,\left[\theta,H\right]\right]=0\\\\
\Leftrightarrow
&\left[H,\left[\varphi,\psi\right]\right]-\left[\varphi,\frac{\partial\psi}{\partial t}\right]+\left[\psi,\frac{\partial \varphi}{\partial t}\right]=0\\\\
\Leftrightarrow
&\frac{\partial}{\partial t}\left[\varphi,\psi\right]+\left[\left[\varphi,\psi\right],H\right]=\frac{\mathrm{d}}{\mathrm{d}t}\left[\varphi,\psi\right]=0\\\\
\Leftrightarrow
&\left[\varphi,\psi\right]=C_3
\end{aligned}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;这被称为泊松定理

* 对于动量矩$$J_x$$、$$J_y$$和$$J_z$$，有

$$
\left\{
\begin{aligned}
&\left[J_x,J_y\right]=J_z\\\\
&\left[J_y,J_z\right]=J_x\\\\
&\left[J_z,J_x\right]=J_y
\end{aligned}
\right.
$$

[返回目录](#5.0) [返回总目录](#0.0)

---

### <h57 id='5.7'> §5.7 哈密顿原理</h57>

[返回目录](#5.0) [返回总目录](#0.0)

* 变分规则：

$$
\left.
\begin{aligned}
&\delta\left(A+B\right)=\delta A+\delta B\\\\
&\delta\left(AB\right)=A\delta B+B\delta A\\\\
&\delta\left(\frac{A}{B}\right)=\frac{B\delta A-A\delta B}{B^2}\\\\
&\delta\left(\mathrm{d}q_\alpha\right)=\mathrm{d}\left(\delta q_\alpha\right)
\end{aligned}
\right\}
$$

* 一般来说，$$\delta$$与$$\frac{\mathrm{d}}{\mathrm{d}t}$$是不能对易的，但是当$$\delta t=0$$的假设下，对易是可以成立的，即有

$$
\delta\left(\frac{\mathrm{d}q_\alpha}{\mathrm{d}t}\right)=\frac{\mathrm{d}}{\mathrm{d}t}\left(\delta q_\alpha\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;二者可以对易的变分叫做等式变分，不可对已的变分叫做不等式变分或全变分。对于全变分，有

$$
\Delta\left(\frac{\mathrm{d}q_\alpha}{\mathrm{d}t}\right)=\frac{\mathrm{d}}{\mathrm{d}t}\left(\Delta q_\alpha\right)-\frac{\mathrm{d}q_\alpha}{\mathrm{d}t}\frac{\mathrm{d}}{\mathrm{d}t}\left(\Delta t\right)
$$

* 哈密顿原理：保守的、完整的力学体系在相同时间内，由某一初位形转移到另一已知位形的一切可能运动中，真实运动的主函数具有稳定值，即对真实运动来说，主函数的变分等于零。其推导过程如下：

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;将保守体系的拉格朗日方程中各项乘以$$\delta q_\alpha$$，对$$\alpha$$求和并对$$t$$积分可得

$$
\int_{t_1}^{t_2}\sum_{\alpha=1}^s\left\{\left[\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\partial L}{\partial \dot{q}_\alpha}\right)-\frac{\partial L}{\partial q_\alpha}\right]\delta q_\alpha\right\}\mathrm{d}t=0
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中

$$
\begin{aligned}
\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\partial L}{\partial \dot{q}_\alpha}\right)\delta q_\alpha
&=\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\partial L}{\partial \dot{q}_\alpha}\delta q_\alpha\right)-\frac{\partial L}{\partial \dot{q}_\alpha}\frac{\mathrm{d}}{\mathrm{d}t}\left(\delta q_\alpha\right)\\\\
&=\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\partial L}{\partial \dot{q}_\alpha}\delta q_\alpha\right)-\frac{\partial L}{\partial \dot{q}_\alpha}\delta \dot{q}_\alpha
\end{aligned}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;因此有

$$
\begin{aligned}
&\int_{t_1}^{t_2}\sum_{\alpha=1}^s\left\{\left[\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\partial L}{\partial \dot{q}_\alpha}\right)-\frac{\partial L}{\partial q_\alpha}\right]\delta q_\alpha\right\}\mathrm{d}t=0\\\\
\Leftrightarrow
&\sum_{\alpha=1}^s\left.\frac{\partial L}{\partial \dot{q}_\alpha}\delta q_\alpha\right|_{t_1}^{t_2}-\int_{t_1}^{t_2}\sum_{\alpha=1}^s\left(\frac{\partial L}{\partial q_\alpha}\delta q_\alpha+\frac{\partial L}{\partial \dot{q}_\alpha}\delta \dot{q}_\alpha\right)\mathrm{d}t=0
\end{aligned}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;由于$$L=L\left(q_\alpha,\dot{q}_\alpha,t\right)$$，而$$\delta \left.q_\alpha\right|_{t=t1}=\delta \left.q_\alpha\right|_{t=t2}=0$$，因此上式可简化为

$$
\int_{t_1}^{t_2}\delta L\mathrm{d}t=\delta\int_{t_1}^{t_2}L\mathrm{d}t=0
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;此即为保守力系中哈密顿原理的数学表达式

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;称$$\int_{t_1}^{t_2}L\mathrm{d}t$$为作用函数，当它表示为端点时间和位置的函数时，也叫主函数$$S$$，有

$$
\delta S=S'-S=\int_{t_1}^{t_2}L\left(q'_\alpha,\dot{q}'_\alpha,t\right)\mathrm{d}t-\int_{t_1}^{t_2}L\left(q_\alpha,\dot{q}_\alpha,t\right)\mathrm{d}t
$$

* 对于真实运动来说，主函数的变分等于零

[返回目录](#5.0) [返回总目录](#0.0)

---

### <h58 id='5.8'> §5.8 正则变换</h58>

[返回目录](#5.0) [返回总目录](#0.0)

* 若通过变数变换，能找到新的函数$$H^*$$使得正则方程的形式不变，则这种变换就是正则变换

* 设经过变数变换后，原有的正则变量$$p_\alpha$$和$$q_\alpha$$变为

$$
\left\{
\begin{aligned}
P_\alpha&=P_\alpha\left(p_1,p_2,\dotsb,p_s;q_1,q_2,\dotsb,q_s;t\right)\\\\
Q_\alpha&=Q_\alpha\left(p_1,p_2,\dotsb,p_s;q_1,q_2,\dotsb,q_s;t\right)
\end{aligned}
\right.
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;若$$P_\alpha$$、$$Q_\alpha$$和$$H$$的表达式中均显含$$t$$，则变换为正则变换的条件是

$$
\sum_{\alpha=1}^s\left(p_\alpha\mathrm{d}q_\alpha-P_\alpha\mathrm{d}Q_\alpha\right)+\left(H^*-H\right)\mathrm{d}t=\mathrm{d}U\ \ \ \ \ (5.8.0)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;证明如下：

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;当正则变换满足方程(5.8.0)时，由于$$\delta t=0$$，有

$$
\sum_{\alpha=1}^s\left(p_\alpha\delta q_\alpha-P_\alpha\delta Q_\alpha\right)=\delta U\ \ \ \ \ (5.8.1)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;求方程(5.8.0)对于时间$$t$$的微商，则有

$$
\sum_{\alpha=1}^s\left(p_\alpha\dot{q}_\alpha-P_\alpha\dot{Q}_\alpha\right)+\left(H^*-H\right)=\dot{U}\ \ \ \ \ (5.8.2)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;取(5.8.1)式对时间$$t$$的微商和(5.8.2)式的变分，比较可得

$$
\begin{aligned}
&\frac{\mathrm{d}}{\mathrm{d}t}\left[\sum_{\alpha=1}^s\left(p_\alpha\delta{q}_\alpha-P_\alpha\delta{Q}_\alpha\right)\right]\\\\
=&\frac{\mathrm{d}}{\mathrm{d}t}\left(\sum_{\alpha=1}^sp_\alpha\delta{q}_\alpha\right)-\frac{\mathrm{d}}{\mathrm{d}t}\left(\sum_{\alpha=1}^sP_\alpha\delta{Q}_\alpha\right)\\\\
=&\frac{\mathrm{d}}{\mathrm{d}t}\left(\delta U\right)=\delta\left(\frac{\mathrm{d}}{\mathrm{d}t}U\right)=\delta\dot{U}\\\\
=&\delta\left[\sum_{\alpha=1}^s\left(p_\alpha\dot{q}_\alpha-P_\alpha\dot{Q}_\alpha\right)\right]+\delta\left(H^*-H\right)\\\\
=&\delta\left(\sum_{\alpha=1}^sp_\alpha\dot{q}_\alpha\right)-\delta\left(\sum_{\alpha=1}^sP_\alpha\dot{Q}_\alpha\right)+\delta H^*-\delta H
\end{aligned}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;移项可得

$$
\delta\left(\sum_{\alpha=1}^sp_\alpha\dot{q}_\alpha\right)-\frac{\mathrm{d}}{\mathrm{d}t}\left(\sum_{\alpha=1}^sp_\alpha\delta{q}_\alpha\right)-\delta H=\delta\left(\sum_{\alpha=1}^sP_\alpha\dot{Q}_\alpha\right)-\frac{\mathrm{d}}{\mathrm{d}t}\left(\sum_{\alpha=1}^sP_\alpha\delta{Q}_\alpha\right)-\delta H^*
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;而

$$
\begin{aligned}
&\delta\left(\sum_{\alpha=1}^sp_\alpha\dot{q}_\alpha\right)-\frac{\mathrm{d}}{\mathrm{d}t}\left(\sum_{\alpha=1}^sp_\alpha\delta{q}_\alpha\right)-\delta H\\\\
=&\sum_{\alpha=1}^s\left(\dot{q}_\alpha\delta p_\alpha-\dot{p}_\alpha\delta q_\alpha\right)-\delta H
=\sum_{\alpha=1}^s\left(\frac{\partial H}{\partial p_\alpha}\delta p_\alpha+\frac{\partial H}{\partial q_\alpha}\delta q_\alpha\right)-\delta H=0
\end{aligned}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;故

$$
\begin{aligned}
&\delta\left(\sum_{\alpha=1}^sP_\alpha\dot{Q}_\alpha\right)-\frac{\mathrm{d}}{\mathrm{d}t}\left(\sum_{\alpha=1}^sP_\alpha\delta{Q}_\alpha\right)-\delta H^*\\\\
=&\sum_{\alpha=1}^s\left(\dot{Q}_\alpha\delta P_\alpha-\dot{P}_\alpha\delta Q_\alpha\right)-\delta H^*\\\\
=&\sum_{\alpha=1}^s\left(\dot{Q}_\alpha-\frac{\partial H^*}{\partial P_\alpha}\right)\delta P_\alpha+\sum_{\alpha=1}^s\left(-\dot{P}_\alpha-\frac{\partial H^*}{\partial Q_\alpha}\right)\delta q_\alpha=0
\end{aligned}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;因此有

$$
\left\{
\begin{aligned}
\dot{P}_\alpha&=-\frac{\partial H^*}{\partial Q_\alpha}\\\\
\dot{Q}_\alpha&=\frac{\partial H^*}{\partial P_\alpha}
\end{aligned}
\right.
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;与原正则方程形式相同。故得证

* 对于(5.8.0)式，若将$$U$$写作$$q$$、$$Q$$和$$t$$的函数，则有

$$
\begin{aligned}
&\sum_{\alpha=1}^s\left(p_\alpha\mathrm{d} q_\alpha-P_\alpha\mathrm{d} Q_\alpha\right)-\left(H-H^*\right)\mathrm{d}t=\mathrm{d}U\left(q,Q,t\right)\\\\
=&\sum_{\alpha=1}^s\left(\frac{\partial U}{\partial q_\alpha}\mathrm{d}q_\alpha+\frac{\partial U}{\partial Q_\alpha}\mathrm{d}Q_\alpha\right)+\frac{\partial U}{\partial t}\mathrm{d}t
\end{aligned}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;因此有

$$
\left\{
\begin{aligned}
&p_\alpha=\frac{\partial U}{\partial q_\alpha},\ \ \ 
P_\alpha=-\frac{\partial U}{\partial Q_\alpha}\ \ \ \left(\alpha=1,2,\dotsb,s\right)\\\\
&H^*-H=\frac{\partial U}{\partial t}
\end{aligned}
\right.
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在这里$$U\left(q,Q,t\right)$$被称为母函数。根据母函数的表达式，结合上式即可求出变换方程

* 若$$P_\alpha$$、$$Q_\alpha$$和$$H$$的表达式中均不显含$$t$$，则正则变换的条件可简化为

$$
\sum_{\alpha=1}^s\left(p_\alpha\mathrm{d} q_\alpha-P_\alpha\mathrm{d} Q_\alpha\right)=0
$$

* 若经过正则变换后，新的哈密顿函数$$H^*$$只是变量$$P_1,P_2,\dotsb,P_s$$和时间$$t$$的函数，即

$$
H^*=H^*\left(P_1,P_2,\dotsb,P_s\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;则可知$$\dot{P}_\alpha=0\left(\alpha=1,2,\dotsb,s\right)$$，即力学体系的$$s$$个$$P_\alpha$$均为常数。同时可利用

$$
Q_\alpha=\int\frac{\partial H^*}{\partial P_\alpha}\mathrm{d}t\ \ \ \ \ \left(\alpha=1,2,\dotsb,s\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;求解出广义坐标$$Q_\alpha$$，则可将力学体系的问题完全解决

* 通过选择合适的母函数可以使得许多坐标成为循环坐标，进而简化运算（主要是消除$$q_\alpha$$）

[返回目录](#5.0) [返回总目录](#0.0)

---

### <h59 id='5.9'> §5.9 哈密顿-雅克比理论</h59>

[返回目录](#5.0) [返回总目录](#0.0)

* 通过选取主函数$$S=\int L\mathrm{d}t$$作为母函数进行正则变换，则有$$p_\alpha=\frac{\partial S}{\partial q_\alpha}$$，且由于

$$
\frac{\mathrm{d}S}{\mathrm{d}t}=\frac{\partial S}{\partial t}+\sum_{\alpha=1}^s\frac{\partial S}{\partial q_\alpha}\frac{\partial q_\alpha}{\partial t}=\frac{\partial S}{\partial t}+\frac{\partial S}{\partial q_\alpha}\dot{q}_\alpha=\frac{\partial S}{\partial t}+\sum_{\alpha=1}^sp_\alpha\dot{q}_\alpha
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;和

$$
H=-L+\sum_{\alpha=1}^sp_\alpha\dot{q}_\alpha
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;有

$$
\begin{aligned}
H^*&=\frac{\partial U}{\partial t}+H=\frac{\partial S}{\partial t}+H\left(t;q_1,q_2,\dotsb,q_s;\frac{\partial S}{\partial q_1},\frac{\partial S}{\partial q_2},\dotsb,\frac{\partial S}{\partial q_s}\right)\\\\
&=\frac{\mathrm{d}S}{\mathrm{d}t}-\sum_{\alpha=1}^sp_\alpha\dot{q}_\alpha+\left[-L\left(t;q_1,q_2,\dotsb,q_s;\frac{\partial S}{\partial q_1},\frac{\partial S}{\partial q_2},\dotsb,\frac{\partial S}{\partial q_s}\right)+\sum_{\alpha=1}^sp_\alpha\dot{q}_\alpha\right]\\\\
&=\frac{\mathrm{d}S}{\mathrm{d}t}-L\left(t;q_1,q_2,\dotsb,q_s;\frac{\partial S}{\partial q_1},\frac{\partial S}{\partial q_2},\dotsb,\frac{\partial S}{\partial q_s}\right)=0
\end{aligned}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;即构造了一个恒等于零的哈密顿量。该方程被称为哈密顿-雅可比偏微分方程，简称哈-雅方程

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;若哈-雅方程已知，则可由哈-雅方程求出$$S$$，然后利用

$$
p_i=\frac{\partial S}{\partial q_i},\ \ \ Q_i=\frac{\partial S}{\partial P_i}\ \ \ \left(i=1,2,\dotsb,s\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;求出$$p_i$$和$$Q_i$$，即可得到全部的积分

* 若体系的哈密顿量不随时间变化，即$$H=E$$，则有

$$
\frac{\partial S}{\partial t}=-H=-E
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;将上式对$$t$$积分，则有

$$
S=-Et+W\left(q_1,q_2\dotsb,q_s;P_1,P_2,\dotsb,P_s;E\right)+C
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中$$W$$为一不显含$$t$$的新函数，称为哈密顿-雅克比特性函数，有

$$
\frac{\partial S}{\partial q_\alpha}=\frac{\partial W}{\partial q_\alpha}\ \ \ \ \ \left(\alpha=1,2,\dotsb,s\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;故有

$$
H\left(q_1,q_2,\dotsb,q_s;\frac{\partial W}{\partial q_1},\frac{\partial W}{\partial q_2},\dotsb,\frac{\partial W}{\partial q_s}\right)=E
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;若上式可以写为如下形式

$$
\begin{aligned}
H=&\frac{1}{2}\left[A_1\left(q_1\right)\left(\frac{\mathrm{d}W_1}{\mathrm{d}q_1}\right)^2+A_2\left(q_2\right)\left(\frac{\mathrm{d}W_2}{\mathrm{d}q_2}\right)^2+\dotsb+A_1\left(q_s\right)\left(\frac{\mathrm{d}W_s}{\mathrm{d}q_s}\right)^2\right]\\\\
&+\left[V_1\left(q_1\right)+V_2\left(q_2\right)+\dotsb+V_s\left(q_s\right)\right]=E
\end{aligned}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;则由于各个$$q_\alpha$$均为独立变量，有

$$
\left\{
\begin{aligned}
\frac{1}{2}A_\alpha\left(q_\alpha\right)\left(\frac{\mathrm{d}W_\alpha}{\mathrm{d}q_\alpha}\right)^2+V\left(q_\alpha\right)&=a_\alpha\ \ \ \ \ \left(\alpha=1,2,\dotsb,s\right)\\\\
a_1+a_2+\dotsb+a_s&=E
\end{aligned}
\right.
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;若每一个$$W_\alpha$$均已求出，则$$W=W_1+W_2+\dotsb+W_s$$，进而

$$
\left\{
\begin{aligned}
\frac{\partial W}{\partial q_\alpha}&=\frac{\partial S}{\partial q_\alpha}=p_\alpha\ \ \ \ \ \left(i=1,2,\dotsb,s\right)\\\\
\frac{\partial W}{\partial E}&=t+\frac{\partial S}{\partial E}=t-t_0\\\\
\frac{\partial W}{\partial P_\alpha}&=\frac{\partial S}{\partial P_\alpha}=Q_\alpha\ \ \ \ \ \left(\alpha=1,2,\dotsb,s\right)
\end{aligned}
\right.
$$

* 对于一般的情况，设哈-雅方程中只有某一坐标$$q_i$$和它相对应的微商$$\frac{\partial S}{\partial q_i}$$以某种形式的组合$$\varphi\left(q_i,\frac{\partial S}{\partial q_i}\right)$$的形式出现，即

$$
H^*=\Phi\left[t;q_1,\dotsb,q_{i-1},q_{i+1}\dotsb,q_s;\frac{\partial S}{\partial t};\frac{\partial S}{\partial q_1},\dotsb,\frac{\partial S}{\partial q_{i-1}},\frac{\partial S}{\partial q_{i+1}},\dotsb,\frac{\partial S}{\partial q_s};\varphi\left(q_i,\frac{\partial S}{\partial q_i}\right)\right]=0
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;在这种情况下，我们寻找如下形式的解

$$
S=S_i\left(q_i\right)+S'\left(t;q_1,\dotsb,q_{i-1},q_{i+1},\dotsb,q_s\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;结合上述二式，有

$$
\Phi\left[t;q_1,\dotsb,q_{i-1},q_{i+1}\dotsb,q_s;\frac{\partial S}{\partial t};\frac{\partial S'}{\partial q_1},\dotsb,\frac{\partial S'}{\partial q_{i-1}},\frac{\partial S'}{\partial q_{i+1}},\dotsb,\frac{\partial S'}{\partial q_s};\varphi\left(q_i,\frac{\partial S_i}{\partial q_i}\right)\right]=0
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;上式为恒等式，因此$$\varphi$$本身为常数，则有

$$
\left\{
\begin{aligned}
&\varphi\left(q_i,\frac{\partial S_i}{\partial q_i}\right)=\alpha_i\\\\
&\Phi\left(t,q_1,\dotsb,q_{i-1},q_{i+1}\dotsb,q_s;\frac{\partial S'}{\partial q_1},\dotsb,\frac{\partial S'}{\partial q_{i-1}},\frac{\partial S'}{\partial q_{i+1}},\dotsb,\frac{\partial S'}{\partial q_s};\alpha_i\right)=0
\end{aligned}
\right.
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;其中第一个方程为常微分方程，函数$$S_i\left(q_i\right)$$可通过简单的积分求出

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;继续运用该方法，则可分离出所有的坐标与时间，进而通过积分求解

* 对于循环坐标，函数$$\varphi\left(q_i,\frac{\partial S}{\partial q_i}\right)$$变为只含$$\frac{\partial S}{\partial q_i}$$，因此有$$S_i=\alpha_i q_i$$，因此有

$$
S=\alpha_i q_i+S'\left(t;q_1,\dotsb,q_{i-1},q_{i+1},\dotsb,q_s\right)
$$

* 对于球坐标问题，例如电子运动问题，动能可以表示为

$$
T=\frac{1}{2m}\left(p_r^2+\frac{p_\theta^2}{r^2}+\frac{p_\phi^2}{r^2\sin^2\theta}\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;势能表示为

$$
V=a\left(r\right)+\frac{b\left(\theta\right)}{r^2}
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;则函数$$W$$的哈-雅方程为

$$
\frac{1}{2m}\left(\frac{\partial W}{\partial r}\right)^2+a\left(r\right)+\frac{1}{2mr^2}\left[\left(\frac{\partial W}{\partial \theta}\right)^2+2mb\left(\theta\right)\right]+\frac{1}{2mr^2\sin^2\theta}\left(\frac{\partial W}{\partial \varphi}\right)^2=E
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;由于$$\varphi$$是循环坐标，故所求的解具有下列形式

$$
S=-Et+p_\varphi\varphi+W_1\left(r\right)+W_2\left(\theta\right)
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;对于$$W_1\left(r\right))$$和$$W_2\left(\theta\right)$$，有

$$
\left\{
\begin{aligned}
\left(\frac{\mathrm{d}W_2}{\mathrm{d}\theta}\right)^2+2mb\left(\theta\right)+\frac{p_\varphi^2}{\sin^2\theta}=\alpha_2\\\\
\frac{1}{2m}\left(\frac{\mathrm{d}W_1}{\mathrm{d}r}\right)^2+a\left(r\right)+\frac{\alpha_2}{2mr^2}=E
\end{aligned}
\right.
$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;积分可得

$$
S=-Et+p_\varphi\varphi+\int\sqrt{\alpha_2-2mb\left(\theta\right)-\frac{p_\varphi^2}{\sin^2\theta}}\mathrm{d}\theta+\int\sqrt{2m\left[E-a\left(r\right)-\frac{\alpha_2}{r^2}\right]}\mathrm{d}r
$$90

[返回目录](#5.0) [返回总目录](#0.0)

---

### <h510 id='5.10'> §*5.10 相积分与角变数</h510>

[返回目录](#5.0) [返回总目录](#0.0)

* 有时间再整理吧

[返回目录](#5.0) [返回总目录](#0.0)

---

### <h511 id='5.11'> §*5.11 刘维尔定理</h511>

[返回目录](#5.0) [返回总目录](#0.0)

* 有时间再整理吧

[返回目录](#5.0) [返回总目录](#0.0)

---