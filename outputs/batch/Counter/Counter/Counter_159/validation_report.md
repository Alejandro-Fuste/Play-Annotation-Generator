# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_159`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_159/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Segment 'Action_DownBlock' for track '18' has invalid range: start=133, end=132. Clamping end to start.
> - Action 'Action_None' range [123-299] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-270] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-274] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-293] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-299] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-189] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-197] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-296] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [133-194] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '10' starts at frame 123, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [123-299] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-181] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-209] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_Handoff' range [154-176] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-157] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-162] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-195] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-276] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [280-299] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [177-208] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-299] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [123-132] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [133-141] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [197-202] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [133-154] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-299] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [133-176] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [182-183] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [189-192] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [194-197] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-150] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-177] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-234] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-244] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [246-252] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-291] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [293-299] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-269] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-276] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-280] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-284] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-293] for track '27' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.