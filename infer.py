## Step -1 - command to create onnx using optimum
# optimum-cli export onnx --model bigcode/starcoderbase-1b starcoder_onnx/


## Step - 2 - infer using onnx model created from step 1
from transformers import AutoTokenizer
from optimum.onnxruntime import ORTModelForCausalLM
import onnxruntime as ort


checkpoint = r"C:\Balaji\onnxinfer\starcoder_onnx"
# device = "cuda"

tokenizer = AutoTokenizer.from_pretrained(r'C:\Balaji\onnxinfer\starcoderbase1b')
model = ORTModelForCausalLM.from_pretrained(checkpoint, use_io_binding=True, providers=['OpenVINOExecutionProvider'])

inputs = tokenizer.encode("Generate python function to add numbers def ", return_tensors="pt")
outputs = model.generate(inputs,max_length=50)

print(tokenizer.decode(outputs[0]))