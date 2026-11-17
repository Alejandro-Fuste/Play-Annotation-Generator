# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_222`
- **Input XML**: `outputs/batch/Power/Power/Power_222/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 41 |
| Player Tracks | 41 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 122 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 719 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 719 as fallback play end.
> - Action 'Action_PreSnap' range [21-173] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-590] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-187] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-602] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-564] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [580-621] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-719] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-596] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [598-605] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [615-634] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [643-644] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [649-653] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-109] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-621] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [630-649] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [651-655] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-540] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [546-548] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [550-570] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-279] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-532] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [533-562] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [568-579] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [599-691] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-388] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [428-566] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [574-647] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [651-653] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-289] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-299] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [309-318] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [320-326] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [334-335] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [338-373] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [376-383] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [385-402] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [404-532] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [533-583] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [585-598] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '9' starts at frame 599, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [599-630] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-60] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-143] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-532] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [533-548] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-259] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-423] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [449-450] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [452-455] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [530-562] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [621-625] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [627-628] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [630-653] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-31] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-49] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-98] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-114] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-128] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-132] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-203] for track '12' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-220] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-243] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-248] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-278] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-129] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-102] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-109] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-153] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-184] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-174] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-215] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-445] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [468-479] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [484-485] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [489-498] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [500-507] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [518-536] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [572-637] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [645-658] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [308-550] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [374-702] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [399-415] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [420-533] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [536-659] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [557-563] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [574-590] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [561-589] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [628-654] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [660-664] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [599-617] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [620-622] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [624-648] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [602-698] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [602-610] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [606-611] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [608-622] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [621-685] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [690-691] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [693-694] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [697-701] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [709-710] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [714-715] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [718-719] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [630-669] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [631-713] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [693-695] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [703-704] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [709-719] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [696-697] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [709-710] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [712-713] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [704-707] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [709-710] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [707-710] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [713-716] for track '39' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.