---
title: "Andrej Karpathy"
title_ru: "Андрей Карпаты"
category: people
tags: [karpathy, openai, tesla, stanford, cs231n, software-2-0, llm-wiki, llm-os, vibe-coding, eureka-labs, deep-learning]
aliases: [Karpathy, Andrej Karpathy, @karpathy]
confidence: high
date: 2026-05-17
updated: 2026-05-17
sources:
  - https://karpathy.ai
  - https://en.wikipedia.org/wiki/Andrej_Karpathy
  - https://karpathy.medium.com/software-2-0-a64152b37c35
  - https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
  - https://www.youtube.com/@AndrejKarpathy
---

## Summary

Andrej Karpathy is a Slovak-Canadian AI researcher, educator, and founding member of OpenAI. He served as Director of AI at Tesla leading Autopilot Vision, created Stanford's legendary CS231n course, and coined foundational concepts including "Software 2.0," "vibe coding," and the "LLM Wiki" pattern. In 2024 he founded Eureka Labs, an AI-native education company.

## Key Ideas

- **Software 2.0 (2017):** Neural networks are not just another ML tool — they represent a fundamental shift in programming. Instead of writing explicit code, we specify goals and datasets, then let optimization search the program space. The "source code" becomes datasets + architecture; training compiles them into a working binary.
- **LLM OS (2025):** An LLM can serve as the kernel of a new operating system for knowledge work — orchestrating tools, memory, and agents. The same model that chats can also manage a filesystem, run code, browse the web, and spawn sub-agents.
- **LLM Wiki pattern (2025):** A three-layer architecture where raw sources are "compiled" into a living wiki by an LLM agent. Layer 1 is raw inputs (immutable), Layer 2 is LLM-written wiki entries (distilled knowledge), Layer 3 is a schema file (AGENTS.md) that controls context injection. Knowledge accumulates rather than being re-derived per query.
- **Vibe coding (Feb 2025):** Coined the term to describe AI-assisted coding where developers describe what they want in natural language and let the AI generate, run, and iterate on code — "I just vibe with the code."
- **LLMs as probabilistic knowledge stores:** Everything an LLM "knows" is vague, statistical, and imprecise. Context window beats parameter memory — always paste reference material directly rather than relying on recall from training.
- **Education as the highest-leverage AI application:** His career trajectory (OpenAI → Tesla → Eureka Labs) reflects a conviction that teaching AI literacy at scale is more impactful than any single product deployment.

## Career Timeline

| Period | Role | Key Contributions |
|--------|------|-------------------|
| 2005–2009 | BSc, University of Toronto | CS + Physics; attended Geoff Hinton's deep learning class |
| 2009–2011 | MSc, UBC | Physically-simulated figure controllers with Michiel van de Panne |
| 2011–2015 | PhD, Stanford | Image captioning, CNN-RNN architectures; designed and taught CS231n (grew from 150 to 750 students) |
| 2015–2017 | Research Scientist, OpenAI | Founding member; worked on deep learning and computer vision |
| 2017–2022 | Director of AI, Tesla | Led Autopilot Vision team; built in-house data labeling, NN training, and deployment on custom inference chip; briefly led Tesla Optimus |
| 2023–2024 | Research Scientist, OpenAI (return) | Built team on midtraining and synthetic data generation |
| 2024–present | Founder, Eureka Labs | AI-native education platform; first course: LLM101n |

## Major Ideas & Contributions

### Software 2.0 (2017)

Karpathy's most influential essay argues that neural networks constitute a new programming paradigm fundamentally different from classical coding. The key insight: in many domains, it's easier to collect training data and specify desired behavior than to write explicit rules. The software industry is undergoing a massive transition where large portions of codebases are being "ported" from Software 1.0 (explicit instructions) to Software 2.0 (learned weights).

Benefits of the 2.0 stack: computationally homogeneous (mostly matmul + ReLU), constant-time execution, constant memory use, highly portable, agile under resource changes, and modules can backpropagate through each other into an optimal whole.

### LLM Wiki Pattern (2025)

Proposed via GitHub Gist and later elaborated in talks, this pattern became the blueprint for this very project. Key architecture:

1. **Raw sources** (`inbox/`, `sources/`) — immutable inputs, never edited
2. **Wiki** (`wiki/`) — LLM-maintained bilingual markdown entries
3. **Schema** (`AGENTS.md`) — navigation map telling the agent where data lives and what format it's in

Three operations sustain the system: Ingest (new source → LLM writes/updates entries), Query (LLM reads wiki, synthesizes answer), Lint (periodic audit for contradictions and staleness). The schema layer is the critical innovation — it controls context injection so agents get exactly the relevant context without scanning everything.

