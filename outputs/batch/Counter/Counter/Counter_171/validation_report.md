# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_171`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_171/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 93 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_None' range [111-175] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [117-155] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [157-205] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-213] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [153-181] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [183-184] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [188-264] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [111-250] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-269] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-238] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-135] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-213] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-232] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-184] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-157] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-269] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-163] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-137] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-146] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-172] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-200] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-175] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-181] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [117-125] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [127-163] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [117-144] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [147-157] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [163-172] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [174-205] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [117-145] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [149-205] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-269] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-116] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [117-127] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [130-131] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [145-158] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-130] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-142] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-152] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-171] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-202] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-217] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [194-198] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-199] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-239] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-248] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-266] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-269] for track '31' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.