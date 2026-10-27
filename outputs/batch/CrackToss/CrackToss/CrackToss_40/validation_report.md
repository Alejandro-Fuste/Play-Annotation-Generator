# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `CrackToss_40`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_40/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 27 |
| Ball Tracks | 1 |
| CSV events parsed | 12 |
| Action Segments inferred | 61 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Event 'Action_None' at frame 116 targets track ID '145', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 82: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - Row 82: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - Row 82: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '2' (Unknown) duration 116 frames exceeds threshold 90 frames [start=60, end=175].
> - Action 'Action_None' range [57-153] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-161] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-174] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [60-175] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [57-175] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-81] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-87] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-146] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-175] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-123] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [89-152] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [154-157] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [159-175] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-175] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-175] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-116] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-156] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-105] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-175] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [57-104] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-175] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-175] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-166] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-175] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [60-154] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [156-159] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-83] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-142] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-175] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-175] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-142] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-175] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-175] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-166] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-165] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-171] for track '27' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.