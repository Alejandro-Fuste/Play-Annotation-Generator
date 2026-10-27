# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_99`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_99/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 100 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 200: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_DownBlock' for track '19' has invalid range: start=43, end=38. Clamping end to start.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [39–53], lower_priority='Action_DownBlock' annotated_start=43, effective_Action_DownBlock_start=54.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [39–53], lower_priority='Action_SnapReceive' annotated_start=39, effective_Action_SnapReceive_start=54.
> - Action 'Action_None' range [39-177] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-183] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-177] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-143] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-154] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-162] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-210] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [39-74] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-108] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-115] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-140] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-210] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [39-79] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [82-157] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-174] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-118] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-177] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [179-210] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-75] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [90-98] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [101-108] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [137-138] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-67] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-147] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-154] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-177] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-117] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-145] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-160] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-210] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [39-183] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [43-67] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [70-129] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-210] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [43-98] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [115-121] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [124-126] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-142] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [39-136] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-147] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-151] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-59] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [76-77] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [83-84] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [43-103] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [107-108] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [110-111] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-204] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [39-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-94] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-153] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-161] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-210] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [129-162] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-177] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-149] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-210] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [173-177] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-210] for track '27' has 3 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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