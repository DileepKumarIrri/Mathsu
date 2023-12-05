from manim import *

class OneStrokeProblem(Scene):
    
    def lines(self):
        A = Text("A").scale(0.6).move_to([-2.2,-2.2,0])  
        self.add(A)
        B = Text("B").scale(0.6).move_to([2.2,2.2,0])  
        self.add(B)
        lines = [
            Line(start=[-2,2,0],end=[-1,2,0]),#第一行
            Line(start=[-1,2,0],end=[1,2,0]),
            Line(start=[1,2,0],end=[2,2,0]),
            Line(start=[-1,1,0],end=[0,1,0]),#第二行
            Line(start=[0,1,0],end=[1,1,0]),
            Line(start=[-2,0,0],end=[-1,0,0]),#第三行
            Line(start=[1,0,0],end=[2,0,0]),
            Line(start=[-1,-1,0],end=[0,-1,0]),#第四行
            Line(start=[0,-1,0],end=[1,-1,0]),
            Line(start=[-2,-2,0],end=[-1,-2,0]),#第五行
            Line(start=[-1,-2,0],end=[1,-2,0]),
            Line(start=[1,-2,0],end=[2,-2,0]),
            Line(start=[-2,2,0],end=[-2,0,0]),#第一列
            Line(start=[-2,0,0],end=[-2,-2,0]),
            Line(start=[-1,2,0],end=[-1,1,0]),#第二列
            Line(start=[-1,1,0],end=[-1,0,0]),
            Line(start=[-1,0,0],end=[-1,-1,0]),
            Line(start=[-1,-1,0],end=[-1,-2,0]),
            Line(start=[0,-1,0],end=[0,1,0]),#第三列
            Line(start=[1,2,0],end=[1,1,0]), #第四列
            Line(start=[1,1,0],end=[1,0,0]),
            Line(start=[1,0,0],end=[1,-1,0]),
            Line(start=[1,-1,0],end=[1,-2,0]),
            Line(start=[2,2,0],end=[2,0,0]),#第五列
            Line(start=[2,0,0],end=[2,-2,0]),
        ]
        for line in lines:
            self.add(line)
        self.wait(1)
        return lines

    def dots(self):
        dots =[
                Dot([-1,2,0]).set_color(RED),#第一行
                Dot([1,2,0]).set_color(RED),
                Dot([-1,1,0]).set_color(RED),#第二行
                Dot([0,1,0]).set_color(RED),
                Dot([1,1,0]).set_color(RED),
                Dot([-2,0,0]).set_color(RED),#第三行
                Dot([-1,0,0]).set_color(RED),
                Dot([1,0,0]).set_color(RED),
                Dot([2,0,0]).set_color(RED),
                Dot([-1,-1,0]).set_color(RED),#第4行
                Dot([0,-1,0]).set_color(RED),
                Dot([1,-1,0]).set_color(RED),
                Dot([-1,-2,0]).set_color(RED),#第5行
                Dot([1,-2,0]).set_color(RED),
            ] 
        for dot in dots:
            self.add(dot)
        self.wait(1)
        return dots
    
    def construct(self):
        # # 创建标题
        # title = Text("The Longest Path Puzzle: A Mathematical Adventure from A to B").scale(0.6)
        # self.play(Write(title))
        # self.wait(1)
        # self.play(FadeOut(title))


        # # 解释一笔画的条件
        # conditions = VGroup(
        #     Text("1. The shape must be a connected graph"),
        #     Text("2. The number of odd points "),
        # ).scale(0.5).arrange(DOWN, aligned_edge=LEFT)
        # self.play(Write(conditions))
        # self.wait(2)
        # self.play(FadeOut(conditions))

        lines = self.lines()
        self.wait(10)
        dots = self.dots()
        self.wait(3)
        a = Dot([-2,-2,0]).set_color(BLUE)
        self.add(a)
        b = Dot([2,2,0]).set_color(BLUE)
        self.add(b)
        self.wait(3)

        self.blink_and_fade_out(lines[9])
        self.fade_out([dots[12],a])

        self.blink_and_fade_out(lines[5])
        self.fade_out([dots[5],dots[6]])
        
        self.blink_and_fade_out(lines[14])
        self.fade_out([dots[0],dots[2]])
        
        self.blink_and_fade_out(lines[2])
        self.fade_out([dots[1],b]) 

        self.blink_and_fade_out(lines[4])
        self.fade_out([dots[3],dots[4]])

        self.blink_and_fade_out(lines[6])
        self.fade_out([dots[7],dots[8]])

        self.blink_and_fade_out(lines[7])
        self.fade_out([dots[9],dots[10]])

        
        self.blink_and_fade_out(lines[22])
        self.fade_out([dots[11],dots[13]])
        
        self.wait(1)
        
    def blink_and_fade_out(self, obj):
        self.play(AnimationGroup(FadeOut(obj),FadeIn(obj),lag_ratio=0.5))
        self.wait(1)
        self.play(FadeOut(obj)) 
    def fade_out(self, objs):
        for obj in objs:
            self.play(FadeOut(obj))
        self.wait(1)