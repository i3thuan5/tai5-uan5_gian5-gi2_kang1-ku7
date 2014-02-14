#!/bin/bash

genList()
{
	ls $1 | awk '{print "basename "$1" .wav"}' | bash > $tmp
	cat $tmp | awk -v w=$1 -v f=$2 '{print w"/"$1".wav "f"/"$1".fea"}' > $3
	cat $tmp | awk -v w=$1 -v f=$2 '{print f"/"$1".fea"}' > $4

}
tsit2_ma1=`pwd`
trainData=`pwd`
trainData=`pwd`/kok4
rate="44100"
rate="16000"
configData="$tsit2_ma1/config"
tiong1ng1Data="$trainData/tiong1"

wavDir=$trainData"/wav"
feaDir=$trainData"/fea"
mfcc39_cfg="$configData/mfcc39.cfg.${rate}"
mfcc39_hcompv="$configData/mfcc39.hcompv.${rate}"
ku7_feature_list=$tiong1ng1Data"/ku7_feature.list"
t_feature_list=$tiong1ng1Data"/t_feature.list"
wav2fea_scp=$tiong1ng1Data"/wav2fea.scp"
tmp="${tiong1ng1Data}/tmp"
bo5_phiau1_a2_im1="${tiong1ng1Data}/bo5_phiau1_a2_im1.tmp"

H="/home/chhsueh/centos/local/HTK-3.4.1/bin/"
HCopy="$H/HCopy"
HLEd="${H}/HLEd"
HDMan="${H}/HDMan"
HCompV="${H}/HCompV"
HHEd="${H}/HHEd"
HERest="${H}/HERest"
HVite="${H}/HVite"
HParse="${H}/HParse"

#標仔檔：一个聲一个標仔，逐个音節一逝
san2_sing1_tik8_ting1='0'
san2_sing1_phiau1_a2='0'
san2_sing1_moo5_hing5='0'
moo5_hing5_ting5_koo1='0'
ke1_pian3_hua3='1'
tshe3_im1='1'
bang2_loo7='0'
pian7_sik4='0'

if [ $san2_sing1_tik8_ting1 -eq '1' ]; then
	echo "第一步：產生特徵"
	if [ ! -e $tiong1ng1Data ]; then
		mkdir $tiong1ng1Data
	fi

	if [ ! -e $feaDir ]; then
		mkdir $feaDir
	fi
	genList $wavDir $feaDir $wav2fea_scp $ku7_feature_list

	##wav gen fea

	##$HCopy -C $mfcc39_cfg -S $wav2fea_scp
	cat ${wav2fea_scp} | xargs -P 8 -n 2 $HCopy -C $mfcc39_cfg

	##ls `cat $ku7_feature_list | sed 's/fea/labels/g' | sed 's/\.labels/.lab/g'` > /dev/null 2> $tmp
	cat $ku7_feature_list | sed 's/fea/labels/g' | sed 's/\.labels/.lab/g' | awk '{print "ls "$1}' | bash > /dev/null 2> $bo5_phiau1_a2_im1

	##rm `cat $tmp | awk '{print $2}' | sed  's/labels/fea/g' | sed 's/lab:/fea/g'`
	cat $bo5_phiau1_a2_im1 | awk '{print $2}' | sed  's/labels/fea/g' | sed 's/lab:/fea/g' | awk '{print "rm "$1}'  | bash

	find $feaDir -type f > $t_feature_list
fi

##############02#################
labDir="$trainData/labels/"
sylMlfWithoutToneAndSil="${tiong1ng1Data}/t_sylWithoutToneAndSil.mlf"
sylListWithoutToneAndSil="${tiong1ng1Data}/t_sylWithoutToneAndSil.list"


label_scp="${tiong1ng1Data}/label.scp"
##golab2mlf $labDir $sylMlfWithoutToneAndSil $sylListWithoutToneAndSil
if [ $san2_sing1_phiau1_a2 -eq '1' ]; then
	echo "第二步：產生標仔"
	find $labDir -type f > $label_scp
	$HLEd -l "*" -i $sylMlfWithoutToneAndSil -n $sylListWithoutToneAndSil -S $label_scp /dev/null
