import gradio as gr
def sketch_recognition(img):
    
    return("Donald Duck or Issy")

gr.Interface(fn=sketch_recognition, inputs="sketchpad", outputs="text").launch(share=True, server_name="0.0.0.0")