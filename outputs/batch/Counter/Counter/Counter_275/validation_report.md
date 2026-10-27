# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_275`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_275/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 113 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 552: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - Row 552: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - Row 552: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Overlapping action conflict at frame 53 for track '17': 'Action_DownBlock' vs 'Action_PullLeadBlock'. Overriding with 'Action_PullLeadBlock'.
> - Validation warning: Action 'Action_DownBlock' for track '19' (RG) duration 98 frames exceeds threshold 90 frames [start=53, end=150].
> - Validation warning: Action 'Action_DownBlock' for track '20' (DT1) duration 98 frames exceeds threshold 90 frames [start=53, end=150].
> - Action 'Action_None' range [46-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-220] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-104] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-137] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-162] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-175] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-185] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-234] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [90-139] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [146-155] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-108] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-137] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-153] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-173] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-190] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-133] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-140] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-200] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-209] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [46-134] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [64-68] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [72-75] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-105] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-117] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-159] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-171] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-200] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [53-108] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-73] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-129] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-89] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [53-59] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [62-79] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-58] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-69] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-117] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-124] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-128] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-151] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-34] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-39] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [53-60] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [62-84] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [90-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-154] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-32] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-39] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [53-56] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [58-60] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [62-116] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [131-133] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-174] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-239] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-56] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-80] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-83] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-88] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-94] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-104] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-118] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-127] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-161] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-213] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-225] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [229-239] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-216] for track '25' has 2 frames without a visible bounding box.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.