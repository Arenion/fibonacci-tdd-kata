import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pytest as pt

    return


app._unparsable_cell(
    r"""
    def fibonnaci(a: int) -> int:
    """,
    name="_"
)


@app.cell
def test_fibo_1(fibonnaci):
    assert fibonnaci()
    return


app._unparsable_cell(
    r"""
    #started this one early, will not be useful until future commit

    @pt.mark.parametrize(
        ("n","expected"),
        [
            (0,0)
            (1,1)
            (2,1)
            (3,2)
            (4,3)
            (5,5)
            (6,8)
            (7,13)
        
        ]
    )
    """,
    name="_"
)


if __name__ == "__main__":
    app.run()
