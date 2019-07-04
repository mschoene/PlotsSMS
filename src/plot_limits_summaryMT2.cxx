//// plot_limits_summary: Plots various limit curves on same canvas

// System includes
#include <fstream>
#include <iostream>

// ROOT includes
#include "TStyle.h"
#include "TLatex.h"
#include "TLegend.h"
#include "TH1D.h"
#include "TROOT.h"
#include "TPad.h"
#include "TError.h" // Controls error level reporting

// User includes
#include "plot_limits_summary.hpp"

using namespace std;
namespace{
  double cmsH = 0.075;
  float legLineH = 0.05;
  float legTextSize = 0.035;
  float fillTransparency = 0.08;

  //int c8TeV(kGray+2);
  int cQuark(kBlue), cTop(kMagenta+1), cBottom(kGreen+1);//, cQuark2(kAzure+10);
  //int cSus15004_1l(kBlack), cSus15007(kCyan+2), cSus15008(kOrange);
}

int main(){
  gErrorIgnoreLevel=kWarning; // Turns off ROOT INFO messages

  // Label definitions
  TString lsp("#tilde{#chi}#lower[0.2]{#scale[0.85]{^{0}}}#kern[-1.3]{#scale[0.85]{_{1}}}");
  TString pp_gluglu("pp #rightarrow #tilde{g}#kern[0.3]{#tilde{g}}");
  //TString pp_sqsq("pp #rightarrow #tilde{q}#kern[0.3]{#tilde{q}}");
  TString pp_sqsq("pp #rightarrow #tilde{q}#kern[0.3]{#bar{#tilde{q}}}");
  TString t2(pp_sqsq+", #tilde{q} #rightarrow q#kern[0.4]{"+lsp+"}");
  TString basetitle(pp_gluglu+",  #tilde{g} #rightarrow ");
  TString t1tttt("#tilde{g} #rightarrow t#kern[0.4]{#bar{t}}#kern[0.4]{"+lsp+"}");
  TString t1bbbb("#tilde{g} #rightarrow b#kern[0.4]{#bar{b}}#kern[0.4]{"+lsp+"}");
  TString t1qqqq("#tilde{g} #rightarrow q#kern[0.4]{#bar{q}}#kern[0.4]{"+lsp+"}");
  TString t2qq_8fold("#tilde{q} = #tilde{q}_{L}+#tilde{q}_{R} (#tilde{u}, #tilde{d}, #tilde{s}, #tilde{c})");
  TString t2qq_1fold("#tilde{q} = one light #tilde{q}");
  TString t2bb      ("#tilde{q} = #tilde{b}");
  //TString t2tt      ("#tilde{q} = #tilde{t} (#rightarrow t#kern[0.4]{"+lsp+"}#kern[0.4]{)}");
  TString t2tt      ("#tilde{q} = #tilde{t}");
  //TString t2qq_8fold("T2qq 8-fold");
  //TString t2qq_1fold("T2qq 1-fold");
  //TString t2bb      ("T2bb");
  TString mj("M#lower[-.1]{_{J}}");
  TString mt2("M#lower[-.1]{_{T2}}"), mht("#slash{H}#lower[-.1]{_{T}}"), aT("#alpha#lower[-.1]{_{T}}");

  // Folder with root files containing the TGraphs
  //  TString folder("config/SUS15003/limits_final/");
  TString folder("config/SUS16015/limits_July24/");
  vector<model_limits> models;

  ///////////////////////////////    Defining T1 plot    /////////////////////////////////
  models.push_back(model_limits("T1", pp_gluglu));
  models.back().add(t1qqqq, folder+"limits_T1qqqq_full_July24.root", 
  		    cQuark, "gr_obs_smoothed", "gr_exp_smoothed");
  models.back().add(t1bbbb, folder+"limits_T1bbbb_full_July24.root", 
  		    cBottom, "gr_obs_smoothed", "gr_exp_smoothed");
  models.back().add(t1tttt, folder+"limits_T1tttt_full_July24.root", 
  		    cTop, "gr_obs_smoothed", "gr_exp_smoothed");
  ///////////////////////////////    Defining T2 plot    /////////////////////////////////
  models.push_back(model_limits("T2", t2));
//  models.back().add(t2qq_8fold, folder+"limits_T2qq_full_01Feb_extrapolated.root", 
//  		    cQuark, "gr_obs_smoothed;2", "gr_exp_smoothed;2");
//  models.back().add(t2qq_1fold, folder+"limits_T2qq_full_01Feb-OneFold_extrapolated.root", 
//  		    cQuark2, "gr_obs_smoothed;2", "gr_exp_smoothed;2");
  models.back().add(t2bb      , folder+"limits_T2bb_full_July24.root", 
  		    cBottom, "gr_obs_smoothed", "gr_exp_smoothed");
  models.back().add(t2tt      , folder+"limits_T2tt_full_July24.root ",
  		    cTop, "gr_obs_smoothed", "gr_exp_smoothed");

  ////// 2015
//  ///////////////////////////////    Defining T1 plot    /////////////////////////////////
//  models.push_back(model_limits("T1", pp_gluglu));
//  models.back().add(t1qqqq, folder+"limits_T1qqqq_full_25Jan.root", 
//  		    cQuark, "gr_obs_smoothed", "gr_exp_smoothed");
//  models.back().add(t1bbbb, folder+"limits_T1bbbb_full_25Jan.root", 
//  		    cBottom, "gr_obs_smoothed", "gr_exp_smoothed");
//  models.back().add(t1tttt, folder+"limits_T1tttt_full_25Jan.root", 
//  		    cTop, "gr_obs_smoothed", "gr_exp_smoothed");
//  ///////////////////////////////    Defining T2 plot    /////////////////////////////////
//  models.push_back(model_limits("T2", t2));
//  models.back().add(t2qq_8fold, folder+"limits_T2qq_full_01Feb_extrapolated.root", 
//  		    cQuark, "gr_obs_smoothed;2", "gr_exp_smoothed;2");
//  models.back().add(t2qq_1fold, folder+"limits_T2qq_full_01Feb-OneFold_extrapolated.root", 
//  		    cQuark2, "gr_obs_smoothed;2", "gr_exp_smoothed;2");
//  models.back().add(t2bb      , folder+"limits_T2bb_full_28Janv2_dM25removed_extrapolated.root", 
//  		    cBottom, "gr_obs_smoothed;2", "gr_exp_smoothed;2");
//  models.back().add(t2tt      , "config/SUS15003/limits_corridor/limits_t2tt_fastsim-genSyst.root ",//limits_T2tt_full_28Janv2_noDivideDiagonal.root", 
//  		    cTop, "gr_obs_smoothed;1", "gr_exp_smoothed;1");
  ///////////////////////////////    Defining T1tttt plot    /////////////////////////////////
  // models.back().add("SUS-15-003, 0-lep ("+mt2+"), 2.2 fb^{-1} (13 TeV)", folder+"t1tttt_sus15_003.root", 
  // 		    cSus15003, "gr_obs_smoothed", "gr_exp_smoothed");
  // models.back().add("SUS-15-004, 0-lep (Razor), 2.1 fb^{-1} (13 TeV)", folder+"t1tbqq_sus15_004.root", 
  // 		    cSus15004, "Obs_T1tttt_MultiJet", "Exp_T1tttt_MultiJet");
  // models.back().add("SUS-15-004, 1-lep (Razor), 2.1 fb^{-1} (13 TeV)", folder+"t1tbqq_sus15_004.root", 
  // 		    cSus15004_1l, "Obs_T1tttt_MuMultiJet_EleMultiJet", "Exp_T1tttt_MuMultiJet_EleMultiJet");
  // models.back().add("SUS-15-007, 1-lep ("+mj+"), 2.1 fb^{-1} (13 TeV)", folder+"t1tttt_sus15_007.root", 
  // 		    cSus15007, "graph_smoothed_Obs", "graph_smoothed_Exp");
  // models.back().add("SUS-15-008, 2-lep (SS), 2.2 fb^{-1} (13 TeV)", folder+"t1tttt_sus15_008.root", 
  // 		    cSus15008, "ssobs", "ssexp");
  // models.back().add("SUS-14-010, 0+1+2+#geq3-lep, 19.5 fb^{-1} (8 TeV)", folder+"t1tttt_sus14_010.root", 
  // 		    c8TeV, "T1tttt_SUS14010", "noplot");

  // ///////////////////////////////    Defining T1bbbb plot    /////////////////////////////////
  // models.push_back(model_limits("T1bbbb", basetitle+"b#kern[0.23]{#bar{b}}#kern[0.2]{"+lsp+"}"));
  // models.back().add("SUS-15-002 ("+mht+"), 2.2 fb^{-1} (13 TeV)", folder+"t1bbbb_sus15_002.root", 
  // 		    cSus15002, "ObsLim", "ExpLim");
  // models.back().add("SUS-15-003 ("+mt2+"), 2.2 fb^{-1} (13 TeV)", folder+"t1bbbb_sus15_003.root", 
  // 		    cSus15003, "gr_obs_smoothed", "gr_exp_smoothed");
  // models.back().add("SUS-15-004 (Razor), 2.1 fb^{-1} (13 TeV)", folder+"t1tbqq_sus15_004.root", 
  // 		    cSus15004, "Obs_T1bbbb_MultiJet", "Exp_T1bbbb_MultiJet");
  // models.back().add("SUS-15-005 ("+aT+"), 2.2 fb^{-1} (13 TeV)", folder+"t1bbbb_sus15_005.root", 
  // 		    cSus15005, "observed", "expected");
  // models.back().add("SUS-14-011 (Razor), 19.3 fb^{-1} (8 TeV)", folder+"t1bbbb_sus14_011.root", 
  // 		    c8TeV, "T1bbbb_SUS14011", "noplot");


  // ///////////////////////////////    Defining T1qqqq plot    /////////////////////////////////
  // models.push_back(model_limits("T1qqqq", basetitle+"q#kern[0.23]{#bar{q}}#kern[0.2]{"+lsp+"}"));
  // models.back().add("SUS-15-002 ("+mht+"), 2.2 fb^{-1} (13 TeV)", folder+"t1qqqq_sus15_002.root", 
  // 		    cSus15002, "ObsLim", "ExpLim");
  // models.back().add("SUS-15-003 ("+mt2+"), 2.2 fb^{-1} (13 TeV)", folder+"t1qqqq_sus15_003.root", 
  // 		    cSus15003, "gr_obs_smoothed", "gr_exp_smoothed");
  // models.back().add("SUS-15-004 (Razor), 2.1 fb^{-1} (13 TeV)", folder+"t1tbqq_sus15_004.root", 
  // 		    cSus15004, "Obs_T1qqqq_MultiJet", "Exp_T1qqqq_MultiJet");
  // models.back().add("SUS-15-005 ("+aT+"), 2.2 fb^{-1} (13 TeV)", folder+"t1qqqq_sus15_005.root", 
  // 		    cSus15005, "observed", "expected");
  // models.back().add("SUS-13-019 ("+mt2+"), 19.5 fb^{-1} (8 TeV)", folder+"t1qqqq_sus13_019.root", 
  // 		    c8TeV, "T1_SUS13019", "noplot");


  //////////////////////////////////////////////////////////////////////////////////////// 
  //////////////////////////////////    Making plots    //////////////////////////////////
  //////////////////////////////////////////////////////////////////////////////////////// 
  
  // Creating canvas
  gStyle->SetOptStat(0);  
  float lMargin(0.14), tMargin(0.08), rMargin(0.02), bMargin(0.14);
  TCanvas can("canvas","", 600, 600);
  setCanvas(can, lMargin, tMargin, rMargin, bMargin);

  // Creating base legend for observed/expected
  int wobs(4), wexp(2);
  TH1D hobs("hobs","",1,0,1), hexp("hexp","",1,0,1);
  hobs.SetLineColor(1); hobs.SetLineWidth(wobs);
  hexp.SetLineColor(1); hexp.SetLineStyle(2); hexp.SetLineWidth(wexp);
  double legX(lMargin+0.23+0.19), legY(1-tMargin-0.065);
  //double legX(1-rMargin-0.04), legY(1-tMargin-0.03);
  double legW = 0.2, legH = 0.07;
  TLegend baseleg(legX-legW, legY-legH, legX, legY);
  baseleg.SetTextSize(0.034); baseleg.SetFillColor(0); 
  baseleg.SetFillStyle(0); baseleg.SetBorderSize(0);
  //baseleg.AddEntry(&hobs, "Observed");
  baseleg.AddEntry(&hexp, "Expected");
  legX = lMargin+0.23;
  TLegend obsleg(legX-legW, legY-legH, legX, legY);
  obsleg.SetTextSize(0.034); obsleg.SetFillColor(0); 
  obsleg.SetFillStyle(0); obsleg.SetBorderSize(0);
  obsleg.AddEntry(&hobs, "Observed");

  // Looping over each model
  cout<<endl;
  for(size_t imodel(0); imodel < models.size(); imodel++){
    model_limits mod(models[imodel]);

    // Creating base histogram and drawing lumi labels
    float Xmin(700), Xmax(2000), Ymin(0), Ymax(1900), glu_lsp;
    TString Xtitle("");
    getModelParams(mod.model, Xmin, Xmax, Ymin, Ymax, Xtitle, glu_lsp);

    TH2D hbase = baseHistogram(Xmin, Xmax, Ymin, Ymax, Xtitle);
    hbase.Draw();
    addLabelsTitle(lMargin, tMargin, rMargin, mod.title);

    // Plotting limits
    size_t ncurves(mod.files.size());
    vector<TGraph*> obs(ncurves, 0), exp(ncurves, 0);
    // Getting all graphs first because the ones that come from TCanvas mess up the colors
    for(size_t file(0); file < ncurves; file++){
      TFile flimit(mod.files[file]);
      exp[file] = getGraph(flimit, mod.expnames[file]);
      obs[file] = getGraph(flimit, mod.obsnames[file]);
    }
    for(size_t file(0); file < ncurves; file++){
      setGraphStyle(exp[file], mod.colors[file], 2, wexp, glu_lsp);
      setGraphStyle(obs[file], mod.colors[file], 1, wobs, glu_lsp);
      obs[file]->Draw("f same");

      TString obsname("obs"); obsname += imodel; obsname += file;
      obs[file]->SetName(obsname);
    } // Loop over curves in each model
    // Plotting the lines on top of the fills
    for(size_t file(0); file < ncurves; file++){
      if(exp[file]) exp[file]->Draw("same");
      obs[file]->Draw("same");
    }// Loop over curves in each model

    // Drawing legends
    baseleg.Draw();
    obsleg.Draw();
    legX = lMargin+0.03; legY = 1-tMargin-cmsH-0.05;
    legW = 0.2; 
    legH = legLineH * ncurves;
    TLegend limleg(legX, legY-legH, legX+legW, legY);
    limleg.SetTextSize(legTextSize); limleg.SetFillColor(0); 
    limleg.SetFillStyle(0); limleg.SetBorderSize(0);
    for(size_t file(0); file < ncurves; file++)
      limleg.AddEntry(obs[file]->GetName(), mod.labels[file], "fl");
    limleg.Draw();

    TString plotname(mod.model+"_limits_summary_mt2.pdf");
    can.SaveAs(plotname);
    cout<<" open "<<plotname<<endl;
  } // Loop over models
  cout<<endl<<endl;
}


