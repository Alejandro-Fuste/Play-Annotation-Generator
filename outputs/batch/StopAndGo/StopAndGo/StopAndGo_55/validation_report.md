# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `StopAndGo_55`
- **Input XML**: `outputs/batch/StopAndGo/StopAndGo/StopAndGo_55/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/StopAndGo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 53 |
| Player Tracks | 53 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 159 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [18–36], lower_priority='Action_PassBlock' annotated_start=21, effective_Action_PassBlock_start=37.
> - Action 'Action_None' range [18-203] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-215] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-221] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-241] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-55] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-143] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-152] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-159] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-147] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [153-173] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-206] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-219] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-237] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-108] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_VerticalStem' range [43-71] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_VerticalStem' range [78-79] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_SellStop' for track '5' starts at frame 90, but the player has no visible bounding box on this frame.
> - Action 'Action_SellStop' range [90-90] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_SellStop' range [96-97] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [101-104] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [106-108] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [110-168] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [171-175] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [177-202] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [210-212] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [220-223] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [18-212] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [18-133] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-153] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-329] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-46] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-74] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-112] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-98] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [100-108] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-122] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-144] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [21-67] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [83-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [152-153] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [156-290] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-73] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-85] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-89] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-97] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-104] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-98] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [100-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-196] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-67] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-106] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [21-22] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [26-29] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [33-34] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [18-28] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [30-32] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' for track '17' starts at frame 37, but the player has no visible bounding box on this frame.
> - Action 'Action_PassBlock' range [37-92] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [94-153] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [21-41] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [46-77] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [80-81] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [83-85] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [87-138] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [171-191] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [206-208] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [215-229] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [235-315] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-191] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-57] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-46] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-123] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-135] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-150] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-269] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [271-272] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-103] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-157] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-267] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-285] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-141] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-215] for track '26' has 8 frames without a visible bounding box.
> - Action 'Action_None' range [147-150] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-183] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [157-159] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-234] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-178] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-198] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-208] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-287] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [289-291] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-329] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [229-231] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-234] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-240] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-240] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-245] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-260] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [251-253] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-257] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-292] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-296] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-315] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-304] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-312] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-326] for track '45' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [308-309] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-311] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-313] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-314] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-314] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-319] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-329] for track '51' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [321-325] for track '52' has 1 frames without a visible bounding box.
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
> - Player track '50' has undefined position. Will map to Position_Unknown.
> - Player track '50' has undefined team_side. Will map to Team_Unknown.
> - Player track '51' has undefined position. Will map to Position_Unknown.
> - Player track '51' has undefined team_side. Will map to Team_Unknown.
> - Player track '52' has undefined position. Will map to Position_Unknown.
> - Player track '52' has undefined team_side. Will map to Team_Unknown.
> - Play definition: no definition found for 'Play_Pass_StopAndGo'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.