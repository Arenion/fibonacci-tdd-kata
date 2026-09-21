import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pytest as pt

    return


@app.function
def fibonnaci(a: int) -> int:
    if a==0:
        return 0
    elif a == 1:
        return 1
    else:
        return fibonnaci(a-2)+fibonnaci(a-1)


@app.cell
def test_fibo_1():
    assert fibonnaci(0)==0

    return


@app.cell
def test_fibo_2():
    assert fibonnaci(1)==1

    return


@app.cell
def test_fibo_3():
    assert fibonnaci(7)==13
    return


@app.cell
def _():
    #started this one early, will not be useful until future commit

    # @pt.mark.parametrize(
    #     ("n","expected"),
    #     [
    #         (0,0)
    #         (1,1)
    #         (2,1)
    #         (3,2)
    #         (4,3)
    #         (5,5)
    #         (6,8)
    #         (7,13)
        
    #     ]
    # )
    return


if __name__ == "__main__":
    app.run()