TGraph* getGraph(TFile &flimit, TString gname){
  TGraph *graph = static_cast<TGraph*>(flimit.Get(gname));
  // If the TGraph is not directly provided in the root file, try to extract it from a TCanvas
  if(graph==0) {
    TPad *current_pad = static_cast<TPad*>(gPad);
    TCanvas *c1 = static_cast<TCanvas*>(flimit.Get("c1"));
    current_pad->cd();
    if(c1==0) return 0;
    graph = static_cast<TGraph*>(c1->GetListOfPrimitives()->FindObject(gname));
    if(graph==0) return 0;
  }
  return graph;
}

void setGraphStyle(TGraph* graph, int color, int style, int width, double glu_lsp){
  if(graph==0) return;

  // Setting graph style
  graph->SetLineColor(color);
  graph->SetLineStyle(style);
  int fillcolor(color);
  graph->SetFillColor(fillcolor);
  graph->SetFillColorAlpha(fillcolor, fillTransparency);
  graph->SetFillStyle(1001);
  graph->SetLineWidth(width); 

  int np(graph->GetN());
  double mglu, iniglu, endglu, mlsp;
  graph->GetPoint(0, iniglu, mlsp);
  graph->GetPoint(np-1, endglu, mlsp);
  // // Reversing graph if printed towards decreasing mgluino
  // if(iniglu > endglu) reverseGraph(graph);
  // // Adding a point so that it goes down to mLSP = 0
  // graph->SetPoint(graph->GetN(), max(iniglu,endglu), 0);
  // np++;

  // reverseGraph(graph);

  // Adding a point at LSP = 0, and removing points beyond the diagonal
  for(int point(0); point < np; point++){
    graph->GetPoint(point, mglu, mlsp);
    if(mlsp > mglu-glu_lsp){
      while(point <= graph->GetN()) 
	graph->RemovePoint(graph->GetN()-1);
      break;
    }
  }
  // // Finding intersection of line between last 2 points and mlsp = mglu - glu_lsp
  // double x1, y1, x2, y2;
  // graph->GetPoint(np-1, x1, y1);
  // graph->GetPoint(np-2, x2, y2);
  // double slope((y1-y2)/(x1-x2)), offset(y1-slope*x1);
  // double intersection((offset+glu_lsp)/(1-slope));

  // // Adding extrapolation into the diagonal, and point for mglu = 0
  // if(slope!=1) graph->SetPoint(graph->GetN(), intersection, intersection-glu_lsp);
  graph->SetPoint(graph->GetN(), 0, -glu_lsp);
  // cout<<slope<<" " <<intersection<<endl;
  // if(x1 == x2 || y1 == y2 || slope == 1){
  //   for(int point(0); point < graph->GetN(); point++){
  //     graph->GetPoint(point, mglu, mlsp);
  //     cout<<point<<": "<<mglu<<", "<<mlsp<<endl;
  //   }
  // }
  // //graph->Print();
}

