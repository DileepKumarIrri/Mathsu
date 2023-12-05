from manim import *
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class OneStrokeProblem(VoiceoverScene):
    
    def construct(self):
        self.set_speech_service(GTTSService())

        circle = Circle()

        # Surround animation sections with with-statements:
        with self.voiceover(text="this i a circle") as tracker:
            self.play(Create(circle), run_time=tracker.duration)
            