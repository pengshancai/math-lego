# Math-Lego 迈思乐高

### Build up your patterns using Lego pieces bsaed on Python！

When I was in my teens, I used to have a big box of Lego. 
Based on thousands of simple Lego pieces,  I build my world of 
knights, wizards, princesses，explorers, pirates and monsters.

Decades later, as a computer science student, I am obsessed with the question: 
Would it be possible to use Python to create a set of Lego pieces, 
based on which people could easily create complex and beautiful patterns.

I'd like to present my answer so far.

### Introduction
No matter how splendid the Lego world is, 
it is build from very simple Lego pieces.

Likewise, our Math-Lego is based on three simple Math-Lego pieces: 
**Constant Bender**, **Linear Bender** and **Sin Bender**.
The shape of each piece is restricted by a different type of derivative. 
By combining these simple Math-Lego pieces together, 
you may create complex and beautiful patterns on a **Matplotlib** "paper".

### Basic Math-Lego Pieces

#### Constant Bender
<img src="https://raw.githubusercontent.com/pengshancai/math-lego/master/imgs/paint_const.png" alt="Constant Bender" width="360" align="middle"/>

**Constant Bender** let you create a curved line with a constant curvature. 
You may adjust the curvature to create a more curved line.

#### Sin Bender
<img src="https://raw.githubusercontent.com/pengshancai/math-lego/master/imgs/paint_sin.png" alt="Sin Bender" width="360" align="middle"/>

The curvature of a **Sin Bender** is a sinusoid. 
I.e. the curvature gradually increases to reach a peak, 
and then gradually falls back.
It is usually applied to create a sharp curve.

#### Linear Bender

<img src="https://raw.githubusercontent.com/pengshancai/math-lego/master/imgs/paint%20linear.png" alt="Linear Bender" width="360" align="middle"/>

A continuous line would usually look more beautiful it is smooth 
(i.e. No abrupt change in curvature)
This requires the function of the line to be differentiable, which means the derivative of the function is continuous. 

The curvature of a **Linear Bender** is a linear function, 
(i.e. the curvature gradually changes from one constant value to another constant value)
Linear Bender could be applied to connect two Math-Lego pieces of different curvature, making the transformation look more smooth. 
（As shown in the above 
It could also be applied to create a line with different curvature at different points.

### Customize your own Math-Lego pieces

You may customize your own Math-Lego pieces by tuning its 
length, width, curvature and color.

By putting your customized Math-Lego pieces together, you could create 
images as such

<img src="https://raw.githubusercontent.com/pengshancai/math-lego/master/imgs/fish.png" alt="sun shine" width="360" align="middle"/>


### Advanced Math-Lego Pieces

In addition to simple Math-Lego pieces, 
we also offer some advanced Math-Lego pieces.
(For now only one, as the semester is about to start 
and the author has other works to do.)
The advanced Math-Lego pieces are made from simple Math-Lego pieces, 
but encapsulated in a way that is easy to be called by users.

<img src="https://raw.githubusercontent.com/pengshancai/math-lego/master/imgs/sunshine.png" alt="sun shine" width="360" align="middle"/>

As shown above, the sunshine Math-Lego piece is made from 
a constant bender and a linear bender.

If combining multiple sunshine Math-Lego pieces in a circular manner, 
we could get the following pattern:

<img src="https://raw.githubusercontent.com/pengshancai/math-lego/master/imgs/sun.png" alt="sun shine" width="360" align="middle"/>

You may also write other advanced Math-Lego pieces by yourself!

### Further into art 

Try exploring other ways to use the Math-Lego on more challenging patterns!

Here is one of my explorations! 

This is an attampt to mimic the Chinese calligraphy of the Chinese character "晴" 
(which stands for "sunny")

Here is the a calligraphy by a human calligrapher:

<img src="https://raw.githubusercontent.com/pengshancai/math-lego/master/imgs/sunny.gif" alt="sun shine" width="360" align="middle"/>

Here is the Math-Lego version:

<img src="https://raw.githubusercontent.com/pengshancai/math-lego/master/imgs/sunny%20function.png" alt="sun shine" width="360" align="middle"/>

You may also see the video of how the painting was done [here]((https://www.youtube.com/watch?v=cLr12miy4nE&feature=youtu.be)))

### Dependencies

 * Python 3
 * Numpy = 1.17.0
 * Matplotlib = 3.1.1
 * Pandas = 0.25.1

### Running instructions

Simply cd into the folder and do 

```
python sunny.py
```

### Contact

Please contact me through pengshancai@umass.edu

Finally, wish you have a sunny day!

<img src="https://raw.githubusercontent.com/pengshancai/math-lego/master/imgs/wish%20you%20have%20a%20sunny%20day.png" alt="sun shine" width="600" align="middle"/>


