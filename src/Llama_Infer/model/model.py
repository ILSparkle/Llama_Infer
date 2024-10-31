from transformers import AutoModelForCausalLM, AutoTokenizer


class OptimizedModel(AutoModelForCausalLM):
    def generate(self, *args, **kwargs):
        outputs = super().generate(*args, **kwargs)
        return outputs
