from flask import Flask, render_template,request
import pickle

mod=pickle.load(open('model.sav','rb'))


app = Flask(__name__)



@app.route("/")
def home():
    return render_template("index.html")




@app.route("/predict", methods=['POST','GET'])
def fun():
    if(request.method=='POST'):
        snr_cit=request.form['snr']
        mon_chrge=request.form['mon']
        tot_chrge=request.form['total']
        gendr=request.form['gndrMale']
        partner=request.form['partnerY']
        depen=request.form['depenY']
        phoneS=request.form['phoneSer']
        multiPhone=request.form['multiPhoneser']
        multiLine=request.form['multipleLine']
        internfib=request.form['internetFibre']
        internetSer=request.form['internetSer']
        onlineInt=request.form['onlineInter']
        onlinesecur=request.form['onlineSecur']
        onlineBack=request.form['onlineBackInt']
        onlineB=request.form['onlineBack']
        deviceP=request.form['deviceProInter']
        devicepro=request.form['devicePro']
        techInt=request.form['techSuppInter']
        techsupp=request.form['techSupp']
        stream=request.form['streamTVInter']
        streamTV=request.form['streamTV']
        streamMovie=request.form['streamMovieInter']
        streamMoviesupp=request.form['streamMovie']
        contractOne=request.form['contractOne']
        contractTwo=request.form['contractTwo']
        paperless=request.form['paperLessBill']
        payCard=request.form['paymentCard']
        payEle=request.form['paymentElec']
        payMail=request.form['paymentMail']
        prediction=mod.predict([[snr_cit,mon_chrge,tot_chrge,gendr,partner,depen,phoneS,multiPhone,multiLine,internfib,internetSer,onlineInt,onlinesecur,onlineBack,onlineB,deviceP,devicepro,techInt,techsupp,stream,streamTV,streamMovie,streamMoviesupp,contractOne,contractTwo,paperless,payCard,payEle,payMail]])
        if prediction==1:
            return render_template('index.html',prediction_text='The customer will churn')
        else:
            return render_template('index.html',prediction_text='The customer will not churn')

    return render_template('index.html')





if __name__== "__main__":
    app.run(debug=True)