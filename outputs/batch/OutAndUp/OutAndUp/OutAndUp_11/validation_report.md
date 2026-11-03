# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutAndUp_11`
- **Input XML**: `outputs/batch/OutAndUp/OutAndUp/OutAndUp_11/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutAndUp.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 104 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [15–29], lower_priority='Action_PassBlock' annotated_start=19, effective_Action_PassBlock_start=30.
> - Action 'Action_None' range [15-161] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-170] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-197] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-206] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-210] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-51] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-93] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-102] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-131] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-157] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-96] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-129] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-179] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-122] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-210] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [19-183] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-173] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [87-210] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-167] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-173] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-180] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-210] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-171] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [173-186] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-191] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-204] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-208] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-114] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-77] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [91-106] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [110-111] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [114-169] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [179-209] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-129] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-44] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-48] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-52] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-173] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [184-191] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-210] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [19-103] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [114-176] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [179-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [184-186] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-142] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-162] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-210] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [19-210] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [15-56] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-129] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-140] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-153] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [162-166] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [19-162] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [183-184] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [186-193] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-137] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-141] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-157] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-162] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-122] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-125] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-202] for track '28' has 1 frames without a visible bounding box.
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