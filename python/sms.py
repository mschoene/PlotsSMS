from array import *

class sms():

    def __init__(self, modelname):
        self.mTopDiagOn = False
        self.t2ccDiagOn = False
        self.diagOn     = False
        if modelname.find("T1tttt") != -1: self.T1tttt()
        if modelname.find("T1bbbb") != -1: self.T1bbbb()
        if modelname.find("T1qqqq") != -1: self.T1qqqq()
        if modelname.find("T2tt")   != -1: self.T2tt  ()
        if modelname.find("T2bb")   != -1: self.T2bb  ()
        if modelname.find("T2qq")   != -1: self.T2qq  ()
        if modelname.find("T2cc")   != -1: self.T2cc  ()
        if modelname.find("T2ttcc") != -1: self.T2ttcc()

        if modelname.find("T2bH") != -1: self.T2bH()
        if modelname.find("TChiWH") != -1: self.TChiWH()


    def T1tttt(self):
        # model name
        self.modelname = "T1tttt"
        # decay chain
        self.label= "pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow t #bar{t} #tilde{#chi}^{0}_{1}";
        # scan range to plot
        self.Xmin = 600
        self.Xmax = 2000
        self.Ymin = 0
        self.Ymax = 1800
        self.Zmin = 0.001
        self.Zmax = 2
        # produce sparticle
        self.sParticle = "m_{#kern[0.2]{#tilde{g}}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # diagonal position: mLSP = mgluino - 2mtop 
        mT = 175
        self.diagX = array('d',[0,20000])
        self.diagY = array('d',[-mT, 20000-mT])        
        # turn off diagonal lines
        self.diagOn = False
        self.mTopDiagOn = False
        
    def T1bbbb(self):
        # model name
        self.modelname = "T1bbbb"
        # decay chain
        self.label= "pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow b #bar{b} #tilde{#chi}^{0}_{1}";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 600
        self.Xmax = 2100
        self.Ymin = 0
        self.Ymax = 1800
        self.Zmin = 0.001
        self.Zmax = 2
        # produce sparticle
        self.sParticle = "m_{#kern[0.2]{#tilde{g}}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # diagonal position: mLSP = mgluino - 2mtop
        self.diagX = array('d',[0,20000])
        self.diagY = array('d',[0, 20000])
        # turn off diagonal lines
        self.diagOn = False
        self.mTopDiagOn = False
 
    def T1qqqq(self):
        # model name
        self.modelname = "T1qqqq"
        # decay chain
        self.label= "pp #rightarrow #tilde{g} #tilde{g}, #tilde{g} #rightarrow q #bar{q} #tilde{#chi}^{0}_{1}";
        # plot boundary. The top 1/4 of the y axis is taken by the legend
        self.Xmin = 600
        self.Xmax = 2000
        self.Ymin = 0
        self.Ymax = 1800
        self.Zmin = 0.001
        self.Zmax = 2
        # produce sparticle
        self.sParticle = "m_{#kern[0.2]{#tilde{g}}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # diagonal position: mLSP = mgluino - 2mtop
        self.diagX = array('d',[0,20000])
        self.diagY = array('d',[0, 20000])
        # turn off diagonal lines
        self.diagOn = False
        self.mTopDiagOn = False

    def T2tt(self):
        # model name
        self.modelname = "T2tt"
        # decay chain
        self.label= "pp #rightarrow #tilde{t} #bar{_{_{ }}#tilde{t}_{_{ }}}, #tilde{t} #rightarrow t #tilde{#chi}^{0}_{1}";
        # scan range to plot
        self.Xmin = 150
        self.Xmax = 1200
        self.Ymin = 0
        self.Ymax = 700
        self.Zmin = 0.001
        self.Zmax = 100
        #self.Zmin = 0.1
        #self.Zmax = 10
        # produce sparticle
        self.sParticle = "m_{#kern[0.7]{#tilde{t}}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # diagonal position: mLSP = mgluino - 2mtop 
        mW = 75
        self.diagX = array('d',[0,20000])
        self.diagY = array('d',[-mW, 20000-mW])        
        # turn off diagonal lines
        self.diagOn = True
        #self.mT, self.dM = 172.5, 6.25
        self.mT, self.dM = 175, 25
        self.mTopDiagOn = True
 
    def T2ttcc(self):
        # model name
        self.modelname = "T2ttcc"
        # decay chain
        self.label= "pp #rightarrow #tilde{t} #bar{#tilde{t}}, #tilde{t} #rightarrow t(c) #tilde{#chi}^{0}_{1}";
        # scan range to plot
        self.Xmin = 100
        self.Xmax = 900
        self.Ymin = 0
        self.Ymax = 500
        self.Zmin = 0.001
        self.Zmax = 200
        #self.Zmin = 0.1
        #self.Zmax = 10
        # produce sparticle
        self.sParticle = "m_{#tilde{t}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # diagonal position: mLSP = mgluino - 2mtop 
        mW = 75
        self.diagX = array('d',[0,20000])
        self.diagY = array('d',[-mW, 20000-mW])        
        # turn off diagonal lines
        #self.diagOn = True
        #self.mT, self.dM = 172.5, 6.25
        self.mT, self.dM = 175, 25
        self.mTopDiagOn = True
    

    def T2cc(self):
        # model name
        self.modelname = "T2cc"
        # decay chain
        self.label= "pp #rightarrow #tilde{t} #bar{#tilde{t}}, #tilde{t} #rightarrow c #tilde{#chi}^{0}_{1}";
        # scan range to plot
        self.Xmin = 100
        self.Xmax = 600
        self.Ymin = 0
        self.Ymax = 800
        self.Zmin = 1
        self.Zmax = 100
        #self.Zmin = 0.1
        #self.Zmax = 10
        # produce sparticle
        self.sParticle = "m_{#tilde{t}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # diagonal position: mLSP = mgluino - 2mtop 
        mW = 0
        self.diagX = array('d',[0,20000])
        self.diagY = array('d',[-mW, 20000-mW])        
        # turn off diagonal lines
        self.diagOn = False
        #self.mT, self.dM = 172.5, 6.25
        self.mT, self.dM = 80, 0
        self.mTopDiagOn = False
        self.t2ccDiagOn = True

    def T2bb(self):
        # model name
        self.modelname = "T2bb"
        # decay chain
        self.label= "pp #rightarrow #tilde{b} #bar{#tilde{b}}, #tilde{b} #rightarrow b #tilde{#chi}^{0}_{1}";
        # scan range to plot
        self.Xmin = 300
        self.Xmax = 1200
        self.Ymin = 0
        self.Ymax = 800
        self.Zmin = 0.001
        self.Zmax = 20
        # produce sparticle
        self.sParticle = "m_{#kern[0.1]{#tilde{b}}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # diagonal position: mLSP = mgluino - 2mtop 
        mW = 75
        self.diagX = array('d',[0,20000])
        self.diagY = array('d',[-mW, 20000-mW])        
        # turn off diagonal lines
        self.diagOn = False
        #self.mT, self.dM = 172.5, 6.25
        self.mT, self.dM = 175, 25
        self.mTopDiagOn = False
        
    def T2qq(self):
        # model name
        self.modelname = "T2qq"
        # decay chain
        self.label= "pp #rightarrow #tilde{q} #bar{#tilde{q}}, #tilde{q} #rightarrow q #tilde{#chi}^{0}_{1}";
        # scan range to plot
        self.Xmin = 300
        self.Xmax = 1600
        self.Ymin = 0
        self.Ymax = 1200
        self.Zmin = 0.001
        self.Zmax = 20
        # produce sparticle
        self.sParticle = "m_{#kern[0.15]{#tilde{q}}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # diagonal position: mLSP = mgluino - 2mtop 
        mW = 75
        self.diagX = array('d',[0,20000])
        self.diagY = array('d',[-mW, 20000-mW])        
        # turn off diagonal lines
        self.diagOn = False
        #self.mT, self.dM = 172.5, 6.25
        self.mT, self.dM = 175, 25
        self.mTopDiagOn = False
        
    def T2bH(self):
        # model name
        self.modelname = "T2bH"
        # decay chain
        self.label= "pp #rightarrow #tilde{b} #bar{#tilde{b}}, #tilde{b} #rightarrow b #tilde{#chi}^{0}_{2}  #rightarrow bH #tilde{#chi}^{0}_{1}";
        # scan range to plot
        self.Xmin = 250
        self.Xmax = 600
        self.Ymin = 0
        self.Ymax = 400
        self.Zmin = 0.1
        self.Zmax = 2
        # produce sparticle
        self.sParticle = "m_{#kern[0.1]{#tilde{b}}} [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # diagonal position: mLSP = mgluino - 2mtop 
        mW = 75
        self.diagX = array('d',[0,20000])
        self.diagY = array('d',[-mW, 20000-mW])        
        # turn off diagonal lines
        self.diagOn = False
        #self.mT, self.dM = 172.5, 6.25
        self.mT, self.dM = 175, 25
        self.mTopDiagOn = False
        
    def TChiWH(self):
        # model name
        self.modelname = "TChiWH"
        # decay chain
        self.label= "pp #rightarrow #tilde{#chi}_{1}^{#pm} #tilde{#chi}_{2}^{0},  #tilde{#chi}_{1}^{#pm} #rightarrow W^{#pm} #tilde{#chi}_{1}^{0}, #tilde{#chi}_{2}^{0} #rightarrow H #tilde{#chi}_{1}^{0} ";
        # scan range to plot
        self.Xmin = 125
        self.Xmax = 250
        self.Ymin = 0
        self.Ymax = 200
        self.Zmin = 1
        self.Zmax = 6
        # produce sparticle
        self.sParticle = "m_{#kern[0.1]{#tilde{#chi}_{1}^{#pm}}} = m_{#kern[0.1]{#tilde{#chi}_{2}^{0}}}  [GeV]"
        # LSP
        self.LSP = "m_{#tilde{#chi}_{1}^{0}} [GeV]"
        # diagonal position: mLSP = mgluino - 2mtop 
        mW = 75
        self.diagX = array('d',[0,20000])
        self.diagY = array('d',[-mW, 20000-mW])        
        # turn off diagonal lines
        self.diagOn = False
        #self.mT, self.dM = 172.5, 6.25
        self.mT, self.dM = 175, 25
        self.mTopDiagOn = False
        
