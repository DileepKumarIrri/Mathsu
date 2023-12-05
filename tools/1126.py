from manim import *
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class OneStrokeProblem(VoiceoverScene):
    
    def construct(self):
        self.set_speech_service(GTTSService())

       
        

        p_A=[-.36,2.2,0]
        p_E=[.36,2.2,0]
        p_B = [-1.2,-.5,0]
        p_D = [1.2,-.5,0]
        p_C = Dot(p_B).rotate(PI/3,about_point=p_D).get_center()
        p_F = Dot(p_B).rotate(-PI/3,about_point=p_D).get_center()
        p_I = Dot(p_F).shift(LEFT*0.28).shift(DOWN*0.48).get_center()
        p_J = Dot(p_F).shift(RIGHT*0.28).shift(DOWN*0.48).get_center()

        p_G = Dot(p_B).shift(RIGHT*1.04).get_center()
        p_H = Dot(p_B).shift(RIGHT*1.36).get_center()


        A = Text("A").scale(0.4).move_to(p_A).shift(UP*0.12).shift(LEFT*0.1)
        self.add(A)
        E = Text("E").scale(0.4).move_to(p_E).shift(UP*0.12).shift(RIGHT*0.1)
        self.add(E)
        F = Text("F").scale(0.4).move_to(p_F).shift(UP*0.22).shift(LEFT*0)
        self.add(F)
        B = Text("B").scale(0.4).move_to(p_B).shift(UP*0.0).shift(LEFT*0.22)
        self.add(B)
        C = Text("C").scale(0.4).move_to(p_C).shift(DOWN*0.22)
        self.add(C)
        D = Text("D").scale(0.4).move_to(p_D).shift(UP*0).shift(RIGHT*0.22)
        self.add(D)
        I = Text("I").scale(0.4).move_to(p_I).shift(UP*0.1).shift(LEFT*0.1)
        self.add(I)
        J = Text("J").scale(0.4).move_to(p_J).shift(UP*0.1).shift(RIGHT*0.1)
        self.add(J)
        G = Text("G").scale(0.4).move_to(p_G).shift(UP*0.14).shift(LEFT*0.12)
        self.add(G)
        H = Text("H").scale(0.4).move_to(p_H).shift(UP*0.14).shift(RIGHT*0.12)
        self.add(H)
        
        BD = Line(p_B,p_D)
        self.add(BD)
        BC = Line(p_B,p_C)
        self.add(BC)
        CD = Line(p_C,p_D)
        self.add(CD)
        BF = Line(p_B,p_F)
        self.add(BF)
        DF = Line(p_D,p_F)
        self.add(DF)
       
        AE = Line(p_A,p_E)
        self.add(AE)
        BE = Line(p_B,p_E)
        self.add(BE)
        CE = Line(p_C,p_E)
        self.add(CE)
        DE = Line(p_D,p_E)
        self.add(DE)
        AB= Line(p_A,p_B)
        self.add(AB)
        AD = Line(p_A,p_D)
        self.add(AD)
        AC = Line(p_A,p_C)
        self.add(AC)
        
        BCI = Polygon(p_A,p_I,p_B,p_C,p_I,p_F,p_J,p_C,p_D,p_J,p_E,p_F)
        BCI.set_color(WHITE)
        BCI.set_fill(color=GRAY, opacity=.5)
        self.add(BCI)

        self.wait(1)
        with self.voiceover(text="""
            Hello young mathematicians! Today we're going to embark on a fun journey into the world of geometry. 
            We're going to solve a puzzle involving triangles and shaded areas. Don't worry, I promise it's going 
            to be as fun as solving a jigsaw puzzle!
        """) as tracker: 
            # 17s
            pass

        self.wait(1)
        with self.voiceover(text="""
            Imagine you're an explorer in the land of shapes, and you come across a strange map. The map shows three 
            triangles
        """) as tracker:
            # 17s
            pass

        self.wait(1)
        with self.voiceover(text="""
            AEF, BDF, and BCD and they are all equilateral triangles which means all their sides are the same length.
        """) as tracker:
            # 17s
            AEF = Polygon(p_A,p_E,p_F).set_color(RED)
            self.add(AEF)
            self.wait(1)
            BDF = Polygon(p_B,p_D,p_F).set_color(GREEN)
            self.add(BDF)
            self.wait(1)
            BCD = Polygon(p_B,p_C,p_D).set_color(YELLOW)
            self.add(BCD)
            pass

        self.wait(1)
        self.remove(AEF,BDF,BCD)
        
        with self.voiceover(text="""
            The map also tells you that the ratio of the lengths of AE to BD is 1:3, and the area of triangle AEF is 1
        """) as tracker:
            # 9s
            self.wait(3)
            AE.set_color(GREEN)
            AE_L = Text("1").scale(0.4).move_to(AE.get_center()).shift(UP*0.12)
            self.add(AE_L)
            self.wait(1)
            BD.set_color(RED)
            BD_L = Text("3").scale(.4).move_to(BD.get_center()).shift(UP*0.14)
            self.add(BD_L)
            self.wait(3)
            self.add(AEF)
            AEF_S = Text("1").scale(0.4).move_to(AEF.get_center()).shift(UP*0.14)
            self.add(AEF_S)
            self.wait(1)
        self.wait(1)
        with self.voiceover(text="""
                            our mission, should you choose to accept it, is to find the area of the shaded region.
                            """) as tracker:
            pass

        self.wait(1)
        self.remove(AEF)
        AE.set_color(WHITE)
        BD.set_color(WHITE)
        with self.voiceover(text="""
                            Now, the first thing you might notice is that the shaded area is symmetrical, like a 
                            butterfly's wings. This means we only need to find the area of one side, and then double 
                            it.
                            """) as tracker:
            self.wait(2)
            MID = DashedLine([0,4,0],[0,-4,0],dash_length=0.1)
            self.add(MID)
            pass

        self.wait(1)
        with self.voiceover(text="""
                            So, let's focus on finding the area of triangles AIF and BCI.
                            """) as tracker:
            self.wait(4)
            AIF = Polygon(p_A,p_I,p_F).set_color(RED)
            self.add(AIF)
            self.wait(1)
            BCI = Polygon(p_B,p_C,p_I).set_color(YELLOW)
            self.add(BCI)
            pass

        self.wait(1)
        self.remove(MID)
        
        with self.voiceover(text="""
                            Let's start with triangle BCI. The area of triangle BCI is equal to the area of triangle ABC minus the area of triangle ABI.
                            """) as tracker:
            self.wait(1)
            self.remove(AIF)
            self.wait(6)
            self.remove(BCI)

            ABC = Polygon(p_A,p_B,p_C).set_color(GREEN)
            self.remove(BCI)
            self.add(ABC)
            BCI.set_stroke(width=0).set_fill(YELLOW,opacity=0.2)
            self.add(BCI)
            self.wait(2)
            ABI = Polygon(p_A,p_B,p_I).set_stroke(width=0).set_fill(RED,opacity=0.2)
            self.add(ABI)
            pass

        self.wait(1)

        with self.voiceover(text="""
                            Here's a cool trick: we can move the vertex A of triangle ABC along a line parallel to the base BC to point D. 
                            This transforms triangle ABC into triangle BCD. So, the area of triangle ABC is equal to the area of triangle BCD.
                            """) as tracker:
            ABC2 = Polygon(p_A,p_B,p_C).set_color(GREEN)
            self.add(ABC2)
            DBC = Polygon(p_D,p_B,p_C).set_color(GREEN)
            self.play(Transform(ABC, DBC), run_time=tracker.duration/2)
            self.wait(1)
            pass
        with self.voiceover(text="""
                            Here's a cool trick: we can move the vertex A of triangle ABC along a line parallel to the base BC to point D. 
                            This transforms triangle ABC into triangle BCD. So, the area of triangle ABC is equal to the area of triangle BCD.
                            """) as tracker:
            ABC2 = Polygon(p_A,p_B,p_C).set_color(GREEN)
            self.add(ABC2)
            DBC = Polygon(p_D,p_B,p_C).set_color(GREEN)
            self.play(Transform(ABC, DBC), run_time=tracker.duration/2)
            self.wait(1)
            pass
        self.remove(ABI)
        self.remove(BCI)
        with self.voiceover(text="""
                            Since triangles AEF and BDF are both equilateral and the ratio of their side lengths is 1:3, 
                            the ratio of their areas is $1^2 : 3^2 = 1:9$. Since we know the area of triangle AEF is 1, 
                            the area of triangle BDF and triangle must be 9. Similarly, since triangle BCD is also equilateral 
                            with the same side length as BDF, its area is also 9, which means the area of triangle ABC is 9.
                            """) as tracker:
            self.wait(2)
            self.add(AE.to)
            self.add(BD)
            
            BDF_S = Text("9").scale(0.5).move_to(BDF.get_center())
            self.add(BDF_S)
            self.wait(1)
            self.play(Transform(BDF_S, BDF_S.copy().shift(BCD.get_center())), run_time=1)
            self.wait(1)
            
            self.wait(1)
            
            pass
        self.wait(1)