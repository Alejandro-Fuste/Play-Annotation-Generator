# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_136`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_136/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 85 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 274: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_BallCarry' for track '3' has invalid range: start=116, end=109. Clamping end to start.
> - Validation warning: Action 'Action_DownBlock' for track '7' (RG) duration 100 frames exceeds threshold 90 frames [start=69, end=168].
> - Action 'Action_None' range [67-222] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-133] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-227] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [69-168] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-109] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-126] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-130] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [69-92] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [95-104] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-104] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [69-168] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-186] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-119] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-159] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [67-95] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-88] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-127] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-137] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-54] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [67-68] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-73] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-82] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-110] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-148] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [150-168] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-14] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [77-82] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [88-95] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [100-119] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-141] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-114] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-143] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-171] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-160] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-147] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-168] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-174] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-239] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-148] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-174] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-148] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-168] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-207] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-228] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-176] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-201] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-211] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-217] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-228] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [230-233] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-237] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-201] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-220] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-232] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-236] for track '31' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.