### LLM OS

Karpathy proposed the LLM as a computational kernel analogous to an operating system. An LLM OS would manage:
- **Memory/File System** — the wiki, context windows, persistent storage
- **I/O** — web browsing, API calls, file operations
- **Process Management** — spawning sub-agents, tool calls, planning
- **Scheduler** — deciding what to attend to, when to reason deeply vs. respond quickly

This directly inspired the three-layer wiki architecture and the agentic pipeline approach.

### Vibe Coding (2025)

Coined on Twitter in February 2025, describing a new mode of software development where developers give high-level descriptions and let AI handle implementation details. Became an instant cultural phenomenon in the developer community. Represents the logical extension of Software 2.0 — the programmer shifts from writing code to specifying intent.

### Educational Philosophy

Karpathy's YouTube channel features two parallel tracks: a technical "Zero to Hero" series on neural network internals, and a general-audience "Deep Dive into LLMs" series. His core belief: AI education must reach both engineers who build the systems and the general public who will live with them. Eureka Labs extends this with an AI-native platform where course material, exercises, and even the teaching assistant are AI-generated and AI-personalized.

## Publications & Projects

### Key Publications
- "Deep Visual-Semantic Alignments for Generating Image Descriptions" (CVPR 2015, Oral) — early image captioning work
- "Large-Scale Video Classification with Convolutional Neural Networks" (CVPR 2014, Oral)
- "DenseCap: Fully Convolutional Localization Networks for Dense Captioning" (CVPR 2016, Oral)
- "Connecting Images and Natural Language" (PhD thesis, 2016)
- ImageNet co-author (IJCV 2015) — the benchmark that drove a decade of computer vision progress

### Notable Open-Source Projects
- **micrograd** — tiny scalar-valued autograd engine implementing backpropagation; widely used for teaching neural net fundamentals
- **char-rnn** — character-level language model (LSTM/GRU/RNN); accompanied by the viral post "The Unreasonable Effectiveness of Recurrent Neural Networks"
- **arxiv-sanity** — tames the flood of arXiv papers with search, recommendations, and similarity; deployed at arxiv-sanity-lite.com
- **ConvNetJS** — deep learning library written entirely in JavaScript for in-browser training
- **llm.c** — pure C/CUDA implementation of GPT-2 training; demonstrates that LLM training can be simple and transparent

### Fun Facts
- Held the title of "reference human" for ImageNet after competing against a ConvNet on 1,000-class classification
- Former speedcuber: solved Rubik's cubes in ~17 seconds; his YouTube channel "badmephisto" has 9M+ views
- Named one of TIME's 100 Most Influential People in AI (2024) and MIT Innovators Under 35 (2020)

## Notable Quotes

> "Software (1.0) is eating the world, and now AI (Software 2.0) is eating software." — Software 2.0, 2017

> "The hottest new programming language is English." — Frequently attributed aphorism

> "Vibe coding is where you fully give in to the vibes, embrace exponentials, and forget that the code even exists." — Twitter, Feb 2025

> "LLMs are not databases. They are probabilistic knowledge stores. Everything they 'know' is vague and statistical — not precise." — Deep Dive into LLMs, 2024

> "When relevant information is in the context window, the model doesn't need to 'recall' — quality improves dramatically. Always paste reference material directly." — Deep Dive into LLMs, 2024

## Related Entries
- [[llm-wiki-pattern]]
- [[karpathy-deep-dive-llms]]
- [[llm-wiki-ecosystem]]
- [[acdc-agent-centric-development-cycle]]
- [[spec-driven-development-bmad]]

---
<!-- RU -->

## Краткое описание

Андрей Карпаты — словацко-канадский исследователь ИИ, педагог и один из основателей OpenAI. Он занимал должность директора по ИИ в Tesla, возглавляя систему компьютерного зрения автопилота, создал легендарный курс Stanford CS231n и ввёл фундаментальные концепции, включая «Software 2.0», «vibe coding» и паттерн «LLM Wiki». В 2024 году основал Eureka Labs — образовательную компанию на базе ИИ.

## Ключевые идеи

