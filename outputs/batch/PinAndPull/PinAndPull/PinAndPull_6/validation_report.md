# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PinAndPull_6`
- **Input XML**: `outputs/batch/PinAndPull/PinAndPull/PinAndPull_6/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PinAndPull.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 100 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 14: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [25-116] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-123] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [25-127] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [28-37] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [43-44] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '3' starts at frame 25, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [25-25] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-123] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-85] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [25-68] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-78] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-98] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-109] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-43] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-53] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-65] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [69-127] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-130] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-148] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [28-32] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [43-51] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [53-80] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' for track '8' starts at frame 48, but the player has no visible bounding box on this frame.
> - Action 'Action_BallCarry' range [48-48] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-59] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-103] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [37-46] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-73] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-80] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-88] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-118] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-31] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-50] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-59] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-128] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-132] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-143] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-43] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-123] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-56] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-92] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-43] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-73] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-82] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-111] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-136] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [28-44] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [48-50] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-131] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-125] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-148] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-36] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-105] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-113] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-127] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-53] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [47-64] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-75] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-118] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [123-125] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-132] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-95] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-61] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-75] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-73] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-85] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-123] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-131] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-138] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-121] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-96] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-101] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-120] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-127] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-133] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-122] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-128] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-130] for track '30' has 1 frames without a visible bounding box.
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
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.