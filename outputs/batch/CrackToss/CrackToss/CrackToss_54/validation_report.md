# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `CrackToss_54`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_54/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 29 |
| Ball Tracks | 1 |
| CSV events parsed | 15 |
| Action Segments inferred | 79 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Event 'Action_None' at frame 100 targets track ID '126', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 109: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 110: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '5' (LT) duration 105 frames exceeds threshold 90 frames [start=50, end=154].
> - Validation warning: Action 'Action_PullBlock' for track '11' (TE2) duration 119 frames exceeds threshold 90 frames [start=50, end=168].
> - Action 'Action_PreSnap' range [0-37] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-115] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-155] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [86-137] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-175] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-85] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-62] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-110] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-114] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-175] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [50-150] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [153-154] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-68] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-81] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-152] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [155-175] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-91] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [47-175] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-108] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [50-168] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-175] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-165] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-175] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [47-65] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-125] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-175] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-86] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-98] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-49] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [50-76] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [78-175] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '18' starts at frame 47, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [47-67] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [69-93] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-69] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-89] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-93] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-77] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-93] for track '20' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-113] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-130] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-107] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-142] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-175] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [88-132] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-136] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-175] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-110] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-175] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-175] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-134] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-145] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-175] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-175] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '29' has 1 frames without a visible bounding box.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.