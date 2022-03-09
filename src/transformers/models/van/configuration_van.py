# coding=utf-8
# Copyright 2022 Meta Platforms, Inc. and The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
""" ConvNeXT model configuration"""

from ...configuration_utils import PretrainedConfig
from ...utils import logging


logger = logging.get_logger(__name__)

VAN_PRETRAINED_CONFIG_ARCHIVE_MAP = {
    "van-base": "https://huggingface.co/van-base/resolve/main/config.json",
}


class VanConfig(PretrainedConfig):
    r"""
    This is the configuration class to store the configuration of a [`VanModel`]. It is used to instantiate an ConvNeXT
    model according to the specified arguments, defining the model architecture. Instantiating a configuration with the
    defaults will yield a similar configuration to that of the ConvNeXT [van-base](https://huggingface.co/van-base)
    architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.

    Args:
        num_channels (`int`, *optional*, defaults to 3):
            The number of input channels.
        patch_size (`int`, optional, defaults to 4):
            Patch size to use in the patch embedding layer.
        hidden_sizes (`List[int]`, *optional*, defaults to [64, 128, 320, 512]):
            Dimensionality (hidden size) at each stage.
        depths (`List[int]`, *optional*, defaults to [3, 3, 12, 3]):
            Depth (number of blocks) for each stage.
        mlp_expansions (`List[int]`, *optional*, defaults to [8, 8, 4, 4]):
            The expansion factor for mlp layer at each stage.
        hidden_act (`str` or `function`, *optional*, defaults to `"gelu"`):
            The non-linear activation function (function or string) in each block. If string, `"gelu"`, `"relu"`,
            `"selu"` and `"gelu_new"` are supported.
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-12):
            The epsilon used by the layer normalization layers.
        layer_scale_init_value (`float`, *optional*, defaults to 1e-6):
            The initial value for the layer scale.
        drop_path_rate (`float`, *optional*, defaults to 0.0):
            The drop rate for stochastic depth.

    Example:
    ```python
    >>> from transformers import VanModel, VanConfig

    >>> # Initializing a Van van-tiny-224 style configuration
    >>> configuration = VanConfig()
    >>> # Initializing a model from the van-tiny-224 style configuration
    >>> model = VanModel(configuration)
    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```"""
    model_type = "van"

    def __init__(
        self,
        num_channels=3,
        patch_sizes=[7, 3, 3, 3],
        strides=[4, 2, 2, 2],
        hidden_sizes=[64, 128, 320, 512],
        depths=[3, 3, 12, 3],
        mlp_expansions=[8, 8, 4, 4],
        hidden_act="gelu",
        initializer_range=0.02,
        layer_norm_eps=1e-12,
        layer_scale_init_value=1e-6,
        drop_path_rate=0.0,
        dropout_rate=0.0,
        image_size=224,
        **kwargs
    ):
        super().__init__(**kwargs)

        self.num_channels = num_channels
        self.patch_sizes = patch_sizes
        self.strides = strides
        self.hidden_sizes = hidden_sizes
        self.depths = depths
        self.mlp_expansions = mlp_expansions
        self.hidden_act = hidden_act
        self.initializer_range = initializer_range
        self.layer_norm_eps = layer_norm_eps
        self.layer_scale_init_value = layer_scale_init_value
        self.drop_path_rate = drop_path_rate
        self.dropout_rate = dropout_rate
        self.image_size = image_size