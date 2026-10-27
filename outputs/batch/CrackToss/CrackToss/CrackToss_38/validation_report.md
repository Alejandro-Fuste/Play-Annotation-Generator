# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `CrackToss_38`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_38/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 117 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Event 'Action_None' at frame 80 targets track ID '116', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 78: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '14' (RT) duration 121 frames exceeds threshold 90 frames [start=30, end=150].
> - Action 'Action_None' range [27-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-113] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-86] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-109] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-121] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [27-80] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [57-113] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [126-129] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [133-136] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [146-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-79] for track '8' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-37] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [42-65] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-71] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-91] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-94] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-109] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [36-72] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [76-81] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [93-98] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-150] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [57-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-29] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [30-61] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [64-65] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [68-69] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-71] for track '13' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [107-150] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [42-43] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [45-46] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [49-56] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [58-65] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [67-71] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [76-81] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [85-92] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [96-113] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [133-134] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [136-150] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [38-39] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-51] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-77] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-44] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [48-65] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [68-69] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-77] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-81] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-81] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-65] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [67-69] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-81] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-88] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-39] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [42-65] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-71] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-61] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [45-61] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [68-69] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-56] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-71] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-88] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-148] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-88] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-93] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-150] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-113] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-119] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-124] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-128] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-150] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-150] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-109] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-109] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-123] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-132] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-150] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-109] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-109] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-150] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-133] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-150] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-150] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-150] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '38' has 1 frames without a visible bounding box.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.