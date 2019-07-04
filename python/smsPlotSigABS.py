import ROOT as rt
from array import *
from sms import *
from color import *
import CMS_lumi
import os
import math

class smsPlotSigABS(object):
    # modelname is the sms name (see sms.py)
    # histo is the 2D xsec map
    # obsLimits is a list of opbserved limits [NOMINAL, +1SIGMA, -1SIGMA]
    # expLimits is a list of expected limits [NOMINAL, +1SIGMA, -1SIGMA]
    # label is a label referring to the analysis (e.g. RA1, RA2, RA2b, etc)

    def __init__(self, modelname, histo, obsLimits, expLimits, obsLimits2, expLimits2, energy, lumi, preliminary, label):
        self.standardDef(modelname, histo, obsLimits, expLimits, obsLimits2, expLimits2, energy, lumi, preliminary)
        self.LABEL = label
        self.c = rt.TCanvas("cABS_%s" %label,"cABS_%s" %label,300,300)
        self.histo = histo

    def standardDef(self, modelname, histo, obsLimits, expLimits, obsLimits2, expLimits2, energy, lumi, preliminary):
        # which SMS?
        self.model = sms(modelname)
        self.OBS = obsLimits
        self.EXP = expLimits
        self.OBS2 = obsLimits2
        self.EXP2 = expLimits2
        self.lumi = lumi
        self.energy = energy
        self.preliminary = preliminary
        # create the reference empty histo
        self.emptyhisto = self.emptyHistogramFromModel()

    def standardSIGDef(self, modelname, histo, energy, lumi, preliminary):
        # which SMS?
        self.model = sms(modelname)
        self.lumi = lumi
        self.energy = energy
        self.preliminary = preliminary
        # create the reference empty histo
        self.emptyhisto = self.emptyHistogramFromModel()

    def emptyHistogramFromModel(self):
        self.emptyHisto = rt.TH2D("emptyHisto", "", 1, self.model.Xmin, self.model.Xmax, 1, self.model.Ymin, self.model.Ymax)
        
    # define the plot canvas
    def setStyle(self):
        # canvas style
        rt.gStyle.SetOptStat(0)
        rt.gStyle.SetOptTitle(0)        

#        self.c.SetLogz()
        self.c.SetTickx(1)
        self.c.SetTicky(1)

        self.c.SetRightMargin(0.19)
        self.c.SetTopMargin(0.08)
        self.c.SetLeftMargin(0.14)
        self.c.SetBottomMargin(0.14)

        # set x axis
        self.emptyHisto.GetXaxis().SetLabelFont(42)
        self.emptyHisto.GetXaxis().SetLabelSize(0.035)
        self.emptyHisto.GetXaxis().SetTitleFont(42)
        self.emptyHisto.GetXaxis().SetTitleSize(0.05)
        self.emptyHisto.GetXaxis().SetTitleOffset(1.2)
        self.emptyHisto.GetXaxis().SetTitle(self.model.sParticle)
        #self.emptyHisto.GetXaxis().CenterTitle(True)

        # set y axis
        self.emptyHisto.GetYaxis().SetLabelFont(42)
        self.emptyHisto.GetYaxis().SetLabelSize(0.035)
        self.emptyHisto.GetYaxis().SetTitleFont(42)
        self.emptyHisto.GetYaxis().SetTitleSize(0.05)
        self.emptyHisto.GetYaxis().SetTitleOffset(1.30)
        self.emptyHisto.GetYaxis().SetTitle(self.model.LSP)
        #self.emptyHisto.GetYaxis().CenterTitle(True)
                
    def DrawText(self):
        #redraw axes
        self.c.RedrawAxis()
        # white background
        graphWhite = rt.TGraph(5)
        graphWhite.SetName("white")
        graphWhite.SetTitle("white")
        graphWhite.SetFillColor(rt.kWhite)
        graphWhite.SetFillStyle(1001)
        graphWhite.SetLineColor(rt.kBlack)
        graphWhite.SetLineStyle(1)
        graphWhite.SetLineWidth(3)
        graphWhite.SetPoint(0,self.model.Xmin, self.model.Ymax)
        graphWhite.SetPoint(1,self.model.Xmax, self.model.Ymax)
        graphWhite.SetPoint(2,self.model.Xmax, self.model.Ymax*0.75)
        graphWhite.SetPoint(3,self.model.Xmin, self.model.Ymax*0.75)
        graphWhite.SetPoint(4,self.model.Xmin, self.model.Ymax)
        graphWhite.Draw("FSAME")
        graphWhite.Draw("LSAME")
        self.c.graphWhite = graphWhite
       	CMS_lumi.writeExtraText = 0
	CMS_lumi.extraText = self.preliminary
	CMS_lumi.lumi_13TeV="%s fb^{-1}" % (self.lumi)

	CMS_lumi.lumi_sqrtS = "%s TeV" % (self.energy)  
	iPos=0
	CMS_lumi.CMS_lumi(self.c,4, iPos)
        # CMS LABEL
        textCMS = rt.TLatex(0.25,0.96,"  %s " %(self.preliminary))
        textCMS.SetNDC()
        textCMS.SetTextAlign(13)
        textCMS.SetTextFont(52)
        textCMS.SetTextSize(0.038)
        textCMS.Draw()
        self.c.textCMS = textCMS
        # MODEL LABEL
        textModelLabel= rt.TLatex(0.15,0.90,"%s  NLO+NLL cross section" %self.model.label)
