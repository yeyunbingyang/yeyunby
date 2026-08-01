### 图片与视频导演 Skill SOP标准操作流程

这是你之前提到的“图片视频提示词生成”方向。

#### 偏影视创作

`visual-skills` 把视频创作拆成戏剧结构、镜头功能、节奏、分镜卡、模型语法和质量检查。它不是只生成一句“电影感、史诗感”的提示词，而是要求明确人物动作、镜头目的、声音、光线和剪辑方式。

适合学习：

- 分镜设计
- 镜头语言
- 广告短片
- 剧情短片
- 角色出场和情绪节奏
- Kling、Veo、Seedance 等模型提示词

#### 偏模型操作与角色一致性

`video-prompting-skill` 包含文生视频、图生视频、角色设定表、场景静帧和视频提示词工作流，覆盖 Sora、Veo、Wan、LTX、Seedance 等模型指南。它推荐按照“角色设定表 → 场景静帧 → 视频提示词”的顺序工作，比较适合系统学习角色一致性。

#### 偏电商和广告

`ai-ad-prompt-guide` 更偏商品图、UGC、B-roll 和商业广告，包含主体、灯光、镜头、技术参数的结构化方法，以及针对多个图片和视频模型的提示建议。

三者不需要全部安装：

|学习目标|优先选择|
|---|---|
|影视、短片、镜头叙事|visual-skills|
|视频模型操作、角色一致性|video-prompting-skill|
|电商、产品、营销广告|ai-ad-prompt-guide|
# 项目SOP

`ask-matt` 是 `mattpocock/skills` 中的**技能导航器**。

你描述当前任务，它会告诉你：

- 应该使用哪个 Skill
    
- 应该按什么顺序使用
    
- 当前处于哪条工作流的哪个阶段
    

它本身**不会完成任务**，不会直接写代码、生成需求文档或制作 SOP，只负责把你路由到合适的 Skill。它必须由用户主动输入 `/ask-matt` 调用。([GitHub](https://github.com/mattpocock/skills/blob/main/docs/engineering/ask-matt.md "skills/docs/engineering/ask-matt.md at main · mattpocock/skills · GitHub"))

## 安装

只安装 `ask-matt`：

```bash
npx skills@latest add mattpocock/skills --skill=ask-matt
```

安装整个技能库：

```bash
npx skills@latest add mattpocock/skills
```

如果安装完整技能库，官方建议在每个项目中先运行一次：

```text
/setup-matt-pocock-skills
```

它会配置问题追踪工具、文档保存位置和相关标签。([GitHub](https://github.com/mattpocock/skills/blob/main/docs/engineering/ask-matt.md "skills/docs/engineering/ask-matt.md at main · mattpocock/skills · GitHub"))

## 使用方法

在 Claude Code、Codex 或支持 Skills 的 Agent 中输入：

```text
/ask-matt 我想开发一个新功能，但目前只有模糊想法，不知道先写需求还是先做原型。
```

它可能会给出类似路线：

```text
/grill-with-docs
→ /to-spec
→ /to-tickets
→ /implement
→ /code-review
```

这代表：

```text
澄清需求
→ 形成规格文档
→ 拆解任务
→ 开发实现
→ 代码审查
```

这个“按流程推荐多个 Skills”，而不是简单推荐一个工具，是 `ask-matt` 的主要价值。([GitHub](https://github.com/mattpocock/skills/blob/main/docs/engineering/ask-matt.md "skills/docs/engineering/ask-matt.md at main · mattpocock/skills · GitHub"))

## 用于你的 SOP 场景

可以这样输入：

```text
/ask-matt

我想把日常工作整理成标准 SOP。

场景包括：
1. 文件分类整理
2. AIGC 图片和视频提示词生成
3. 项目工作流设计
4. 最终文件检查和归档

我目前只有零散经验，没有形成正式流程。
请告诉我应该使用哪些 skills，以及执行顺序。
```

它大概率会先推荐：

```text
/grill-me
```

通过连续提问，帮你明确：

- SOP 的使用者
    
- 流程起点和终点
    
- 每一步的执行动作
    
- 检查标准
    
- 异常处理
    
- 输出和归档规则
    

之后，若你想把这套 SOP 封装成以后可重复调用的 Skill，可以使用：

```text
/writing-great-skills
```

该 Skill 是该仓库里专门用于指导创建和修改高质量 Skills 的参考能力；`grill-me` 则适合非代码场景中的流程、计划和方案梳理。([GitHub](https://github.com/mattpocock/skills "GitHub - mattpocock/skills: Skills for Real Engineers. Straight from my .agents directory. · GitHub"))

因此你的实际路线可以是：

```text
/ask-matt
→ /grill-me
→ 生成 SOP 文档
→ /writing-great-skills
→ 将 SOP 封装成自定义 Skill
```

可以把 `ask-matt` 理解成：

> **Skills 库的智能前台，不负责干活，但负责把任务送到正确的专家手上。**