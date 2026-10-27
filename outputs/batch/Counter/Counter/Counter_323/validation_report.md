# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_323`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_323/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 79 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '17' (LG) duration 103 frames exceeds threshold 90 frames [start=176, end=278].
> - Validation warning: Action 'Action_DownBlock' for track '21' (RT) duration 103 frames exceeds threshold 90 frames [start=176, end=278].
> - Action 'Action_None' range [173-344] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [349-350] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-371] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-389] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-302] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [305-372] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-225] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-251] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [173-343] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [173-355] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-389] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-389] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [176-190] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [200-205] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [207-211] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-355] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-265] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [215-266] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [272-389] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-302] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-374] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [376-384] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-252] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [176-205] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [176-217] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [219-223] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [230-233] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-234] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [239-247] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-389] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [248-251] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-259] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-266] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-271] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-389] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [347-349] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [373-374] for track '28' has 1 frames without a visible bounding box.
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