void reverseGraph(TGraph *graph){
  int np(graph->GetN());
  double mglu, mlsp;
  vector<double> mglus, mlsps;
  for(int point(np-1); point >= 0; point--){
    graph->GetPoint(point, mglu, mlsp);
    mglus.push_back(mglu);
    mlsps.push_back(mlsp);
  }
  for(int point(0); point < np; point++)
    graph->SetPoint(point, mglus[point], mlsps[point]);
}

void getModelParams(TString model, float &Xmin, float &Xmax, float &Ymin, float &Ymax, TString &Xtitle, float &glu_lsp){
  TString mglu("m_{#kern[0.15]{#tilde{g}}} [GeV]");
  //TString msq("m_{#tilde{q}} [GeV]");
  TString msq("m_{#kern[0.15]{#tilde{q}}} [GeV]");
  Xtitle = mglu;
  if(model == "T1"){
    Xmin = 600; Xmax = 2100;
    Ymin = 0;   Ymax = 1885;
    glu_lsp = 0;
  }
  if(model == "T2"){
    Xmin = 100; Xmax = 1350;
    Ymin = 0;   Ymax = 1000;
    glu_lsp = 0;
    Xtitle = msq;
  }
  if(model == "T1tttt"){
    Xmin = 600; Xmax = 1950;
    Ymin = 0;   Ymax = 1885;
    glu_lsp = 225;
  }
  if(model == "T1bbbb"){
    Xmin = 600; Xmax = 1950;
    Ymin = 0;   Ymax = 1885;
    glu_lsp = 25;
  }    
  if(model == "T1qqqq"){
    Xmin = 600; Xmax = 1950;
    Ymin = 0;   Ymax = 1750;
    glu_lsp = 25;
  }    
}


