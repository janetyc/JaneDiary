Jane's Diary
----

### How to run the code? 
#### configutation (twitter api, data folder)
- create ```janediary.conf``` based on ```janediary.conf.template``` janediary.conf
- modify ```janediary.conf```
	- (1) add authetication key for twitter api (consumer_key, consumer_secret, access_token, access_token_secrect)
	- (2) indicate the output folder (data_path)

### install required package
```
pip install -r requirements.txt
```
### execute the python code to get a twitter story
```
python get_twitter_story.py
```

### Result
<div style="border: 1px #aaa solid; padding: 5px;">
2019-07-29 23:00 Rainy<br/>
@ceekyrianne Gotham Na you’re like my mum .. Spoiler alert Jane makes BIG BREAD and if you start prison break they kill the witness x Awww!!!!! Felt this.. You heard em 🙏🏽🙏🏽🙏🏽 #SZNSoutNow  She is worthy! From her first appearance to her first swing of Mjolnir, revisit the comic history of Jane Foster with #MarvelUn… @ChantelHouston if you live in a city or rural town. I am a big fan of simple democracy and having a voting base th…  Good morning from sweet Jane.<br/>
<br/>
She’s a shy Terrier of just 1 yr looking for a soft lap to feel safe and secure by.<br/>
<br/>
She… Must-See LGBTQ TV: 'Jane the Virgin' series finale and new season of 'Dear White People' @eaglen_jane hello do you think we can win tomorrow night? 💚💛💚💛 otbc  here for this write up 🤧🙏🏽🙈 thank you tis the #SZN y’all !!! The "Honorable" Elijah Cummings and his wife soon to be under investigation for potentially illegally pocketing million… I vote for @jane_campbell1 of @HoustonDash for @NWSL Save of the Week! Vote #CampbellSOW<br/>
<br/>

2019年7月29日23時 雨天<br/>
@ceekyrianne Gotham Na你就像我的媽媽.. Spoiler提醒Jane做了大麵包，如果你開始越獄，他們會殺死證人x Awww !!!!!覺得這個..你聽說過他們#SZNSoutNow她是值得的！從她的第一次出場到她第一次搖擺的Mjolnir，如果你住在一個城市或鄉村小鎮，可以和＃MarvelUn ... @ChantelHouston一起重溫Jane Foster的漫畫歷史。我是簡單民主的忠實粉絲，擁有投票基礎......早上好，簡甜。她是一個只有1年的害羞的a小獵犬
</div>

### Change Logs
- 2019.07.29 replace googletrans with translate (for stablizing the translation part --> unknown issue)