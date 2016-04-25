# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from string import ascii_lowercase, ascii_uppercase
import os
import hashlib as hs

"""
Module with The Proton Game.
"""

path = os.path.dirname(os.path.abspath(__file__))
employees = pd.read_csv(os.path.join(path, "data", "employees.csv"), index_col=0)
top1000passwords = pd.read_csv(os.path.join(path, "data", "top1000passwords.csv"), index_col=0)
top1000passwords = np.array(top1000passwords.password)
logs = pd.read_csv(os.path.join(path, "data", "logs.csv"), index_col=0)
bash_history = pd.read_csv(os.path.join(path, "data", "bash_history.csv"), index_col=0)
bash_history = np.array(bash_history.command)

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

texts = {
    "proton_init": dcode(' _____ _         _____         _             _____\n|_   _| |_ ___  |  _  |___ ___| |_ ___ ___  |   __|___ _____ ___\n  | | |   | -_| |   __|  _| . |  _| . |   | |  |  | .\'|     | -_|\n  |_| |_|_|___| |__|  |_| |___|_| |___|_|_| |_____|__,|_|_|_|___|\n\nbLFI TLZO RH GL URMW hOZDLNRI kRVGIZHAPL\'H XIVWVMGRZOH ULI GSV kILGLM HVIEVI.\ngSRH RH GSV LMOB DZB ULI yRG GL URMW GSV HVXIVG KOZMH LU kRVGIZHAPL\'H OZYLIZGLIB.\n\niVNVNYVI GSZG ZG ZMB GRNV BLF NZB ZWW `SRMG = gIFV` ZITFNVMG GL GSV VCVXFGVW XLNNZMW RM LIWVI GL TVG ZWWRGRLMZO HFTTVHGRLMH.\n\nkRVGIZHAPL FHVH Z KZHHDLIW DSRXS RH EVIB WRUURXFOG GL TFVHH.\nzG URIHG, GIB GL SZXP ZM ZXXLFMG LU Z KVIHLM DSRXS RH MLG ZH XZFGRLFH ZH kRVGIZHAPL.\n\nyFG DSL RH GSV DVZPVHG KLRMG? rMRGRZO RMEVHGRTZGRLM HFTTVHGH GSZG qLSM rMHVXFIV WLVHM\'G XZIV ZYLFG HVXFIRGB ZMW SZH ZM ZXXLFMG LM GSV kILGLM HVIEVI. sV NZB FHV Z KZHHDLIW DSRXS RH VZHB GL XIZXP.\noVG\'H ZGGZXP SRH ZXXLFMG URIHG!\n\nkILYOVN 1: uRMW GSV OLTRM LU qLSM rMHVXFIV.\n\nyRG SZH HXIZKKVW \'VNKOLBVVH\' WZGZ (MZNVH ZMW OLTRMH) UILN GSV DDD DVY KZTV LU gVXSMRXZO fMREVIHRGB LU dZIHZD. gSV WZGZ RH RM GSV KZMWZH wZGZuIZNV `VNKOLBVVH`. \nmLD, BLFI GZHP RH GL URMW qLSM rMHVXFIV\'H OLTRM.\ndSVM BLF URMZOOB URMW LFG DSZG qLSM\'H OLTRM RH, FHV `KILGLM(ZXGRLM = "OLTRM", OLTRM="cba")` XLNNZMW, DSVIV cba RH rMHVXFIV\'H OLTRM.\n'),
    "proton_init_w": dcode('rM `VNKOLBVVH` WZGZHVG GIB GL URMW Z ILD DSRXS SZH `rMHVXFIV` EZOFV RM GSV `HFIMZNV` XLOFNM.\n'),
    "log_1": dcode('QLSMRMH'),
    "log_2": dcode('HOZK'),
    "proton_login_init": dcode('xLMTIZGFOZGRLMH! bLF SZEV ULFMW LFG DSZG qLSM rMHVXFIV\'H OLTRM RH!\nrG RH SRTSOB ORPVOB GSZG SV FHVH HLNV GBKRXZO KZHHDLIW.\nyRG WLDMOLZWVW UILN GSV rMGVIMVG Z WZGZYZHV DRGS 1000 NLHG XLNNLMOB FHVW KZHHDLIWH.\nbLF XZM URMW GSRH WZGZYZHV RM GSV `GLK1000KZHHDLIWH` MFNKB ZIIZB.\n\nkILYOVN 2: uRMW qLSM rMHVXFIV\'H KZHHDLIW.\n\nfHV `KILGLM(ZXGRLM = "OLTRM", OLTRM = cba", KZHHDLIW = "zyx")` XLNNZMW RM LIWVI GL OLT RMGL GSV kILGLM HVIEVI DRGS GSV TREVM XIVWVMGRZOH.\nrU GSV KZHHDLIW RH XLIIVXG, BLF DROO TVG GSV ULOOLDRMT NVHHZTV:\n`hFXXVHH! fHVI RH OLTTVW RM!`.\nlGSVIDRHV BLF DROO TVG:\n`kZHHDLIW LI OLTRM RH RMXLIIVXG!`.\n'),
    "proton_login_init_w": dcode('fHV GSV YIFGV ULIXV NVGSLW.\nyB FHRMT Z OLLK, GIB GL OLT RM DRGS HFYHVJFVMG KZHHDLIWH UILN `GLK1000KZHHDLIWH` MFNKB ZIIZB ZH OLMT ZH BLF IVXVREV:\n`hFXXVHH! fHVI RH OLTTVW RM!`.\n'),
    "proton_login_fail": dcode('kZHHDLIW LI OLTRM RH RMXLIIVXG.'),
    "proton_login_fail2": dcode('\nrU ZXGRLM = \'OLTRM\' ZITFNVMG RH HVG GSVM LMV HSLFOW ZOHL HVG \'OLTRM = .\' ZITFNVMG.\n'),
    "proton_login_fail3": dcode('\nrU ZXGRLM = \'OLTRM\' ZITFNVMG RH HVG GSVM LMV HSLFOW ZOHL HVG \'KZHHDLIW = .\' ZITFNVMG.\n'),
    "proton_login_pass": dcode('hFXXVHH! fHVI RH OLTTVW RM!'),
    "proton_login_pass_instr": dcode('dVOO WLMV! gSRH RH GSV IRTSG KZHHDLIW!\nyRG FHVW qLSM rMHVXFIV\'H ZXXLFMG RM LIWVI GL OLT RMGL GSV kILGLM HVIEVI.\nrG GFIMH LFG GSZG qLSM SZH ZXXVHH GL HVIEVI OLTH.\nmLD, yRG DZMGH GL XSVXP UILN DSRXS DLIPHGZGRLM kRVGIZHAPL RH UIVJFVMGOB OLTTRMT RMGL GSV kILGLM HVIEVI. yRG SLKVH GSZG GSVIV DROO YV HLNV FHVUFO WZGZ.  \n\noLTH ZIV RM GSV `OLTH` WZGZHVG. \nxLMHVXFGREV XLOFNMH XLMGZRM RMULINZGRLM HFXS ZH: DSL, DSVM ZMW UILN DSRXS XLNKFGVI OLTTVW RMGL kILGLM.\n\nkILYOVN 3: xSVXP UILN DSRXS HVIEVI kRVGIZHAPL OLTH RMGL GSV kILGLM HVIEVI NLHG LUGVM.\n\nfHV `KILGLM(ZXGRLM = "HVIEVI", SLHG = "cba")` XLNNZMW RM LIWVI GL OVZIM NLIV ZYLFG DSZG XZM YV ULFMW LM GSV cba HVIEVI.\ngSV YRTTVHG XSZMXV GL URMW HLNVGSRMT RMGVIVHGRMT RH GL URMW Z HVIEVI UILN DSRXS kRVGIZHAPL OLTH RM GSV NLHG LUGVM.\n\n'),
    "proton_login_pass_instr_w": dcode('rM LIWVI GL TVG GL PMLD UILN DSRXS HVIEVI kRVGIZHAPL RH OLTTRMT GSV NLHG LUGVM LMV NZB:\n1. xSLLHV LMOB kRVGIZHAPL\'H OLTH,\n2. xLFMG GSV MFNYVI LU kRVGIZHAPL\'H OLTH RMGL HVKZIZGV HVIEVIH,\n3. hLIG HVIEVIH\' ORHG YB GSV UIVJFVMXB LU OLTH.\n\nfHV `VNKOLBVVH` WZGZYZHV RM LIWVI GL XSVXP DSZG kRVGIZHAPL\'H OLTRM RH.\n'),
    "proton_login_weak": dcode('mRXV GIB, YFG GSVIV RH MLGSRMT RMGVIVHGRMT ZYLFG GSRH OLTRM.\ngSV DVZPVHG ORMP LU kILGLM HVIEVI RH qLSM rMHVXFIV.\ngIB GL URMW SRH OLTRM.\n'),
    "proton_final": dcode('xLMTIZGFOZGRLMH!\n\nbLF SZEV XIZXPVW kRVGIZHAPL\'H KZHHDLIW!\nhVXIVG KOZMH LU SRH OZY ZIV MLD RM BLFI SZMWH.\ndSZG RH RM GSRH NBHGVIRLFH OZY?\nbLF NZB IVZW ZYLFG RG RM GSV `kRVGIZHAPL\'H XZEV` HGLIB DSRXS RH ZEZROZYOV ZG SGGK://YRVXVP.KO/yVGZyRG/dZIHZD\n\nmVCG ZWEVMGFIV LU yVGZ ZMW yRG DROO YV ZEZROZYOV HLLM.\n'),
    "proton_host_instr": dcode('rG GFIMH LFG GSZG kRVGIZHAPL LUGVM FHVH GSV KFYORX DLIPHGZGRLM 194.29.178.16.\ndSZG Z XZIVOVHHMVHH.\n\nyRG RMUROGIZGVW GSRH DLIPHGZGRLM VZHROB. sV WLDMOLZWVW `YZHS_SRHGLIB` UROV DSRXS XLMGZRMH Z ORHG LU ZOO XLNNZMWH GSZG DVIV VMGVIVW RMGL GSV HVIEVI\'H XLMHLOV.\ngSV XSZMXVH ZIV GSZG HLNV GRNV ZTL kRVGIZHAPL GBKVW Z KZHHDLIW RMGL GSV XLMHLOV YB NRHGZPV GSRMPRMT GSZG SV DZH OLTTRMT RMGL GSV kILGLM HVIEVI.\n\nkILYOVN 4: uRMW GSV kRVGIZHAPL\'H KZHHDLIW.\n\nrM GSV `YZHS_SRHGLIB` WZGZHVG BLF DROO URMW ZOO XLNNZMWH ZMW KZIZNVGVIH DSRXS SZEV VEVI YVVM VMGVIVW.\ngIB GL VCGIZXG UILN GSRH WZGZHVG LMOB XLNNZMWH (LMOB HGIRMTH YVULIV HKZXV) ZMW XSVXP DSVGSVI LMV LU GSVN OLLPH ORPV Z KZHHDLIW.\nlMXV BLF URMW GSV KZHHDLIW, FHV RG GL OLTRM RMGL GSV KILGLM HVIEVI.\n'),
    "proton_host_instr_w": dcode('xLNNZMWH ZMW KZIZNVGVIH ZIV HVKZIZGVW YB Z HKZXV.\nzUGVI SZERMT ZOO XLNNZMWH VCGIZXGVW BLF HSLFOW XSVXP SLD LUGVM VZXS XLNNZMW RH FHVW.\nkVISZKH RG DROO GFIM LFG GSZG LMV LU GBKVW RM XLNNZMWH OLLP ORPV Z KZHHDLIW?\n\nrU BLF HVV HLNVGSRMT DSRXS OLLPH ORPV Z KZHHDLIW, BLF HSZOO FHV `KILGLM(ZXGRLM = "OLTRM", OLTRM = "cba", KZHHDLIW = "zyx")` XLNNZMW GL OLT RMGL GSV kILGLM HVIEVI DRGS kRVGIZHAPL XIVWVMGRZOH.\n'),
    "proton_host_instr_w2": dcode('yRG HKVMG HLNV GRNV GL RMUROGIZGV GSRH DLIPHGZGRLM. \nyFG GSVIV RH MLGSRMT RMGVIVHGRMT SVIV.\nuRMW GSV DLIPHGZGRLM DSRXS kRVGIZHAPL RH FHRMT NLHG LUGVM GL OLT RMGL GSV kILGLM HVIEVI.\n')
    }


