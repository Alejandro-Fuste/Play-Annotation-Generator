# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_79`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_79/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 88 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Segment 'Action_BallCarry' for track '18' has invalid range: start=125, end=115. Clamping end to start.
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [82–95], lower_priority='Action_DownBlock' annotated_start=86, effective_Action_DownBlock_start=96.
> - Action 'Action_None' range [82-118] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-128] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-135] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-143] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-359] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-276] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [278-327] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-190] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [86-147] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-182] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-359] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-125] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-160] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-189] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-232] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-279] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-324] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-107] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-176] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-149] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-153] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-169] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-358] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [82-136] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-359] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [86-147] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-115] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-336] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [344-345] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-210] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [96-147] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [149-159] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [161-162] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-155] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-359] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-207] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-285] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-233] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-248] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-261] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-260] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-297] for track '29' has 1 frames without a visible bounding box.
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