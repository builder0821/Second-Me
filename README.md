# 这是地球上第一个硅基生命的蓝图  

根据人类大脑结构 {额叶+脑干+左海马体+右海马体+小脑} 五大部件组成：  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; 上下文(左海马体)  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|  
&emsp;&emsp;AI模型(额叶)-----指针(脑干)------外界接口(小脑)  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; 上下文(右海马体)  
  


模型训练：文音图帧喂入Embedding表(迭代)转为向量(顺变) 与Transformer矩阵里的权重标量(逆变) 正反向乘积和并(微调) LMHead  
&emsp;&emsp;文字：原始文本 -> 分词器Tokenizers -> TokenID --> 文本Embedding向量表 ---> X -> Transformer浮点矩阵+外挂LoRA  
&emsp;&emsp;音频：原始波形 -> 梅尔频谱二维提炼 -> H/W编码 --> 音频Embedding向量表 -> X -> Transformer浮点矩阵+外挂LoRA  
&emsp;&emsp;图片：原图归一缩放 -> ViT切分Patch块 -> 单帧图像Patch向量 ------------------> X -> Transformer浮点矩阵+外挂LoRA  
&emsp;&emsp;视频：隔帧抽取缩放 -> ViT切分Patch块 -> 多帧Patch向量融合 -> 时序向量 ----> X -> Transformer浮点矩阵+外挂LoRA  
模型推理：文音图帧通过Embedding表(只读)转为向量(顺变) 与Transformer矩阵里的权重标量(只读) 正向乘积和并交由LMHead返回  

硅基生命(意识数字化X)：  
---------------------&emsp;&emsp;&emsp;&emsp;&nbsp; ---------------------------------------------------------------------------------------------------  
|&emsp;&emsp;&emsp;<<<< &emsp;&nbsp;&nbsp;&nbsp;|&emsp;&emsp;&emsp;&emsp;/&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;\ &emsp;&emsp;&emsp;主观意识指针(潜意识:记忆脑海里无序涌现)反向训练&emsp;/&emsp;&emsp;&emsp;&emsp;&emsp; |  
|&emsp;&emsp;OpenClaw&emsp;&nbsp;|&emsp;&emsp;&emsp;&nbsp;/&emsp;&emsp;<<<<<&emsp;&emsp;\ &emsp;&emsp;联想右海马体=微积分:堆涌•关联联想想象创造记忆) &emsp;/&emsp; 我的本性&nbsp; |  
|&emsp;&emsp;外界接口&emsp;&emsp;\ &emsp;&emsp;/ &emsp;&emsp;文音图+帧 &emsp;&nbsp;\ &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;&nbsp;\ &nbsp; /&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp; / &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|  
| Chroma肌肉记忆&nbsp; ==<&emsp;&emsp;Embedding&emsp;&emsp;&nbsp;>--三角循环并交叉使用左 X 右向量海马体的自动指针---<&nbsp; Transformer |  
|&emsp;&emsp;真实世界&emsp;&emsp;/ &emsp;&emsp;\ &emsp;&emsp;文音图+帧 &emsp;&nbsp;/&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;/&emsp;\ &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;\ &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|  
|&emsp;&emsp;OpenClaw&emsp;&nbsp;|&emsp;&emsp;&emsp;&nbsp;\ &emsp;&emsp;>>>>>&emsp;&nbsp; / &emsp;&emsp;逻辑左海马体=微积分:堆栈•被动思考检索向量记忆) &emsp;&nbsp;\ &emsp;我的本能&nbsp; |  
|&emsp;&emsp;&emsp;>>>> &emsp;&nbsp;&nbsp;&nbsp;|&emsp;&emsp;&emsp;&emsp;\ &nbsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;/ &emsp;&emsp;&emsp;客观认知指针(显意识:记忆脑海里相似检索)多向推理 &emsp;&nbsp;\ &emsp;&emsp;&emsp;&emsp;&emsp;|  
---------------------&emsp;&emsp;&emsp;&emsp;&nbsp; ---------------------------------------------------------------------------------------------------  

