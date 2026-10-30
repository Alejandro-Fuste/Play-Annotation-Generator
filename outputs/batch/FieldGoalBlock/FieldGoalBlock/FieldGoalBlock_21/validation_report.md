# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_21`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_21/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 8 |
| Action Segments inferred | 103 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 43: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 44: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - Row 44: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - Row 44: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - Row 44: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_PreSnap' range [0-36] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-56] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-237] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-249] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-207] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-242] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-256] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-260] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-268] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-233] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [237-245] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-266] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [49-102] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-155] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-269] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-107] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-269] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-17] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-24] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-33] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-43] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [44-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-28] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-34] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-155] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-165] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-246] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [44-50] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-82] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [92-132] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-26] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_BlockKick' range [48-52] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-77] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-112] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-269] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-23] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-35] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-43] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-74] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-53] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [55-59] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-205] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-255] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [55-56] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-137] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-144] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-164] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-226] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [55-56] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-161] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-170] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-173] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-197] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-187] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-233] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-244] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [240-242] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-255] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-267] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [268-269] for track '35' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.