import gradio as gr
from src.detector import PPEVisionDetector
detector = PPEVisionDetector()
def run_ppe_check(image):
    if image is None: return None, {"Error": "No frame provided"}
    return detector.detect(image)
demo = gr.Interface(
    fn=run_ppe_check,
    inputs=gr.Image(type="pil", label="CCTV Camera Frame"),
    outputs=[gr.Image(type="pil", label="PPE Safety Vision Annotations"), gr.JSON(label="Compliance Telemetry")],
    title="🛡️ AI-Powered Industrial PPE Detection (YOLOv11)"
)
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7875, share=False)
