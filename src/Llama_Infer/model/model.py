from transformers import AutoModelForCausalLM
from transformers.models.qwen2 import Qwen2Model

"""
TODO:改写from_pretrained，将模型的加载行为从加载Qwen2Model
改为加载我们自己的OptimizedQwen2Model
"""
class OptimizedModel(AutoModelForCausalLM):
    @classmethod
    def from_pretrained(cls, *args, **kwargs):
        model = super().from_pretrained(*args, **kwargs)
        return model


"""
TODO:在此处更改模型的forward推理，进行优化
"""
class OptimizedQwen2Model(Qwen2Model):
    def forward(self,
                input_ids = None,
                attention_mask = None,
                position_ids = None,
                past_key_values = None,
                inputs_embeds = None,
                use_cache = None,
                output_attentions = None,
                output_hidden_states = None,
                return_dict = None,
                cache_position = None):
        ret = super().forward(input_ids,
                               attention_mask,
                               position_ids,
                               past_key_values,
                               inputs_embeds,
                               use_cache,
                               output_attentions,
                               output_hidden_states,
                               return_dict,
                               cache_position)
        return ret
