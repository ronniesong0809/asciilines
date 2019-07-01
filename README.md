# asciilines
Copyright (c) 2019 Ronnie Song

This is a toy that render a `.tvg` file ("Text Vector Graphics") to ASCII output.

For example test1.tvg:
```
3 4
* 1 -1 h 5
# -1 1 v 5
```
should render to:
```
.#..
*#**
.#..
```

## Run

```
$ python3 asciilines.py tests/test1.tvg
.#..
*#**
.#..
```

## License

This program is licensed under the "MIT License".  Please
see the file `LICENSE` in the source distribution of this
software for license terms.
