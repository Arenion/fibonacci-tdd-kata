import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    return


app._unparsable_cell(
    r"""
    def fibonnaci(a: int, b: int) -> int:
    
    """,
    name="_"
)


if __name__ == "__main__":
    app.run()