fi
cmdForAddSilence="${configData}/cmdForAddSilence.txt"
sylMlfWithoutTone="${tiong1ng1Data}/t_sylWithoutTone.mlf"
sylListWithoutTone="${tiong1ng1Data}/t_sylWithoutTone.list"
if [ $san2_sing1_phiau1_a2 -eq '1' ]; then
	#dosCmd = "hled -l * -i %s -n %s %s %s" % (sylMlfWithoutTone, sylListWithoutTone, cmdForAddSilence, sylMlfWithoutToneAndSil);
	$HLEd -l "*" -i $sylMlfWithoutTone -n $sylListWithoutTone $cmdForAddSilence $sylMlfWithoutToneAndSil
fi

syl2PhoneDict="${configData}/Syl2Monophone.dic"
cmdForSyl2Phone="${configData}/cmdForSyl2Monophone.txt"
## 訓練語料
monoMlfWithoutTone="${tiong1ng1Data}/t_monoWithoutTone.mlf"
monoListWithoutTone="${tiong1ng1Data}/t_monoWithoutTone.list"
if [ $san2_sing1_phiau1_a2 -eq '1' ]; then
	$HLEd -l "*" -i $monoMlfWithoutTone -n $monoListWithoutTone -d $syl2PhoneDict $cmdForSyl2Phone $sylMlfWithoutTone
fi
## 共字典內底無用著的擲掉
new_syl2MonophoneDict="${tiong1ng1Data}/t_Syl2Monophone.dic"
if [ $san2_sing1_phiau1_a2 -eq '1' ]; then
	$HDMan -m -w $sylListWithoutTone $new_syl2MonophoneDict $syl2PhoneDict
fi

##################03##########################


## 需要參數檔設定: hmm.cfg
## 需要的檔案和資料夾
monoInitMacroWithoutTone="${tiong1ng1Data}/monoWithoutTone.init.macro"
tempMonoInitMacroWithoutTone="${tiong1ng1Data}/monoWithoutTone.init.temp.macro"
monoFinalMacroWithoutTone="${tiong1ng1Data}/monoWithoutTone.final.macro"
## 產生 HMM 基本模型
## =========================================================================
## 讀取參數設定
protoHMM="${configData}/proto";
#state="3"
#mixture="1"
#stream="39"
#mfcc="MFCC_E_D_A_Z"
#outMacro Plainhs DiagC $state \"$mixture\" $mfcc \"$stream\" > $protoHMM

