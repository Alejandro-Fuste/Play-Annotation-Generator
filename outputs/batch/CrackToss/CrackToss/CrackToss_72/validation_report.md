# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `CrackToss_72`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_72/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 63 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Event 'Action_None' at frame 131 targets track ID '171', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 145: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '3' (LT) duration 127 frames exceeds threshold 90 frames [start=74, end=200].
> - Action 'Action_None' range [71-200] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [103-126] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [129-200] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-181] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-186] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-200] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [74-99] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [103-131] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [136-200] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-200] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-200] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [71-101] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-200] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-200] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-142] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-156] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-200] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-200] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-97] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-200] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-152] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-131] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-115] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-200] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [83-99] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [101-195] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [197-200] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-131] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-200] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-111] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-137] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-146] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-155] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-200] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-198] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-131] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-191] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-200] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-200] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-171] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-200] for track '26' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.