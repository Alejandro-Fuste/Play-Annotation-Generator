# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `CrackToss_39`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_39/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 67 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Event 'Action_None' at frame 114 targets track ID '157', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 80: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '12' (RT) duration 103 frames exceeds threshold 90 frames [start=69, end=171].
> - Action 'Action_None' range [66-126] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-112] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-161] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-175] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-108] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-175] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [66-175] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-91] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-128] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-117] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-175] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-156] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [96-175] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [66-114] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-175] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [69-103] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [105-171] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-97] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-175] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-32] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-54] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-58] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-61] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-90] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-104] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-175] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-72] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-88] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-107] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-112] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-119] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-65] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-175] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [69-175] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-175] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-147] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-175] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-111] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-175] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-139] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-150] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-175] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-175] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-175] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [163-175] for track '25' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.