from flask import Flask, request, Response
from flask_ngrok import run_with_ngrok
import pandas as pd
import json

app = Flask(__name__)
#run_with_ngrok(app)  # Start ngrok when app is run

@app.route("/otimiza/", defaults={'n_clusters': 2}, methods=['POST'])
@app.route("/otimiza/<n_clusters>", methods=['POST'])
def otimiza(n_clusters):
    data = json.loads(request.data)
    df = pd.DataFrame(data)
    df_predito = treina(df, n_clusters)

    return Response(df_predito.to_json(orient='records'), mimetype='Application/Json')

def treina(df, n_clusters=2):
    from sklearn.cluster import KMeans

    km = KMeans(n_clusters=int(n_clusters))
    km.fit(df[["cep"]])

    df["motoboy"] = km.predict(df[["cep"]])

    return df

if __name__ == '__main__':
    app.run(host='0.0.0.0')