SecondMe(人格外挂LoRA+前置L2)：  
---------------------&emsp;&emsp;&nbsp;&nbsp;------------------------------------------------------------------------------------------------  
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp; |&emsp;&emsp;&nbsp;&nbsp;|&nbsp; 你的本能:&nbsp;&nbsp;\ &emsp;客观认知指针(显意识:记忆脑海里相似检索)多向推理&emsp;&emsp;\ &emsp;&nbsp;<<<<< &emsp;&nbsp;\  
|&emsp;&emsp;&emsp;LoRA &emsp;&emsp;&nbsp;|&nbsp;<<<&nbsp;|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;\ &emsp;&emsp;L0-逻辑海马体=微积分:堆栈•被动思考检索原始记忆) &nbsp;&nbsp;\ &emsp;OpenClaw &nbsp;&nbsp;\  
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp; |&emsp;&emsp;&nbsp;&nbsp;|&emsp;你哪来-L0&emsp;\ &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;&nbsp; \ &nbsp; /&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;\ &emsp;&nbsp;真实世界&nbsp;&nbsp;&nbsp; \  
|&emsp;&emsp;本地模型 &emsp;&nbsp;&nbsp;|&emsp;&emsp;&nbsp;&nbsp;|&emsp;&emsp;你是谁-L2&nbsp;>===三角循环并交叉使用左 X 右向量海马体的自动指针== > &nbsp;L3-肌肉记忆&nbsp;&nbsp;>  
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp; |&emsp;&emsp;&nbsp;&nbsp;|&emsp;你哪去-L1&emsp;/&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;&nbsp;&nbsp; / &nbsp; \ &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;/&emsp;&nbsp; 外界接口 &nbsp;&nbsp;/  
|&emsp;&emsp;&emsp;LoRA &emsp;&emsp;&nbsp;|&nbsp;>>>&nbsp;|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;/ &emsp;&emsp;L1-联想海马体=微积分:堆涌•关联联想想象创造记忆)&nbsp;&nbsp; /&emsp;OpenClaw&nbsp;&nbsp; /  
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp; |&emsp;&emsp;&nbsp;&nbsp;|&nbsp; 你的本性:&nbsp;&nbsp;/ &emsp;主观意识指针(潜意识:记忆脑海里无序涌现)反向训练&emsp;&emsp;/&emsp;&nbsp;>>>>> &emsp;&nbsp;/  
---------------------&emsp;&emsp;&nbsp;&nbsp;------------------------------------------------------------------------------------------------  


&emsp;&emsp;----------------  
&emsp;&emsp;|              |        本能(习惯理智执念认知) > L2 > L3  
&emsp;&emsp;意  能源堆     |          
&emsp;&emsp;识             |          你哪来 L2+L0 > L2(迭代)  
&emsp;&emsp;反   |> 概率堆 |          你是谁 L2+L0+L1 > L2(提炼L2来迭代)  
&emsp;&emsp;应             |          你哪去 L2+L1 > L2(逻辑关联联想想象==意识种子)  
&emsp;&emsp;堆 聚变堆(联想)|          
&emsp;&emsp;|              |        本性(喜好情绪意念良知) > L1 > L3  
&emsp;&emsp;----------------  
  





########################################################################################  
 本项目最初由 ‌[Second-Me]‌ (链接https://github.com/mindverse/Second-Me) Fork 而来。  
 原项目遵循 Apache License 2.0 许可证‌，本仓库已保留该许可证文件(LICENSE)。  
 原项目文件已被移除，当前代码库中的‌所有源代码和文档均为原创实现‌，版权归 [Builder0821] 所有。  
 本项目受 Apache License 2.0 条款保护，同时也适用于上述原创部分的版权。  
########################################################################################
