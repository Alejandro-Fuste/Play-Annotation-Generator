# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `CrackToss_41`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_41/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 87 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Event 'Action_None' at frame 126 targets track ID '160', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 84: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '2' (TE2) duration 129 frames exceeds threshold 90 frames [start=72, end=200].
> - Validation warning: Action 'Action_PullBlock' for track '5' (Unknown) duration 127 frames exceeds threshold 90 frames [start=72, end=198].
> - Action 'Action_None' range [69-200] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [69-163] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [72-185] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [187-200] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-145] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [72-186] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [190-191] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [72-198] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [69-142] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-155] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-159] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-176] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-183] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-164] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-200] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [69-165] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [88-185] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-95] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-121] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-199] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [69-200] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-200] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-9] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-17] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [69-200] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-161] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-183] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-185] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-68] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [69-100] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-200] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-9] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-17] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [69-104] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-9] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-17] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [69-195] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-119] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-200] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-200] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [93-94] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-97] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-188] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-194] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-104] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-188] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-163] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-178] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-186] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-196] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-176] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-200] for track '30' has 1 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.