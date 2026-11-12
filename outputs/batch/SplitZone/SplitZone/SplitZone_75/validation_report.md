# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_75`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_75/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 98 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '9' (RT) duration 96 frames exceeds threshold 90 frames [start=109, end=204].
> - Validation warning: Action 'Action_ZoneBlock' for track '10' (LG) duration 96 frames exceeds threshold 90 frames [start=109, end=204].
> - Validation warning: Action 'Action_ZoneBlock' for track '12' (LT) duration 96 frames exceeds threshold 90 frames [start=109, end=204].
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (C) duration 96 frames exceeds threshold 90 frames [start=109, end=204].
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [106–121], lower_priority='Action_ZoneBlock' annotated_start=109, effective_Action_ZoneBlock_start=122.
> - Action 'Action_SplitBlock' range [114-161] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-178] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-299] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-195] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-242] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-253] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-299] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-187] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-186] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-195] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [109-204] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [109-196] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-208] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-223] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-227] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-133] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-185] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-204] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [217-221] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-214] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [109-151] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [157-158] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-184] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-189] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-244] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-255] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [136-173] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [181-182] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-294] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-260] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-267] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [272-291] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-137] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-278] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-299] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [106-119] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [123-133] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [149-153] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [157-167] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-299] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-202] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [204-206] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-215] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-209] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-222] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-193] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-228] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-234] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-299] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-269] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [272-273] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-268] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-297] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-289] for track '32' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.