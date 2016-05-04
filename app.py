from flask import Flask, render_template, request, redirect

import fetching                 # my fetching.py file

app = Flask(__name__)


@app.route('/')
def main():
    return redirect('/index')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/leaflet')
def leaflet():

    nyc = fetching.nyc_current()

    plotdf = nyc[['MonitoredVehicleJourney_PublishedLineName',
                  'MonitoredVehicleJourney_VehicleLocation_Latitude',
                  'MonitoredVehicleJourney_VehicleLocation_Longitude']]

    # add this for plot (may not be using yet)
    plotdf = plotdf.assign(intensity=0.2);
    #data = list(plotdf.itertuples())
    #data = plotdf.values.tolist()
    data = plotdf[['MonitoredVehicleJourney_VehicleLocation_Latitude',
                   'MonitoredVehicleJourney_VehicleLocation_Longitude']].values.tolist()
    return render_template('leaflet.html', data=data)

@app.route('/live_example')
def live_example():
    return render_template('live_example.html')


if __name__ == '__main__':
    app.run(port=33507)