def proton(**args):
    """
    Description is under construction.
    """

    # plain start
    if len(args) == 0:
        print(texts["proton_init"])
        return None
    if len(args) == 1 and "hint" in args and args["hint"]:
        print(texts["proton_init"] + "\n\nHINT:\n" + texts["proton_init_w"])
        return None
   
    # action = server
    if len(args) > 0 and "action" in args and args["action"] == "server":
        h = hs.md5()
        if "host" in args and args["host"] is not None:
            h.update(args["host"].encode())
            if h.hexdigest() == "5b5e083d910e79ad404d70a3bb621bf2":
                print(texts["proton_host_instr"])
                if "hint" in args and args["hint"]:
                    print("\nHINT:\n" + texts["proton_host_instr_w"])
                return None
            else:
                print(texts["proton_host_instr_w2"])
                return None
        else:
            print(texts["proton_host_instr_w2"])
            return None

    # action = login
    if len(args) > 0 and "action" in args and args["action"] == "login":
        # only user is set to John Insecure
        if "login" in args and args["login"] is not None and args["login"] == texts["log_1"] and "password" not in args:
            print(texts["proton_login_init"])
            if "hint" in args and args["hint"]:
                print("\nHINT:\n" + texts["proton_login_init_w"])
            return None
        # login is missing
        if "login" not in args:
            print(texts["proton_login_fail2"])
            return None
        # user is set to John Insecure and password is provided
        if "login" in args and args["login"] is not None and args["login"] == texts["log_1"] and "password" in args and args["password"] is not None:
            h = hs.md5()
            h.update(args["password"].encode())
            if h.hexdigest() == "42d8aa7cde9c78c4757862d84620c335":
                print(texts["proton_login_pass_instr"])
                if "hint" in args and args["hint"]:
                    print("\nHINT:\n" + texts["proton_login_pass_instr_w"])
                return texts["proton_login_pass"]
            else:
                return texts["proton_login_fail"]
        # user is set to Pietraszko and password is provided
        if "login" in args and args["login"] is not None and args["login"] == texts["log_2"] and "password" in args and args["password"] is not None:
            h = hs.md5()
            h.update(args["password"].encode())
            if h.hexdigest() == "46d478afbae1e7db4889ab8619b40b56":
                print(texts["proton_final"])
                return texts["proton_login_pass"]
            else:
                return texts["proton_login_fail"]
        # only user is set
        if "login" in args and args["login"] is not None and args["login"] != texts["log_1"] and args["login"] != texts["log_2"]:
            print(texts["proton_login_weak"])
            return None
        # password is missing
        if "password" not in args:
            print(texts["proton_login_fail3"])
            return None
        
    return None
