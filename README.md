# Team RNX ɑ

## RustFi Hackathon - Challenge 4

### In search of Alpha with Rust: Design an Algo Trading 
strategy with most Alpha***

### Goal

A system which can yield/provide asset-specific recommendations of an ideal set of parameters via evolutionary computation (more specifically using genetic algorithms for optimization) for any given indicator-based signal (either pre-defined or user-designed), based on the performance of the strategy over the historical data of the concerned asset (i.e. w/ backtesting).

---

# How-To Guide

Simply run the `main.py` file



---

# Notes

<aside>
❕ **Signal:** The implementation of the trading strategy involving an indicator.

</aside>

- Any given technical indicator has a set of parameters which require their values to be specified
- The set of all possible values for a TIs set of parameters is called the **search space**
- The introduction of a new parameter results in an additional dimension being added to said **search space**. This causes the required computational time of running to increase exponentially (with each additional new param - dim)
- Genetic algorithms are a subclass of evolutionary algorithms and are widely used for optimization probs

# Compelling Reasons

- Keyrock are keen/enthusiatic/investigating/blabla on using evolutionary computing for their market making trading. That is (just my) impression after doing some online investigation.

## Misc

- Evolutionary computing (i.e. genetic algos) however is simply a means of optimizing (the parameters of) a trading strategy. I.e. a trading strategy that uses the RSI technical indicator entails having to assign values to the RSI  "overbought" & "oversold" parameters (typically 70 & 30 respectively).

## Solution Search Space

Searching through the solution space (AKA search space) involves 2 kinds/types of searches:

1. Local Search
    1. A more reserved search procedure which is mostly confined to the surroundings of the current best solution.
    2. This, in the context of `Genetic Algorithms`, is achieved via the use of the `Crossover` operator
2. Global Search
    1. A more comprehensive searching procedure spanning the complete domain.
    2. This, in the context of `Genetic Algorithms`, is achieved via the use of the `Mutation` operator

## Objective Function (OF)

This is the function which has to be optimized as per a/the problem statement

$\text{F(x)}$

## Fitness Function

- Is derived from the **objective function**
- Is used to evaluate each individual formed during the procedure and forms the basis for Natural Selection.

$\text{f(x)}$

## Problem Statement

If the problem statement involves

- **maximisation** of the **objective function**
    
    take the **fitness function** to be the same as the **objective function**
    
    $\text{f(x)}=\text{F(x)}$
    
- **minimisation** of the **objective function**
    
    convert the problem statement into one involving **maximisation** by first taking the reciprocal of the **objective function,** $\text{F(x)}$, with + 1 to it in the denominator to account for the **objective function** being = to 0 at some points) and then taking this modified **objective function** as the **fitness function**
    
    $\text{f(x)}=\frac{1}{1+\text{F(x)}}$
    

## Genetic Algorithm *Operators*

### Selection

- Fundemental principle of *Natural Selection:* “*A Fitter individual has a higher survival duration and is more suited for the environment.”*
- Is used to identify *individuals* from the current lot, who are more likely to contribute to the development of the final solution (fittest individual).
- Each *individual* is ranked based on their *fitness value* which is obtained from the **fitness function**
- Lastly, a few of the top *individuals* are selected for use in order to further offspring formation & to keep the *evolution* continuing with going on.
