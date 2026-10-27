# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_142`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_142/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 102 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 286: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '1' (RG) duration 98 frames exceeds threshold 90 frames [start=50, end=147].
> - Validation warning: Action 'Action_DownBlock' for track '7' (LG) duration 98 frames exceeds threshold 90 frames [start=50, end=147].
> - Action 'Action_None' range [48-112] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-178] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [50-73] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-229] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-58] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-118] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-78] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [82-179] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [181-186] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [188-269] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [48-120] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-136] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-175] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-256] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-129] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [50-115] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [122-147] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-69] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-109] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-142] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-89] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-93] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-99] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-219] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-78] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [48-103] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-117] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-130] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-178] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-228] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [50-66] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [71-72] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-47] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [79-87] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [89-92] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-129] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [50-68] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [71-82] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-154] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-171] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-98] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-204] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-130] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-142] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-152] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-168] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [182-228] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-136] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-143] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-115] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-153] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-221] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-229] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-131] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-220] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-139] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-179] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-226] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-175] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-183] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-190] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-206] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-245] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [247-250] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-256] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-266] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-251] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-269] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-269] for track '32' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.