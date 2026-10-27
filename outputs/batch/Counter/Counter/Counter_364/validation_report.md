# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_364`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_364/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 108 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 730: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '11' (RG) duration 103 frames exceeds threshold 90 frames [start=148, end=250].
> - Segment 'Action_BallCarry' for track '16' has invalid range: start=188, end=45. Clamping end to start.
> - Action 'Action_None' range [145-249] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [145-195] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-255] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [145-202] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-211] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-271] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-329] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-187] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-313] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-221] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-244] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [148-172] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [174-187] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [200-214] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [220-224] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [148-179] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [187-191] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [198-242] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [148-218] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-315] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [188-305] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [148-161] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [167-169] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [171-172] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [174-178] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [193-204] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-170] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-176] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-95] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-115] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [145-217] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-45] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-15] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-34] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [148-158] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [163-171] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [179-188] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-34] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-38] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-35] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-123] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-231] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-158] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-219] for track '22' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [222-322] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-237] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [177-185] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-329] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-232] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-249] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-276] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-304] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-246] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-261] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-292] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [296-298] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-308] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [310-312] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-319] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-274] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-293] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-326] for track '31' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [237-301] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [307-316] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-280] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-285] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-290] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-276] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-329] for track '37' has 3 frames without a visible bounding box.
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
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.