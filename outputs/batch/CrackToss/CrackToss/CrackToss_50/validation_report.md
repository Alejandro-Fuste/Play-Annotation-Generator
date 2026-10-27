# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `CrackToss_50`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_50/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 77 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Event 'Action_None' at frame 80 targets track ID '93', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [19-125] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-47] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-39] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-107] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-125] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [19-100] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [103-106] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-125] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-23] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-27] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-31] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-39] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-45] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-125] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-95] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-23] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [51-92] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [19-23] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-31] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-23] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-125] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-107] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-113] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-118] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-60] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_Toss' for track '15' starts at frame 33, but the player has no visible bounding box on this frame.
> - Action 'Action_Toss' range [33-33] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_Toss' range [35-50] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-125] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-20] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [22-23] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [108-125] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-23] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-27] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-106] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-23] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [66-69] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-125] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [19-21] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [22-23] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-30] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '21' starts at frame 19, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [19-19] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-81] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-108] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-125] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-84] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-96] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-125] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-120] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-125] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-98] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-125] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-120] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-125] for track '29' has 2 frames without a visible bounding box.
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