
# Fuzzy Logic System for Penguin Enclosure Air Conditioning Control

This project uses fuzzy logic to control air conditioning in a penguin zoo enclosure, based on outside temperature, biologic temperature, and the number of penguins. This system leverages the scikit-fuzzy library to define fuzzy variables, membership functions, and rules for controlling air conditioning levels in the enclosure.
Project Structure

## The project defines three fuzzy variables (or antecedents) as inputs:

    outside_temperature (in °C)
    biologic_temperature (in °C)
    penguins_number (count of penguins in the enclosure)

## The output (consequent) variable is:

    air_conditioning (desired temperature adjustment level)

# Dependencies

To run this code, install the following libraries:

bash

pip install numpy scikit-fuzzy matplotlib

## Fuzzy Variables and Membership Functions

Each variable has associated membership functions that categorize it into linguistic terms. For example:

    Outside Temperature:
        cold (trapmf)
        warm (trimf)
        hot (trapmf)

    Biologic Temperature:
        cool dead (trapmf)
        good (gaussmf)
        hot dead (trapmf)

    Penguins Number:
        low, average, crowded (automf with custom names)

    Air Conditioning:
        cold (trapmf)
        warm (trimf)
        hot (trapmf)

# Fuzzy Rules

The control system is based on the following rules:

    If outside_temperature is hot and penguins_number is crowded, or if biologic_temperature is hot dead, then set air_conditioning to cold.
    If outside_temperature is warm and penguins_number is average, or if biologic_temperature is good, then set air_conditioning to warm.
    If outside_temperature is cold and penguins_number is low, or if biologic_temperature is cool dead, then set air_conditioning to hot.