# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_12`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_12/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 43 |
| Player Tracks | 43 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 108 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 26: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_BallSnap' for track '17' has invalid range: start=66, end=48. Clamping end to start.
> - Action 'Action_None' range [42-51] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-105] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-98] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-145] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-177] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [45-57] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [66-88] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [42-91] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-72] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-110] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-123] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-199] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [45-139] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-52] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-59] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [62-72] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [42-110] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-117] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-133] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [45-139] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-143] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-169] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-153] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-176] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [42-43] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-46] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-56] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-65] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-126] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-145] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-181] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [42-158] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [42-46] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '15' starts at frame 49, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [49-49] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_FakePassDroptoHandoff' range [55-56] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [83-84] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [90-91] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [97-98] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-80] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-71] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-94] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-125] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-220] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-123] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-219] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-165] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-121] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-121] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-141] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-141] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-149] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-160] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-207] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-139] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-142] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-215] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-239] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-227] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [229-233] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-177] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-200] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-208] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-223] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-239] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-187] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-211] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [219-232] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-239] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-239] for track '41' has 1 frames without a visible bounding box.
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
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.