void setCanvas(TCanvas &can, float lMargin, float tMargin, float rMargin, float bMargin){
  can.SetLogz();
  can.SetTickx(1);
  can.SetTicky(1);
  can.SetLeftMargin(lMargin);
  can.SetTopMargin(tMargin);
  can.SetRightMargin(rMargin);
  can.SetBottomMargin(bMargin);
}

void addLabelsTitle(float lMargin, float tMargin, float rMargin, TString title){
  TLatex label; label.SetNDC();  
  // Printing CMS Preliminary
  double offsetx(0.045);
  double ycms(1-tMargin+0.018); //ycms(1-tMargin-cmsH);
  label.SetTextAlign(11); label.SetTextFont(61); label.SetTextSize(0.75*tMargin);
  //label.DrawLatex(lMargin+offsetx, ycms, "CMS");
  label.DrawLatex(lMargin, ycms, "CMS");
  label.SetTextAlign(11); label.SetTextFont(52); label.SetTextSize(0.038);
  ////label.DrawLatex(0.27+offsetx, ycms, "Preliminary");
  label.DrawLatex(0.27, ycms, "Preliminary");
  // Printing process title
  label.SetTextAlign(22); label.SetTextFont(42); label.SetTextSize(0.6*tMargin);
  //label.DrawLatex((1-rMargin-lMargin)/2.+lMargin-0.05, 1-tMargin/2., title);
  label.DrawLatex(0.75, 1-tMargin-0.15, title);
  // Printing luminosity
  label.SetTextAlign(31); label.SetTextFont(42); label.SetTextSize(0.6*tMargin);
  //  label.DrawLatex(1-rMargin-0.02, 1-tMargin+0.018, "2.3 fb^{-1} (13 TeV)");
  label.DrawLatex(1-rMargin-0.02, 1-tMargin+0.018, "12.9 fb^{-1} (13 TeV)");
  //label.DrawLatex(1-rMargin-0.02, 1-tMargin+0.018, "Dec 2015");
  // Printing analysis name
  label.SetTextAlign(11); label.SetTextFont(42); label.SetTextSize(legTextSize);
  //  label.DrawLatex(lMargin+offsetx, 1-tMargin-cmsH+0.01, "SUS-15-003, 0-lep (M#lower[-.1]{_{T2}})");
  label.DrawLatex(lMargin+offsetx, 1-tMargin-cmsH+0.01, "SUS-16-015, 0-lep (M#lower[-.1]{_{T2}})");
}