#        textModelLabel= rt.TLatex(0.15,0.90,"%s  NLO+NLL exclusion" %self.model.label)
        textModelLabel.SetNDC()
        textModelLabel.SetTextAlign(13)
        textModelLabel.SetTextFont(42)
        textModelLabel.SetTextSize(0.035)
        textModelLabel.Draw()
        self.c.textModelLabel = textModelLabel
        # NLO NLL XSEC
        textNLONLL= rt.TLatex(0.16,0.32,"NLO-NLL exclusion")
        textNLONLL.SetNDC()
        textNLONLL.SetTextAlign(13)
        textNLONLL.SetTextFont(42)
        textNLONLL.SetTextSize(0.04)
        textNLONLL.Draw()
        #self.c.textNLONLL = textNLONLL

        # Labels for the two set of curves in T2qq 
        if self.model.modelname != "T2qq": return

        # 8 squark label
        text8squark= rt.TLatex(750,600,"#tilde{q}_{L}+#tilde{q}_{R} (#tilde{u}, #tilde{d}, #tilde{s}, #tilde{c})")
        #text8squark.SetNDC()
        text8squark.SetTextAlign(11)
        text8squark.SetTextFont(42)
        text8squark.SetTextSize(0.035)
        text8squark.Draw()
        self.c.text8squark = text8squark
