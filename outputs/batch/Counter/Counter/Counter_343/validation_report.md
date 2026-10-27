# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_343`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_343/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 93 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 688: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Segment 'Action_BallCarry' for track '6' has invalid range: start=184, end=178. Clamping end to start.
> - Validation warning: Action 'Action_DownBlock' for track '17' (RT) duration 96 frames exceeds threshold 90 frames [start=141, end=236].
> - Validation warning: Action 'Action_DownBlock' for track '20' (RG) duration 96 frames exceeds threshold 90 frames [start=141, end=236].
> - Validation warning: Action 'Action_DownBlock' for track '21' (C) duration 96 frames exceeds threshold 90 frames [start=141, end=236].
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [138–150], lower_priority='Action_DownBlock' annotated_start=141, effective_Action_DownBlock_start=151.
> - Action 'Action_None' range [138-174] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-359] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-359] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-359] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-201] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-347] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [349-351] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-359] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-234] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [242-245] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [247-359] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-345] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-147] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-178] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [141-184] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-312] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-359] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-339] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [343-359] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-222] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-316] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-184] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-189] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-233] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-263] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [138-280] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-359] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-301] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-310] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-161] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-166] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-247] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [249-352] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [141-157] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [159-219] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [224-236] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-359] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [141-236] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-322] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-359] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [141-195] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [138-146] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [151-220] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-348] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-195] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-359] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-359] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-207] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-213] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-246] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-267] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-282] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [285-292] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-316] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-325] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-355] for track '29' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
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