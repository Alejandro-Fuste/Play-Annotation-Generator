# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `CrackToss_70`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_70/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Event 'Action_None' at frame 88 targets track ID '117', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 142: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - Row 142: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - Row 142: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '10' (Unknown) duration 132 frames exceeds threshold 90 frames [start=19, end=150].
> - Validation warning: Action 'Action_PullBlock' for track '11' (TE1) duration 132 frames exceeds threshold 90 frames [start=19, end=150].
> - Action 'Action_None' range [16-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-150] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-59] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-109] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [41-99] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [103-134] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-150] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-89] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [93-104] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-103] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-82] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [19-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [19-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-150] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [19-31] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [44-45] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-150] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-63] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [24-67] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [69-150] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [16-17] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-32] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-109] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-138] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [16-36] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-76] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-80] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-59] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [62-64] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-150] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-59] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-90] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-147] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [47-59] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [60-68] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [70-79] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-90] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-108] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [65-79] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-81] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-114] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-150] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-86] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-93] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-102] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-110] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-150] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-150] for track '30' has 1 frames without a visible bounding box.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.