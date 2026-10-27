# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_126`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_126/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 28 |
| Ball Tracks | 1 |
| CSV events parsed | 18 |
| Action Segments inferred | 72 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Overlapping action conflict at frame 143 for track '5': 'Action_PlaySideFakeStep' vs 'Action_PullLeadBlock'. Overriding with 'Action_PullLeadBlock'.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [140–150], lower_priority='Action_DownBlock' annotated_start=143, effective_Action_DownBlock_start=151.
> - Action 'Action_None' range [140-258] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-226] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-152] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-158] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-299] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [143-213] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-199] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-235] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-299] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-229] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-251] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-256] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-296] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [181-289] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [151-160] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [186-187] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-226] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-206] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-198] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-183] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-199] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-214] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-225] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-245] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-299] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-233] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-272] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-276] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-289] for track '27' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.