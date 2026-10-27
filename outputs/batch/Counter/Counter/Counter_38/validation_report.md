# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_38`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_38/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 30 |
| Ball Tracks | 1 |
| CSV events parsed | 20 |
| Action Segments inferred | 73 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Segment 'Action_BallSnap' for track '16' has invalid range: start=193, end=171. Clamping end to start.
> - Action 'Action_None' range [159-230] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-236] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [161-183] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-269] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-290] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-299] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [161-245] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-256] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [161-245] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [282-283] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-190] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-213] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-299] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [161-171] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [173-181] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [184-194] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-178] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-270] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [172-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [211-278] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [281-292] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-243] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-296] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-299] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-212] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-227] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-299] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-231] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [274-276] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-280] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-281] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [284-292] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-258] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-283] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [291-294] for track '30' has 1 frames without a visible bounding box.
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