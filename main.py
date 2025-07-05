import gradio as gr

def echo(text):
    return f"You entered: {text}"

iface = gr.Interface(fn=echo, inputs="text", outputs="text", title="Echo App")

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=7860, share=True)
