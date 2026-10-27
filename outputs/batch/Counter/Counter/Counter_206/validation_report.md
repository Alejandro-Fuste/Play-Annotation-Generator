# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_206`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_206/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 88 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [131–144], lower_priority='Action_DownBlock' annotated_start=132, effective_Action_DownBlock_start=145.
> - Segment 'Action_DownBlock' for track '15' has invalid range: start=132, end=96. Clamping end to start.
> - Action 'Action_PreSnap' range [0-76] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-222] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-77] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [137-168] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [172-195] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [162-171] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-195] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-320] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-225] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-250] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-226] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-156] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-246] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [250-253] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-46] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-167] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-202] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-240] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [145-184] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [186-192] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [196-198] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [202-203] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-230] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-131] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [132-163] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [165-220] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-353] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [132-158] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [162-171] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [175-178] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-225] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-229] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-75] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-93] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-168] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-359] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-176] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [132-143] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-96] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [131-164] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-104] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-184] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-328] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-343] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-184] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-155] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-166] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-188] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-193] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-221] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-222] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-359] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-200] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-245] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-249] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-253] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-256] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-325] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-331] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-359] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-343] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-355] for track '34' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.