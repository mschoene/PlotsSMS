import ROOT as rt
from array import *
from sms import *
from smsPlotABS import *

# class producing the 2D plot with xsec colors
class smsPlotXSEC(smsPlotABS):

    def __init__(self, modelname, histo, obsLimits, expLimits, histo2, obsLimits2, expLimits2, energy, lumi, preliminary, label):
        self.standardDef(modelname, histo, obsLimits, expLimits, obsLimits2, expLimits2, energy, lumi, preliminary)
        self.LABEL = label
        # canvas for the plot
        self.c = rt.TCanvas("cCONT_%s" %label,"cCONT_%s" %label,600,600)
        self.histo  = histo ['histogram']
        self.histo2 = histo2
        # canvas style
        self.setStyle()
        self.setStyleCOLZ()

    # define the plot canvas
    def setStyleCOLZ(self):        
        # set z axis
        self.histo.GetZaxis().SetLabelFont(42)
        self.histo.GetZaxis().SetTitleFont(42)
        self.histo.GetZaxis().SetLabelSize(0.035)
        self.histo.GetZaxis().SetTitleSize(0.035)
        self.histo.SetMinimum(self.model.Zmin)
        self.histo.SetMaximum(self.model.Zmax)

        # define the palette for z axis
        NRGBs = 5
        NCont = 255
        stops = array("d",[0.00, 0.34, 0.61, 0.84, 1.00])
        red= array("d",[0.50, 0.50, 1.00, 1.00, 1.00])
        green = array("d",[ 0.50, 1.00, 1.00, 0.60, 0.50])
        blue = array("d",[1.00, 1.00, 0.50, 0.40, 0.50])
        rt.TColor.CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont)
        rt.gStyle.SetNumberContours(NCont)
        
        self.c.cd()
        self.histo.Draw("colz")
        
        rt.gPad.Update()
        palette = self.histo.GetListOfFunctions().FindObject("palette")
        palette.SetX1NDC(1.-0.18)
        palette.SetY1NDC(0.14)
        palette.SetX2NDC(1.-0.13)
        palette.SetY2NDC(1.-0.08)
        palette.SetLabelFont(42)
        palette.SetLabelSize(0.035)

    def DrawPaletteLabel(self):
        textCOLZ = rt.TLatex(0.98,0.15,"95% CL upper limit on cross section [pb]")
        textCOLZ.SetNDC()
        #textCOLZ.SetTextAlign(13)
        textCOLZ.SetTextFont(42)
        textCOLZ.SetTextSize(0.045)
        textCOLZ.SetTextAngle(90)
        textCOLZ.Draw()
        self.c.textCOLZ = textCOLZ
            
    def Draw(self):
        self.emptyHisto.GetXaxis().SetRangeUser(self.model.Xmin, self.model.Xmax)
        self.emptyHisto.GetYaxis().SetRangeUser(self.model.Ymin, self.model.Ymax)
        self.emptyHisto.Draw()
        self.histo.Draw("COLZSAME")
        #if self.model.mTopDiagOn:
        #    self.DrawMtopDiagonal(1)
        self.DrawLines()
        if self.histo2:
            #gg = self.OBS2['nominal'].Clone("gg")
            gg = rt.TGraph(3, array('d',[100,self.model.Ymax+80]), array('d',[20,self.model.Ymax]))
            gg.SetName("gg")
            gg.SetFillColor(rt.kWhite)
            gg.Draw("FSAME")
            self.gg = gg
            self.histo2['histogram'].SetMinimum(self.model.Zmin)
            self.histo2['histogram'].SetMaximum(self.model.Zmax)
            self.histo2['histogram'].Draw("COLSAME")
        if self.OBS2:
            self.DrawLines2()
        if self.model.diagOn:
            self.DrawDiagonal()
        if self.model.mTopDiagOn:
            self.DrawMtopDiagonal(1)
            #gdiagonal = self.c.mtopgdiagonal.Clone("MtopDiagonalClone")
            #gdiagonal.SetFillColorAlpha(rt.kWhite, 0.6)
            #ldiagonal = self.c.mtopldiagonal
            #tdiagonal = self.c.mtoptdiagonal
            #gdiagonal.Draw("FSAME")
            #ldiagonal.Draw("LSAME")
            #tdiagonal.Draw("SAME")
            #self.c.mtopgdiagonal2 = gdiagonal
        if self.model.t2ccDiagOn:
            self.DrawT2ccDiagonal()
        self.DrawText()
        self.DrawLegend()
        self.DrawPaletteLabel()
        
