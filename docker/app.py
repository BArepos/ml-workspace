import os
import gradio as gr


def greet(name):
    return f"Hello {name}!"


demo = gr.Interface(fn=greet, inputs="text", outputs="text")

if __name__ == "__main__":
    print("launchinnnn")
    demo.launch(server_port = 9090)
