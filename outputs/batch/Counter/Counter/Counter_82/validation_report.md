# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_82`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_82/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 79 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Overlapping action conflict at frame 24 for track '5': 'Action_BallSnap' vs 'Action_DownBlock'. Overriding with 'Action_DownBlock'.
> - Action 'Action_PullBlock' range [24-85] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [87-94] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [24-95] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [45-56] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-111] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [24-46] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-110] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-185] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-294] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [24-103] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-285] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [24-119] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [24-290] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [57-151] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [24-95] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-78] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-39] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-31] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-46] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-51] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-64] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-42] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-58] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-232] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-245] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-256] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [258-260] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-51] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-76] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-299] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-253] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [91-94] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-187] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-153] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [155-158] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-165] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-183] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-299] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [135-138] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-146] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-151] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-299] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-287] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [266-269] for track '30' has 1 frames without a visible bounding box.
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