#        # 1 squark label
#        text1squark= rt.TLatex(470,300,"one light #tilde{q}")
#        #text1squark.SetNDC()
#        text1squark.SetTextAlign(11)
#        text1squark.SetTextFont(42)
#        text1squark.SetTextSize(0.035)
#        text1squark.Draw()
#        self.c.text1squark = text1squark

    def Save(self,label):
        # save the output
        os.system("mkdir -p plots")
        self.c.SaveAs("plots/%s.pdf" %label)
        self.c.SaveAs("plots/%s.root" %label)
        
    def DrawLegend(self):
        xRange = self.model.Xmax-self.model.Xmin
        yRange = self.model.Ymax-self.model.Ymin
        
        LObs = rt.TGraph(2)
        LObs.SetName("LObs")
        LObs.SetTitle("LObs")
        LObs.SetLineColor(color(self.OBS['colorLine']))
        LObs.SetLineStyle(1)
        LObs.SetLineWidth(4)
        LObs.SetMarkerStyle(20)
        LObs.SetPoint(0,self.model.Xmin+3*xRange/100, self.model.Ymax-1.35*yRange/100*10)
        LObs.SetPoint(1,self.model.Xmin+10*xRange/100, self.model.Ymax-1.35*yRange/100*10)

        LObsP = rt.TGraph(2)
        LObsP.SetName("LObsP")
        LObsP.SetTitle("LObsP")
        LObsP.SetLineColor(color(self.OBS['colorLine']))
        LObsP.SetLineStyle(1)
        LObsP.SetLineWidth(2)
        LObsP.SetMarkerStyle(20)
        LObsP.SetPoint(0,self.model.Xmin+3*xRange/100, self.model.Ymax-1.20*yRange/100*10)
        LObsP.SetPoint(1,self.model.Xmin+10*xRange/100, self.model.Ymax-1.20*yRange/100*10)

        LObsM = rt.TGraph(2)
        LObsM.SetName("LObsM")
        LObsM.SetTitle("LObsM")
        LObsM.SetLineColor(color(self.OBS['colorLine']))
        LObsM.SetLineStyle(1)
        LObsM.SetLineWidth(2)
        LObsM.SetMarkerStyle(20)
        LObsM.SetPoint(0,self.model.Xmin+3*xRange/100, self.model.Ymax-1.50*yRange/100*10)
        LObsM.SetPoint(1,self.model.Xmin+10*xRange/100, self.model.Ymax-1.50*yRange/100*10)

        textObs = rt.TLatex(self.model.Xmin+11*xRange/100, self.model.Ymax-1.50*yRange/100*10, "Observed #pm 1 #sigma_{theory}")
        textObs.SetTextFont(42)
        textObs.SetTextSize(0.040)
        textObs.Draw()
        self.c.textObs = textObs

        LExpP = rt.TGraph(2)
        LExpP.SetName("LExpP")
        LExpP.SetTitle("LExpP")
        LExpP.SetLineColor(color(self.EXP['colorLine']))
        LExpP.SetLineStyle(7)
        LExpP.SetLineWidth(2)  
        if 'plus2' not in self.EXP:        
            LExpP.SetPoint(0,self.model.Xmin+3*xRange/100, self.model.Ymax-1.85*yRange/100*10)
            LExpP.SetPoint(1,self.model.Xmin+10*xRange/100, self.model.Ymax-1.85*yRange/100*10)
        else:
            LExpP.SetPoint(0,self.model.Xmin+3*xRange/100, self.model.Ymax-1.9*yRange/100*10)
            LExpP.SetPoint(1,self.model.Xmin+10*xRange/100, self.model.Ymax-1.9*yRange/100*10)

        LExp = rt.TGraph(2)
        LExp.SetName("LExp")
        LExp.SetTitle("LExp")
        LExp.SetLineColor(color(self.EXP['colorLine']))
        LExp.SetLineStyle(7)
        LExp.SetLineWidth(4)
        LExp.SetPoint(0,self.model.Xmin+3*xRange/100, self.model.Ymax-2.00*yRange/100*10)
        LExp.SetPoint(1,self.model.Xmin+10*xRange/100, self.model.Ymax-2.00*yRange/100*10)
        
        LExpM = rt.TGraph(2)
        LExpM.SetName("LExpM")
        LExpM.SetTitle("LExpM")
        LExpM.SetLineColor(color(self.EXP['colorLine']))
        LExpM.SetLineStyle(7)
        LExpM.SetLineWidth(2)  
        if 'plus2' not in self.EXP:        
            LExpM.SetPoint(0,self.model.Xmin+3*xRange/100, self.model.Ymax-2.15*yRange/100*10)
            LExpM.SetPoint(1,self.model.Xmin+10*xRange/100, self.model.Ymax-2.15*yRange/100*10)
        else:
            LExpM.SetPoint(0,self.model.Xmin+3*xRange/100, self.model.Ymax-2.1*yRange/100*10)
            LExpM.SetPoint(1,self.model.Xmin+10*xRange/100, self.model.Ymax-2.1*yRange/100*10)

        LExp2P = rt.TGraph(2)
        LExp2P.SetName("LExp2P")
        LExp2P.SetTitle("LExp2P")
        LExp2P.SetLineColor(color(self.EXP['colorLine']))
        LExp2P.SetLineStyle(3)
        LExp2P.SetLineWidth(2)  
        LExp2P.SetPoint(0,self.model.Xmin+3*xRange/100, self.model.Ymax-1.8*yRange/100*10)
        LExp2P.SetPoint(1,self.model.Xmin+10*xRange/100, self.model.Ymax-1.8*yRange/100*10)

        LExp2M = rt.TGraph(2)
        LExp2M.SetName("LExp2M")
        LExp2M.SetTitle("LExp2M")
        LExp2M.SetLineColor(color(self.EXP['colorLine']))
        LExp2M.SetLineStyle(3)
        LExp2M.SetLineWidth(2)  
        LExp2M.SetPoint(0,self.model.Xmin+3*xRange/100, self.model.Ymax-2.2*yRange/100*10)
        LExp2M.SetPoint(1,self.model.Xmin+10*xRange/100, self.model.Ymax-2.2*yRange/100*10)

        if 'plus2' not in self.EXP:
            textExp = rt.TLatex(self.model.Xmin+11*xRange/100, self.model.Ymax-2.15*yRange/100*10, "Expected #pm 1 #sigma_{experiment}")
        else:
            textExp = rt.TLatex(self.model.Xmin+11*xRange/100, self.model.Ymax-2.15*yRange/100*10, "Expected #pm 1, 2 #sigma_{experiment}")
        textExp.SetTextFont(42)
        textExp.SetTextSize(0.040)
        textExp.Draw()
        self.c.textExp = textExp

        LObs.Draw("LSAME")
        LObsM.Draw("LSAME")
        LObsP.Draw("LSAME")
        LExp.Draw("LSAME")
        LExpM.Draw("LSAME")
        LExpP.Draw("LSAME")
        if 'plus2' in self.EXP:
            LExp2M.Draw("LSAME")
            LExp2P.Draw("LSAME")
        
        self.c.LObs = LObs
        self.c.LObsM = LObsM
        self.c.LObsP = LObsP
        self.c.LExp = LExp
        self.c.LExpM = LExpM
        self.c.LExpP = LExpP
        if 'plus2' in self.EXP:
            LExp2M.c = LExp2M
            LExp2P.c = LExp2P

    def DrawMtopDiagonal(self, transparency=1):
        diagX = array('f',[self.model.mT+self.model.dM,self.model.mT+self.model.dM+5000,self.model.mT-self.model.dM+5000,self.model.mT-self.model.dM])
        diagY = array('f',[0,5000,5000,0])
        gdiagonal = rt.TGraph(4, diagX, diagY)
        gdiagonal.SetName("MtopDiagonal")
        #gdiagonal.SetFillColor(rt.kWhite)
        gdiagonal.SetFillColorAlpha(rt.kWhite, transparency)
        #gdiagonal.SetFillColorAlpha(18, 0.7)
        #gdiagonal.SetFillColor(18)
        ldiagonal = rt.TLine(self.model.mT,0,self.model.mT+self.model.Ymax,self.model.Ymax)
        ldiagonal.SetLineColor(rt.kGray)
        ldiagonal.SetLineStyle(2)
        #tdiagonal = rt.TLatex(200, 200-self.model.mT,"m_{#tilde{t}} = m_{t} + m_{#tilde{#chi}_{1}^{0}}")
        tdiagonal = rt.TLatex(450, 450-self.model.mT,"m_{#tilde{t}} = m_{t} + m_{#tilde{#chi}_{1}^{0}}")
        tdiagonal.SetTextAngle(math.degrees(math.atan(float(self.model.Xmax)/float(self.model.Ymax))))
        tdiagonal.SetTextColor(rt.kGray+2)
        tdiagonal.SetTextAlign(11)
        tdiagonal.SetTextSize(0.025)
        gdiagonal.Draw("FSAME")
        ldiagonal.Draw("LSAME")
        tdiagonal.Draw("SAME")
        self.c.mtopgdiagonal = gdiagonal
        self.c.mtopldiagonal = ldiagonal
        self.c.mtoptdiagonal = tdiagonal
 
    def DrawSmallMtopDiagonal(self, transparency=1):
        diagX = array('f',[self.model.mT+self.model.dM,self.model.mT+self.model.dM+87.5,self.model.mT-self.model.dM+87.5+25.0,self.model.mT-self.model.dM])
        diagY = array('f',[0,87.5,87.5+25.0,0])
        gdiagonal = rt.TGraph(4, diagX, diagY)
        gdiagonal.SetName("MtopDiagonal")
        #gdiagonal.SetFillColor(rt.kWhite)
        gdiagonal.SetFillColorAlpha(rt.kWhite, transparency)
        #gdiagonal.SetFillColorAlpha(18, 0.7)
        #gdiagonal.SetFillColor(18)
        ldiagonal = rt.TLine(self.model.mT,0,self.model.mT+self.model.Ymax,self.model.Ymax)
        ldiagonal.SetLineColor(rt.kGray)
        ldiagonal.SetLineStyle(2)
        #tdiagonal = rt.TLatex(200, 200-self.model.mT,"m_{#tilde{t}} = m_{t} + m_{#tilde{#chi}_{1}^{0}}")
        tdiagonal = rt.TLatex(450, 450-self.model.mT,"m_{#tilde{t}} = m_{t} + m_{#tilde{#chi}_{1}^{0}}")
        tdiagonal.SetTextAngle(math.degrees(math.atan(float(self.model.Xmax)/float(self.model.Ymax))))
