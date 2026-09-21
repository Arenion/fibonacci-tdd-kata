import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pytest as pt

    return


@app.cell
def _():
    fibodict={0:0,1:1}
    def fibonnaci(a: int) -> int:
        if not isinstance(a, int) or a<0:
            raise ValueError("fibonnaci, the function that calculate the value of fibonnaci of an integer, expect a positive integer")
        if a in fibodict:
            return fibodict[a]
        else:
            newresult= fibonnaci(a-2)+fibonnaci(a-1)
            fibodict[a]= newresult
            return newresult


    return (fibonnaci,)


@app.cell
def test_fibo_1(fibonnaci):
    assert fibonnaci(0)==0

    return


@app.cell
def test_fibo_2(fibonnaci):
    assert fibonnaci(1)==1

    return


@app.cell
def test_fibo_3(fibonnaci):
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