## 訓練 monophone 為單位的聲學模型
## =========================================================================
## 初始化參數
hmmInitDir="${tiong1ng1Data}/hmmInit"
hcompv_hmm="${tiong1ng1Data}/hcompv.hmm"
if [ $san2_sing1_moo5_hing5 -eq '1' ]; then
	echo "第三步：產生模型"
	  rm -rf $hmmInitDir
	  mkdir $hmmInitDir
	  #goMacroInitial $hmmInitDir $monoMlfWithoutTone $monoListWithoutTone $t_feature_list $protoHMM
	  echo start HCompV
	  $HCompV -A -C $mfcc39_hcompv -m -f 0.0001 -o $hcompv_hmm -M ${tiong1ng1Data} -I $monoMlfWithoutTone -S $t_feature_list $protoHMM
	  echo finish HCompV

		#head -n 3 $tempMonoInitMacroWithoutTone > $monoInitMacroWithoutTone
		head -n 3 $hcompv_hmm > $monoInitMacroWithoutTone
		## 將 vFloos 複製到 macro 內
		vFloor="${tiong1ng1Data}/vFloors"
		cat $vFloor >> $monoInitMacroWithoutTone

		## 將獨立的模型檔案合併成一個檔案
	  while read line 
	  do
		  tail -n +4 $hcompv_hmm | sed 's/'${hcompv_hmm//\//\\\/}'/'$line'/g' >> $monoInitMacroWithoutTone
		  > $hmmInitDir/$line
	  done < $monoListWithoutTone
	  #cat $hmmInitDir/* > $tempMonoInitMacroWithoutTone
	  #tail -n +4 $tempMonoInitMacroWithoutTone >> $monoInitMacroWithoutTone
fi

## 重新調整聲學模型的參數 (monophone)
hmmInitDir="${tiong1ng1Data}/hmmInit"
herestN="${tiong1ng1Data}/herestN"
herestN_temp="${herestN}/temp"
if [ $moo5_hing5_ting5_koo1 -eq '1' ]; then
	echo "第四步：模型重估"
	 #dosCmd="goHERestN %s %d %s %s %s %s %s" % (".", N, monoInitMacroWithoutTone, monoFinalMacroWithoutTone, monoMlfWithoutTone, monoListWithoutTone, t_feature_list);

	 echo ========== Execute HERest For N Times ==========
	 declare -i N=3
	 declare -i i=1

	 if [ ! -e $herestN ]; then
		 mkdir $herestN 
	 fi
	 if [ ! -e $herestN_temp ]; then
		 mkdir $herestN_temp
	 fi
	 cp $monoInitMacroWithoutTone $herestN/macro.0

	 while ((i<=N)); do
		 declare -i prev=$i-1
		 cp ${herestN}/macro.$prev ${herestN_temp}/macro.$i
		 echo HERest $i Start ...
		 $HERest -A -C $mfcc39_hcompv -T 407 -t 450.0 150.0 1000.0 -s ${herestN}/${i}.sts -M ${herestN} -H ${herestN_temp}/macro.$i -I $monoMlfWithoutTone -S $t_feature_list $monoListWithoutTone #> ${herestN}/$i.log
		 echo HERest $i End ...
		 date
		 i=$i+1
	 done
	 cp ${herestN}/macro.$N $monoFinalMacroWithoutTone
fi
## 提升 mixture 數
## =======================================================================
goIncreasingMixNum()
{
 echo
}
mxup="${tiong1ng1Data}/mxup"
hmm="${tiong1ng1Data}/hmm"
monoFinalMacroWithoutToneAfterUpMixture="${tiong1ng1Data}/monoWithoutTone.final.upMixture.macro";
## 替 silence model 額外增加 1 個 mixture 數
mixture=(1 5 10 15 20 25 30)
if [ $ke1_pian3_hua3 -eq '1' ]; then
	echo "第五步：加變化"
	 rm -rf $mxup $hmm
	 mkdir -p $mxup $hmm
	 declare -i N=${#mixture[@]}
	 declare -i iterNum=3

	 #dosCmd = "goMacroTrain %s %d %d %s %s %s %s %s" % (".", N, iterNum, monoFinalMacroWithoutTone, m1_monoFinalMacroWithoutTone, monoMlfWithoutTone, t_feature_list, monoListWithoutTone);

	 mkdir $hmm/temp
	 mkdir $hmm/hmm.0
	 cp $monoFinalMacroWithoutTone $hmm/hmm.0/macro.0_$iterNum

	 declare -i i=1
	 while ((i<=N)); do
		 declare -i prev=$i-1
		 echo Iteration $i
		 mxup_scp="${mxup}/mxup$i.scp"
		 declare -i mixNum=${mixture[$prev]}
		 declare -i mixNum2=$mixNum*2
		 echo "MU ${mixNum} {*.state[2-4].mix}" > $mxup_scp
		 echo "MU ${mixNum2} {sil.state[2-4].mix}" >> $mxup_scp
		 mkdir ${hmm}/hmm.$i
		 echo Mixture Adjustment Using ${mxup_scp} ...
		 $HHEd -A -w $hmm/temp/macro.${i}_1 -H $hmm/hmm.${prev}/macro.${prev}_$iterNum $mxup_scp $monoListWithoutTone
		 #mkdir $hmm/hmm.$i

		 declare -i j=1
		 while ((j<=iterNum)); do
			 echo HERest $j `date`
			 $HERest -A -v 0.00001 -T 407 -t 450.0 150.0 1000.0 -s $hmm/hmm.$i/${i}_${j}.sts -M $hmm/hmm.$i -H $hmm/temp/macro.${i}_${j} -I $monoMlfWithoutTone -S $t_feature_list $monoListWithoutTone > $hmm/hmm.${i}/${i}_${j}.log
			 declare -i next=$j+1
			 cp $hmm/hmm.$i/macro.${i}_${j} $hmm/temp/macro.${i}_$next
			 j=$j+1
		 done
		 i=$i+1
	 done

	 cp $hmm/hmm.${N}/macro.${N}_${iterNum} $monoFinalMacroWithoutToneAfterUpMixture
fi

#alignment
resultMlf="${tiong1ng1Data}/孤音位切家己結果.mlf"
tshe2_im1_siong1_tui3="${tiong1ng1Data}/mono2mono.dic"
if [ $tshe3_im1 -eq '1' ]; then
	echo "第六步：切音"
	#$HVite -A -p -20 -o N -H $monoFinalMacroWithoutToneAfterUpMixture -l "*" -t 400 -i mono.final.result.mlf -I $monoMlfWithoutTone -S $t_feature_list $new_syl2MonophoneDict $monoListWithoutTone

	### im1 tsiat8
#	$HVite -A -p -20 -o N -H $monoFinalMacroWithoutToneAfterUpMixture -t 400 -i mono.final.result.mlf -I $sylMlfWithoutTone -S $t_feature_list $new_syl2MonophoneDict $monoListWithoutTone
#####
	cat $monoListWithoutTone | awk '{print $1"\t"$1}' > $tshe2_im1_siong1_tui3
	$HVite -A -p -20 -o N -H $monoFinalMacroWithoutToneAfterUpMixture -l "*" -t 400 -i $resultMlf -I $monoMlfWithoutTone -S $t_feature_list $tshe2_im1_siong1_tui3 $monoListWithoutTone
fi
## 把字典轉成 monophone
#sylMlfWithoutTone="${tiong1ng1Data}/t_sylWithoutTone.mlf"
#sylListWithoutTone="${tiong1ng1Data}/t_sylWithoutTone.list"
#new_syl2MonophoneDict="${tiong1ng1Data}/t_Syl2Monophone.dic"
#$HDMan -m -w $sylListWithoutTone $new_syl2MonophoneDict $syl2PhoneDict
bang2_loo7_gi2_huat4="${tiong1ng1Data}/辨識語法.gram"
pian7_sik4_bang2_loo7="${tiong1ng1Data}/辨識網路.net"
if [ $bang2_loo7 -eq '1' ]; then
	echo "第七步：產生辨識網路"
	echo "(sil <" > $bang2_loo7_gi2_huat4
	grep -v 'sil' $sylListWithoutToneAndSil | awk '{print $1" |"}' >> $bang2_loo7_gi2_huat4
	echo "sil > sil)" >> $bang2_loo7_gi2_huat4
	
	$HParse $bang2_loo7_gi2_huat4 $pian7_sik4_bang2_loo7
fi


pian7_sik4_tsu1_liau7="${tiong1ng1Data}/辨識檔案列表.list"
pian7_sik4_ket4_ko2="${tiong1ng1Data}/單音位辨識結果.mlf"

tsit8_giam7_im1_tong2="${trainData}/愛辨識語料"
tsit8_giam7_tik8_ting1="${tiong1ng1Data}/愛辨識特徵"
tsit8_giam7_tong2_an3="${tiong1ng1Data}/愛辨識檔案表.scp"
tsit8_giam7_tik8_ting1_pio2="${tiong1ng1Data}/愛辨識特徵表.list"
tsit8_giam7_ket4_ko2="${tiong1ng1Data}/愛辨識上好結果.mlf"
tsit8_giam7_so2_tsai7="${tiong1ng1Data}/愛辨識結果路線"

if [ $pian7_sik4 -eq '1' ]; then
	echo "第八步：辨識語料"
	head $t_feature_list > $pian7_sik4_tsu1_liau7
	#$HVite -p -20 -o N -H $monoFinalMacroWithoutToneAfterUpMixture -l "*" -t 400 -i $pian7_sik4_ket4_ko2 -w $pian7_sik4_bang2_loo7 -S $pian7_sik4_tsu1_liau7 $syl2PhoneDict $monoListWithoutTone

	if [ ! -e $tsit8_giam7_tik8_ting1 ]; then
		mkdir $tsit8_giam7_tik8_ting1
	fi
	genList $tsit8_giam7_im1_tong2 $tsit8_giam7_tik8_ting1 $tsit8_giam7_tong2_an3 $tsit8_giam7_tik8_ting1_pio2
	cat $tsit8_giam7_tong2_an3 | xargs -P 8 -n 2 $HCopy -C $mfcc39_cfg
	if [ ! -e $tsit8_giam7_so2_tsai7 ]; then
		mkdir $tsit8_giam7_so2_tsai7
	fi
	#$HVite -p -20 -o N -H $monoFinalMacroWithoutToneAfterUpMixture -l "*" -t 400 -i $tsit8_giam7_ket4_ko2 -w $pian7_sik4_bang2_loo7 -S $tsit8_giam7_tik8_ting1_pio2 $syl2PhoneDict $monoListWithoutTone
	$HVite -p -20 -o N -n 2 -z path -H $monoFinalMacroWithoutToneAfterUpMixture -l $tsit8_giam7_so2_tsai7 -t 400 -i $tsit8_giam7_ket4_ko2 -w $pian7_sik4_bang2_loo7 -S $tsit8_giam7_tik8_ting1_pio2 $syl2PhoneDict $monoListWithoutTone
fi