- **Software 2.0 (2017):** Нейросети — не просто ещё один инструмент ML, а фундаментальный сдвиг в программировании. Вместо написания явного кода мы задаём цели и датасеты, а оптимизация ищет программу в пространстве решений. «Исходный код» — это датасеты + архитектура; обучение компилирует их в работающую программу.
- **LLM OS (2025):** LLM может служить ядром новой операционной системы для интеллектуальной работы — оркестрируя инструменты, память и агентов. Та же модель, что ведёт диалог, может управлять файловой системой, запускать код, просматривать веб и порождать субагентов.
- **Паттерн LLM Wiki (2025):** Трёхуровневая архитектура, где сырые источники «компилируются» LLM-агентом в живую вики. Уровень 1 — неизменяемые входные данные, Уровень 2 — статьи вики, написанные LLM, Уровень 3 — файл схемы (AGENTS.md), контролирующий инъекцию контекста. Знания накапливаются, а не пересоздаются при каждом запросе.
- **Vibe coding (февраль 2025):** Ввёл этот термин для описания разработки с помощью ИИ, когда разработчик описывает желаемое на естественном языке и позволяет ИИ генерировать, запускать и итерировать код.
- **LLM как вероятностное хранилище знаний:** Всё, что LLM «знает», расплывчато, статистично и неточно. Контекстное окно важнее параметрической памяти — всегда вставляйте справочный материал напрямую, а не полагайтесь на воспроизведение из обучения.
- **Образование как ИИ-приложение с наивысшим рычагом:** Траектория его карьеры (OpenAI → Tesla → Eureka Labs) отражает убеждение, что обучение ИИ-грамотности в масштабе важнее любого отдельного продукта.

## Хронология карьеры

| Период | Роль | Ключевой вклад |
|--------|------|----------------|
| 2005–2009 | Бакалавриат, University of Toronto | CS + физика; посещал курс глубокого обучения Джеффри Хинтона |
| 2009–2011 | Магистратура, UBC | Контроллеры для физически симулированных фигур |
| 2011–2015 | PhD, Stanford | Генерация описаний изображений; создал и преподавал CS231n (вырос с 150 до 750 студентов) |
| 2015–2017 | Научный сотрудник, OpenAI | Член-основатель; глубокое обучение и компьютерное зрение |
| 2017–2022 | Директор по ИИ, Tesla | Руководил командой компьютерного зрения автопилота; разметка данных, обучение нейросетей, развёртывание на собственном чипе |
| 2023–2024 | Научный сотрудник, OpenAI (возвращение) | Создал команду по midtraining и генерации синтетических данных |
| 2024–наст. время | Основатель, Eureka Labs | Образовательная платформа на базе ИИ; первый курс: LLM101n |

## Основные идеи и вклад

### Software 2.0 (2017)

Самое влиятельное эссе Карпаты утверждает, что нейросети формируют новую парадигму программирования, фундаментально отличную от классического кодирования. Ключевое прозрение: во многих областях проще собрать обучающие данные и задать желаемое поведение, чем написать явные правила. Индустрия ПО переживает массовый переход, где большие части кодовых баз «портируются» из Software 1.0 (явные инструкции) в Software 2.0 (обученные веса).

Преимущества стека 2.0: вычислительная однородность (в основном matmul + ReLU), постоянное время выполнения, постоянное использование памяти, высокая портативность, гибкость при изменении ресурсов и возможность обратного распространения через модули в оптимальное целое.

### Vibe Coding (2025)

Термин, введённый в Twitter в феврале 2025, описывающий новый режим разработки ПО, где разработчики дают высокоуровневые описания и позволяют ИИ заниматься деталями реализации. Мгновенно стал культурным феноменом в сообществе разработчиков. Представляет логическое расширение Software 2.0 — программист переходит от написания кода к спецификации намерений.

### Образовательная философия

YouTube-канал Карпаты содержит два параллельных трека: техническую серию «Zero to Hero» по внутреннему устройству нейросетей и серию для широкой аудитории «Deep Dive into LLMs». Его ключевое убеждение: ИИ-образование должно охватывать как инженеров, создающих системы, так и общественность, которая будет с ними жить.

### Интересные факты
- Носил титул «эталонного человека» для ImageNet после соревнования с нейросетью в классификации 1 000 классов
- Бывший спидкубер: собирал кубики Рубика за ~17 секунд; его YouTube-канал «badmephisto» имеет более 9 млн просмотров
- Назван одним из 100 самых влиятельных людей в ИИ по версии TIME (2024) и MIT Innovators Under 35 (2020)

## Примечательные цитаты

> «Софт (1.0) пожирает мир, а теперь ИИ (Software 2.0) пожирает софт.» — Software 2.0, 2017

> «LLM — это не базы данных. Это вероятностные хранилища знаний. Всё, что они "знают", расплывчато и статистично — не точно.» — Deep Dive into LLMs, 2024

> «Vibe coding — это когда ты полностью отдаёшься вайбу, принимаешь экспоненты и забываешь, что код вообще существует.» — Twitter, февраль 2025

## Связанные записи
- [[llm-wiki-pattern]]
- [[karpathy-deep-dive-llms]]
- [[llm-wiki-ecosystem]]
- [[acdc-agent-centric-development-cycle]]
