#!/usr/bin/env python3
import pandas as pd
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

def main():
    wave_df = pd.read_pickle('./wave_data.pkl').sort_index()
    
    X = wave_df.drop(columns=['surf_humanRelation', 'timestamp_utc', 'rating']).to_numpy()
    y = wave_df['rating'].to_numpy()
    
    (X_train, X_test, y_train, y_test) = train_test_split(X, y, test_size=0.25, random_state=0)
    
    logit_model = LogisticRegression(random_state=0, penalty='elasticnet', solver='saga', l1_ratio=0.5).fit(X_train, y_train) # ElasticNet from experience tends to do better. But really an arb choice on my part here

    y_pred = logit_model.predict(X_test)
    accuracy = np.round(100 * np.sum(y_pred == y_test) / len(y_test), 4)
    
    print(f'Model Accuracy: {accuracy}')
    print('---------------------------')
    
    # for (y_p, y_t) in zip(y_pred, y_test):
    #     if y_p == y_t:
    #         print(f'Passed: y_hat {y_p} | y_test {y_t}')
    #     else:
    #         print(f'Failed: y_hat {y_p} | y_test {y_t}')

    
if __name__ == '__main__':
    main()
