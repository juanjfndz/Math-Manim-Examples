#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This script defines a Manim scene called ODEScene, which animates the derivation
of the solution to the first-order ordinary differential equation of the form
y' + ay = b using the method of integrating factors.
"""

from manim import *

class ODEScene(Scene):
    """
    This class defines a Manim scene for animating the derivation of the solution
    to the differential equation y' + ay = b using the method of integrating factors.
    """

    def construct(self):
        """
        Animates the derivation of the solution to the differential equation y' + ay = b
        using the method of integrating factors.
        """

        # Define the steps for the animation
        eq_list = [
            MathTex(r''),
            MathTex(r"y'", r"+", r"ay", r"=",  r"b"),
            MathTex(r"\frac{dy}{dx}", r"+", r"ay", r"=", r"b"), 
            MathTex(r"dx", r"\left(\frac{dy}{dx} + a\right)", r"y", r"=", r"b dx"), 
            MathTex(r"dx", r"\frac{dy}{dx}", r"+", r"adx", r"y", r"=", r"b dx"), 
            MathTex(r"\int", r"\frac{dy}{dx}", r"dx", r"+", r"\int", r"ay", r"dx", r"=", r"\int", r"b", r"dx"),
            MathTex(r"y(x)", r"=", r"e^{-ax}", r"\left(C", r"+", r"\frac{b}{a}", r"\right)"),
            MathTex(r"y(x)", r"=", r"\frac{b}{a}", r"+", r"C", r"e^{-ax}"), 
            MathTex(r"y(0)", r"=", r"\frac{b}{a}", r"+", r"C", r"e^{0}"), 
            MathTex(r"C", r"=", r"y(0)", r"-", r"\frac{b}{a}"), 
            MathTex(r"y(x)", r"=", r"\frac{b}{a}", r"+", r"y(0)", r"e^{-ax}", r"-", r"\frac{b}{a}", r"e^{-ax}"), 
            MathTex(r"y(x)", r"=", r"\frac{b}{a}", r"\left( 1 - e^{-ax} \right)", r"+", r"y(0)", r"e^{-ax}")
        ] 
        
        # Play the animation step by step
        for i in range(1, len(eq_list)):
            self.play(TransformMatchingTex(eq_list[i-1], eq_list[i]))
            self.wait()
