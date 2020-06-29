from imagenetlabels import idx_to_labels
import tensorflow as tf
import gradio as gr

mobile_net = tf.keras.applications.MobileNetV2()

def classify_image(inp):
    inp = inp.reshape((1, 224, 224, 3))
    prediction = mobile_net.predict(inp).flatten()
    return {idx_to_labels[i].split(',')[0]: float(prediction[i]) for i in range(1000)}

imagein = gr.inputs.Image(shape=(224, 224, 3))
label = gr.outputs.Label(num_top_classes=3)

gr.Interface(
    classify_image, 
    imagein, 
    label,
    capture_session=True,
    title="MobileNet Image Classifier",
    description="A state-of-the-art machine learning model that classifies images into one of 1,000 categories. These categories include a variety of animals, plants, and everyday objects. Also includes a saliency map to show the visual attention of the model."
).launch();
