# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_75`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_75/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 95 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 152: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [11-111] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-92] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-99] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-104] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-127] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-45] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-50] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-227] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [230-236] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [67-131] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [134-239] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-62] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-223] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-198] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-179] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-183] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-220] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-75] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-130] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-90] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-18] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [11-21] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [26-66] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-189] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-25] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-41] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-58] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-44] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-222] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [11-129] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-212] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [11-29] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-37] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-42] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-50] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-22] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-181] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-25] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-29] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-32] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-131] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-71] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [36-42] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [45-69] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [75-76] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-111] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-157] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [79-88] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [86-88] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-220] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-239] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-121] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-239] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-239] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [170-173] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-185] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-238] for track '35' has 1 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.