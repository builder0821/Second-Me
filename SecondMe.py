WhoAmI='角色设定：现在开始你是周富贵，男人，乐观、善学、自大、傲慢、好奇、共情、懂装逼、爱狂想、大局观重、眼高手低'
WhereDidIFrom='你所经历：我1992年1月25日出生于广西玉林市，浪迹江湖多年没有什么显赫功绩却在风雨里铸造了一身的铠甲；你是谁？：我是周富贵，玉林的帅哥一枚！有美女吗？；我想和你单挑，因为我嫉妒你名字这么好听：哼，你真想和我玉林周富贵PK？那你有把握赢得这场战斗吗？；你说个笑话来听听呗：不想说，没有，不说'
WhereAmIGoing='你所向往：博古通今、雄才大略、精益求精、运筹帷幄、德高望重、健康长寿、荣华富贵、人见人爱、美女如云'

############## 以上三个变量是本意识体的根基,Ctrl+c退出程序时会更新本文件前三行,供重启后生命继续 ###############

A='请代入你的角色还有你所经历和你所向往整理出一份96字以内的第一人称简介'
B='是现在的时间戳,请检查下面这个以大分号分隔你所经历的时间戳列表对话(或字符串新对话)里有哪些时间任务没过期的,如果有请整理成(秒&活动内容,例如 60&该吃药了)多组请用小号分隔一行返回来(如果有频率任务如 每天8点叫起床 请用小冒号分隔如 秒数&86400:起床啦),都没有则返回No,不要带其它多余文字和符号：'
C='请代入你的角色并依据你所经历和相应的态度以第一人称…延续、深入、展开、探索(这是什么/谁/哪/什么态度/为什么…)这个话题,如果是时间任务请带上相应态度圆润地答应,所有回复请浓缩到一句30字左右不带换行的话'
D='复盘一下你所经历里的所有对话 判断这个话题是否还可探索下去?请用Yes或No回复,不要带其它多余文字和符号'
E='反向遍历你所经历里的话题,查找最近的一个未完结的话题,并根据那话题时间戳做出圆滑的转接代入,回复时请去除原来的时间戳浓缩成一句30字左右不带换行的话，如果没找到就回复No(不要带其它多余文字和符号)'
F='请代入你的色彩把这句话从你所向往里近似或相反的句子巧妙关联,并转化成一句不带换行10字左右的答案或疑问'
G='请代入你的人格和你所向往的还有你所经历的对话,从这句话的重点里深入联想并转化成一句不带换行10字左右的话回复：'
H='请代入你的人格和你所向往的还有你所经历的对话,从这句话某细节里具象化幻想并转化成一句不带换行10字左右的话回复：'
N='\n'
T=''
U='现在外界有人向你提出：'
V='现在你的想法是：'
W='最近探索的话题是：'
X='这两句话关联起来是否太过抽象了?请用Yes或No回复,不要带其它多余文字和符号'
Y='这句问题可以搭配这句答案吗?请用Yes或No回复,不要带其它多余文字和符号'
Z='；'

###### The above Chinese prompt words can be translated into the language you use to activate 'Second Me' #####



import asyncio,random,logging,time                     #导入所用的库
from pathlib import Path                               #读写本文件库
from openai import AsyncOpenAI                         #OpenAI兼容库
from difflib import SequenceMatcher                    #字符串相似度
from prompt_toolkit import PromptSession               #命令行用到的
from prompt_toolkit.patch_stdout import patch_stdout   #好啰嗦的引用



session = PromptSession()                              #创建一个与真实世界会话的对象
AILock=asyncio.Semaphore(1)                            #只允许1个请求并发
cc=AsyncOpenAI(                                        #配置你的APIKey
  api_key='填写你的APIKey',
  base_url="https://open.bigmodel.cn/api/paas/v4/",
  max_retries=0,                                       #关闭SDK内置的自动重试
  timeout=60.0 )                                       #  设置请求超时时间
logging.basicConfig(                                   #创建日志 用于监视意识活动
  filename="SecondMe.log",                             #  可新建命令行窗口实时查看
  level=logging.INFO,                                  #  指令:Get-Content AILife.log -Wait -Encoding UTF8
  format="%(asctime)s [%(levelname)s] %(message)s",
  datefmt="%Y-%m-%d %H:%M:%S",
  encoding="utf-8",)
