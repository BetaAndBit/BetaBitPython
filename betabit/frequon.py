# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from string import ascii_lowercase, ascii_uppercase
import os
import hashlib as hs
import re

"""
Module with The Frequon Game.
"""

path = os.path.dirname(os.path.abspath(__file__))
englishLetterFrequency = pd.read_csv(os.path.join(path, "data", "englishLetterFrequency.csv"), index_col=0)
top100commonWords = pd.read_csv(os.path.join(path, "data", "top100commonWords.csv"), index_col=0)
top100commonWords = np.array(top100commonWords.word)
wikiquotes = pd.read_csv(os.path.join(path, "data", "wikiquotes.csv"), index_col=0)
messages = pd.read_csv(os.path.join(path, "data", "messages.csv"), index_col=0)
ginklai = np.array(messages.ginklai)[0]
pcs = np.array(messages.pcs)[0]
roses = np.array(messages.roses)[0]
level = -1

def dcode(text):
    """
    Auxiliary decoding function.
    """
    
    tmp1 = np.array(list(ascii_uppercase) + list(ascii_lowercase))
    text_list = list(text)
    indexes = np.unique(text_list, return_index = True)[1]
    tmp2 = [text_list[index] for index in sorted(indexes)]
    tmp2 = [x for x in tmp2 if x not in tmp1]
    let = np.hstack((tmp1, tmp2))
    let_names = np.hstack(((tmp1[-1::-1]), tmp2))
    text_result = ""
    for i in range(len(text_list)):
        text_result = text_result + let[np.where(let_names == text_list[i])][0]
    return text_result


