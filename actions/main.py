import gradio as gr

def echo(text):
    return f"You entered: {text}"

iface = gr.Interface(fn=echo, inputs="text", outputs="text", title="Echo App")

if __name__ == "__main__":
    iface.launch()
