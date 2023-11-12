# NZ Twin Grid

Model of a potential power grid for New Zealand, with 98%+ renewable energy

## Usage

* Download files
* Download dependancies from pip (matplotlib, scipy)
* For single model, run `python3 main.py`
* For optimisation, run `python3 find-optimal.py`

## Usage example

```
> Python3 main.py

Summary statistics
Modelled 17520 time steps in total
Generation matched demand on 17520
Generation exceeded demand on 0
Demand exceeded generation on 0

Cost: $4,290,731,337.48

Battery maximum state of charge: 1000.0

Source             Generated (GWh)    Used (GWh)  Proportion of total usage
---------------  -----------------  ------------  ---------------------------
Total                     81642.84      81625.34  100.00%
  Renewable               79892.45      79874.95  97.86%
    geo                   14333.31      14333.31  17.56%
    wind                  17143.85      17126.36  20.98%
    hydro                 32165.69      32165.69  39.41%
    solar                 16249.60      16249.60  19.91%
  Non-renewable            1750.39       1750.39  2.14%
    fossil                 1750.39       1750.39  2.14%
```

* Edit or replace any of the text files to alter input data
* Set the `NO_TEXT_OUT` attribute to `false` to not print after every timestep

## Contributing

1. Fork it (<https://github.com/HackSheffield8-Team3/SZchallenge3>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## Credits

* Jason - main logic, optimisation ideas, staying up all night
* Echo - graphing, horrific code
* Ben - fixing Echo's code, maths
* Emma - wind model, diagrams
