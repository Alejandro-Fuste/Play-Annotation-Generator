# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_230`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_230/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 101 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 462: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '3' (RG) duration 115 frames exceeds threshold 90 frames [start=150, end=264].
> - Validation warning: Action 'Action_PullBlock' for track '9' (LG) duration 115 frames exceeds threshold 90 frames [start=150, end=264].
> - Segment 'Action_BallCarry' for track '12' has invalid range: start=193, end=178. Clamping end to start.
> - Validation warning: Action 'Action_DownBlock' for track '14' (RT) duration 115 frames exceeds threshold 90 frames [start=150, end=264].
> - Validation warning: Action 'Action_DownBlock' for track '16' (C) duration 107 frames exceeds threshold 90 frames [start=150, end=256].
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [149–160], lower_priority='Action_DownBlock' annotated_start=150, effective_Action_DownBlock_start=161.
> - Action 'Action_None' range [149-212] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-249] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_Handoff' range [175-186] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-320] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-389] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [150-222] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [228-246] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [250-252] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-320] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '4' starts at frame 149, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [149-149] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-204] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-228] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-314] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-225] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-315] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [322-365] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-199] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-206] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-221] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-373] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-172] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-368] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [150-175] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [178-190] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [202-247] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-370] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-380] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [150-154] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [157-162] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [150-178] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-215] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [150-237] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [239-261] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-301] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-314] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [335-336] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-151] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-154] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [149-159] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [182-183] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [185-186] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [192-194] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [197-199] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [201-256] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-155] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-199] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-176] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-267] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-339] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-212] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-273] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-312] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [314-329] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-232] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-389] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-219] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-372] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [377-385] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-243] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-351] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-371] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-389] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-275] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-275] for track '31' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.