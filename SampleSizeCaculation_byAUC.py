from math import ceil
from statsmodels.stats.power import NormalIndPower

# Initialize parameters
AUC_exp = '0.97' # as example
AUC_H0 = '0.95'
effect_size = AUC_exp - AUC_H0  # The difference between expected AUC and H0 AUC
alpha = 0.05  # Significance level
power = 0.95  # Desired power
ratio_neg_to_pos = 4 / 1  # 4:1 ratio of negative to positive samples

# Using NormalIndPower to calculate the sample size
power_analysis = NormalIndPower()

# Calculate the total sample size required
total_sample_size = power_analysis.solve_power(effect_size=effect_size, alpha=alpha, power=power, ratio=ratio_neg_to_pos)

# Since we can't have fractions of samples, rounding up to the nearest whole number
total_sample_size_rounded = ceil(total_sample_size)

# Calculating the number of positive and negative samples based on the 4:1 ratio
num_negative_samples = ceil(total_sample_size_rounded * (ratio_neg_to_pos / (1 + ratio_neg_to_pos)))
num_positive_samples = total_sample_size_rounded - num_negative_samples

total_sample_size_rounded, num_negative_samples, num_positive_samples