def frequon(**args):
    """
    The 'frequon' function is used for solving problems in the data-based game "The Frequon Game".
    
    Keyword arguments:
    args -- 'frequon' function is called by different arguments, which vary depending on a problem that Bit is trying to solve. See 'Details' in order to learn more about the list of possible arguments.
    
    Details:
    
    Every time when some additional hints are needed one should add 'hint = True' argument to the 'frequon' function.
    
    In this game you are in contact with a group of people that are going to stop terrorists. You can communicate with them through 'frequon' function.

    In each call add 'subject' parameter that will indicate which message you are answering. Add 'content' parameter. It's value should match the request.
    
    "The Frequon Game" is a free of charge, educational project of the SmarterPoland.pl Foundation.
    """
    
    global level
    
    subjects = {
        "s0": 're: interested?',
        "s1": 're: frequencies',
        "s2": 're: transcription',
        "s3": 're: key',
        "s4": 're: next text',
        "s5": 're: lengths in the text',
        "s6": 're: language in and message',
        "s7": 're: password'
        }
    
    commands = {
        "intro": dcode('bLF\'EV tLG nZRO\n\nuILN: 154VY7278UX44650YWW2YY39YY2Y5X69@NZRO.GLI\ngL: X81632WXV28XZ740U2U2503656U3W62Z@NZRO.GLI\nhFYQVXG: rMGVIVHGVW?\n\nsR,\ndV ZIV OLLPRMT ULI Z HNZIG TFB DRGS VCGIZLIWRMZIB SZXPRMT HPROOH.\nlFI NFGFZO UIRVMW ZHHFIVW FH GSZG BLF ZIV LFI NZM.\n\ngo;wi: dV ZIV LYHVIERMT Z TILFK LU GVIILIRHGH GSZG ZIV KOZMMRMT HLNVGSRMT.\ndV SZEV RMGVIXVKGVW HLNV WZGZ, YFG WL MLG PMLD SLD GL IVZW RG (ZGGZXSVW).\n\ngSVIV RH Z KZHHDLIW HLNVDSVIV. dV SZEV GL URMW RG GL HGLK GVIILIRHGH.\ndLFOW BLF ORPV GL QLRM LFI GVZN? sVOK FH ZMW DV DROO SVOK BLF RM GSV UFGFIV.\n\nrG\'H MLG XOVZI SLD GL HGZIG. lFI RMULINVI GLOW FH GSZG GSV PVB RH HLNVSLD\nIVOZGVW DRGS GSIVV PVB KSIZHVH: \'TFMH\', \'ZMW\', \'ILHVH\'.\nkILYZYOB GSVHV ZIV GSV MZNVH LU HLNV NVHHZTVH / WZGZHVGH.\ndLFOW BLF ORPV GL XSVXP RU BLF SZEV ZXXVHH GL ZMB LU GSVN?\n\nrU BLF DZMG GL SVOK, KOVZHV GBKV:\n\'UIVJFLM(HFYQVXG = "iV: rMGVIVHGVW?", XLMGVMG = "gVCG LU GSV NVHHZTV GSZG BLF SZEV ZXXVHH GL")\'\nHL ZH DV XLFOW IVZW GSV NVHHZTV GLL.\n\niVNVNYVI: ZMB GRNV BLF DZMG, BLF XZM TVG HLNV KRVXV LU ZWERXV, QFHG\nGBKV: \'UIVJFLM(SRMG = gIFV)\'.'),
        "task1": dcode('bLF\'EV tLG nZRO\n\nuILN: 154VY7278UX44650YWW2YY39YY2Y5X69@NZRO.GLI\ngL: X81632WXV28XZ740U2U2503656U3W62Z@NZRO.GLI\nhFYQVXG: uIVJFVMXRVH\n\ndV ZIV HL TOZW BLF DZMG GL SVOK FH!\n\ngSZMP BLF ULI GSV NVHHZTV, RG OLLPH RMGVIVHGRMT... sLDVEVI, GSRH GVCG\nRH GLL OLMT GL YV GSV KZHHDLIW GSZG DV ZIV HVVPRMT ULI. gSRH NFHG YV HLNV XLWVW\nNVHHZTV. rU LMOB DV XLFOW PMLD GSV PVB...\n\nyFG OVG\'H GZPV Z OLLP.\ngSV \'K\' OVGGVI ZKKVZIH EVIB LUGVM.\nzMW \'R\' WLVHM`G. rM VMTORHS OZMTFZTV OVGGVI \'V\' LXXFIVH\nGSV NLHG LUGVM. rU DV PMVD SLD LUGVM VZXS OVGGVI RH FHVW RM\nGSV NVHHZTV, DV XLFOW XLNKZIV GSVN DRGS DVOO-PMLDM vMTORHS\nOVGGVI UIVJFVMXRVH! hL OVG\'H WL GSRH!\n\ngZPV GSV NVHHZTV GSZG BLF SZEV ULFMW, IVNLEV VEVIBGSRMT GSZG RH MLG Z OVGGVI\nZMW XZOXFOZGV UIVJFVMXRVH LU OVGGVIH.\ngSV IVHFOG HSLFOW YV YV Z WRXGRLMZIB DRGS PVBH XLIIVHKLMWRMT GL OVGGVIH ZMW EZOFVH\nXLIIVHKLMWRMT GL MFNYVI LU LXXFIZXVH.\n\nhVMW FH Z IVKOB: \'UIVJFLM(HFYQVXG = "iV: uIVJFVMXRVH", XLMGVMG = "UIVJ")\' ZH HLLM ZH BLF\nURMRHS. \'UIVJ\' RH GSV WRXGRLMZIB LU UIVJFVMXRVH ULI VZXS OVGGVI.\nkOVZHV, IVNVNYVI GL HVG WRXGRLMZIB\'H PVBH DRGS ZKKILKIRZGV OVGGVIH!'),
        "task2": dcode('bLF\'EV tLG nZRO\n\nuILN: 154VY7278UX44650YWW2YY39YY2Y5X69@NZRO.GLI\ngL: X81632WXV28XZ740U2U2503656U3W62Z@NZRO.GLI\nhFYQVXG: gIZMHXIRKGRLM\n\ntIVZG QLY! mLD, DSVM DV WL PMLD DSRXS OVGGVIH ZIV FHVW GSV NLHG LUGVM\nZMW DSRXS ZIV GSV OVZHG XLNNLM, DV XZM XLNYRMV GSVN DRGS DVOO-PMLDM\nVMTORHS UIVJFVMXRVH LU OVGGVIH. dV SZEV KIVKZIVW ZMW ZGGZXSVW\nGSV \'vMTORHSoVGGVIuIVJFVMXB\' WZGZHVG. rG XLMGZRMH\nUIVJFVMXRVH LU OVGGVIH RM GSV vMTORHS OZMTFZTV.\n\nmLD BLF XZM HFYHGRGFGV LOW XRKSVIVW OVGGVIH DRGS GSV MVD\nvMTORHS OVGGVIH.\nhFXS LKVIZGRLM RH XZOOVW XSZIZXGVI GIZMHOZGRLM / GIZMHORGVIZGRLM.\nxZM BLF KZHH GSV GIZMHORGVIZGVW NVHHZTV GL FH?\n\nhVMW FH IVKOB: \'UIVJFLM(HFYQVXG = "iV: gIZMHXIRKGRLM", XLMGVMG = "GVCG_BLF_DROO_TVG")\'.\ndV DRHS BLF OFXP!\n\nyVHG IVTZIWH!'),
        "task3": dcode('bLF\'EV tLG nZRO\n\nuILN: 154VY7278UX44650YWW2YY39YY2Y5X69@NZRO.GLI\ngL: X81632WXV28XZ740U2U2503656U3W62Z@NZRO.GLI\nhFYQVXG: pVB\n\ndVOO WLMV! dV ZIV HL XOLHV MLD! lFI NVHHZTV OLLPH Z ORGGOV YRG UZNRORZI.\ngSVIV ZIV VEVM HLNV DLIWH GSZG DV XZM IVXLTMRAV.\nyFG GSVIV ZIV HGROO HLNV DLIWH GSZG ZIV OLLPRMT HGIZMTV.\nrG NVZMH GSZG LFI PVB RH MLG XLNKOVGVOB XLIIVXG ZMW DV MVVW GL\nXLIIVXG GSVHV OVGGVIH GSZG DVIV NRHGIZMHOZGVW.\n\noVG\'H FHV GSV DLIW UIVJFVMXB GL XLIIVXG GSV GIZMHORGVIZGRLM.\n\noVG\'H XLFMG ZOO GSV DLIWH.\ngSLHV DSRXS ZKKVZI GSV NLHG LUGVM ZIV ULI FH VZHB GL ZNVMW.\ngSV LMVH DSRXS ZKKVZI GSV OVZHG LUGVM ZIV KVISZKH VZHROB IVXLTMRHZYOV MLFMH?\n\ngZPV ZWEZMGZTV LU \'GLK100XLNNLMdLIWH\'.\nuRMW GSV IRTSG GIZMHORGVIZGRLM RM LIWVI GL WVXLWV RG RMGL GSV KILKVI vMTORHS.\ndLIP DRGS OLDVIXZHVW GVCG.\n\ngBKV:\n\'UIVJFLM(HFYQVXG = "iV: pVB", XLMGVMG = {"LOW": "ZYXWVU...A", "MVD": "MVDOVGGVIHIVHKVXGREVOB"})\',\nDSVIV \'LOW\' ZIV GSV OVGGVIH RM GSV XLWV\'H HVMHV ZMW \'MVD\' ZIV URGGVW IVZO OVGGVIH.\n\ntLLW OFXP!'),
        "task4": dcode('bLF\'EV tLG nZRO\n\nuILN: 154VY7278UX44650YWW2YY39YY2Y5X69@NZRO.GLI\ngL: X81632WXV28XZ740U2U2503656U3W62Z@NZRO.GLI\nhFYQVXG: mVCG GVCG\n\nvCXVOOVMG DLIP, BLF SZEV XIZXPVW GSV XLWV!\n\nsLDVEVI, GSVIV RH ML KZHHDLIW RM SVIV.\ngSVIV NFHG YV HLNV XOFV RM GSRH NVHHZTV...\n\nkVISZKH LFI UIRVMW FHVW GSV PVB\nGL XRKSVI GSV MZNVH LU GSV GDL IVNZRMRMT NVHHZTVH?\nxZM BLF SZEV ZXXVHH GL GSVN MLD?\n\ngIZMHORGVIZGV GSVHV MZNVH: \'TFMH\', \'ZMW\', \'ILHVH\' ZMW XSVXP RU GSVIV ZIV WZGZHVGH DRGS GSVHV MVD MZNVH.\n\nkOVZHV, HVMW FH IVKOB:\n\'UIVJFLM(HFYQVXG = "iV: mVCG GVCG", XLMGVMG = "xLMGVMG LU GSV FMOLXPVW NVHHZTV")\'.\n\ndV DLFOW YV TIZGVUFO.'),
        "task5": dcode('bLF\'EV tLG nZRO\n\nuILN: 154VY7278UX44650YWW2YY39YY2Y5X69@NZRO.GLI\ngL: X81632WXV28XZ740U2U2503656U3W62Z@NZRO.GLI\nhFYQVXG: oVMTGSH RM GSV GVCG\n\nlYERLFHOB GSRH NVHHZTV RH ZOHL XRKSVIVW. dV GIRVW GL FHV GSV PVB\nYFG FMULIGFMZGVOB RG GFIMVW LFG GSZG RG DZH DIRGGVM RM Z OZMTFZTV GSZG DV WLM\'G PMLD.\n\nxZM BLF IVXLTMRAV GSV OZMTFZTV?\n\ndV PMLD Z HRNKOV RWVZ SLD GL IVXLTMRAV GSV OZMTFZTV LU ZMB\nXRKSVIVW NVHHZTV. zOO BLF MVVW GL WL RH GL NVZHFIV GSV OVMTGS LU VZXS DLIW. rU DV PMVD\nSLD NZMB DLIWH SZW GSV OVMTGSH LU 1, 2, 3, ZMW HL LM, DV XLFOW XLNKZIV\nGSVN DRGS GSV OVMTGSH LU GSV DLIWH RM OZMTFZTVH GSZG DV PMLD!\n\nmZGFIZOOB, DV MVVW Z SFTV ZNLFMG LU DLIWH RM NZMB OZMTFZTVH.\nuLIGFMZGVOB DV SZEV Z HZNKOV UILN DRPRKVWRZ IVHLFIXVH, HL DV XZM HSZIV RG DRGS BLF.\nkOVZHV, URMW GSV \'DRPRJFLGVH\' ZGGZXSVW.\n\ngSVIV RH Z ORHG LU JFLGVH RM NZMB OZMTFZTVH.\ndV SLKV GSRH DROO YV VMLFTS ULI LFI MVVWH.\n\nmLGV GSZG WRUUVIVMG OZMTFZTVH ZIV FHRMT WRUUVIVMG OVGGVIH, GSFH GL URMW DLIWH FHV GSV HKZXV \' \' ZH Z HVKZIZGLI.\n\ngSRH RH Z GRNV-XLMHFNRMT QLY GL NVZHFIV GSV OVMTGS LU VZXS DLIW ULI ZOO LU GSV OZMTFZTVH, YFG DV YVORVEV GSZG BLF PMLD HLNV UZHG DZB GL XLKV DRGS GSRH KILYOVN.\n\nhVMW FH BLFI IVHFOGH:\n\'UIVJFLM(HFYQVXG = "iV: oVMTGSH RM GSV GVCG", XLMGVMG = "OVMTGSH", ZGGZXSNVMG = "DRPR_OVMTGSH")\'.\n\'OVMTGSH\' RH GSV WRXGRLMZIB LU XLFMGH LU DLIWH LU TREVM OVMTGS (PVBH - OVMTGSH ZMW EZOFVH - XLFMGH).\n\'DRPR_OVMTGSH\' RH GSV WRXGRLMZIB DRGS WRXGRLMZIRVH LU XLFMGH ULI VZXS OZMTFZTV.\nkOVZHV, IVNVNYVI GL MZNV GSRH WRXGRLMZIB DRGS ZKILKIRZGV OZMTFZTVH!'),
        "task6": dcode('bLF\'EV tLG nZRO\n\nuILN: 154VY7278UX44650YWW2YY39YY2Y5X69@NZRO.GLI\ngL: X81632WXV28XZ740U2U2503656U3W62Z@NZRO.GLI\nhFYQVXG: oZMTFZTV RM GSV NVHHZTV\n\ndVOO WLMV!\n\nmLD DV MVVW GL XLNKZIV UIVJFVMXRVH ULI LFI NVHHZTV ZMW UIVJFVMXRVH ULI LGSVI OZMTFZTVH.\ngIB GL KOLG YZIKOLGH ULI VZXS OZMTFZTV ZMW GSVM Z YZIKOLG ULI LFG NVHHZTV.\nrG DROO YV VZHRVI GL XLNKZIV GSVHV UIVJFVMXRVH TIZKSRXZOOB.\n\nmLD DV XZM RMEVHGRTZGV DSZG OZMTFZTV DZH FHVW GL KIVKZIV GSV HVXLMW NVHHZTV.\ndSZG WL BLF GSRMP?\ndSRXS WRHGIRYFGRLM RH GSV NLHG HRNROZI GL GSV WRHGIRYFGRLM LU GSV OVMTGSH RM LFI NVHHZTV?\n\nhVMW FH BLFI GSLFTSGH! gBKV:\n\'UIVJFLM(HFYQVXG = "iV: oZMTFZTV RM ZMW NVHHZTV", XLMGVMG = "oZMTFZTV")\'\nDSVIV \'oZMTFZTV\' RH GSV MZNV LU GSV XLIIVXG OZMTFZTV.'),
        "task7": dcode('bLF\'EV tLG nZRO\n\nuILN: 154VY7278UX44650YWW2YY39YY2Y5X69@NZRO.GLI\ngL: X81632WXV28XZ740U2U2503656U3W62Z@NZRO.GLI\nhFYQVXG: kZHHDLIW\n\ndV GSRMP HL GLL. tIVZG QLY! mLD DV SZEV GSV PVB, DV PMLD GSV OZMTFZTV ...\nkVISZKH YVULIV DV HGZIG GIZMHOZGRMT GSRH NVHHZTV, DV DROO GIB GL TVG ZM ZXXVHH\nGL GSV KSIZHV \'TFMH\'. dV PMLD GSZG LFI UIRVMW ORPVH GL FHV GSV PVB\nUILN LMV KFAAOV RM LIWVI GL VMXLWV GSV MZNV LU GSV LGSVI LMV. hL NZBYV ZOHL GSRH GRNV ...\nwL BLF PMLD DSZG RH GSV oRGSFZMRZM XLFMGVIKZIG LU GSV DLIW \'TFMH\'?\n\ndV ZIV IVHKLMHRYOV ULI GIZMHOZGRMT GSV NVHHZTV. rU BLF URMW HLNVGSRMT RMGVIVHGRMT\nRM GSV GSRIW LU LFI NVHHZTVH, OVG FH PMLD, KOVZHV!\n\ngBKV:\n\'UIVJFLM(HFYQVXG = "iV: kZHHDLIW", XLMGVMG = "GSVkZHHDLIWbLFdROOuRMW")\'.'),
        "outro": dcode('bLF\'EV tLG nZRO\n\nuILN: 154VY7278UX44650YWW2YY39YY2Y5X69@NZRO.GLI\ngL: X81632WXV28XZ740U2U2503656U3W62Z@NZRO.GLI\nhFYQVXG: bLF ZIV GSV YVHG!'),
        "hint0": dcode('xSVXP RU BLF SZEV ZXXVHH GL ZMB WZGZ DRGS MZNV ORPV \'TFMH\', \'ZMW\' LI \'ILHVH\'.\nrU BVH, GSVM HVMW RG GSILFTS GSV \'UIVJFLM()\' UFMXGRLM.'),
        "hint1": dcode('uRIHGOB, GIB GL ZMHDVI GSV ULOOLDRMT JFVHGRLMH:\n  * wLVH kBGSLM GIVZG \'z\' ZMW \'Z\' ZH GSV HZNV OVGGVI?\n  * rH \'DLIW\' ZMW \'DLIW,\' GSV HZNV DLIW ULI kBGSLM?\n\ngSV UFMXGRLMH ORPV: \'OLDVI()/FKKVI()\', \'HFY()\' UILN \'IV\' IVTFOZI VCKIVHHRLM LKVIZGRLMH KZXPZTV NRTSG YV FHVUFO GL SZMWOV GSVHV RHHFVH. xLMHRWVI IVKOZXRMT ZOO MLM-ZOKSZMFNVIRX XSZIZXGVIH DRGS VNKGB HGIRMTH ().\ngSV VZHRVHG DZB GL WVZO DRGS GSRH PRMW LU KILYOVN RH GL FHV IVTVC. hGIRMT: \'[^Z-A ]\' ZOOLDH BLF GL VCGIZXG ZOO MLM-OVGGVI XSZIZGVIH DRGS HKZXVH.\n\nuRMZOOB UZNRORZIRAV BLFIHVOU DRGS \'ORHG()\' ZMW \'EZOFV_XLFMGH()\' UILN \'KZMWZH\' KZXPZTV GL XLFMG ZOO LU GSV OVGGVIH VZHROB.\ngSV \'ZHXRR_OLDVIXZHV\' UILN \'HGIRMT\' KZXPZTV NZB ZOHL YV EVIB SVOKUFO ULI GSV KILYOVN.\n\ngL HVV DSRXS OVGGVIH LXXFIV GSV NLHG UIVJFVMGOB FHV \'HLIG_EZOFVH()\' UILN \'KZMWZH\' KZXPZTV.\n\ngL XIVZGV JFRXPOB Z WRXGRLMRZIB GIB \'ARK()\' UFMXGRLM.'),
        "hint2": dcode('nZMFZO HFYHRGFGRLM NZB YB KIVGGB WVNZMWRMT. gSRH RH DSB BLF NZB ZKKIVXRZGV Z \'GIZMHOZGV()\' UFMXGRLM UILN \'HGIRMT\' KZXPZTV. :)\niVNVNYVI GL XLMEVIG ZOO OVGGVIH GL OLDVIXZHVH.\n'),
        "hint3": '',
        "hint4": dcode('zOO BLF MVVW GL WL RH HKORG GSV DSLOV GVCG YB HKZXVH ZMW GZYOV ZOO XIVZGVW DLIWH. wL BLF IVNVNYVI SLD \'HKORG()\' UFMXGRLM DLIPH?\n\nrU BLF WL GSRH, GIB GL KFG LOW OVGGVIH RM ZOKSZYVGRXZO LIWVI.'),
        "hint5": dcode('iVNVNYVI GSZG RU DV SZEV \'LOW\' ZH XRKSVIVW OVGGVIH ZMW \'MVD\' ZH IVZO LMVH, DV MVVW GL URMW IVZO OVGGVIH RM \'MVD\' ZMW HVVP ULI GSVRI GIZMHOZGRLM RM GSV \'LOW\' XSZIZXGVI HGIRMT.'),
        "hint6": dcode('gSVIV RH Z EVIB FHVUFO UFMXGRLM RM kBGSLM GL NVZHFIV MFNYVI LU XSZIZXGVIH RM DLIWH. gZPV ZWEZMGZTV LU \'OVM()\' UFMXGRLM. iVNVNYVI GL HKORG GSV HGIRMT RMGL HRMTOV DLIWH DRGS \'HKORG()\' ZH BLF KILYZYOB WRW YVULIV. gL XSVXP GSV OVMTGS LU VZXS DLIW XLIIVXGOB KZB ZGGVMGRLM GL ZOO XLNNZH ZMW WLGH! rH GSV OVMTGS LU "WLGH." ZMW "WLGH" GSV HZNV? \'HFY()\' UFMXGRLM UILN \'IV\' KZXPZTV DRGS \'[^Z-A ]\' IVTVC NZB YV SVOKUFO SVIV (LMOB RU BLF XLMEVIG BLFI GVCG GL OLDVIXZHV!).\n\nwL GSV HZNV GSRMT DRGS ZOO LU GSV VOVNVMGH LU GSV \'DRPRJFLGVH\' wZGZuIZNV. bLF NZB FHV \'ULI\' OLLK GL WL GSRH VZHRVI ZMW UZHGVI!'),
        "hint7": dcode('xLNKZIV WRHGIRYFGRLMH FHRMT \'YZI()\' UFMXGRLM UILN \'NZGKOLGORY\' KZXPZTV ULI XLFMGVW OVMTGSH LU DLIWH RM GSV NVHHZTV ZMW XLFMGVW OVMTGSH LU DLIWH RM ZOO OZMTFZTVH.'),
        "errorIntro": dcode('dV DVIV OLLPRMT HL OLMT ULI HLNVYLWB ORPV BLF DSL XLFOW\nSVOK FH HLOEV GSRH NRHGVIB. rU BLF WLM\'G SZEV ZXXVHH GL GSV\nNVHHZTVH, GSZM DV DRRO SZEV GL ZHP HLNVLMV VOHV. :('),
        "errorNans": dcode('mRXV GIB, YFG GSVIV RH LMV LI NLIV NRHHRMT EZOFVH (MZM) RM GSV TREVM WRXGRLMZIB.\niVKOZXV ZOO GSV MZMH ZMW GSVM GIB GL KZHH GSV WRXGRLMRZIB ZTZRM.'),
        "errorFrequencies": dcode('gSVIV RH HLNVGSRMT DILMT DRGS GSV TREVM UIVJFVMXRVH...\nsZEV BLF XLMEVIGVW GSV GVCG GL OLDVIXZHV?\nzIV BLF HFIV BLF WRW GSRH KILKVIOB?\nhLNV OVGGVIH WL MLG LXXFIV RM GSV NVHHZTV (ORPV \'P\'), YFG NZPV HFIV GSZG UIVJFVMXB ULI GSVN RH 0 RM GSV WRXGRLMZIB.'),
        "errorNoNAMES": dcode('gSV XLMGVMG GSZG BLF KZHHVW RH MLG Z WRXGRLMZIB. kOVZHV, KZHH WRXGRLMZIB.'),
        "errorLetters": dcode('bLF WRW MLG KZHH UIVJFVMXRVH ULI ZOO LU GSV OVGGVIH. :('),
        "errorDecipher": dcode('gSRH GIZMHOZGRLM HVVNH MLG GL URG GL GSV \'ILHVH\'.\nwRW BLF HLIG \'UIVJ\' ZIIZB XLIIVXGOB YVULIV GIZMHOZGRLM?'),
        "errorKey1": dcode('dV WLM\'G FMWVIHGZMW GSV \'PVB\' EZOFV RM GSV TREVM ULIN. gBKV ZTZRM GSV PVB BLF ULFMW RM GSV ULOOLDRMT ULIN: {"LOW": "LOWOVGGVIHZYXW...A", "MVD": "MVDOVGGVIHIVHKVXGREVOB"}.'),
        "errorKey2": dcode('wLM\'G BLF GSRMP GSZG YLGS OVMTGSH LU \'LOW\' ZMW \'MVD\' HSLFOW YV VJFZO GL 26?\ngSRH RH GSV MFNYVI LU ZOO OVGGVIH RM GSV oZGRM ZOKSZYVG.\n\nkOVZHV, XLIIVXG GSRH NRHGZPV ZMW GIB ZTZRM.'),
        "errorBadKey": dcode('mRXV GIB. sLDVEVI, GSRH PVB WLVH MLG GIZMHOZGV GSV NVHHZTV XLIIVXGOB.\nzIV BLF HFIV GSZG VEVIBGSRMT RH ZOO IRTSG?'),
        "errorBadX": dcode('zXXLIWRMT GL GSV URIHG LFI IVNZRMRMT NVHHZTVH ZIV MZNVW \'TFMH\' ZMW \'ZMW\'.\ngSRH RH DSB c HSLFOW YV LMV LU GSVHV MZNVH.'),
        "errorBadX2": dcode('sZEV BLF IVZOOB FMOLXPVW GSV \'TFMH\' NVHHZTV?'),
        "errorBadAND": dcode('dV XZM MLG LKVM GSV NVHHZTV. gIB ZTZRM. nZBYV BLF HVMG Z YZW UROV?'),
        "errorWikiNames": dcode('mZNVH LU ZGGZXSNVMG ZIV RMXLIIVXG. kOVZHV, HVMW FH \'OVMTGSH\' DRGS MZNVH ZXXLIWRMT GL \'DRPRJFLGVH\' MZNVH.'),
        "errorWikiNames2": dcode('gSV XLMGVMG LI GSV ZGGZXSNVMG GSZG BLF KZHHVW RH MLG Z WRXGRLMZIRVH. kOVZHV, KZHH WRXGRLMZIB.'),
        "errorLengths": dcode('gSVIV RH HLNVGSRMT DILMT DRGS GSV DZB BLF XLFMG GSV OVMTGSH LU GSV DLIWH RM GSV NVHHZTV. kOVZHV, GIB ZTZRM. rG HSLFOW YV Z WRXGRLMZIB DRGS MFNYVI LU DLIWH DRGS TREVM OVMTGS.'),
        "errorLengths0": dcode('oVMTGSH LU DLIWH RM NVHHZTV ZIV LP, YFG HLNVGSRMT RH DILMT DRGS GSV DZB BLF XLFMG GSV OVMTGSH LU GSV DLIWH RM \'DRPRJLFGVH\' UROV. gSV IVHFOG HSLFOW YV Z WRXGRLMZIB DRGS MZNVH LU OZMTFZTVH ZMW WRXGRLMZIRVH LU UIVJFVMXRVH. kOVZHV, GIB ZTZRM.'),
        "errorLanguage": dcode('dV WLM\'G GSRMP GSZG GSRH RH GSV IRTSG ZMHDVI. gSV OZMTFZTV BLF HFTTVHGVW WLVHM\'G URG LFI NVHHZTV.'),
        "errorEnd": dcode('dV ZIV ZUIZRW GSRH RH MLG GSV KZHHDLIW GSZG DV ZIV OLLPRMT ULI. zIV BLF HFIV GSVIV RH MLGSRMT VOHV GL HVV?'),
        "errorAttachment": dcode('rG HVVNH GSZG BLF NRTSG SZEV ULITLGGVM GL ZGGZXS UROVH. kOVZHV, HVMW GSRH NVHHZTV DRGS GSV ZGGZXSVNVMG.'),
        "errorContent": dcode('wRW BLF HVMW GSRH NVHHZTV DRGSLFG XLMGVMG?'),
        "errorSubject": dcode('wL BLF DZMG GL HVMW GSRH NVHHZTV DRGSLFG GSV HFYQVXG?'),
        "errorSubject2": dcode('xSVXP GSV NZRO\'H HFYQVXG. hLNVGSRMT RH DILMT GSVIV!')
        }
    
    def hintf(level):
        """
        Auxiliary printing hints function.
        """
        
        print(commands["hint" + str(level)])
        return None
    
    def taskf(level):
        """
        Auxiliary printing tasks function.
        """
        
        print(commands["task" + str(level)])
        return None
    
    # plain start
    if len(args) == 0:
        print(commands["intro"])
        level = 0
        return None
    
    if "subject" in args and "content" in args:
        
        # wrong subject
        if args["subject"].lower() not in subjects.values():
            print(commands["errorSubject2"])
            return None
        
        # 0. show an interest
        if args["subject"].lower() == subjects["s0"]:
            h = hs.md5()
            h.update(args["content"].encode())
            if h.hexdigest() == "89d81a0b78f34acabedf92273fba5d74":
                level = 1
                taskf(level)
            elif level == 0:
                print(commands["errorIntro"])
                return None
        
        # 1. give a dictionary of frequencies
        if args["subject"].lower() == subjects["s1"]:
            if type(args["content"]) != dict:
                print(commands["errorNoNAMES"])
                return None
            else:
                if any(np.isnan(list(args["content"].values()))):
                    print(commands["errorNans"])
                    return None
                else:
                    keys = args["content"].keys()
                    if not all([x in list(ascii_lowercase) for x in list(keys)]) or len(keys) != len(list(ascii_lowercase)):
                        print(commands["errorLetters"])
                        return None
                    frequencies = [y + str(x) for (y,x) in args["content"].items()]
                    frequencies.sort()
                    frequencies = ''.join(frequencies)
                    h = hs.md5()
                    h.update(frequencies.encode())
                    if h.hexdigest() == "87c229c35a78e31a3dcc5f5ad121a1e5":
                        level = 2
                        taskf(level)
                    else:
                        print(commands["errorFrequencies"])
                        return None
                    
        # 2. substitute letters from EnglishLetterFrequency
        if args["subject"].lower() == subjects["s2"]:
            In = re.sub("[^A-Z]", "", args["content"].upper())
            h = hs.md5()
            h.update(In.encode())
            if h.hexdigest() == "1ad289e2cc0b8e5d369575f8b4204833":
                level = 3
                taskf(level)
            else:
                print(commands["errorDecipher"])
                return None
         
        # 3. translate ALL of the letters (find a complete key)
        if args["subject"].lower() == subjects["s3"]:
            if len(args["content"]) != 2 or any([x not in ["old", "new"] for x in args["content"].keys()]):
                print(commands["errorKey1"])
                return None
            else:
                if any([len(x) != 26 for x in args["content"].values()]):
                    print(commands["errorKey2"])
                    return None
                else:
                    Ord = np.array(list((args["content"]["old"]))).argsort()
                    In = np.array(list((args["content"]["new"])))[Ord]
                    In = np.delete(In, [1, 20, 8])
                    In = ''.join(In)
                    h = hs.md5()
                    h.update(In.encode())
                    if h.hexdigest() == "2f6091325893792fa833a7e00eb8a7f2":
                        level = 4
                        taskf(level)
                    else:
                        print(commands["errorBadKey"])
                        return None
          
        # 4. find another cipher
        if args["subject"].lower() == subjects["s4"]:
            subjectSplit = args["subject"].split(" ")
            if subjectSplit[2] in ["and", "guns"]:
                print(commands["errorBadX"])
                return None
            elif subjectSplit[2] == "guns":
                print(commands["errorBadX2"])
                return None
            In = re.sub("[^A-Z]", "", args["content"].upper())
            h = hs.md5()
            h.update(In.encode())
            if h.hexdigest() == "659ce97a91e8fa7aa276c55b523580f7":
                level = 5
                taskf(level)
            else:
                print(commands["errorBadAND"])
                return None
        
        # 5. count the words' lengths
        if args["subject"].lower() == subjects["s5"]:
            if "attachment" not in args:
                print(commands["errorAttachment"])
                return None
            else:
                if type(args["content"]) != dict or type(args["attachment"]) != dict:
                    print(commands["errorWikiNames2"])
                    return None
                elif not all([x in wikiquotes.columns for x in args["attachment"].keys()]):
                    print(commands["errorWikiNames"])
                    return None
                lengths = ["l" + str(y) + str(x) for (y,x) in args["content"].items()]
                lengths = ''.join(lengths[1:10])
                h = hs.md5()
                h.update(lengths.encode())
                if h.hexdigest() == "974e95c76211946fc02b547d52ac63eb":
                    lengths2 = ["l" + str(y) + str(x) for (y,x) in args["attachment"]["Czech"].items()]
                    lengths2 = ''.join(lengths2[2:11])
                    h2 = hs.md5()
                    h2.update(lengths2.encode())
                    if h2.hexdigest() == "9dbc4538d5e0af713acc0d1c6a16d182":
                        level = 6
                        taskf(level)
                    else:
                        print(commands["errorLengths0"])
                        return None
                else:
                    print(commands["errorLengths"])
                    return None
        
        # 6. give a language:
        if args["subject"].lower() == subjects["s6"]: 
            h = hs.md5()
            h.update(args["content"].encode())
            if h.hexdigest() == "65b01cd12dc5cb80b5481e1a123cef23":
                level = 7
                taskf(level)
            else:
                print(commands["errorLanguage"])
                return None
        
        # 7. give a password:
        if args["subject"].lower() == subjects["s7"]:
            h = hs.md5()
            h.update(args["content"].encode())
            if h.hexdigest() == "9e7f33f403cd4c06f2b9e78c30c83366":
                print(commands["outro"])
                return None
            else:
                print(commands["errorEnd"])
                return None
    
    if len(args) > 0 and "content" not in args and "hint" not in args:
        print(commands["errorContent"])
        
    if len(args) > 0 and "subject" not in args and "hint" not in args:
        print(commands["errorSubject"])
    
    if "hint" in args and args["hint"]:
        hintf(level)
    
    return None