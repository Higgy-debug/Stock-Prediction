X_test=[]
for i in range(60,inputs_data.shape[0]):
    X_test.append(inputs_data[i-60:i,0])
X_test=np.array(X_test)

X_test=np.reshape(X_test,(X_test.shape[0],X_test.shape[1],1))
prediction_closing_point = lstm_model.predict(X_test)
prediction_closing_point = scaler.inverse_transform(prediction_closing_point)

lstm_model.save("saved_lstm_model.h5")

train_data=new_dataset[:987]
valid_data=new_dataset[987:]
valid_data['Predictions'] = prediction_closing_point
plt.plot(train_data["Close"])
plt.plot(valid_data[['Close',"Predictions"]])
