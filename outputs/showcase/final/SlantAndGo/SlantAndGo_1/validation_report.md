# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SlantAndGo_1`
- **Input XML**: `output_showcase_final/SlantAndGo/SlantAndGo_1/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SlantAndGo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 87 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [6–21], lower_priority='Action_PassBlock' annotated_start=9, effective_Action_PassBlock_start=22.
> - Action 'Action_None' range [6-194] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-142] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-177] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-185] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-236] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-228] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-93] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-227] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-207] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [9-177] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-240] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-247] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-267] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [6-191] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-146] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-194] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-25] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-44] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [22-66] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [70-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [125-126] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [129-132] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [137-218] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-130] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-142] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-159] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-299] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [6-135] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [6-144] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [146-204] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [9-135] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [137-164] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-160] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [9-171] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [6-57] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-190] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [9-36] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_VerticalStem' range [62-220] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [8-10] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-19] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-36] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-48] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-160] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-167] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-177] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-179] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-189] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-252] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-264] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [256-278] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-299] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-266] for track '32' has 1 frames without a visible bounding box.
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
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.