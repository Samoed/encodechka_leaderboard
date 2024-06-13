from dataclasses import dataclass
from enum import Enum


@dataclass
class Task:
    benchmark: str
    metric: str
    col_name: str


class Tasks(Enum):
    STS = Task("STS", "STS", "STS")
    PI = Task("PI", "PI", "PI")
    NLI = Task("NLI", "NLI", "NLI")
    SA = Task("SA", "SA", "SA")
    TI = Task("TI", "TI", "TI")
    II = Task("II", "II", "II")
    IC = Task("IC", "IC", "IC")
    ICX = Task("ICX", "ICX", "ICX")
    NE1 = Task("NE1", "NE1", "NE1")
    NE2 = Task("NE2", "NE2", "NE2")


TITLE = """<h1 align="center" id="space-title">Encodechka</h1>"""

INTRODUCTION_TEXT = """
<a href="https://github.com/avidale/encodechka">Оригинальный репозиторий GitHub</a>

Задачи
- Semantic text similarity (**STS**) на основе переведённого датасета
[STS-B](https://huggingface.co/datasets/stsb_multi_mt);
- Paraphrase identification (**PI**) на основе датасета paraphraser.ru;
- Natural language inference (**NLI**) на датасете [XNLI](https://github.com/facebookresearch/XNLI);
- Sentiment analysis (**SA**) на данных [SentiRuEval2016](http://www.dialog-21.ru/evaluation/2016/sentiment/).
- Toxicity identification (**TI**) на датасете токсичных комментариев из
[OKMLCup](https://cups.mail.ru/ru/contests/okmlcup2020);
- Inappropriateness identification (**II**) на
[датасете Сколтеха](https://github.com/skoltech-nlp/inappropriate-sensitive-topics);
- Intent classification (**IC**) и её кросс-язычная версия **ICX** на датасете
[NLU-evaluation-data](https://github.com/xliuhw/NLU-Evaluation-Data), который я автоматически перевёл на русский.
В IC классификатор обучается на русских данных, а в ICX – на английских, а тестируется в обоих случаях на русских.
- Распознавание именованных сущностей на датасетах
[factRuEval-2016](https://github.com/dialogue-evaluation/factRuEval-2016) (**NE1**) и
[RuDReC](https://github.com/cimm-kzn/RuDReC) (**NE2**). Эти две задачи требуют получать эмбеддинги отдельных токенов,
а не целых предложений; поэтому там участвуют не все модели.
"""