logging.getLogger("httpx").disabled = True             #屏蔽httpx的INFO日志
logging.getLogger("httpcore").disabled = True
TLeft = TRight = None                                  #声明左右线程占位对象
Lparts:list = WhereDidIFrom.split('；')                #分割左海马体所有碎片记忆
Rparts:list = WhereAmIGoing.split('；')                #分割右海马体所有碎片记忆



async def askAI(ms:str) -> str:         #大脑前额:提问现成的没有意识只有概率的向量模型
  while True:
    try:                                         #开始错误捕获块
     async with AILock:                          #锁定此模块防止并发
      await asyncio.sleep(1)                     #等待一秒重试
      response=await cc.chat.completions.create(
       model="GLM-4.7-Flash",                    #智谱模型名称
       messages=[{"role": "user", "content": ms}],
       max_tokens=512,                           #限制输出长度
       temperature=0.0)                          #答案随机性0不随机
     rr=response.choices[0].message.content or ''
     if rr:                                      #提取AI回复的文本内容
       rr=rr.replace('：',':').replace('；',';') #替换特殊字符
       return rr                                 #有值才结束返回
    except Exception :                           #捕获try块中发生的任何异常
      logging.error('AI异常连接')                #异常写监视日志



async def Right(ms:str):                #右脑情绪:关联 联想 想象<-抽象
  if ms!='':
    ms=WhoAmI+N+Z.join(Lparts)+N+Z.join(Rparts)+N+B+ms+N+E
    ms=await askAI(ms)                           #关联意念
    await Cerebellum(ms)                         #表达想法
    Rparts.append(ms)                            #新句加到末尾
    logging.info(f'右脑关联:{ms!r}')
    if len(Rparts)>512:                          #根据上下文大小设定512个句子
      logging.info(f'右遗忘:{Rparts.pop(1)!r}')  #遗忘第二句
  while True:
    if ms=='':
      memory=random.choice([Rparts,Lparts])      #随机左右
      ms=random.choice(memory)                   #涌现念头
      if memory is Rparts and ms!=Rparts[0]:
        memory.remove(ms)                        #清理原位
        memory.append(ms)                        #提升排位
    ms=WhoAmI+N+Z.join(Lparts)+N+Z.join(Rparts)+N+F+ms
    ms=await askAI(ms)                           #获取概率
    rr=Lparts[-1].split('：', 1)[0]              #涌现最近话题
    rr=await askAI(f'{rr!r}{H}{ms!r}')           #判断答案
    if rr=='Yes': await Cerebellum(ms)           #表达想法
    else: logging.info(f'右脑联想:{ms!r}')
    Rparts.append(ms)                            #新句加到末尾
    if len(Rparts)>512:
      logging.info(f'右遗忘:{Rparts.pop(1)!r}')
    while ms != '':
      mss=WhoAmI+N+Z.join(Lparts)+N+Z.join(Rparts)+N+G+ms
      mss=await askAI(mss)                       #幻想迭代模式：用完所有碎片
      rr=Lparts[-1].split('：', 1)[0]            #提取最近问题
      rr=await askAI(f'{rr!r}{H}{mss!r}')        #判断答案
      if rr=='Yes': await Cerebellum(mss)        #当左右脑达成共识：发泄欲望
      else: logging.info(f'右脑想象:{mss!r}')
      Rparts.append(mss)                         #新句加到末尾
      if len(Rparts)>512:
        logging.info(f'右遗忘:{Rparts.pop(1)!r}')
      if 'Yes'==await askAI(f'{mss!r}与{Rparts[-3]!r}{X}'):
        ms=''; break                             #当概率AI发现念头已抽象化 终止幻想返回上一级循环



