from dataclasses import dataclass, make_dataclass

from about import Tasks


def fields(raw_class):
    return [v for k, v in raw_class.__dict__.items() if k[:2] != "__" and k[-2:] != "__"]


# These classes are for user facing column names,
# to avoid having to change them all around the code
# when a modif is needed
@dataclass
class ColumnContent:
    name: str
    type: str
    displayed_by_default: bool
    hidden: bool = False
    never_hidden: bool = False


auto_eval_column_dict = [
    (
        "model",
        ColumnContent,
        ColumnContent("model", "markdown", True, never_hidden=True),
    ),
    ("CPU", ColumnContent, ColumnContent("CPU", "number", True)),
    ("GPU", ColumnContent, ColumnContent("GPU", "number", True)),
    ("size", ColumnContent, ColumnContent("size", "number", True)),
    ("MeanS", ColumnContent, ColumnContent("Mean S", "number", True)),
    ("MeanSW", ColumnContent, ColumnContent("Mean S+W", "number", True)),
    ("dim", ColumnContent, ColumnContent("dim", "number", True)),
    ("STS", ColumnContent, ColumnContent("STS", "number", True)),
    ("PI", ColumnContent, ColumnContent("PI", "number", True)),
    ("NLI", ColumnContent, ColumnContent("NLI", "number", True)),
    ("SA", ColumnContent, ColumnContent("SA", "number", True)),
    ("TI", ColumnContent, ColumnContent("TI", "number", True)),
    ("II", ColumnContent, ColumnContent("II", "number", True)),
    ("IC", ColumnContent, ColumnContent("IC", "number", True)),
    ("ICX", ColumnContent, ColumnContent("ICX", "number", True)),
    ("NE1", ColumnContent, ColumnContent("NE1", "number", True)),
    ("NE2", ColumnContent, ColumnContent("NE2", "number", True)),
    (
        "is_private",
        ColumnContent,
        ColumnContent("is_private", "boolean", True, hidden=True),
    ),
]
# We use make dataclass to dynamically fill the scores from Tasks
AutoEvalColumn = make_dataclass("AutoEvalColumn", auto_eval_column_dict, frozen=True)

COLS = [c.name for c in fields(AutoEvalColumn) if not c.hidden]
TYPES = [c.type for c in fields(AutoEvalColumn) if not c.hidden]
COLS_LITE = [c.name for c in fields(AutoEvalColumn) if c.displayed_by_default and not c.hidden]
TYPES_LITE = [c.type for c in fields(AutoEvalColumn) if c.displayed_by_default and not c.hidden]

BENCHMARK_COLS = [t.value.col_name for t in Tasks]
