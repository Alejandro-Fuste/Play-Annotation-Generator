# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_6`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_6/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 77 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [32–46], lower_priority='Action_PassBlock' annotated_start=35, effective_Action_PassBlock_start=47.
> - Action 'Action_None' range [32-148] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-151] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-104] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [35-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-155] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [161-164] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-215] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-102] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-299] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-112] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [98-256] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [270-275] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-145] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-150] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-187] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-220] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [32-92] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-100] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-142] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-152] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-238] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [32-46] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [47-48] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [53-54] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [62-99] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [106-124] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-35] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-46] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-44] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-47] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-30] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-119] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-134] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-166] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-217] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-102] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-91] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-98] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-144] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-270] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [280-291] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-299] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-160] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-164] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-155] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-226] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-184] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-230] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-203] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-234] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [210-299] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-241] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-272] for track '27' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.