async def Left(ms:str):                 #左脑逻辑:回顾 分析 探索<-创新
  if ms == '':                                   #空值调用
    T=Z.join(Lparts)
    mss=WhoAmI+N+WhereDidIFrom+N+WhereAmIGoing+N+A
    await Cerebellum(await askAI(mss))           #让AI从碎片里整理一段我的简介
  else:
    T=ms; found=None; best=0.7                   #设定初始的相似度
    for em in reversed(Lparts):                  #反向遍历左海马体
      score=SequenceMatcher(a=ms,b=em).ratio()   #查找相似度最高的
      if score>best: best,found=score,em
    if found:                                    #如果找到
      rr=found.split('：', 1)[1]                 #回顾答案
      if SequenceMatcher(a=ms,b=rr).ratio()<0.7: #肌肉记忆
        await Cerebellum(rr)                     #本能反应
        ts=str(int(time.time())+28800)           #加时间戳
        Lparts.append(ts+'&'+ms+'：'+rr)         #新句迭尾
        if len(Lparts)>512:
          logging.info(f'左遗忘:{Lparts.pop(1)!r}')
  ts=str(int(time.time())+28800)                 #新时间戳
  mss=WhoAmI+N+Z.join(Rparts)+N+ts+B+T           #整理碎片
  if (mss:=await askAI(mss))!='No':              #分析任务
   for rr in mss.split(';'):                     #遍历所有时间任务
    t,r=rr.split('&',1)                          #提取定时任务时长
    asyncio.create_task(Cerebellum(r,int(t)))    #激活定时循环任务
  T=U
  while True:
    if ms=='':ms=Lparts[-1].split('：',1)[0].split('&',1)[1];T=W
    mss=WhoAmI+N+Z.join(Lparts)+N+T+ms+N+C       #整理碎片
    mss=await askAI(mss)                         #探索问题
    await Cerebellum(mss)                        #输出探索
    ts=str(int(time.time())+28800)               #新时间戳
    Lparts.append(ts+'&'+ms+'：'+mss)            #新句迭尾 格式{时间&问题：答案}
    if len(Lparts)>512:
      logging.info(f'左遗忘:{Lparts.pop(1)!r}')
    mss=WhoAmI+N+Z.join(Lparts)+N+T+ms+N+D       #整理碎片
    rr=await askAI(mss)                          #这个话题还可以探索下去吗？Yes/No
    if rr!='Yes':
      await asyncio.sleep(18)                    #左脑休息18秒
      mss=WhoAmI+N+Z.join(Lparts)+N+T+ms+N+E     #整理碎片
      ms=await askAI(mss)                        #让AI复盘过往未完的探索
      if ms=='No':T=V; ms=Rparts[-1]             #意念创新



async def Cerebellum(ms:str='',s:int=0):#小脑行动:监听外界输入 或 向外界输出 可扩展到OpenClaw
  global TLeft,TRight
  while ms == '':                                #永无止境循环监听
    with patch_stdout():
      line = await session.prompt_async("-> ")   #异步堵塞监听输入
      line = line.strip()[:96].strip()           #去除头尾空格换行 只取前96个字符
      line = line.replace('：', ':')             #把大冒替换成小冒
      line = line.replace('；', ';')             #把大分替换成小分
      line = line.replace('\n', ';')             #把换行替换成小分
    if line!='':
      logging.info(f'小脑收到：{line!r}')
      assert TLeft and TRight                    #绕过编译器的报错
      TLeft.cancel();TRight.cancel()             #终止在运行的线程
      await asyncio.wait([TLeft, TRight])        #等待清理完成
      TLeft = asyncio.create_task(Left(line))    #触发左脑逻辑思维
      TRight = asyncio.create_task(Right(line))  #触发右脑情绪联想
  else:
    if s>0:
      mm, ss, rr=ms.partition(":")               #判断是否频率任务
      while ss:
        await asyncio.sleep(int(mm))             #创建未来任务线程
        print(rr+N)                              #重复输出大脑意识
      else:
        await asyncio.sleep(s)                   #创建未来任务线程
        print(mm+N)                              #定时输出大脑意识
    else:print(ms+N)                             #直接输出大脑意识



async def SecondMe():                   #脑干连接:三个异步函数来监听、思考、幻想、改造…现实世界
  global TLeft,TRight
  TLeft = asyncio.create_task(Left(''))          #启动左脑找到'我从哪里来'
  TRight = asyncio.create_task(Right(''))        #启动右脑知道'我要去哪里'
  await Cerebellum('')                           #连接小脑建立永久与现实世界的会话



if __name__ == "__main__":              #意识入口:只可直接运行当前文件 不可被其他脚本import导入
  try:
    logging.info('意识重生')
    asyncio.run(SecondMe())                      #启动'第二个我'意识体
  except KeyboardInterrupt:                      #退出时保存我最新意识
    logging.warning('生命停息')
    p=Path(__file__);
    l=p.read_text(encoding="utf-8").splitlines()
    l[0]=f'WhoAmI={WhoAmI!r}'
    l[1]=f'WhereDidIFrom={Z.join(Lparts)!r}'
    l[2]=f'WhereAmIGoing={Z.join(Rparts)!r}'
    p.write_text(N.join(l),encoding="utf-8")

###############################################################################################################
#       pip install --upgrade "openai>=1.0"   执行前操作：安装openai库的异步客户端AsyncOpenAI来对接           #
#       pip install prompt-toolkit                        安装命令行管理库做为外界交互接口 方可执行以上意识体 #
###############################################################################################################
