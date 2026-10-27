# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_185`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_185/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
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
> - Action 'Action_None' range [169-209] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [177-258] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-282] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-267] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-237] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-292] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-251] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [173-187] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [194-217] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [224-225] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [173-206] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [227-230] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-299] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [211-243] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [173-198] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [206-247] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-198] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-299] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-260] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-267] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [269-273] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-276] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-299] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [271-299] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-283] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-298] for track '29' has 2 frames without a visible bounding box.
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
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.