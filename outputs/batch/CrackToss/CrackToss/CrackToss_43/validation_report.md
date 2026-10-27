# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `CrackToss_43`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_43/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Event 'Action_None' at frame 126 targets track ID '152', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 88: Duplicate assignment for track ID '17' in grid. Overwriting previous assignment.
> - Row 88: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - Row 88: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '3' (TE1) duration 130 frames exceeds threshold 90 frames [start=71, end=200].
> - Validation warning: Action 'Action_PullBlock' for track '5' (RT) duration 122 frames exceeds threshold 90 frames [start=71, end=192].
> - Action 'Action_None' range [68-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-169] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [181-200] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [68-158] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-200] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [71-200] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [68-200] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [71-175] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [177-181] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [189-192] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-193] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-200] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [71-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [122-123] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [128-200] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-161] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-131] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-200] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-130] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-200] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-137] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-117] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [92-163] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-200] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [68-100] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-158] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-200] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [68-200] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-200] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-81] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-123] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-200] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-85] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [100-108] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-117] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-133] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-106] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-191] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-200] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-143] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-167] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-180] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-190] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-200] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-200] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-188] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-200] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-200] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-198] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-200] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-200] for track '31' has 1 frames without a visible bounding box.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.