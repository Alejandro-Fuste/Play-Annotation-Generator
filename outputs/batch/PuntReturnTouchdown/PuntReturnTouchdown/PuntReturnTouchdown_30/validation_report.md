# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_30`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_30/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 50 |
| Player Tracks | 50 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 136 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 629 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 629 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [140-629] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-167] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-384] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [387-629] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [194-508] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [511-512] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [523-562] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [564-571] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [573-629] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-344] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-350] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [357-629] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-372] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-544] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [558-570] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-190] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-320] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-359] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-497] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-407] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [416-439] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [441-442] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [444-445] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [450-600] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-161] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-306] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [309-310] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-445] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-167] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-629] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [211-273] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-291] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [140-236] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-367] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [379-380] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-217] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-219] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-489] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-384] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-558] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [566-567] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-385] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [387-446] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-182] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-259] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-404] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [408-510] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-226] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-556] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-247] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-397] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-330] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [318-536] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [543-621] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-571] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-388] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-450] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [452-629] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [396-566] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [576-587] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [413-419] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [422-430] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [464-476] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [482-484] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [492-495] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [498-499] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [501-518] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [522-555] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [563-565] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [579-591] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [487-611] for track '33' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [620-627] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [492-493] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [500-554] for track '36' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [507-508] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [513-540] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [542-546] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [523-526] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [529-540] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [543-546] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [553-557] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [559-560] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [562-563] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [608-609] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [612-613] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [539-546] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [549-553] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [555-561] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [580-585] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [583-595] for track '44' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [608-609] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [612-624] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [612-613] for track '47' has 1 frames without a visible bounding box.
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
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.
> - Player track '48' has undefined position. Will map to Position_Unknown.
> - Player track '48' has undefined team_side. Will map to Team_Unknown.
> - Player track '49' has undefined position. Will map to Position_Unknown.
> - Player track '49' has undefined team_side. Will map to Team_Unknown.
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.