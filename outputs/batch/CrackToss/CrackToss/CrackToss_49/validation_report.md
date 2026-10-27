# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `CrackToss_49`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_49/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 81 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Event 'Action_None' at frame 135 targets track ID '168', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 99: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - Row 100: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - Row 100: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '2' (Unknown) duration 119 frames exceeds threshold 90 frames [start=82, end=200].
> - Validation warning: Action 'Action_PullBlock' for track '17' (Unknown) duration 144 frames exceeds threshold 90 frames [start=82, end=225].
> - Segment 'Action_BallSnap' for track '18' has invalid range: start=88, end=81. Clamping end to start.
> - Action 'Action_None' range [79-152] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-194] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-225] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-95] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-136] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [82-155] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [158-183] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [185-200] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [79-153] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-195] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [113-185] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-111] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-96] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-114] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-138] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-143] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-155] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-225] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [82-105] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_Toss' range [97-108] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-157] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-94] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-107] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-93] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-100] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-95] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-140] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-145] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-9] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [82-155] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [160-225] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-225] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [105-112] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-207] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-122] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-134] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-146] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-160] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-179] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-130] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-160] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-153] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-131] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-152] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [155-225] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-143] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-164] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-191] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [193-202] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-197] for track '27' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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