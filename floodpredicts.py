
def predictflooded(latis,longis,rainfall,temps,humids,rivers,wlevel,eliv,wbody,stype,pdensity,infras,hist):
    import pickle
    import pandas as pd
    print(type(latis))
    # Load the saved model
    with open('flood_batata.pkl', 'rb') as file:
        loaded_model = pickle.load(file)

    # Prepare new data for prediction
    new_data = pd.DataFrame({
        'Latitude': [latis],
        'Longitude': [longis],
        'Rainfall (mm)': [rainfall],
        'Temperature (°C)': [temps],
        'Humidity (%)': [humids],
        'River Discharge (m³/s)': [rivers],
        'Water Level (m)': [wlevel],
        'Elevation (m)': [eliv],
        'Land Cover': [wbody],
        'Soil Type': [stype],
        'Population Density': [pdensity],
        'Infrastructure': [infras],
        'Historical Floods': [hist]
    })

    print(new_data)

    # Make predictions using the loaded model
    predicted_probabilities = loaded_model.predict_proba(new_data)[:, 1]  # Get the probability of flood (class 1)

    # Output the predicted flood probability
    print(f"Predicted Flood Probability: {predicted_probabilities[0]}")

    # Check if the flood probability is greater than 50%
    if predicted_probabilities[0] > 0.5:
        out="The place is NOT good for building (high flood risk)."
    else:
        out="The place is GOOD for building (low flood risk)."

    return out 

# predictflooded(18.861663,78.835584,78.835584,34.144337,43.912963,4677.182888,200.415552,377.465433,'Water Body','Clay',7600.74,1,0)