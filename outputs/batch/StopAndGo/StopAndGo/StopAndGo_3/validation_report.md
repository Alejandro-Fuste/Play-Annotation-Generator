# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `StopAndGo_3`
- **Input XML**: `outputs/batch/StopAndGo/StopAndGo/StopAndGo_3/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/StopAndGo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 42 |
| Player Tracks | 42 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 138 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 7: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [5–24], lower_priority='Action_PassBlock' annotated_start=8, effective_Action_PassBlock_start=25.
> - Action 'Action_SellStop' range [71-94] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [95-99] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [101-183] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [189-192] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-46] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-101] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-138] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-126] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-167] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [170-176] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-184] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-239] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-88] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [5-149] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-156] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-175] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [177-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-187] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-196] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-204] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [208-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-63] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-126] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-130] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-155] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-165] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-239] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [5-197] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-223] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-234] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-239] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [5-93] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-152] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-159] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-166] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-188] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-217] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-53] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-60] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-111] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-125] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-130] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-136] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [8-42] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [45-191] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [216-239] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-39] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-61] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-188] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-235] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-141] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [5-18] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [23-24] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-103] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-106] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-118] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-54] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-63] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [68-69] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-130] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [138-208] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-230] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [87-88] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-97] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-129] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-133] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-139] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-168] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-176] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-182] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-175] for track '27' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [192-194] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-139] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-191] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-201] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-206] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-238] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [109-110] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-140] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-166] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-151] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-166] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-175] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-192] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-209] for track '32' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [211-216] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-226] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-204] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-209] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-226] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-224] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-234] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-234] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-232] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-232] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-234] for track '41' has 1 frames without a visible bounding box.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
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
> - Play definition: no definition found for 'Play_Pass_StopAndGo'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.