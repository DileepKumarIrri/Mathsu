from manim import *


class CircleOfNumbers(Scene):
    def construct(self):
        
         # 创建六个数
        numbers = [Tex(str(i)) for i in ['a', 'b', 'c', 'd', 'e', 'f']]

        # 将六个数排成一排
        numbers_in_line = VGroup(*numbers).arrange(RIGHT)
        self.play(Write(numbers_in_line))
        self.wait(1)

        # 将六个数围成一个圈
        circle = Circle(radius=1.9)
        self.play(Create(circle))
        self.wait(1)
        
        letter_circle = Circle(radius=2.1)
        
        # 将每个数移动到圆上的对应位置
        for i, number in enumerate(numbers):
            angle = - i * TAU / 6 + PI/2
            new_position = letter_circle.point_at_angle(angle)
            self.play(number.animate.move_to(new_position))
        
        self.wait(3)
        
        circle_num = Circle(radius=2.5)

        # 第四号位要能被四整除
        n1 = Tex('(1)')
        n1.move_to(circle_num.point_at_angle(PI/2))
        self.play(Create(n1))

        curved_arrow_ccw = CurvedArrow(start_point=circle_num.point_at_angle(PI/2+PI/10), end_point=circle_num.point_at_angle(3*PI/2-PI/10),radius=2.5)
        self.play(Create(curved_arrow_ccw))
        self.wait(1)
        
        n4 = Tex('(4)')
        n4.move_to(circle_num.point_at_angle(3*PI/2))
        self.play(Create(n4))
        
        curved_arrow_cw = CurvedArrow(start_point=circle_num.point_at_angle(PI/2-PI/10), end_point=circle_num.point_at_angle(3*PI/2+PI/10),angle=-2.5,color=RED)
        self.play(Create(curved_arrow_cw))
        self.wait(1)
        
        n4.set_color(RED)
        
        self.wait(1)

        group = Group(n1,n4,curved_arrow_ccw,curved_arrow_cw)
        for i in range(5):
            self.play(Rotate(group,angle=-TAU/6))
            self.wait(1)
        
        self.play(FadeOut(group))
       
        rule_1 = Tex('1: all of a, b, c, d, e, f must be divisible by 4') 
        rule_1.move_to([-2.0,3.5,0])
        self.play(Create(rule_1))
        self.wait(1)
        
        
        # 第三位和第六位可以被三整除
        n1 = Tex('(1)')
        n1.move_to(circle_num.point_at_angle(PI/2))
        self.play(Create(n1))

        curved_arrow_ccw = CurvedArrow(start_point=circle_num.point_at_angle(PI/2+PI/10), end_point=circle_num.point_at_angle(PI/2+TAU/6-PI/10),radius=2.5)
        self.play(Create(curved_arrow_ccw))
        self.wait(1) 

        
        n3 = Tex('(3)')
        n3.move_to(circle_num.point_at_angle(2*TAU/6+ PI/2))
        self.play(Create(n3))

        n6 = Tex('(6)')
        n6.move_to(circle_num.point_at_angle(5*TAU/6+ PI/2))
        self.play(Create(n6))

        curved_arrow_cw = CurvedArrow(start_point=circle_num.point_at_angle(PI/2-PI/10), end_point=circle_num.point_at_angle(PI/2-TAU/6+PI/10),radius=-2.5,color=RED)
        self.play(Create(curved_arrow_cw))
        self.wait(1) 

        
        n3_cw = Tex('(3)',color=RED)
        n3_cw.move_to(circle_num.point_at_angle(-2*TAU/6+ PI/2))
        self.play(Create(n3_cw))

        n6_cw = Tex('(6)',color=RED)
        n6_cw.move_to(circle_num.point_at_angle(-5*TAU/6+ PI/2))
        self.play(Create(n6_cw))
        
        rule_2_text = [
            MathTex(r'(b,e) \mid 3 \quad or \quad (c,f) \mid 3', font_size=35).move_to([-5.2,0.4,0]),
            MathTex(r'(a,d) \mid 3 \quad or \quad (c,f) \mid 3', font_size=35).move_to([-5.2,0.0,0]),
            MathTex(r'(b,e) \mid 3 \quad or \quad (a,d) \mid 3', font_size=35).move_to([-5.2,-0.4,0]),
        ]
        self.play(Create(rule_2_text[0]))
        self.wait(1)

        rule_2_group = Group(n1,n3,n3_cw,n6,n6_cw,curved_arrow_ccw,curved_arrow_cw)
        for i in range(5):
            self.play(Rotate(rule_2_group,angle=-TAU/6,about_point=[0,0,0]))
            self.wait(1)
            self.play(Create(rule_2_text[(i+1)%3]))
            self.wait(1)
        
        self.play(FadeOut(rule_2_group))
        self.wait(1)
        
        rec = Rectangle(height=2,width=3.8)
        rec.move_to([-5.2,0,0])
        self.play(Create(rec))
        self.wait(1)
        
        arrow = Arrow([-5.2,0.8,0],[-5.2,2.8,0])
        self.play(Create(arrow))
        self.wait(1)
        
        rule_1 = Tex('2: b,c,e,f must be divisible by 3') 
        rule_1.move_to([-3.435,3.1,0])
        self.play(Create(rule_1))
        self.wait(1)
        
        rule_2_group = Group(rule_2_text[0],rule_2_text[1],rule_2_text[2],arrow,rec)
        self.play(FadeOut(rule_2_group))
        self.wait(1)


        # 第五位被五整除
        n1 = Tex('(1)')
        n1.move_to(circle_num.point_at_angle(PI/2))
        self.play(Create(n1))

        curved_arrow_ccw = CurvedArrow(start_point=circle_num.point_at_angle(PI/2+PI/10), end_point=circle_num.point_at_angle(PI/2+TAU/6-PI/10),radius=2.5)
        self.play(Create(curved_arrow_ccw))
        self.wait(1) 
        
        
        n5 = Tex('(5)')
        n5.move_to(circle_num.point_at_angle(4*TAU/6+ PI/2))
        self.play(Create(n5))


        curved_arrow_cw = CurvedArrow(start_point=circle_num.point_at_angle(PI/2-PI/10), end_point=circle_num.point_at_angle(PI/2-TAU/6+PI/10),radius=-2.5,color=RED)
        self.play(Create(curved_arrow_cw))
        self.wait(1) 

        
        n5_cw = Tex('(5)',color=RED)
        n5_cw.move_to(circle_num.point_at_angle(-4*TAU/6+ PI/2))
        self.play(Create(n5_cw))

        rule_3_text = [
            MathTex(r'c \mid 5 \quad or \quad e \mid 5', font_size=35).move_to([-5.5,0.8,0]),
            MathTex(r'd \mid 5 \quad or \quad f \mid 5', font_size=35).move_to([-5.5,0.4,0]),
            MathTex(r'a \mid 5 \quad or \quad e \mid 5', font_size=35).move_to([-5.5,0.0,0]),
            MathTex(r'b \mid 5 \quad or \quad f \mid 5', font_size=35).move_to([-5.5,-0.4,0]),
            MathTex(r'a \mid 5 \quad or \quad c \mid 5', font_size=35).move_to([-5.5,-0.8,0]),
            MathTex(r'b \mid 5 \quad or \quad d \mid 5', font_size=35).move_to([-5.5,-1.2,0]),
        ]
        self.play(Create(rule_3_text[0]))
        self.wait(1)

        rule_3_group = Group(n1,n5,n5_cw,curved_arrow_ccw,curved_arrow_cw)
        for i in range(5):
            self.play(Rotate(rule_3_group,angle=-TAU/6,about_point=[0,0,0]))
            self.wait(1)
            self.play(Create(rule_3_text[i+1]))
            self.wait(1)
            
        self.play(FadeOut(rule_3_group))
        self.wait(1)
        
        rec = Rectangle(height=2.5,width=2.8)
        rec.move_to([-5.5,-0.2,0])
        self.play(Create(rec))
        self.wait(1)
        
        arrow = Arrow([-5.8,0.8,0],[-5.8,2.8,0])
        self.play(Create(arrow))
        self.wait(1)
        
        rule_1 = Tex('3: a,b,c,d must be divisible by 5') 
        rule_1.move_to([-3.335,2.7,0])
        self.play(Create(rule_1))
        self.wait(1)

        rule_3_group = Group(rule_3_text[0],rule_3_text[1],rule_3_text[2],rule_3_text[3],rule_3_text[4],rule_3_text[5],arrow,rec)
        self.play(FadeOut(rule_3_group))
        self.wait(1)
        
        rec = Rectangle(height=1.0,width=7.3)
        rec.move_to([-3.4,2.9,0])
        self.play(Create(rec))
        self.wait(1)
        
        
        arrow = Arrow([-5.2,2.6,0],[-5.2,0.8,0])
        self.play(Create(arrow))
        self.wait(1)
        
        self.play(FadeOut(rec))
        
        math_tex = MathTex(r'e \mid 3 \quad and \quad f \mid 3', font_size=35).move_to([-5.5,0.8,0])
        self.play(Create(math_tex))
        self.wait(1)
        math_tex = MathTex(r'a \mid 5 \quad and \quad d \mid 5', font_size=35).move_to([-5.5,0.4,0])
        self.play(Create(math_tex))
        self.wait(1)
        math_tex = MathTex(r'b \mid 15 \quad and \quad c \mid 15', font_size=35).move_to([-5.4,0.0,0])
        self.play(Create(math_tex))
        self.wait(1)

        self.play(FadeOut(arrow))

        value_circle = Circle(radius=1.5)
        e = Tex('12',font_size=35).move_to([-3.5,0.8,0])
        self.play(Create(e))
        self.wait(1)    
        self.play(e.animate.move_to(value_circle.point_at_angle(PI/2 - 4*TAU/6)).scale(1.2))
        self.wait(1)
        
        f = Tex('24',font_size=35).move_to([-3.5,0.8,0])
        self.play(Create(f))
        self.wait(1)    
        self.play(f.animate.move_to(value_circle.point_at_angle(PI/2 - 5*TAU/6)).scale(1.2))
        self.wait(1)

        a = Tex('20',font_size=35).move_to([-3.5,0.4,0])
        self.play(Create(a))
        self.wait(1)    
        self.play(a.animate.move_to(value_circle.point_at_angle(PI/2 - 0*TAU/6)).scale(1.2))
        self.wait(1)

        d = Tex('40',font_size=35).move_to([-3.5,0.4,0])
        self.play(Create(d))
        self.wait(1)    
        self.play(d.animate.move_to(value_circle.point_at_angle(PI/2 - 3*TAU/6)).scale(1.2))
        self.wait(1)

        b = Tex('60',font_size=35).move_to([-3.5,0,0])
        self.play(Create(b))
        self.wait(1)    
        self.play(b.animate.move_to(value_circle.point_at_angle(PI/2 - 1*TAU/6)).scale(1.2))
        self.wait(1)

        c = Tex('120',font_size=35).move_to([-3.5,0,0])
        self.play(Create(c))
        self.wait(1)    
        self.play(c.animate.move_to(value_circle.point_at_angle(PI/2 - 2*TAU/6)).scale(1.2))
        self.wait(1)
        