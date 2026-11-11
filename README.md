# Dual Types and Base Stat Totals in Pokémon

## 1. Research Question

Do Pokémon with two types have higher base stat totals than Pokémon with a single type? Base stat total is the main summary of a Pokémon's strength, so this tests whether the game's designers gave dual-type Pokémon more total power alongside their extra type.

## 2. Hypothesis

Null hypothesis (H0): Having a second type has no relationship with base stat total. Any observed difference in mean base stat total between dual-type and single-type Pokémon is no larger than random shuffling of the type labels would produce.

Alternative hypothesis (H1): Dual-type Pokémon have a higher mean base stat total than single-type Pokémon.

## 3. Data Description

* Source: pokemon.csv, a public GitHub Gist by user armgilles (https://gist.github.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6).
* Unit of analysis: one Pokémon form per row.
* Size and variables: 800 rows covering 721 Pokédex numbers from Generations 1 to 6. The columns are Pokédex number, name, Type 1, Type 2, the six base stats (HP, Attack, Defense, Sp. Atk, Sp. Def, Speed), Total, Generation and Legendary. 414 rows have a second type and 386 do not.
* Cleaning: Mega and Primal forms (50 rows) and other alternate forms share a Pokédex number with their base forms and have merged names (for example, VenusaurMega Venusaur). I will separate them so that each species is counted once. I will confirm that Total equals the sum of the six stats, and create a single-type or dual-type label from Type 2.

## 4. Methods

* Test statistic: the difference in mean base stat total (dual-type minus single-type).
* Simulation under the null: shuffle the single-type and dual-type labels across Pokémon many times, recompute the difference each time, and compare the observed difference with this permutation distribution.
* Bootstrap metrics: the difference in mean base stat total and the difference in median base stat total.
* Non-CLT metric: the difference in medians. The Central Limit Theorem describes the sampling distribution of means, not of medians, so its interval comes from the bootstrap alone.

## 5. Results

To be completed.

## 6. Uncertainty Estimation

To be completed.

## 7. Limitations

The file was created by an individual rather than an official source and covers only Generations 1 to 6, so its values need checking against a reference such as PokéAPI. Legendary Pokémon have unusually high totals and may distort the comparison, so I will check whether the result holds with them removed.

## 8. References

* armgilles, pokemon.csv, GitHub Gist: https://gist.github.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6
* PokéAPI: https://pokeapi.co
* Python libraries: pandas, NumPy, Matplotlib
* Bergstrom, C. T. and West, J. D., Calling Bullshit (2020)
