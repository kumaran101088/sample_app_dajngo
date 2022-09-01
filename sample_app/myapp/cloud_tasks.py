import pandas as pd

def read_convert_file(filename):
    df = pd.read_csv(filename, low_memory=False)

    def convert_bp(value):
        try:
            value = int(abs(value))
        except:
            value = 120
        if value == 0:
            value = 100
        elif (value == 1) or (value == 2):
            value = value * 100
        elif (value >= 3) and (value <= 24):
            value = value * 10
        elif value > 240:
            value = 220
        return value

    df['ap_hi_new'] = df['ap_hi'].apply(convert_bp)
    df['ap_lo_new'] = df['ap_lo'].apply(convert_bp)

    for row in range(0, len(df)):
        if df.loc[row, 'ap_hi_new'] < 30:
            print(df.loc[row, 'ap_hi_new'])
        elif df.loc[row, 'ap_hi_new'] > 240:
            print(row)
            print(df.loc[row, 'ap_hi_new'])

    for row in range(0, len(df)):
        if df.loc[row, 'ap_lo_new'] < 30:
            print(row)
            print(df.loc[row, 'ap_lo_new'])
        elif df.loc[row, 'ap_lo_new'] > 240:
            print(row)
            print(df.loc[row, 'ap_lo_new'])

    medication_new = []

    for row in range(0, len(df)):
        value = df.loc[row, 'medication']
        if value not in ['Y', 'N']:
            if (df.loc[row, 'ap_hi_new'] != 120) or (df.loc[row, 'ap_lo_new'] != 80) or (df.loc[row, 'cardio'] != 0) or (df.loc[row, 'alco'] !=0) or (df.loc[row, 'smoke'] !=0) or (df.loc[row, 'gluc'] > 1) or (df.loc[row, 'cholesterol'] > 1):
                medication_new.append('Y')
            else:
                medication_new.append('N')
        else:
            medication_new.append('N')


    df['medication_new'] = medication_new
    print('BEFORE')
    try:
        df.to_csv('MOCK_DATA.csv')
    except Exception as e:
        print(e)
    print('AFTER')