TH2D baseHistogram(float Xmin, float Xmax, float Ymin, float Ymax, TString Xtitle){
  TH2D hbase("hbase", "", 1, Xmin, Xmax, 1, Ymin, Ymax);
  hbase.GetXaxis()->SetLabelFont(42);
  hbase.GetXaxis()->SetLabelSize(0.035);
  hbase.GetXaxis()->SetTitleFont(42);
  hbase.GetXaxis()->SetTitleSize(0.05);
  hbase.GetXaxis()->SetTitleOffset(1.2);
  hbase.GetXaxis()->SetTitle(Xtitle);
  hbase.GetYaxis()->SetLabelFont(42);
  hbase.GetYaxis()->SetLabelSize(0.035);
  hbase.GetYaxis()->SetTitleFont(42);
  hbase.GetYaxis()->SetTitleSize(0.05);
  hbase.GetYaxis()->SetTitleOffset(1.3);
  hbase.GetYaxis()->SetTitle("m_{#tilde{#chi}_{1}^{0}} [GeV]");
  return hbase;
}

void model_limits::add(TString label, TString file, int color, TString obsname, TString expname){
  labels.push_back(label);
  files.push_back(file);
  obsnames.push_back(obsname);
  expnames.push_back(expname);
  colors.push_back(color);
}

model_limits::model_limits(TString imodel, TString ititle):
  model(imodel),
  title(ititle){
  }