#        tdiagonal.SetTextColor(rt.kGray+2)
        tdiagonal.SetTextColor(rt.kGray+3)
        tdiagonal.SetTextAlign(11)
        tdiagonal.SetTextSize(0.025)
        gdiagonal.Draw("FSAME")
        ldiagonal.Draw("LSAME")
        tdiagonal.Draw("SAME")
        self.c.mtopgdiagonal = gdiagonal
        self.c.mtopldiagonal = ldiagonal
        self.c.mtoptdiagonal = tdiagonal
 
    def DrawT2ccDiagonal(self, transparency=1):
        diagonal = rt.TLine(self.model.Xmin, self.model.Xmin, self.model.Xmax, self.model.Xmax)
        diagonal.SetLineColor(rt.kGray)
        diagonal.SetLineStyle(2)
        tdiagonal = rt.TLatex(450, 450+10,"m_{#tilde{t}} = m_{#tilde{#chi}_{1}^{0}}")
        tdiagonal.SetTextAngle(math.degrees(math.atan(float(self.model.Xmax)/float(self.model.Ymax))))
        tdiagonal.SetTextColor(rt.kGray+2)
        tdiagonal.SetTextAlign(11)
        tdiagonal.SetTextSize(0.025)
        diagonal.Draw("LSAME")
        tdiagonal.Draw("SAME")
        mW = 80
        diagonalW = rt.TLine(self.model.Xmin, self.model.Xmin-mW, self.model.Xmax, self.model.Xmax-mW)
        diagonalW.SetLineColor(rt.kGray)
        diagonalW.SetLineStyle(2)
        tdiagonalW = rt.TLatex(450, 450-mW-10,"m_{#tilde{t}} = m_{W} + m_{#tilde{#chi}_{1}^{0}}")
        tdiagonalW.SetTextAngle(math.degrees(math.atan(float(self.model.Xmax)/float(self.model.Ymax))))
        tdiagonalW.SetTextColor(rt.kGray+2)
        tdiagonalW.SetTextAlign(13)
        tdiagonalW.SetTextSize(0.025)
        diagonalW.Draw("LSAME")
        tdiagonalW.Draw("SAME")
        self.c.diagonal   = diagonal
        self.c.diagonalW  = diagonalW
        self.c.tdiagonal  = tdiagonal
        self.c.tdiagonalW = tdiagonalW
        


    def DrawDiagonal(self):
        diagonal = rt.TGraph(3, self.model.diagX, self.model.diagY)
        diagonal.SetName("diagonal")
        diagonal.SetFillColor(rt.kWhite)
        diagonal.SetLineColor(rt.kGray)
        diagonal.SetLineStyle(2)
        diagonal.Draw("FSAME")
        #diagonal.Draw("LSAME")
        self.c.diagonal = diagonal
        
    def DrawLines(self):
        # observed
        self.OBS['nominal'].SetLineColor(color(self.OBS['colorLine']))
        self.OBS['nominal'].SetLineStyle(1)
        self.OBS['nominal'].SetLineWidth(4)
        # observed + 1sigma
        self.OBS['plus'].SetLineColor(color(self.OBS['colorLine']))
        self.OBS['plus'].SetLineStyle(1)
        self.OBS['plus'].SetLineWidth(2)        
        # observed - 1sigma
        self.OBS['minus'].SetLineColor(color(self.OBS['colorLine']))
        self.OBS['minus'].SetLineStyle(1)
        self.OBS['minus'].SetLineWidth(2)        
        # expected + 1sigma
        self.EXP['plus'].SetLineColor(color(self.EXP['colorLine']))
        self.EXP['plus'].SetLineStyle(7)
        self.EXP['plus'].SetLineWidth(2)                
        # expected
        self.EXP['nominal'].SetLineColor(color(self.EXP['colorLine']))
        self.EXP['nominal'].SetLineStyle(7)
        self.EXP['nominal'].SetLineWidth(4)        
        # expected - 1sigma
        self.EXP['minus'].SetLineColor(color(self.EXP['colorLine']))
        self.EXP['minus'].SetLineStyle(7)
        self.EXP['minus'].SetLineWidth(2)                        
        # expected + 2sigma
        if 'plus2' in self.EXP: self.EXP['plus2'].SetLineColor(color(self.EXP['colorLine']))
        if 'plus2' in self.EXP: self.EXP['plus2'].SetLineStyle(3)
        if 'plus2' in self.EXP: self.EXP['plus2'].SetLineWidth(2)                
        # expected - 2sigma
        if 'minus2' in self.EXP: self.EXP['minus2'].SetLineColor(color(self.EXP['colorLine']))
        if 'minus2' in self.EXP: self.EXP['minus2'].SetLineStyle(3)
        if 'minus2' in self.EXP: self.EXP['minus2'].SetLineWidth(2)                        
        # DRAW LINES
        self.EXP['nominal'].Draw("LSAME")
        self.EXP['plus'].Draw("LSAME")
        self.EXP['minus'].Draw("LSAME")
        self.OBS['nominal'].Draw("LSAME")
        self.OBS['plus'].Draw("LSAME")
        self.OBS['minus'].Draw("LSAME")        
        if 'plus2'  in self.EXP: self.EXP['plus2' ].Draw("LSAME")
        if 'minus2' in self.EXP: self.EXP['minus2'].Draw("LSAME")

    def DrawLines2(self):
        # observed
        self.OBS2['nominal'].SetLineColor(color(self.OBS2['colorLine']))
        self.OBS2['nominal'].SetLineStyle(1)
        self.OBS2['nominal'].SetLineWidth(4)
        # observed + 1sigma
        self.OBS2['plus'].SetLineColor(color(self.OBS2['colorLine']))
        self.OBS2['plus'].SetLineStyle(1)
        self.OBS2['plus'].SetLineWidth(2)        
        # observed - 1sigma
        self.OBS2['minus'].SetLineColor(color(self.OBS2['colorLine']))
        self.OBS2['minus'].SetLineStyle(1)
        self.OBS2['minus'].SetLineWidth(2)        
        # expected + 1sigma
        self.EXP2['plus'].SetLineColor(color(self.EXP2['colorLine']))
        self.EXP2['plus'].SetLineStyle(7)
        self.EXP2['plus'].SetLineWidth(2)                
        # expected
        self.EXP2['nominal'].SetLineColor(color(self.EXP2['colorLine']))
        self.EXP2['nominal'].SetLineStyle(7)
        self.EXP2['nominal'].SetLineWidth(4)        
        # expected - 1sigma
        self.EXP2['minus'].SetLineColor(color(self.EXP2['colorLine']))
        self.EXP2['minus'].SetLineStyle(7)
        self.EXP2['minus'].SetLineWidth(2)                        
        # expected + 2sigma
        if 'plus2' in self.EXP2: self.EXP2['plus2'].SetLineColor(color(self.EXP2['colorLine']))
        if 'plus2' in self.EXP2: self.EXP2['plus2'].SetLineStyle(3)
        if 'plus2' in self.EXP2: self.EXP2['plus2'].SetLineWidth(2)                
        # expected - 2sigma
        if 'minus2' in self.EXP2: self.EXP2['minus2'].SetLineColor(color(self.EXP2['colorLine']))
        if 'minus2' in self.EXP2: self.EXP2['minus2'].SetLineStyle(3)
        if 'minus2' in self.EXP2: self.EXP2['minus2'].SetLineWidth(2)                        
        # DRAW LINES
        self.EXP2['nominal'].Draw("LSAME")
        self.EXP2['plus'].Draw("LSAME")
        self.EXP2['minus'].Draw("LSAME")
        self.OBS2['nominal'].Draw("LSAME")
        self.OBS2['plus'].Draw("LSAME")
        self.OBS2['minus'].Draw("LSAME")        
        if 'plus2'  in self.EXP2: self.EXP2['plus2' ].Draw("LSAME")
        if 'minus2' in self.EXP2: self.EXP2['minus2'].Draw("LSAME")
        
