# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_293`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_293/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 114 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 588: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Segment 'Action_BallCarry' for track '5' has invalid range: start=195, end=187. Clamping end to start.
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [154–170], lower_priority='Action_DownBlock' annotated_start=157, effective_Action_DownBlock_start=171.
> - Action 'Action_None' range [154-201] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-203] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-207] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-203] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-307] for track '4' has 5 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [163-187] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-211] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-311] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-35] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-153] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-230] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-207] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-321] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-271] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-296] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-329] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-226] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-164] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-205] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [154-168] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [179-185] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-49] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-71] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-127] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-180] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-325] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-329] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [157-163] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [157-235] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [236-311] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-189] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-122] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-156] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-187] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-205] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-212] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-101] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [159-162] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [166-173] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [175-190] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [193-195] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [203-208] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [210-224] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-259] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [261-268] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-192] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-329] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [193-237] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-241] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-205] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-235] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-252] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-329] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-212] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-329] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-329] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [243-277] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-329] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [248-250] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-259] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [252-262] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-272] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-284] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [297-300] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-304] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-261] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-270] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [274-284] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [293-294] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-299] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-305] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-285] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-304] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-328] for track '37' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.