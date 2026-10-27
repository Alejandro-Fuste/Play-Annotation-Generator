# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_186`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_186/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 107 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
> - Track ID '19' in Player Track ID sheet does not exist in MOT gt.txt.
> - Track ID '21' in Player Track ID sheet does not exist in MOT gt.txt.
> - Track ID '18' in Player Track ID sheet does not exist in MOT gt.txt.
> - Track ID '16' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Segment 'Action_PullBlock' for track '16' has invalid range: start=193, end=189. Clamping end to start.
> - Action 'Action_PreSnap' range [0-64] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-234] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-249] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-264] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-293] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [295-330] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-357] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [193-219] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-296] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-89] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-195] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [196-219] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [236-331] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-203] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-211] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-220] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-227] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-238] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [193-245] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [248-257] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [273-278] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-63] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [193-203] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [207-217] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [224-227] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [246-250] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [258-267] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-319] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-16] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-189] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-221] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-93] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-105] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-109] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-125] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-130] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-136] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-166] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-175] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-182] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-197] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [209-213] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [193-206] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [213-272] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-20] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-23] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-31] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-78] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-155] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-158] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-211] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-222] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-248] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-207] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [214-229] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [223-259] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-271] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-237] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-359] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-266] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-286] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-359] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-336] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [251-264] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [266-348] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [279-297] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-322] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-359] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-359] for track '27' has 1 frames without a visible bounding box.
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