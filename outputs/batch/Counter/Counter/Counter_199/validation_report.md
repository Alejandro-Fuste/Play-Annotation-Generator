# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_199`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_199/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 81 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '8' (RG) duration 98 frames exceeds threshold 90 frames [start=170, end=267].
> - Validation warning: Action 'Action_DownBlock' for track '12' (RT) duration 98 frames exceeds threshold 90 frames [start=170, end=267].
> - Validation warning: Action 'Action_DownBlock' for track '15' (C) duration 98 frames exceeds threshold 90 frames [start=170, end=267].
> - Validation warning: Action 'Action_PullBlock' for track '20' (LG) duration 98 frames exceeds threshold 90 frames [start=170, end=267].
> - Action 'Action_None' range [168-325] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-341] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-199] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [212-237] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [239-359] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-271] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-359] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-300] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-257] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-359] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [170-184] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [188-258] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [268-279] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-330] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [332-335] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-338] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-242] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-278] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-296] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-344] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [170-192] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [203-233] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [242-260] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [268-269] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-288] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-204] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-189] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-359] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-260] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [170-232] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-331] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-70] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-169] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [170-267] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [268-309] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-359] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-215] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [276-352] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-314] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-329] for track '26' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.