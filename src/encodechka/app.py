import gradio as gr
import pandas as pd
from about import (
    INTRODUCTION_TEXT,
    TITLE,
)
from apscheduler.schedulers.background import BackgroundScheduler
from display.css_html_js import custom_css
from display.utils import (
    COLS,
    TYPES,
    AutoEvalColumn,
    fields,
)

from parser import update_leaderboard_table
from populate import get_leaderboard_df
from settings import (
    get_settings,
)

settings = get_settings()



def filter_table(
    hidden_df: pd.DataFrame,
    columns: list,
    show_deleted: bool,
    query: str,
) -> pd.DataFrame:
    filtered_df = filter_models(hidden_df, show_deleted)
    filtered_df = filter_queries(query, filtered_df)
    df = select_columns(filtered_df, columns)
    return df


def search_table(df: pd.DataFrame, query: str) -> pd.DataFrame:
    return df[(df[AutoEvalColumn.model.name].str.contains(query, case=False))]


def select_columns(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    always_here_cols = [
        AutoEvalColumn.model.name.lower(),
    ]
    s = [c for c in COLS if c in df.columns and c in columns]
    filtered_df = df[always_here_cols + s]
    return filtered_df


def filter_queries(query: str, filtered_df: pd.DataFrame) -> pd.DataFrame:
    final_df = []
    if query != "":
        queries = [q.strip() for q in query.split(";")]
        for _q in queries:
            _q = _q.strip()
            if _q != "":
                temp_filtered_df = search_table(filtered_df, _q)
                if len(temp_filtered_df) > 0:
                    final_df.append(temp_filtered_df)
        if len(final_df) > 0:
            filtered_df = pd.concat(final_df)
            filtered_df = filtered_df.drop_duplicates(
                subset=[
                    AutoEvalColumn.model.name,
                ]
            )
    return filtered_df


def filter_models(
    df: pd.DataFrame,
    show_deleted: bool,
) -> pd.DataFrame:
    if show_deleted:
        filtered_df = df
    else:
        filtered_df = df[df[AutoEvalColumn.is_private.name]]

    return filtered_df


def get_leaderboard() -> gr.TabItem:
    with gr.TabItem("🏅 Encodechka", elem_id="llm-benchmark-tab-table", id=0) as leaderboard_tab:
        with gr.Row():
            with gr.Column():
                with gr.Row():
                    search_bar = gr.Textbox(
                        placeholder=" 🔍 Search for your model (separate multiple queries with `;`) "
                                    "and press ENTER...",
                        show_label=False,
                        elem_id="search-bar",
                    )
                with gr.Row():
                    shown_columns = gr.CheckboxGroup(
                        choices=[c.name for c in fields(AutoEvalColumn) if not c.hidden and not c.never_hidden],
                        value=[
                            c.name
                            for c in fields(AutoEvalColumn)
                            if c.displayed_by_default and not c.hidden and not c.never_hidden
                        ],
                        label="Select columns to show",
                        elem_id="column-select",
                        interactive=True,
                    )
                with gr.Row():
                    private_models_visibility = gr.Checkbox(
                        value=True,
                        label="Show private models",
                        interactive=True,
                    )

        leaderboard_table = gr.Dataframe(
            value=get_leaderboard_df(),
            headers=[c.name for c in fields(AutoEvalColumn) if c.never_hidden] + shown_columns.value,
            datatype=TYPES,
            elem_id="leaderboard-table",
            interactive=False,
            visible=True,
        )

        hidden_leaderboard_table_for_search = gr.Dataframe(
            value=get_leaderboard_df(),
            headers=COLS,
            datatype=TYPES,
            visible=False,
        )
        search_bar.submit(
            filter_table,
            [
                hidden_leaderboard_table_for_search,
                shown_columns,
                private_models_visibility,
                search_bar,
            ],
            leaderboard_table,
        )
        for selector in [
            shown_columns,
            private_models_visibility,
        ]:
            selector.change(
                filter_table,
                [
                    hidden_leaderboard_table_for_search,
                    shown_columns,
                    private_models_visibility,
                    search_bar,
                ],
                leaderboard_table,
                queue=True,
            )
    return leaderboard_tab


def build_app() -> gr.Blocks:
    with gr.Blocks(css=custom_css) as app:
        gr.HTML(TITLE)
        gr.Markdown(INTRODUCTION_TEXT, elem_classes="markdown-text")
        get_leaderboard()
        return app


def main():
    update_leaderboard_table()
    app = build_app()
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_leaderboard_table, "interval", days=1)
    scheduler.start()
    app.queue(default_concurrency_limit=40).launch()


if __name__ == "__main__":
    main()
