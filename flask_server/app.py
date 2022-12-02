from flask import Flask,request,jsonify

from interface import BreastCancerInterface
from base64 import encodebytes

app = Flask(__name__)

breastCancerInterface = BreastCancerInterface()

chart_types_constant = ['Violin Plot', 'Box Plot', 'Joint Plot', 'Swarm Plot', 'HeatMap']

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

def get_response_image(byte_arr):
    encoded_img = encodebytes(byte_arr.getvalue()).decode('ascii') # encode as base64
    return encoded_img


@app.route("/api/charts",methods=['POST'])
def get_charts():
    request_data = request.get_json()
    features = request_data['features']
    chart_types = request_data['chartTypes']
    return_obj = {}
    print(features)
    print(chart_types)
    for chart in chart_types:
        if(chart == 'Violin Plot'):
            print(chart)
            return_obj[chart] = breastCancerInterface.get_violion_plot(features)
        if(chart == 'Box Plot'):
            print(chart)            
            return_obj[chart] = breastCancerInterface.get_box_plot(features)
        if(chart == 'Joint Plot'):
            print(chart)
            return_obj[chart] = breastCancerInterface.get_joint_plot(features)
        if(chart == 'Swarm Plot'):
            print(chart)
            return_obj[chart] = breastCancerInterface.get_swarm_plot(features)
        if(chart == 'HeatMap'):
            print(chart)
            return_obj[chart] = breastCancerInterface.get_heat_map_plot(features)
    encoded_imges = {}
    for key in return_obj:
        encoded_imges[key] = get_response_image(return_obj[key])
    return jsonify({**encoded_imges})

@app.route("/api/prediction",methods=['POST'])
def get_prediction():
    print("Hello")
    request_data = request.get_json()
    print(request_data)
    return jsonify(11.28)

if __name__ == "__main__":
    app.run(debug=True,threaded=True)