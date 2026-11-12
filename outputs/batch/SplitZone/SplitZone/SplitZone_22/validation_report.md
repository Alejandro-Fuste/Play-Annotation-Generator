# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_22`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_22/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 43 |
| Player Tracks | 43 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 108 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '1' (LT) duration 91 frames exceeds threshold 90 frames [start=65, end=155].
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [62–77], lower_priority='Action_ZoneBlock' annotated_start=65, effective_Action_ZoneBlock_start=78.
> - Validation warning: Action 'Action_ZoneBlock' for track '15' (RG) duration 91 frames exceeds threshold 90 frames [start=65, end=155].
> - Action 'Action_None' range [62-201] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-287] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-344] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [65-129] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [138-139] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [151-154] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-177] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [185-187] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-214] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-175] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-119] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-162] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-171] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-208] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-261] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-102] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-143] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [62-136] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-277] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [65-82] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [62-183] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-189] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-193] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-153] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [78-101] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [65-99] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-92] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-419] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [62-94] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-184] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [64-71] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [81-92] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [101-155] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-419] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [65-132] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [139-155] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-204] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-208] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-119] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-179] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-44] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [105-188] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [193-249] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [253-290] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [301-304] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [313-314] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-94] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-106] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-115] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-124] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-136] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-184] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-194] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-187] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-196] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-354] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-204] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-227] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [197-293] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-256] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-344] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-247] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-276] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [278-279] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-288] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-283] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-308] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-320] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-413] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-351] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-356] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [392-395] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [399-413] for track '38' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [418-419] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [406-419] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [417-419] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [418-419] for track '42' has 1 frames without a visible bounding box.
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
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.