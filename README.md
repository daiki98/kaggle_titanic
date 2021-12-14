# Kaggle Titanic competition

## Data info

<img src="image/data_info.png" alt="data_info" width="400">
<img src="image/num_unique_value.png" alt="data_info" width="400">
<img src="image/null_rate.png" alt="data_info" width="300">

## How to clean the data
### Missing values:
* Cabin
* Age
* Embarked

### Categorical value
* Sex<br>
It has only two values, so I gonna convert it to 0 and 1.
* Name & Ticket<br>
They don't have any useful information, so I gonna drop it off. 
* Cabin
It could be useful if it doesn't drop such a many data. 77% of missing data is too much missing.
* 
