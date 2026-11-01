# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_22`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_22/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 92 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '0' (RG) duration 98 frames exceeds threshold 90 frames [start=57, end=154].
> - Validation warning: Action 'Action_ZoneBlock' for track '1' (RT) duration 98 frames exceeds threshold 90 frames [start=57, end=154].
> - Validation warning: Action 'Action_ZoneBlock' for track '2' (LG) duration 98 frames exceeds threshold 90 frames [start=57, end=154].
> - Validation warning: Action 'Action_ZoneBlock' for track '5' (LT) duration 98 frames exceeds threshold 90 frames [start=57, end=154].
> - Validation warning: Action 'Action_ZoneBlock' for track '10' (C) duration 98 frames exceeds threshold 90 frames [start=57, end=154].
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [55–69], lower_priority='Action_ZoneBlock' annotated_start=57, effective_Action_ZoneBlock_start=70.
> - Action 'Action_ZoneBlock' range [57-154] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-191] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-218] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [57-154] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-171] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-184] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-89] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [95-157] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-177] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-197] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-208] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-269] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [55-94] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-98] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-124] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-205] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [55-177] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-186] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-116] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-146] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [55-254] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-206] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-78] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-59] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-77] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-98] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-103] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-98] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-133] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-244] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-159] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-269] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-230] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-249] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [254-269] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-142] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-168] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-249] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [256-269] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-246] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [248-260] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-268] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-239] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-203] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-186] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-217] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-234] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-264] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-219] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-261] for track '32' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.