FROM manimcommunity/manim

USER root
RUN apt update
RUN apt install -y libsox-fmt-all
RUN apt install -y sox
USER manimuser
RUN pip install sox -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install "manim-voiceover[azure,gtts]" -i https://pypi.tuna.tsinghua.edu.cn/simple